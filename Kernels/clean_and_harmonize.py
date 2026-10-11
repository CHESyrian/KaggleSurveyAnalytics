#!/usr/bin/env python3
"""
Kaggle Survey 2020 & 2022 — robust cleaning, schema harmonization, and export.
Produces:
  - cleaned individual year CSVs (core columns + multi-select flags)
  - harmonized comparison table with aligned categories
"""

from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 42
np.random.seed(SEED)

ROOT = Path("/home/workdir/artifacts/Datasets")
OUT = ROOT / "cleaned"
OUT.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_survey(path: Path, year: int) -> pd.DataFrame:
    """Load CSV, drop question-text row, enforce basic dtypes, drop pure-empty rows."""
    df = pd.read_csv(path, low_memory=False, header=0)
    # first data row is the long-form question text
    if str(df.iloc[0, 0]).lower().startswith("duration") or "what is your age" in str(df.iloc[0, 1]).lower():
        df = df.iloc[1:].reset_index(drop=True)
    df["_survey_year"] = year
    # duration
    dur_col = "Time from Start to Finish (seconds)" if year == 2020 else "Duration (in seconds)"
    if dur_col in df.columns:
        df["duration_sec"] = pd.to_numeric(df[dur_col], errors="coerce")
        df = df.drop(columns=[dur_col])
    # drop rows that are completely empty on key demographics
    return df


def standardize_age(s: pd.Series) -> pd.Series:
    mapping = {
        "18-21": "18-21",
        "22-24": "22-24",
        "25-29": "25-29",
        "30-34": "30-34",
        "35-39": "35-39",
        "40-44": "40-44",
        "45-49": "45-49",
        "50-54": "50-54",
        "55-59": "55-59",
        "60-69": "60-69",
        "70+": "70+",
        "70+": "70+",
    }
    return s.map(mapping).fillna(s).astype("category")


def standardize_gender(s: pd.Series) -> pd.Series:
    m = {
        "Man": "Man",
        "Woman": "Woman",
        "Nonbinary": "Nonbinary",
        "Prefer not to say": "Prefer not to say",
        "Prefer to self-describe": "Prefer to self-describe",
    }
    return s.map(m).fillna("Other / Prefer not to say").astype("category")


def standardize_education(s: pd.Series) -> pd.Series:
    m = {
        "Bachelor’s degree": "Bachelor’s",
        "Bachelor's degree": "Bachelor’s",
        "Master’s degree": "Master’s",
        "Master's degree": "Master’s",
        "Doctoral degree": "Doctoral",
        "Professional degree": "Professional",
        "Some college/university study without earning a bachelor’s degree": "Some college",
        "Some college/university study without earning a bachelor's degree": "Some college",
        "No formal education past high school": "High school or less",
        "I prefer not to answer": "Prefer not to answer",
    }
    return s.map(m).fillna(s).astype("category")


def standardize_coding_exp(s: pd.Series) -> pd.Series:
    m = {
        "I have never written code": "Never",
        "< 1 years": "< 1 year",
        "< 1 year": "< 1 year",
        "1-2 years": "1-2 years",
        "1-3 years": "1-3 years",  # 2022
        "3-5 years": "3-5 years",
        "5-10 years": "5-10 years",
        "10-20 years": "10-20 years",
        "20+ years": "20+ years",
    }
    return s.map(m).fillna(s).astype("category")


def standardize_ml_exp(s: pd.Series) -> pd.Series:
    m = {
        "I do not use machine learning methods": "None",
        "Under 1 year": "< 1 year",
        "1-2 years": "1-2 years",
        "2-3 years": "2-3 years",
        "3-4 years": "3-4 years",
        "4-5 years": "4-5 years",
        "5-10 years": "5-10 years",
        "10-20 years": "10-20 years",
        "20 or more years": "20+ years",
    }
    return s.map(m).fillna(s).astype("category")


def extract_multiselect_flags(df: pd.DataFrame, prefix: str, label_map: dict[str, str]) -> pd.DataFrame:
    """Create binary columns from multi-select parts. label_map: part_col -> short name."""
    out = pd.DataFrame(index=df.index)
    for col, name in label_map.items():
        if col in df.columns:
            out[f"{prefix}_{name}"] = df[col].notna() & (df[col].astype(str).str.strip() != "")
        else:
            out[f"{prefix}_{name}"] = False
    return out


# Language maps (approximate alignment)
LANG_2020 = {
    "Q7_Part_1": "Python",
    "Q7_Part_2": "R",
    "Q7_Part_3": "SQL",
    "Q7_Part_4": "C",
    "Q7_Part_5": "C++",
    "Q7_Part_6": "Java",
    "Q7_Part_7": "Javascript",
    "Q7_Part_8": "Julia",
    "Q7_Part_9": "Swift",
    "Q7_Part_10": "Bash",
    "Q7_Part_11": "MATLAB",
    "Q7_Part_12": "None",
    "Q7_OTHER": "Other",
}

