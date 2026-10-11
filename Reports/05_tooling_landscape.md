# Tooling Landscape: Languages & Frameworks 2020 → 2022

**Focus:** What the Kaggle community actually reports using regularly — and what shifted in two years.

---

## 1. Programming languages

| Language | 2020 | 2022 | Change |
|----------|------|------|--------|
| **Python** | 77.8% | 77.9% | Flat — universal baseline |
| **SQL** | 37.7% | **40.2%** | **+2.5 pp** |
| R | 21.5% | 19.1% | −2.4 pp |
| C++ | 19.1% | 19.0% | Flat |
| Java | 16.8% | 16.2% | Slight down |
| JavaScript | 15.0% | 14.6% | Flat |
| Bash | — | present | Secondary scripting |
| MATLAB / Julia | Low single digits | Low | Niche |

### Key language insights

- **Python is non-negotiable** for this community. Curriculum and platforms can treat it as the default.  
- **SQL is the clear #2 and still growing.** The Python + SQL dual stack rose from **33% → 36%** of respondents.  
- **R is slowly losing share**, especially outside research-heavy and U.S. segments (India R use is only ~14% in 2022).  
- Breadth is limited: mean languages per person ≈ **2.2–2.3**; only ~8–9% use 5+.

---

## 2. ML frameworks

| Framework | 2020 | 2022 | Change |
|-----------|------|------|--------|
| **Scikit-learn** | 51.3% | 47.8% | −3.5 pp (still #1) |
| **TensorFlow** | 34.7% | 33.2% | −1.5 pp |
| **Keras** | 31.0% | 27.5% | −3.5 pp |
| **PyTorch** | 21.0% | **21.7%** | **+0.7 pp** |
| XGBoost | 19.8% | 18.7% | −1.1 pp |
| LightGBM | 9.1% | 8.0% | −1.1 pp |
| CatBoost / Fast.ai / JAX | Lower single digits | Lower | Niche / emerging |

### Key framework insights

- **Scikit-learn remains the workhorse** despite a modest decline — still nearly half of respondents.  
- **TensorFlow + Keras are sliding**; PyTorch is the only major framework with a clear upward tick.  
- Absolute PyTorch gain is small at the full-sample level, but **much larger inside ML Engineer and Research Scientist roles** (see role playbooks).  
- Mean frameworks per person ≈ **1.7–1.8**; share with **zero frameworks rose** (37% → 41%), consistent with more learners / non-ML respondents.

---

## 3. Stack patterns (2022)

| Pattern | Share of sample (approx.) | Meaning |
|---------|---------------------------|---------|
| TensorFlow only (no PyTorch) | ~19% | Legacy / TF-centric DL |
| PyTorch only (no TF) | ~7% | PyTorch-native path |
| Both TF and PyTorch | ~14% | Multi-framework practitioners |
| Scikit-learn without TF/Keras/PyTorch | ~15% | Classical ML without DL |
| XGBoost users who also use sklearn | **92%** | Boosting sits on a sklearn base |

**Practical default stacks observed**

1. **Learner / analyst:** Python → SQL → Scikit-learn  
2. **Industry DS:** Python + SQL + sklearn + XGBoost (+ optional TF or PT)  
3. **ML Engineer:** Python + PyTorch and/or TensorFlow + sklearn  
4. **Research:** Python + PyTorch (rising) + sklearn; less SQL  

---

## 4. Who drives the PyTorch signal?

Full-sample PyTorch use only edged up (+0.7 pp), but:

| Role | PyTorch 2020 | PyTorch 2022 |
|------|--------------|--------------|
| ML Engineer | 43% | **57%** |
| Research Scientist | 31% | **41%** |
| Data Scientist | 28% | **34%** |

The ecosystem shift is **concentrated among specialist roles**, not uniform across students and analysts. Product and course decisions should segment by audience.

---

## 5. Regional tool differences (2022)

| Tool | India | Rest of world |
|------|-------|---------------|
| Python | 78% | 78% |
| SQL | 39% | 41% |
| R | **14%** | **22%** |
| Scikit-learn | 46% | 49% |
| PyTorch | **17%** | **24%** |
| TensorFlow | 33% | 34% |

India matches on Python/SQL/TF but lags on R and PyTorch — relevant if you localize content by geography.

---

## 6. Recommendations by audience

| Audience | Prioritize | Deprioritize / optional |
|----------|------------|-------------------------|
| **Beginners / students** | Python, SQL, Scikit-learn | Early DL frameworks |
| **Data Analysts** | SQL, Python, sklearn, viz | Heavy DL, multi-framework |
| **Data Scientists** | Python, SQL, sklearn, XGBoost, one DL framework | — |
| **ML Engineers** | Python, PyTorch (and/or TF), sklearn | R |
| **Researchers** | Python, PyTorch, methods depth | SQL-first paths |
| **Global content** | Python + SQL as universal | Assuming R is default outside research |

---

## 7. Caveats

- “Regular use” is self-reported; intensity and proficiency are unknown.  
- Multi-select questions allow stacking; percentages are not mutually exclusive.  
- Framework lists differ slightly by year; only common items are compared.  
- Sample composition shifted (more India, younger) — some framework rate changes may be compositional.

---

*Related: `03_role_playbooks.md` · `02_india_deep_dive.md` · `01_executive_one_pager.md` · `Reports/key_insights.md`*
