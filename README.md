# Kaggle Survey Analysis — 2020 vs 2022

Comparative analysis of the official **Kaggle Machine Learning & Data Science Surveys** (2020 and 2022). The project delivers cleaned harmonized datasets, polished Jupyter notebooks, and an interactive Streamlit dashboard for exploring how the global data-science community changed over two years.

---

## Data source

| Survey | Source | Raw responses (approx.) | After cleaning |
|--------|--------|-------------------------|----------------|
| **2020** | [Kaggle ML & DS Survey 2020](https://www.kaggle.com/c/kaggle-survey-2020) | ~20,000 | ~19,000 |
| **2022** | [Kaggle ML & DS Survey 2022](https://www.kaggle.com/c/kaggle-survey-2022) | ~24,000 | ~23,200 |

- **Grain:** one row = one respondent  
- **Collection:** online, self-selected convenience sample of Kaggle users  
- **Raw files:** `Datasets/survey-2020/kaggle_survey_2020_responses.csv`, `Datasets/survey-2022/kaggle_survey_2022_responses.csv`  
- **Cleaned / harmonized:** `Datasets/cleaned/`

**Important limitations**

- Not a probability sample of data scientists worldwide.  
- Question wording and option sets changed between years; only high-confidence category mappings are harmonized.  
- Compensation has substantial non-response and non-comparable band labels — treat salary views as descriptive only.

---

## Project layout

```
artifacts/
├── Datasets/
│   ├── survey-2020/          # raw 2020 CSV
│   ├── survey-2022/          # raw 2022 CSV
│   └── cleaned/              # cleaned + harmonized extracts (CSV & Parquet)
├── Kernels/
│   ├── clean_and_harmonize.py
│   ├── 01_survey_2020_eda.ipynb
│   ├── 02_survey_2022_eda.ipynb
│   └── 03_kaggle_survey_2020_vs_2022_comparative.ipynb
├── Dashboards/
│   └── kaggle_survey_app/          # unified Streamlit app
│       ├── app.py                  # home
│       └── pages/
│           ├── 1_Data_Explorer.py
│           └── 2_Reports.py
├── Reports/
├── requirements.txt
└── README.md
```

---

## Analysis sections & charts

### 1. Data quality & missingness
- Missing-value profile for core demographics, experience, and compensation  
- **Chart:** bar chart of compensation non-response rate by survey year  

### 2. Demographics
- Age and gender distributions by year  
- **Charts:** grouped bar charts (age bands, gender)  
- Statistical tests: χ² and Cramér’s V for year-over-year shifts  

### 3. Education & experience
- Highest formal education  
- Years writing code / using ML methods  
- **Charts:** grouped bar charts for education, coding experience, and ML experience  

### 4. Programming languages & ML frameworks
- Regular-use rates for Python, R, SQL, C/C++, Java, JavaScript, Bash, MATLAB, Julia  
- Framework rates for Scikit-learn, TensorFlow, Keras, PyTorch, XGBoost, LightGBM, CatBoost, Fast.ai, JAX  
- **Charts:** horizontal grouped bar charts comparing 2020 vs 2022 usage  

### 5. Roles & geography
- Harmonized role groups (Data Scientist, Software Engineer, Student, etc.)  
- Top countries by share of responses  
- **Charts:** grouped bar charts for roles; horizontal bars for top-12 countries  

### 6. Compensation (descriptive)
- Most common compensation bands among respondents who answered  
- **Table / chart:** year-side-by-side band frequencies (with strong caveats)  

### 7. Feature engineering & segmentation
- Approximate experience scores (coding / ML years)  
- Tool-diversity counts (number of languages, number of frameworks)  
- **Charts:** overlaid histograms of language and framework diversity  
- Lightweight k-means segmentation (learners → practitioners → polyglots → veterans) with year mix per cluster  

### 8. Interactive dashboard
Streamlit app with:
- Filters: year, country, role group, gender  
- KPI strip (respondent counts, Python %, Scikit-learn %)  
- Tabs mirroring the analysis sections above (Plotly interactive charts)  
- Download of filtered or full harmonized CSV  

---

## How to run

### Environment
```bash
pip install -r requirements.txt
```

### Re-run cleaning (optional)
```bash
python Kernels/clean_and_harmonize.py
```
Outputs land in `Datasets/cleaned/`.

### Notebooks
Open any notebook under `Kernels/` in Jupyter / VS Code / Cursor.  
Start with `03_kaggle_survey_2020_vs_2022_comparative.ipynb` for the full comparative story.

### Unified web app (data explorer + reports)
```bash
pip install -r requirements.txt
cd Dashboards/kaggle_survey_app
streamlit run app.py
```
Sidebar pages: **Data Explorer** (filters & charts) · **Reports** (all analytical briefs).

Dependencies are centralized in the project-root `requirements.txt`.

---

## Reproducibility

- Random seed: **42**  
- Cleaning logic is centralized in `Kernels/clean_and_harmonize.py`  
- Harmonized schema: age, gender, country, education, role group, coding/ML experience, compensation, company size, language flags, framework flags, duration  

---

## Key takeaways (high level)

| Theme | Finding |
|-------|---------|
| Sample | ~19k (2020) / ~23k (2022) usable after cleaning |
| Demographics | Younger cohort share rose; gender gap remains large |
| Education | Master’s is the modal level |
| Languages | Python dominant; SQL and R strong secondary |
| Frameworks | PyTorch share increased relative to TensorFlow / Keras |
| Experience | Large learner segment (no / &lt;1 year ML) |
| Compensation | High non-response; bands not fully comparable across years |

---

## License & attribution

Survey data is published by Kaggle under the terms of the respective competition/dataset licenses. This analysis code and derived cleaned extracts are provided for research and educational use within this project.
