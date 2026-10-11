"""
Kaggle Survey 2020 vs 2022 — Unified Web App
Home · Data Explorer · Reports

Run from this folder:
  streamlit run app.py
"""

from __future__ import annotations

import streamlit as st
from theme import apply_theme, render_theme_toggle

st.set_page_config(
    page_title="Kaggle Survey 2020 vs 2022",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

dark = render_theme_toggle()
apply_theme(dark)

st.markdown(
    """
    <div class="hero">
      <h1>Kaggle Survey 2020 vs 2022</h1>
      <p>Interactive data explorer and analytical reports from the cleaned ML &amp; DS surveys</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    Use the **sidebar** to open:

    | Page | What you get |
    |------|----------------|
    | **Data Explorer** | Filters, KPIs, demographics, tools, roles, experience charts, CSV download |
    | **Reports** | Executive one-pager, India deep-dive, role playbooks, gender briefing, tooling landscape, full insights |
    """
)

c1, c2 = st.columns(2)
with c1:
    st.markdown(
        """
        <div class="card">
          <h3>📊 Data Explorer</h3>
          <p>Filter by year, country, role, and gender. Compare distributions and download the filtered extract.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        """
        <div class="card">
          <h3>📑 Reports</h3>
          <p>Read decision-oriented briefs: headlines, India composition, role stacks, gender patterns, and tooling shifts.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    **Data:** Cleaned harmonized responses in `Datasets/cleaned/`  
    **Notebooks:** `Kernels/` · **Markdown sources:** `Reports/`
    """
)
st.markdown(
    """
    <p class="app-footer">
    Self-selected Kaggle community sample · Not population-representative ·
    Question wording changed between years · Compensation highly incomplete
    </p>
    """,
    unsafe_allow_html=True,
)
