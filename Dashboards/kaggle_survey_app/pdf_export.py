"""Markdown → PDF export using reportlab."""

from __future__ import annotations

import re
from io import BytesIO
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
    HRFlowable,
    KeepTogether,
)


def _styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "TitleCustom",
            parent=base["Heading1"],
            fontSize=16,
            textColor=colors.HexColor("#1B3A4B"),
            spaceAfter=10,
            spaceBefore=4,
        ),
        "h1": ParagraphStyle(
            "H1Custom",
            parent=base["Heading1"],
            fontSize=14,
            textColor=colors.HexColor("#1B3A4B"),
            spaceBefore=14,
            spaceAfter=8,
        ),
        "h2": ParagraphStyle(
            "H2Custom",
            parent=base["Heading2"],
            fontSize=12,
            textColor=colors.HexColor("#1B3A4B"),
            spaceBefore=12,
            spaceAfter=6,
        ),
        "h3": ParagraphStyle(
            "H3Custom",
            parent=base["Heading3"],
            fontSize=11,
            textColor=colors.HexColor("#2C5F7A"),
            spaceBefore=8,
            spaceAfter=4,
        ),
        "body": ParagraphStyle(
            "BodyCustom",
            parent=base["Normal"],
            fontSize=9.5,
            leading=13,
            textColor=colors.HexColor("#1A1A1A"),
            spaceAfter=4,
        ),
        "bullet": ParagraphStyle(
            "BulletCustom",
            parent=base["Normal"],
            fontSize=9.5,
            leading=13,
            leftIndent=12,
            textColor=colors.HexColor("#1A1A1A"),
            spaceAfter=2,
        ),
        "muted": ParagraphStyle(
            "MutedCustom",
            parent=base["Normal"],
            fontSize=8,
            textColor=colors.HexColor("#6B6560"),
            spaceBefore=8,
        ),
    }


def _escape(text: str) -> str:
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # bold/italic markdown
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*(.+?)\*", r"<i>\1</i>", text)
    text = re.sub(r"`(.+?)`", r"<font face='Courier' size='8'>\1</font>", text)
    return text


def _parse_table(lines: list[str]) -> list[list[str]] | None:
    rows = []
    for line in lines:
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if all(re.match(r"^:?-+:?$", c) for c in cells):
            continue  # separator
        rows.append(cells)
    return rows or None


def markdown_to_pdf(md_text: str, title: str = "Report") -> bytes:
    """Convert a simple Markdown document to PDF bytes."""
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=16 * mm,
        bottomMargin=16 * mm,
        title=title,
    )
    styles = _styles()
    story = []

    lines = md_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            story.append(Spacer(1, 4))
            i += 1
            continue

        if stripped.startswith("# "):
            story.append(Paragraph(_escape(stripped[2:]), styles["title"]))
            story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#2A9D8F")))
            i += 1
            continue
        if stripped.startswith("## "):
            story.append(Paragraph(_escape(stripped[3:]), styles["h1"]))
            i += 1
            continue
        if stripped.startswith("### "):
            story.append(Paragraph(_escape(stripped[4:]), styles["h2"]))
            i += 1
            continue
        if stripped.startswith("#### "):
            story.append(Paragraph(_escape(stripped[5:]), styles["h3"]))
            i += 1
            continue

        if stripped.startswith("---"):
            story.append(Spacer(1, 4))
            story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#D4CBBE")))
            story.append(Spacer(1, 4))
            i += 1
            continue

        if stripped.startswith("|"):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            rows = _parse_table(table_lines)
            if rows:
                # paragraph-wrap cells
                data = [[Paragraph(_escape(c), styles["body"]) for c in row] for row in rows]
                col_count = max(len(r) for r in data)
                for row in data:
                    while len(row) < col_count:
                        row.append(Paragraph("", styles["body"]))
                avail = A4[0] - 36 * mm
                col_w = avail / col_count
                t = Table(data, colWidths=[col_w] * col_count, repeatRows=1)
                t.setStyle(
                    TableStyle(
                        [
                            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1B3A4B")),
                            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                            ("FONTSIZE", (0, 0), (-1, -1), 8),
                            ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#D4CBBE")),
                            ("VALIGN", (0, 0), (-1, -1), "TOP"),
                            ("LEFTPADDING", (0, 0), (-1, -1), 4),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                            ("TOPPADDING", (0, 0), (-1, -1), 3),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F7F4EF")]),
                        ]
                    )
                )
                story.append(KeepTogether([t, Spacer(1, 8)]))
            continue

        if stripped.startswith("- ") or stripped.startswith("* "):
            story.append(Paragraph("• " + _escape(stripped[2:]), styles["bullet"]))
            i += 1
            continue

        if re.match(r"^\d+\.\s", stripped):
            story.append(Paragraph(_escape(stripped), styles["bullet"]))
            i += 1
            continue

        if stripped.startswith("*") and stripped.endswith("*") and not stripped.startswith("**"):
            story.append(Paragraph(_escape(stripped), styles["muted"]))
            i += 1
            continue

        story.append(Paragraph(_escape(stripped), styles["body"]))
        i += 1

    story.append(Spacer(1, 12))
    story.append(
        Paragraph(
            "Source: Kaggle ML &amp; DS Survey analysis · Self-selected sample · Not population-representative",
            styles["muted"],
        )
    )

    doc.build(story)
    return buffer.getvalue()


def report_file_to_pdf(path: Path, title: str) -> bytes:
    text = path.read_text(encoding="utf-8")
    return markdown_to_pdf(text, title=title)
