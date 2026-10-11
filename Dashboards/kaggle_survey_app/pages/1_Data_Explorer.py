"""
Data Explorer page — part of unified Kaggle Survey app
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import sys

HOME_DIR = Path(__file__).resolve().parent.parent.parent.parent
from theme import apply_theme, render_theme_toggle

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Data Explorer · Kaggle Survey",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


DATA = HOME_DIR / "Datasets/cleaned"
SEED = 42

# Professional palette
COLORS = {"2020": "#2A9D8F", "2022": "#1B3A4B"}
COLOR_SEQ = ["#2A9D8F", "#1B3A4B", "#E76F51", "#E9C46A", "#2C5F7A"]

# ---------------------------------------------------------------------------
# Data loading (cached)
# ---------------------------------------------------------------------------
@st.cache_data(show_spinner="Loading harmonized survey data…")
def load_data() -> pd.DataFrame:
    path = DATA / "survey_harmonized_2020_2022.parquet"
    if not path.exists():
        path = DATA / "survey_harmonized_2020_2022.csv"
    df = pd.read_parquet(path) if path.suffix == ".parquet" else pd.read_csv(path)
    df["survey_year"] = df["survey_year"].astype(int)
    # Tool diversity features
    lang_cols = [c for c in df.columns if c.startswith("lang_") and c not in ("lang_None", "lang_Other")]
    fw_cols = [c for c in df.columns if c.startswith("fw_") and c not in ("fw_None", "fw_Other")]
    df["n_languages"] = df[lang_cols].sum(axis=1)
    df["n_frameworks"] = df[fw_cols].sum(axis=1)
    return df


def filter_df(df: pd.DataFrame, years, countries, roles, genders) -> pd.DataFrame:
    out = df[df["survey_year"].isin(years)]
    if countries and "All" not in countries:
        out = out[out["country"].isin(countries)]
    if roles and "All" not in roles:
        out = out[out["role_group"].isin(roles)]
    if genders and "All" not in genders:
        out = out[out["gender"].isin(genders)]
    return out


# ---------------------------------------------------------------------------
# UI helpers
# ---------------------------------------------------------------------------
def kpi_card(label: str, value: str, delta: str | None = None):
    st.metric(label, value, delta=delta)


def year_bar(df: pd.DataFrame, col: str, title: str, order: list | None = None, orient: str = "v", template: str = "plotly_white"):
    counts = (
        df.groupby(["survey_year", col], observed=True)
        .size()
        .reset_index(name="n")
    )
    totals = counts.groupby("survey_year")["n"].transform("sum")
    counts["pct"] = counts["n"] / totals * 100
    if order:
        counts[col] = pd.Categorical(counts[col], categories=order, ordered=True)
        counts = counts.sort_values(col)
    fig = px.bar(
        counts,
        x=col if orient == "v" else "pct",
        y="pct" if orient == "v" else col,
        color="survey_year",
        barmode="group",
        color_discrete_map={2020: COLORS["2020"], 2022: COLORS["2022"]},
        title=title,
        labels={"pct": "% of respondents", "survey_year": "Year"},
        text=counts["pct"].round(1),
    )
    fig.update_traces(textposition="outside", cliponaxis=False)
    fig.update_layout(
        template=template,
        legend_title_text="Year",
        margin=dict(t=50, b=40),
        height=420,
        uniformtext_minsize=8,
        uniformtext_mode="hide",
    )
    return fig


def usage_horizontal(df: pd.DataFrame, prefix: str, items: list[str], title: str, template: str = "plotly_white"):
    rows = []
    for year, g in df.groupby("survey_year"):
        for item in items:
            col = f"{prefix}_{item}"
            if col in g.columns:
                rows.append({"year": str(year), "item": item, "pct": g[col].mean() * 100})
    u = pd.DataFrame(rows)
    if u.empty:
        return go.Figure()
    fig = px.bar(
        u,
        y="item",
        x="pct",
        color="year",
        barmode="group",
        orientation="h",
        color_discrete_map={"2020": COLORS["2020"], "2022": COLORS["2022"]},
        title=title,
        labels={"pct": "% using regularly", "item": ""},
        category_orders={"item": items},
    )
    fig.update_layout(template=template, height=480, margin=dict(t=50, l=10), yaxis=dict(autorange="reversed"))
    return fig


# ---------------------------------------------------------------------------
# App
# ---------------------------------------------------------------------------
def main():
    dark = render_theme_toggle()
    apply_theme(dark)
    plotly_template = "plotly_dark" if dark else "plotly_white"
    st.markdown(
        """
        <div class="app-header">
          <h1>Data Explorer</h1>
          <p>2020 vs 2022 · Demographics, skills, tools &amp; roles</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    df = load_data()

    # Sidebar filters
    with st.sidebar:
        st.header("Filters")
        years = st.multiselect("Survey year", [2020, 2022], default=[2020, 2022])
        top_countries = df["country"].value_counts().head(20).index.tolist()
        countries = st.multiselect("Country (top 20 + All)", ["All"] + top_countries, default=["All"])
        roles = st.multiselect(
            "Role group",
            ["All"] + sorted(df["role_group"].dropna().unique().tolist()),
            default=["All"],
        )
        genders = st.multiselect(
            "Gender",
            ["All"] + sorted(df["gender"].dropna().unique().tolist()),
            default=["All"],
        )
        st.divider()
        st.caption("Data: cleaned & harmonized Kaggle ML & DS Surveys")
        st.caption(f"Total rows loaded: {len(df):,}")

    if not years:
        st.warning("Select at least one survey year.")
        return

    fdf = filter_df(df, years, countries, roles, genders)

    # KPI strip
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        kpi_card("Respondents", f"{len(fdf):,}")
    with c2:
        n20 = (fdf["survey_year"] == 2020).sum()
        kpi_card("2020", f"{n20:,}")
    with c3:
        n22 = (fdf["survey_year"] == 2022).sum()
        kpi_card("2022", f"{n22:,}")
    with c4:
        py = fdf["lang_Python"].mean() * 100 if "lang_Python" in fdf.columns else 0
        kpi_card("Python usage", f"{py:.0f}%")
    with c5:
        sk = fdf["fw_Scikit-learn"].mean() * 100 if "fw_Scikit-learn" in fdf.columns else 0
        kpi_card("Scikit-learn", f"{sk:.0f}%")

    st.divider()

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["Demographics", "Skills & Tools", "Roles & Countries", "Experience", "Download"]
    )

    with tab1:
        col_a, col_b = st.columns(2)
        with col_a:
            age_order = ["18-21", "22-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-69", "70+"]
            st.plotly_chart(year_bar(fdf, "age", "Age distribution", age_order, template=plotly_template), use_container_width=True)
        with col_b:
            st.plotly_chart(year_bar(fdf, "gender", "Gender distribution", template=plotly_template), use_container_width=True)
        st.plotly_chart(year_bar(fdf, "education", "Education level", template=plotly_template), use_container_width=True)

    with tab2:
        langs = ["Python", "R", "SQL", "C", "C++", "Java", "Javascript", "Bash", "MATLAB", "Julia"]
        fws = ["Scikit-learn", "TensorFlow", "Keras", "PyTorch", "Xgboost", "LightGBM", "CatBoost", "Fast.ai", "JAX"]
        c1, c2 = st.columns(2)
        with c1:
            st.plotly_chart(usage_horizontal(fdf, "lang", langs, "Programming languages", template=plotly_template), use_container_width=True)
        with c2:
            st.plotly_chart(usage_horizontal(fdf, "fw", fws, "ML frameworks", template=plotly_template), use_container_width=True)

    with tab3:
        c1, c2 = st.columns(2)
        with c1:
            st.plotly_chart(year_bar(fdf, "role_group", "Role groups", template=plotly_template), use_container_width=True)
        with c2:
            top12 = fdf["country"].value_counts().head(12).index.tolist()
            sub = fdf[fdf["country"].isin(top12)]
            st.plotly_chart(year_bar(sub, "country", "Top 12 countries", template=plotly_template), use_container_width=True)

    with tab4:
        c1, c2 = st.columns(2)
        with c1:
            st.plotly_chart(year_bar(fdf, "coding_experience", "Coding experience", template=plotly_template), use_container_width=True)
        with c2:
            st.plotly_chart(year_bar(fdf, "ml_experience", "ML experience", template=plotly_template), use_container_width=True)

        # Diversity histograms
        fig = go.Figure()
        for year, color in [(2020, COLORS["2020"]), (2022, COLORS["2022"])]:
            sub = fdf[fdf["survey_year"] == year]
            fig.add_trace(go.Histogram(x=sub["n_languages"], name=str(year), marker_color=color, opacity=0.7, nbinsx=12))
        fig.update_layout(title="Language diversity (count)", barmode="overlay", template=plotly_template, height=360)
        st.plotly_chart(fig, use_container_width=True)

    with tab5:
        st.subheader("Download filtered data")
        st.write(f"Current filter returns **{len(fdf):,}** rows.")
        csv = fdf.to_csv(index=False).encode("utf-8")
        st.download_button(
            "Download CSV (filtered)",
            data=csv,
            file_name="kaggle_survey_filtered.csv",
            mime="text/csv",
        )
        st.download_button(
            "Download full harmonized CSV",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="survey_harmonized_2020_2022.csv",
            mime="text/csv",
        )
        st.info(
            "Cleaned per-year extracts are also available under "
            "`Datasets/cleaned/survey_2020_cleaned.csv` and `survey_2022_cleaned.csv`."
        )

    st.markdown(
        """
        <hr style="margin-top:2rem;border:none;border-top:1px solid #E2E8F0;">
        <p style="color:#94A3B8;font-size:0.85rem;">
        Self-selected Kaggle community sample · Not population-representative ·
        Question wording changed between years · Harmonization applied only where categories map cleanly.
        </p>
        """,
        unsafe_allow_html=True,
    )


main()
