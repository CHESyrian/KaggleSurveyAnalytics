# Role Playbooks: Stacks & Profiles (Kaggle Survey)

Practical profiles for major roles using cleaned survey data.  
**Primary year for detail: 2020** (clearer role labels). **2022** shown where titles map cleanly.

---

## How to read these playbooks

- **Stack %** = share of that role reporting regular use of the tool.  
- Profiles are **descriptive of Kaggle respondents**, not job-market ground truth.  
- 2022 role field changed; “Other” inflated — prefer 2020 for role structure, 2022 for tool updates on clear titles.

---

## 1. Data Scientist

| | 2020 | 2022 |
|--|------|------|
| n | 2,554 | 1,861 |
| Women | 16% | 16% |
| Master’s (2020) | 52% | — |
| Under 1 yr ML | 17% | 14% |

**Typical stack (high intensity)**

| Tool | 2020 | 2022 |
|------|------|------|
| Python | 92% | **94%** |
| SQL | 55% | **60%** |
| R | 37% | — |
| Scikit-learn | 76% | **82%** |
| XGBoost | 44% | **49%** |
| TensorFlow | 47% | 47% |
| PyTorch | 28% | **34%** |

**Profile:** Most tool-rich role. Strong classical ML (sklearn + boosting) plus growing deep learning. SQL is core, not optional. Experience is higher than the sample average (few absolute beginners).

**Implications:** Job specs and courses for DS should assume Python + SQL + sklearn as baseline; boosting and at least one DL framework (increasingly PyTorch) as differentiators.

---

## 2. Machine Learning Engineer

| | 2020 | 2022 |
|--|------|------|
| n | 1,030 | 546 |
| Women | 12% | **10%** |
| Under 1 yr ML | 21% | 12% |

**Typical stack (DL-heavy)**

| Tool | 2020 | 2022 |
|------|------|------|
| Python | 94% | **97%** |
| SQL | 31% | 40% |
| Scikit-learn | 69% | 78% |
| TensorFlow | 60% | 61% |
| PyTorch | 43% | **57%** |
| XGBoost | 29% | 42% |

**Profile:** Highest deep-learning intensity. PyTorch adoption jumped. SQL matters but less than for Data Scientists. Lowest women’s share among major technical roles in this sample.

**Implications:** ML Engineer paths should lead with Python + DL frameworks (PyTorch increasingly central), with solid sklearn/boosting secondary. Representation gap is widest here.

---

## 3. Data Analyst

| | 2020 |
|--|------|
| n | 1,397 |
| Women | **24%** |
| Under 1 yr ML | 36% |
| Master’s | 49% |

**Typical stack (analytics-first)**

| Tool | 2020 |
|------|------|
| Python | 77% |
| SQL | **55%** |
| R | 32% |
| Scikit-learn | 50% |
| TensorFlow | 26% |
| PyTorch | 15% |
| XGBoost | 19% |

**Profile:** Strong SQL and solid Python; more R than engineers. Classical ML moderate; deep learning secondary. Higher women’s share than DS/ML Eng. More early-ML than pure DS roles.

**Implications:** Analyst programs should prioritize SQL + Python + visualization/stats, with optional sklearn — not DL-first curricula.

---

## 4. Software Engineer

| | 2020 | 2022 |
|--|------|------|
| n | 1,873 | 949 |
| Women | 13% | 14% |
| Under 1 yr ML | 34% | 32% |

**Typical stack**

| Tool | 2020 | 2022 |
|------|------|------|
| Python | 76% | 80% |
| SQL | 51% | 54% |
| Scikit-learn | 51% | 53% |
| TensorFlow | 40% | 41% |
| PyTorch | 25% | 28% |
| R | 8% | — |

**Profile:** Generalist builders. Python and SQL common; ML tools used but less intensely than DS/ML Eng. R is rare. A third still early in ML — many are adjacent to DS rather than specialized.

**Implications:** Bridge content (software eng → ML) should assume coding fluency, teach ML from sklearn upward, and not assume prior DL.

---

## 5. Student

| | 2020 |
|--|------|
| n | 4,912 |
| Women | 24% |
| Age 18–24 | ~78% |
| Under 1 yr ML | **45%** |
| Master’s | 30% |

**Typical stack**

| Tool | 2020 |
|------|------|
| Python | 84% |
| SQL | 27% |
| Scikit-learn | 46% |
| TensorFlow | 34% |
| PyTorch | 19% |
| R | 18% |

**Profile:** Largest clear cohort in 2020. Young, learner-heavy, Python-first, weaker SQL than working roles. High interest in DL frameworks relative to experience level.

**Implications:** Student content needs fundamentals (Python, basic stats, sklearn) before DL; SQL is a gap worth closing early.

---

## 6. Research Scientist

| | 2020 | 2022 |
|--|------|------|
| n | 1,114 | 573 |
| Women | 20% | 18% |
| Under 1 yr ML | 20% | 13% |

**Typical stack**

| Tool | 2020 | 2022 |
|------|------|------|
| Python | 80% | 83% |
| SQL | 22% | 22% |
| Scikit-learn | 57% | 62% |
| TensorFlow | 46% | 45% |
| PyTorch | 31% | **41%** |
| R | 28% | — |

**Profile:** Strong DL (PyTorch rising), moderate classical ML, **low SQL**. More academic tooling mix; R still relevant in 2020.

**Implications:** Research-oriented tracks can emphasize PyTorch and methods depth; SQL and production boosting stacks are less central than for industry DS.

---

## Cross-role snapshot (2020)

| Role | Python | SQL | Sklearn | PyTorch | Women | Early ML |
|------|--------|-----|---------|---------|-------|----------|
| Data Scientist | 92% | 55% | 76% | 28% | 16% | 17% |
| ML Engineer | 94% | 31% | 69% | 43% | 12% | 21% |
| Data Analyst | 77% | 55% | 50% | 15% | 24% | 36% |
| Software Engineer | 76% | 51% | 51% | 25% | 13% | 34% |
| Student | 84% | 27% | 46% | 19% | 24% | 45% |
| Research Scientist | 80% | 22% | 57% | 31% | 20% | 20% |

---

## Takeaways for hiring & learning design

1. **One stack does not fit all** — DS ≠ ML Eng ≠ Analyst.  
2. **Python is universal; SQL separates industry analytics/DS from research/student paths.**  
3. **PyTorch growth is strongest in ML Engineer and Research Scientist titles.**  
4. **Women’s representation is higher in Student/Analyst/Academic paths than in ML Engineer.**  
5. **Students need SQL and fundamentals more than more DL frameworks.**

---

*Related: `05_tooling_landscape.md` · `04_gender_gap_briefing.md` · `01_executive_one_pager.md`*
