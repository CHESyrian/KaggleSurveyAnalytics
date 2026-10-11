# Key Insights: Kaggle Survey 2020 vs 2022

**Sample:** ~19,000 usable responses in 2020 and ~23,200 in 2022 after cleaning (question-text row removed, exact duplicates dropped, extreme survey durations filtered).

---

## Demographics

- **Younger respondents gained share.** The 18–21 group rose from ~17% (2020) to ~19% (2022) and became the single largest age band in 2022, overtaking 25–29.
- **Gender imbalance eased only slightly.** Men fell from ~79% to ~76%; women rose from ~19% to ~22%. The gap remains large.
- Statistical tests confirm a real but **small** shift in age mix (Cramér’s V ≈ 0.05).
- **Women’s share is highest in the youngest cohorts.** In 2022, women are ~25–26% of 18–24 respondents vs ~21–22% of those aged 30+. The gender gap narrows at the entry level but reappears with age/seniority in the sample.

---

## Education & experience

- **Master’s remains the modal degree** (~40% → ~39%), followed by Bachelor’s (~36% → ~33%). Doctoral share is stable (~11–12%).
- **Most people are still early in ML.** About **44%** in both years report under 1 year of ML experience; another ~23–24% report 1–2 years. The community is still heavily weighted toward learners.
- Coding experience is harder to compare directly (2022 uses a “1–3 years” band), but early-career bands dominate both surveys.
- **ML inexperience is concentrated among the young.** Roughly 41–43% of 18–24 respondents report under 1 year of ML use, vs ~20–21% of respondents aged 40+.
- **Long coding tenure tracks with advanced degrees.** In 2022, ~18% of Doctoral respondents report 20+ years of coding vs ~3% of Bachelor’s and ~6% of Master’s. Conversely, Never / &lt;1 year coding is most common among Bachelor’s holders (~37%).
- **A non-trivial “never coded” group remains.** In 2022, ~8.5% report never having written code. That group is more gender-balanced (~35% women) than the overall sample and spans multiple age bands — consistent with business/analytics entrants exploring data science.

---

## Languages

- **Python is near-universal** (~78% in both years).
- **SQL grew** (38% → 40%); **R declined slightly** (22% → 19%).
- C++, Java, and JavaScript held roughly steady (~15–19%).
- **Python + SQL is the dominant dual stack** and is growing: 33% of respondents used both in 2020 vs **36%** in 2022.
- **Mean languages per respondent is low and stable** (~2.3 in 2020, ~2.2 in 2022). About 37–39% use 3+ languages; only ~8–9% use 5+.
- **Regional language stacks differ.** In 2022, U.S. respondents report higher SQL (49%) and R (32%) than India (SQL 39%, R 14%), while Python rates are similar (~77–78%).

---

## ML frameworks

- **Scikit-learn is still the workhorse** but slipped (51% → 48%).
- **TensorFlow and Keras declined** (TF 35% → 33%; Keras 31% → 28%).
- **PyTorch edged up** (21.0% → 21.7%) — a modest but consistent signal of the ecosystem shift toward PyTorch relative to the TF/Keras stack.
- XGBoost and LightGBM remain secondary (~19% and ~8–9%).
- **Deep-learning adoption is overlapping, not exclusive.** In 2022: ~19% use TensorFlow only, ~7% PyTorch only, and ~14% use both. Classical ML without DL remains common: ~15% use Scikit-learn with no TensorFlow, Keras, or PyTorch.
- **Boosting users are almost always Scikit-learn users.** Among XGBoost users in 2022, **92%** also report Scikit-learn; 40% also report PyTorch — a practical “full stack” pattern.
- **Framework count is modest.** Mean frameworks used: ~1.8 (2020) → ~1.7 (2022). Share reporting zero frameworks rose (37% → 41%), consistent with a larger learner / non-ML cohort.
- **Data Scientists run a much richer stack.** Among those labeled Data Scientist, Python exceeds 90%, Scikit-learn ~76–82%, XGBoost ~44–49%, and PyTorch ~28–34% — well above overall survey averages. Tool intensity for this role rose further between 2020 and 2022.

---

## Gender gaps in tools & roles

- **Tools (2022):** Men report higher regular use than women — Python 80% vs 70%, Scikit-learn 50% vs 39%, PyTorch 24% vs 14%, TensorFlow 35% vs 26%. These are descriptive sample patterns, not causal claims.
- **Roles (2020):** Women’s share is higher among Students (~24%) and Data Analysts (~24%) than among Data Scientists (~16%), Software Engineers (~13%), or ML Engineers (~12%). Research Scientists sit in between (~20%).
- **Roles (2022, clearer titles):** Academic / Teacher roles have the highest women’s share among professional groups (~32%). ML Engineer remains lowest (~10%). Data Scientist ~16%, Software Engineer ~14%, Manager / Executive ~12%.
- Pattern: women are better represented in education, student, and analyst roles than in engineering-titled ML roles within this sample.

