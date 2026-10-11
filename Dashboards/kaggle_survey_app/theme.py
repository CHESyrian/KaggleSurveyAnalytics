"""Shared theme (dark/light) helpers for the unified Kaggle Survey app."""

from __future__ import annotations

import streamlit as st

# Single source of truth for the toggle widget key
THEME_KEY = "dark_mode"

LIGHT_CSS = """
<style>
.block-container { padding-top: 1.5rem; }
.app-header, .hero {
    background: linear-gradient(135deg, #1B3A4B 0%, #2C5F7A 100%) !important;
    color: #fff !important;
    padding: 1.5rem 1.75rem;
    border-radius: 12px;
    margin-bottom: 1.25rem;
    box-shadow: 0 4px 14px rgba(27,58,75,0.25);
    border: none !important;
}
.app-header h1, .hero h1 { margin: 0 0 0.35rem 0; font-size: 1.65rem; color: #fff !important; }
.app-header p, .hero p { margin: 0; color: #A8C5D4 !important; font-size: 0.95rem; }
.report-card, .card {
    background: #fff !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 10px;
    padding: 1.1rem 1.25rem;
    margin-bottom: 0.85rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}
.report-card h3, .card h3 { margin: 0 0 0.35rem 0; font-size: 1.1rem; color: #1B3A4B !important; }
.report-card .desc, .card p { color: #475569 !important; font-size: 0.9rem; margin: 0 0 0.4rem 0; }
.report-card .aud { color: #2A9D8F !important; font-size: 0.8rem; font-weight: 600; margin: 0; }
.app-footer { margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #E2E8F0; color: #94A3B8 !important; font-size: 0.82rem; }
</style>
"""

DARK_CSS = """
<style>
/* Base surfaces */
.stApp, [data-testid="stAppViewContainer"] {
    background-color: #0F172A !important;
}
.block-container { padding-top: 1.5rem; }
[data-testid="stHeader"] { background: #0F172A !important; }
[data-testid="stSidebar"] {
    background-color: #1E293B !important;
}
[data-testid="stSidebar"] .stMarkdown p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] span {
    color: #E2E8F0 !important;
}

/* Custom banners */
.app-header, .hero {
    background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%) !important;
    color: #F1F5F9 !important;
    padding: 1.5rem 1.75rem;
    border-radius: 12px;
    margin-bottom: 1.25rem;
    border: 1px solid #334155 !important;
    box-shadow: none !important;
}
.app-header h1, .hero h1 { margin: 0 0 0.35rem 0; font-size: 1.65rem; color: #F8FAFC !important; }
.app-header p, .hero p { margin: 0; color: #94A3B8 !important; font-size: 0.95rem; }

/* Cards */
.report-card, .card {
    background: #1E293B !important;
    border: 1px solid #334155 !important;
    border-radius: 10px;
    padding: 1.1rem 1.25rem;
    margin-bottom: 0.85rem;
    box-shadow: none !important;
}
.report-card h3, .card h3 { margin: 0 0 0.35rem 0; font-size: 1.1rem; color: #F1F5F9 !important; }
.report-card .desc, .card p { color: #94A3B8 !important; font-size: 0.9rem; margin: 0 0 0.4rem 0; }
.report-card .aud { color: #2DD4BF !important; font-size: 0.8rem; font-weight: 600; margin: 0; }

.app-footer {
    margin-top: 2rem;
    padding-top: 1rem;
    border-top: 1px solid #334155 !important;
    color: #64748B !important;
    font-size: 0.82rem;
}

/* Main markdown */
div[data-testid="stMarkdownContainer"] p,
div[data-testid="stMarkdownContainer"] li {
    color: #E2E8F0 !important;
}
div[data-testid="stMarkdownContainer"] h1,
div[data-testid="stMarkdownContainer"] h2 {
    color: #F8FAFC !important;
}
div[data-testid="stMarkdownContainer"] h3 {
    color: #2DD4BF !important;
}
div[data-testid="stMarkdownContainer"] code {
    background: #334155 !important;
    color: #E2E8F0 !important;
}

/* Metrics */
[data-testid="stMetricValue"] { color: #F1F5F9 !important; }
[data-testid="stMetricLabel"] { color: #94A3B8 !important; }
[data-testid="stCaption"] { color: #94A3B8 !important; }

/* Tabs & expanders */
button[data-baseweb="tab"] { color: #E2E8F0 !important; }
div[data-testid="stExpander"] {
    background: #1E293B !important;
    border-color: #334155 !important;
}

/* Dataframes */
[data-testid="stDataFrame"] { background: #1E293B !important; }

/* Info/warning boxes */
div[data-testid="stAlert"] { background-color: #1E293B !important; color: #E2E8F0 !important; }
</style>
"""


def is_dark() -> bool:
    """Current dark-mode flag (defaults to False)."""
    return bool(st.session_state.get(THEME_KEY, False))


def render_theme_toggle() -> bool:
    """
    Sidebar dark-mode toggle.

    Uses a single session_state key (THEME_KEY) as the widget key so Streamlit
    owns the value — do not also pass value= (that causes reset/flicker bugs).
    """
    if THEME_KEY not in st.session_state:
        st.session_state[THEME_KEY] = False

    st.sidebar.markdown("---")
    st.sidebar.toggle(
        "Dark mode",
        key=THEME_KEY,
        help="Switch between light and dark appearance",
    )
    return bool(st.session_state[THEME_KEY])


def apply_theme(dark: bool | None = None) -> None:
    """Inject light or dark CSS into the page."""
    if dark is None:
        dark = is_dark()
    st.markdown(DARK_CSS if dark else LIGHT_CSS, unsafe_allow_html=True)


def plotly_template(dark: bool | None = None) -> str:
    if dark is None:
        dark = is_dark()
    return "plotly_dark" if dark else "plotly_white"