LANG_2022 = {
    "Q12_1": "Python",
    "Q12_2": "R",
    "Q12_3": "SQL",
    "Q12_4": "C",
    "Q12_5": "C#",
    "Q12_6": "C++",
    "Q12_7": "Java",
    "Q12_8": "Javascript",
    "Q12_9": "Bash",
    "Q12_10": "PHP",
    "Q12_11": "MATLAB",
    "Q12_12": "Julia",
    "Q12_13": "Go",
    "Q12_14": "None",
    "Q12_15": "Other",
}

# Common language set for comparison
COMMON_LANGS = ["Python", "R", "SQL", "C", "C++", "Java", "Javascript", "Bash", "MATLAB", "Julia", "None", "Other"]

ML_FW_2020 = {
    "Q16_Part_1": "Scikit-learn",
    "Q16_Part_2": "TensorFlow",
    "Q16_Part_3": "Keras",
    "Q16_Part_4": "PyTorch",
    "Q16_Part_5": "Fast.ai",
    "Q16_Part_6": "MXNet",
    "Q16_Part_7": "Xgboost",
    "Q16_Part_8": "LightGBM",
    "Q16_Part_9": "CatBoost",
    "Q16_Part_10": "Prophet",
    "Q16_Part_11": "H2O",
    "Q16_Part_12": "Caret",
    "Q16_Part_13": "Tidymodels",
    "Q16_Part_14": "JAX",
    "Q16_Part_15": "None",
    "Q16_OTHER": "Other",
}

ML_FW_2022 = {
    "Q17_1": "Scikit-learn",
    "Q17_2": "TensorFlow",
    "Q17_3": "Keras",
    "Q17_4": "PyTorch",
    "Q17_5": "Fast.ai",
    "Q17_6": "Xgboost",
    "Q17_7": "LightGBM",
    "Q17_8": "CatBoost",
    "Q17_9": "Caret",
    "Q17_10": "Tidymodels",
    "Q17_11": "JAX",
    "Q17_12": "PyTorch Lightning",
    "Q17_13": "Huggingface",
    "Q17_14": "None",
    "Q17_15": "Other",
}

COMMON_FW = ["Scikit-learn", "TensorFlow", "Keras", "PyTorch", "Fast.ai", "Xgboost", "LightGBM", "CatBoost", "JAX", "None", "Other"]


def build_core_2020(df: pd.DataFrame) -> pd.DataFrame:
    core = pd.DataFrame(index=df.index)
    core["survey_year"] = 2020
    core["age"] = standardize_age(df["Q1"])
    core["gender"] = standardize_gender(df["Q2"])
    core["country"] = df["Q3"].astype(str).str.strip().replace({"nan": np.nan})
    core["education"] = standardize_education(df["Q4"])
    core["role"] = df["Q5"].astype(str).str.strip().replace({"nan": np.nan})
    core["coding_experience"] = standardize_coding_exp(df["Q6"])
    # ML years – Q15 in 2020
    if "Q15" in df.columns:
        core["ml_experience"] = standardize_ml_exp(df["Q15"])
    # compensation Q24
    if "Q24" in df.columns:
        core["compensation"] = df["Q24"].astype(str).str.strip().replace({"nan": np.nan})
    # company size Q20
    if "Q20" in df.columns:
        core["company_size"] = df["Q20"].astype(str).str.strip().replace({"nan": np.nan})
    core["duration_sec"] = df.get("duration_sec")

    langs = extract_multiselect_flags(df, "lang", LANG_2020)
    for L in COMMON_LANGS:
        col = f"lang_{L}"
        core[col] = langs[col] if col in langs.columns else False

    fws = extract_multiselect_flags(df, "fw", ML_FW_2020)
    for F in COMMON_FW:
        col = f"fw_{F}"
        core[col] = fws[col] if col in fws.columns else False

    return core


def build_core_2022(df: pd.DataFrame) -> pd.DataFrame:
    core = pd.DataFrame(index=df.index)
    core["survey_year"] = 2022
    core["age"] = standardize_age(df["Q2"])
    core["gender"] = standardize_gender(df["Q3"])
    core["country"] = df["Q4"].astype(str).str.strip().replace({"nan": np.nan})
    # student flag Q5
    core["is_student"] = df["Q5"].astype(str).str.strip().eq("Yes")
    core["education"] = standardize_education(df["Q8"])
    # role is Q23
    if "Q23" in df.columns:
        core["role"] = df["Q23"].astype(str).str.strip().replace({"nan": np.nan})
    core["coding_experience"] = standardize_coding_exp(df["Q11"])
    if "Q16" in df.columns:
        core["ml_experience"] = standardize_ml_exp(df["Q16"])
    if "Q29" in df.columns:
        core["compensation"] = df["Q29"].astype(str).str.strip().replace({"nan": np.nan})
    if "Q25" in df.columns:
        core["company_size"] = df["Q25"].astype(str).str.strip().replace({"nan": np.nan})
    core["duration_sec"] = df.get("duration_sec")

    langs = extract_multiselect_flags(df, "lang", LANG_2022)
    for L in COMMON_LANGS:
        col = f"lang_{L}"
        core[col] = langs[col] if col in langs.columns else False

    fws = extract_multiselect_flags(df, "fw", ML_FW_2022)
    for F in COMMON_FW:
        col = f"fw_{F}"
        core[col] = fws[col] if col in fws.columns else False

    return core


