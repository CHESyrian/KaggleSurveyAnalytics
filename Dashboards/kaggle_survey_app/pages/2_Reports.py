"""Reports page — part of unified Kaggle Survey app (dark mode + PDF export)."""

from __future__ import annotations

from pathlib import Path
import sys

import streamlit as st

# Allow imports from parent app folder
HOME_DIR = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(HOME_DIR))

from theme import apply_theme, render_theme_toggle
from pdf_export import markdown_to_pdf

st.set_page_config(
    page_title="Reports · Kaggle Survey",
    page_icon="📑",
    layout="wide",
    initial_sidebar_state="expanded",
)

REPORTS_DIR = HOME_DIR / "Reports"

REPORTS = [
    {
        "id": "executive",
        "title": "Executive One-Pager",
        "file": "01_executive_one_pager.md",
        "icon": "🎯",
        "desc": "Headline KPIs, three implications, what not to over-claim.",
        "audience": "Leadership · Product · Curriculum",
    },
    {
        "id": "india",
        "title": "India Deep-Dive",
        "file": "02_india_deep_dive.md",
        "icon": "🇮🇳",
        "desc": "How India’s growth reshapes age, education, tools, and global averages.",
        "audience": "Strategy · Regional programs",
    },
    {
        "id": "roles",
        "title": "Role Playbooks",
        "file": "03_role_playbooks.md",
        "icon": "👔",
        "desc": "Stacks and profiles for Data Scientist, ML Engineer, Analyst, and more.",
        "audience": "Hiring · Career · Learning design",
    },
    {
        "id": "gender",
        "title": "Gender Gap Briefing",
        "file": "04_gender_gap_briefing.md",
        "icon": "⚖️",
        "desc": "Representation by year, age, role, and tools — with clear caveats.",
        "audience": "Community · DEI · Programs",
    },
    {
        "id": "tooling",
        "title": "Tooling Landscape",
        "file": "05_tooling_landscape.md",
        "icon": "🛠️",
        "desc": "Language & framework shifts, stack patterns, audience recommendations.",
        "audience": "Educators · Platform · Content",
    },
    {
        "id": "insights",
        "title": "Full Key Insights",
        "file": "key_insights.md",
        "icon": "📊",
        "desc": "Complete insight compilation across all analysis themes.",
        "audience": "Analysts · Reference",
    },
]


@st.cache_data
def load_report(filename: str) -> str:
    path = REPORTS_DIR / filename
    if not path.exists():
        return f"*Report not found:* `{filename}`"
    return path.read_text(encoding="utf-8")


@st.cache_data
def build_pdf(filename: str, title: str) -> bytes:
    md = load_report(filename)
    return markdown_to_pdf(md, title=title)


def main():
    dark = render_theme_toggle()
    apply_theme(dark)

    with st.sidebar:
        st.markdown("### Reports")
        choice = st.radio(
            "Select a report",
            options=["Home"] + [r["title"] for r in REPORTS],
            index=0,
            label_visibility="collapsed",
        )
        st.divider()
        st.caption("Kaggle ML & DS Surveys · 2020 · 2022")
        st.caption("Self-selected sample · Not population-representative")

    st.markdown(
        """
        <div class="app-header">
          <h1>Reports</h1>
          <p>Executive briefs, India deep-dive, role playbooks, gender &amp; tooling</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if choice == "Home":
        st.markdown(
            "Browse analytical reports from the cleaned surveys. "
            "Open a report in the sidebar, download **Markdown** or **PDF**."
        )
        st.markdown("### Available reports")
        for r in REPORTS:
            st.markdown(
                f"""
                <div class="report-card">
                  <h3>{r["icon"]} {r["title"]}</h3>
                  <p class="desc">{r["desc"]}</p>
                  <p class="aud">{r["audience"]}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        st.info("Select a report in the sidebar to read it and export PDF.")
        st.markdown(
            """
            <div class="app-footer">
              Sources: <code>Reports/</code> · Data: <code>Datasets/cleaned/</code>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    report = next(r for r in REPORTS if r["title"] == choice)
    st.markdown(f"**{report['icon']} {report['title']}** · {report['audience']}")
    st.caption(report["desc"])

    md = load_report(report["file"])
    pdf_bytes = build_pdf(report["file"], report["title"])

    c1, c2, c3 = st.columns([1.2, 1.2, 2])
    with c1:
        st.download_button(
            "Download Markdown",
            data=md.encode("utf-8"),
            file_name=report["file"],
            mime="text/markdown",
            use_container_width=True,
        )
    with c2:
        st.download_button(
            "Download PDF",
            data=pdf_bytes,
            file_name=report["file"].replace(".md", ".pdf"),
            mime="application/pdf",
            use_container_width=True,
        )

    st.divider()
    st.markdown(md)

    st.markdown(
        """
        <div class="app-footer">
          Descriptive findings from a self-selected Kaggle community sample.
          Not causal estimates and not representative of the global data-science workforce.
        </div>
        """,
        unsafe_allow_html=True,
    )


main()