---

## Roles & geography

- **Students** were the largest named group in 2020 (~26%). In 2022 many titles map less cleanly to the 2020 role list, so “Other” inflates — treat role YoY changes with caution.
- Among clearer titles, **Data Scientist**, **Software Engineer**, and **ML Engineer** remain core professional roles.
- **Early ML use varies sharply by role (2020).** Under 1 year / none is ~45% among Students, ~36% among Data Analysts, ~34% among Software Engineers, but only ~17% among Data Scientists and ~20–21% among ML Engineers and Research Scientists.
- **Age profiles differ by role.** Data Scientists and ML Engineers concentrate in the 25–39 range; Students (2020) are overwhelmingly 18–24 (~78% combined).
- **India’s share of responses rose sharply** (29% → 37%, +7.4 percentage points). The **United States** is second (~11–12%, slight increase). Pakistan, Egypt, Nigeria, Mexico, and Bangladesh also gained share.
- **Several high-income countries declined in share:** Germany, Russia, and the UK each dropped more than 1 percentage point. Japan’s share also fell. This is a change in *sample composition*, not necessarily in absolute participation.
- **Geographic concentration increased.** Top country share rose (29% → 37%); top-3 combined 47% → 55%; top-10 66% → 71%. India drives most of this concentration.
- **India’s sample is much younger than the U.S. sample.** In 2022, 18–24 is ~57% of India respondents vs a much flatter, older distribution in the U.S. (peak bands 25–39). Education mix also differs: India more Bachelor’s-heavy (42%), U.S. more Master’s- (45%) and Doctoral-heavy (16%).

---

## Company size (where reported)

- Among respondents who reported employer size, **small firms (0–49 employees)** shrank as a share (37% → 24%), while **large employers (1,000+ and 10,000+)** grew. The employed subset of the sample looks more “enterprise-weighted” in 2022 than in 2020.
- Many respondents leave company size blank (students, unemployed, non-response), so interpret only within the employed subset.

---

## Survey behavior

- **Median completion time fell** from ~10 minutes (2020) to ~7 minutes (2022). Mean times are higher (right-skewed), but the drop in median suggests a faster, possibly less detailed response pattern in 2022 — relevant when comparing free-text richness or multi-select depth.

---

## Compensation

- Non-response is high and rising (~46% missing in 2020, ~66% in 2022). Bands are also not fully comparable across years, so **no strong salary conclusions** should be drawn without careful imputation and caveats.
- Higher non-response in 2022 coincides with a younger, more student-heavy and geographically shifted sample — another reason salary tables are fragile.

---

## Tool diversity & segments

- Most respondents use a **small stack**: typically 1–3 languages and 0–2 frameworks.
- A simple experience/tool clustering separates a large **learner** segment, a **practitioner** middle, higher-diversity **polyglots**, and a smaller **veteran** group. That structure is fairly stable across the two years.
- Learners dominate the overall sample; professional roles (especially Data Scientist / ML Engineer) concentrate the practitioner and veteran segments.

---

## Method & caveats

- Self-selected Kaggle community sample — not representative of all data scientists globally.
- Role and experience category labels changed between survey waves; only high-confidence mappings are harmonized.
- Country “Other” and rare territories limit fine-grained geographic analysis.
- All percentages are of respondents in the cleaned sample (or stated subset), not of a population.
- Gender–tool and gender–role associations may reflect role mix, experience, and self-selection; they should not be read as causal.

---

## Bottom line

Between 2020 and 2022 the Kaggle community became slightly younger and a bit more gender-balanced, stayed heavily Master’s-educated and learner-heavy in ML, kept Python/SQL at the center, and showed a mild move from TensorFlow/Keras toward PyTorch. India’s weight in the sample grew markedly and made the overall sample younger and more geographically concentrated; several European and other high-income countries lost share. Tool use is much deeper among Data Scientists than in the sample overall; gender gaps in frameworks and engineering-titled roles remain visible. Survey completion got faster, and compensation data is too incomplete for firm claims.

---

*Source: harmonized extracts in `Datasets/cleaned/`; full analysis in `Kernels/03_kaggle_survey_2020_vs_2022_comparative.ipynb`.*