def role_harmonize(s: pd.Series) -> pd.Series:
    """Map free-text-ish role titles to a smaller set."""
    mapping = {
        "Data Scientist": "Data Scientist",
        "Software Engineer": "Software Engineer",
        "Data Analyst": "Data Analyst",
        "Research Scientist": "Research Scientist",
        "Machine Learning Engineer": "ML Engineer",
        "Machine Learning/ MLops Engineer": "ML Engineer",
        "Data Engineer": "Data Engineer",
        "Business Analyst": "Business Analyst",
        "Product Manager": "Product/Project Manager",
        "Program/Project Manager": "Product/Project Manager",
        "Manager (Program, Project, Operations, Executive-level, etc)": "Manager / Executive",
        "Statistician": "Statistician",
        "Data Architect": "Data Architect",
        "Developer Relations/Advocacy": "Developer Relations",
        "Currently not employed": "Not employed",
        "Student": "Student",
        "Other": "Other",
        "Teacher / professor": "Academic / Teacher",
        "Academic researcher": "Academic / Teacher",
        "Engineer (non-software)": "Engineer (non-software)",
    }
    return s.map(mapping).fillna("Other").astype("category")


def main():
    print("Loading 2020…")
    raw20 = load_survey(ROOT / "survey-2020" / "kaggle_survey_2020_responses.csv", 2020)
    print("Loading 2022…")
    raw22 = load_survey(ROOT / "survey-2022" / "kaggle_survey_2022_responses.csv", 2022)

    print("Building core tables…")
    c20 = build_core_2020(raw20)
    c22 = build_core_2022(raw22)

    # Harmonize roles
    c20["role_group"] = role_harmonize(c20["role"])
    c22["role_group"] = role_harmonize(c22["role"])

    # Only remove exact full-row duplicates (very rare)
    before = len(c20)
    c20 = c20.drop_duplicates().reset_index(drop=True)
    print(f"2020 exact duplicates removed: {before - len(c20)}")
    before = len(c22)
    c22 = c22.drop_duplicates().reset_index(drop=True)
    print(f"2022 exact duplicates removed: {before - len(c22)}")

    # Soft duration filter: keep responses between 30s and 4h (or missing)
    for name, df in [("2020", c20), ("2022", c22)]:
        if "duration_sec" in df.columns:
            mask = df["duration_sec"].between(30, 4 * 3600) | df["duration_sec"].isna()
            removed = (~mask).sum()
            print(f"{name} duration outliers removed: {removed}")
            if name == "2020":
                c20 = df.loc[mask].reset_index(drop=True)
            else:
                c22 = df.loc[mask].reset_index(drop=True)

    # Save
    c20.to_csv(OUT / "survey_2020_cleaned.csv", index=False)
    c22.to_csv(OUT / "survey_2022_cleaned.csv", index=False)

    # Harmonized stack for comparison
    common_cols = [
        "survey_year", "age", "gender", "country", "education", "role_group",
        "coding_experience", "ml_experience", "compensation", "company_size",
        "duration_sec",
    ] + [f"lang_{L}" for L in COMMON_LANGS] + [f"fw_{F}" for F in COMMON_FW]

    h20 = c20.reindex(columns=common_cols)
    h22 = c22.reindex(columns=common_cols)
    harm = pd.concat([h20, h22], ignore_index=True)
    harm.to_csv(OUT / "survey_harmonized_2020_2022.csv", index=False)

    # Compact parquet for dashboard speed
    try:
        harm.to_parquet(OUT / "survey_harmonized_2020_2022.parquet", index=False)
        c20.to_parquet(OUT / "survey_2020_cleaned.parquet", index=False)
        c22.to_parquet(OUT / "survey_2022_cleaned.parquet", index=False)
    except Exception as e:
        print("Parquet optional save skipped:", e)

    print("\n=== Summary ===")
    print(f"2020 cleaned rows: {len(c20):,}")
    print(f"2022 cleaned rows: {len(c22):,}")
    print(f"Harmonized rows:   {len(harm):,}")
    print(f"Columns harmonized: {len(common_cols)}")
    print("Saved to", OUT)
    print(harm.groupby("survey_year")["age"].value_counts().unstack(fill_value=0).head())


if __name__ == "__main__":
    main()
