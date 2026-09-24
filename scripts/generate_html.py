#!/usr/bin/env python3
"""
HTML Documentation Generator for 4.0m x 3.0m Freestanding Pergola Project.
Converts Markdown files into styled, responsive HTML pages with navigation,
print styles, embedded SVG diagrams, and a unified all-in-one printable manual.
"""

import os
import re
import sys
from pathlib import Path

import markdown_it
from mdit_py_plugins.dollarmath import dollarmath_plugin
from mdit_py_plugins.tasklists import tasklists_plugin

# Project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Files configuration
PAGES = [
    {
        "src": "README.md",
        "dest": "index.html",
        "title": "Master Overview & Plan",
        "short_title": "Overview",
        "diagrams": ["diagrams/elevation_and_plan.svg"]
    },
    {
        "src": "01_PROJECT_SPECIFICATIONS.md",
        "dest": "01_PROJECT_SPECIFICATIONS.html",
        "title": "01 — Project Specifications",
        "short_title": "01 Specs",
        "diagrams": ["diagrams/elevation_and_plan.svg"]
    },
    {
        "src": "02_BILL_OF_MATERIALS.md",
        "dest": "02_BILL_OF_MATERIALS.html",
        "title": "02 — Bill of Materials (BOM)",
        "short_title": "02 Materials",
        "diagrams": []
    },
    {
        "src": "03_CUT_LIST_AND_TIMBER_OPTIMIZATION.md",
        "dest": "03_CUT_LIST_AND_TIMBER_OPTIMIZATION.html",
        "title": "03 — Cut List & Timber Optimization",
        "short_title": "03 Cut List",
        "diagrams": []
    },
    {
        "src": "04_JOINERY_AND_CONNECTION_DETAILS.md",
        "dest": "04_JOINERY_AND_CONNECTION_DETAILS.html",
        "title": "04 — Joinery & Connection Details",
        "short_title": "04 Joinery",
        "diagrams": ["diagrams/joinery_details.svg"]
    },
    {
        "src": "05_STEP_BY_STEP_BUILD_GUIDE.md",
        "dest": "05_STEP_BY_STEP_BUILD_GUIDE.html",
        "title": "05 — Step-by-Step Construction Guide",
        "short_title": "05 Build Guide",
        "diagrams": []
    },
    {
        "src": "06_TOOL_AND_SAFETY_CHECKLIST.md",
        "dest": "06_TOOL_AND_SAFETY_CHECKLIST.html",
        "title": "06 — Tool & Safety Checklist",
        "short_title": "06 Tools",
        "diagrams": []
    },
]

# Relative path to standalone stylesheet
CSS_REL_PATH = "css/styles.css"


def create_markdown_parser():
    md = markdown_it.MarkdownIt("commonmark").enable("table").enable("strikethrough")
    tasklists_plugin(md)
    dollarmath_plugin(md)
    return md

def post_process_html(html_content, current_page_dest=""):
    # 1. Wrap tables in responsive wrapper
    html_content = re.sub(
        r"(<table>.*?</table>)",
        r'<div class="table-wrapper">\1</div>',
        html_content,
        flags=re.DOTALL
    )

    # 2. Transform GitHub Alerts into styled callout blocks
    alert_types = {
        "NOTE": ("callout-note", "ℹ️", "Note"),
        "TIP": ("callout-tip", "💡", "Tip"),
        "IMPORTANT": ("callout-important", "📌", "Important"),
        "WARNING": ("callout-warning", "⚠️", "Warning"),
        "CAUTION": ("callout-caution", "🛑", "Caution"),
    }

    def replace_alert(match):
        kind = match.group(1).upper()
        body = match.group(2).strip()
        css_class, icon, label = alert_types.get(kind, ("callout-note", "ℹ️", kind.capitalize()))
        return f'<div class="callout {css_class}"><div class="callout-header"><span class="callout-icon">{icon}</span> {label}</div><div class="callout-body"><p>{body}</p></div></div>'

    # Pattern matches <blockquote><p>[!TYPE]\nBody...</p></blockquote>
    alert_pattern = re.compile(
        r'<blockquote>\s*<p>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*<br\s*/?>?\s*(.*?)</p>\s*</blockquote>',
        re.DOTALL | re.IGNORECASE
    )
    html_content = alert_pattern.sub(replace_alert, html_content)

    # Also handle single-line alert without <br>
    alert_pattern_simple = re.compile(
        r'<blockquote>\s*<p>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*(.*?)</p>\s*</blockquote>',
        re.DOTALL | re.IGNORECASE
    )
    html_content = alert_pattern_simple.sub(replace_alert, html_content)

    # 3. Rewrite internal links
    # Rewrite file:///Users/.../foo.md or relative foo.md to foo.html
    def rewrite_link(match):
        href = match.group(1)
        # Normalize
        filename = href.split("/")[-1]
        if filename == "README.md":
            return 'href="index.html"'
        elif filename.endswith(".md"):
            return f'href="{filename[:-3]}.html"'
        return match.group(0)

    html_content = re.sub(r'href="([^"]+\.md)"', rewrite_link, html_content)

    # 4. Format math spans
    html_content = re.sub(
        r'<span class="math inline">\\sqrt\{(.*?)\}</span>',
        r'<span class="math-inline">√(\1)</span>',
        html_content
    )
    html_content = re.sub(
        r'<span class="math inline">(.*?)</span>',
        r'<span class="math-inline">\1</span>',
        html_content
    )

    return html_content

def build_header(current_dest):
    nav_items = []
    for page in PAGES:
        active_class = " active" if page["dest"] == current_dest else ""
        nav_items.append(
            f'<a href="{page["dest"]}" class="nav-item{active_class}">{page["short_title"]}</a>'
        )

    all_in_one_active = " active" if current_dest == "complete_build_manual.html" else ""
    nav_items.append(
        f'<a href="complete_build_manual.html" class="nav-item{all_in_one_active}" style="font-weight:700; color:var(--brand);">📖 Full Manual</a>'
    )

    nav_html = "\n".join(nav_items)

    return f"""
<header class="site-header">
  <div class="header-container">
    <a href="index.html" class="logo-area">
      <span class="logo-icon">🌲</span>
      <span>Pergola 4×3m Build Plan</span>
    </a>
    <nav class="nav-links">
      {nav_html}
    </nav>
    <div class="header-actions">
      <button class="btn-action" onclick="toggleTheme()" title="Toggle Dark/Light Mode">🌓 Mode</button>
      <button class="btn-action btn-action-primary" onclick="window.print()" title="Print Current Document">🖨️ Print</button>
    </div>
  </div>
</header>
"""

THEME_SCRIPT = """
<script>
  function initTheme() {
    const saved = localStorage.getItem('pergola-theme');
    if (saved) {
      document.documentElement.setAttribute('data-theme', saved);
    } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      document.documentElement.setAttribute('data-theme', 'dark');
    }
  }
  function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme');
    const target = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', target);
    localStorage.setItem('pergola-theme', target);
  }
  initTheme();
</script>
"""

def generate_individual_pages(md_parser):
    print("Generating individual HTML pages...")
    for page in PAGES:
        src_path = BASE_DIR / page["src"]
        dest_path = BASE_DIR / page["dest"]

        if not src_path.exists():
            print(f"Warning: {src_path} does not exist, skipping.")
            continue

        raw_md = src_path.read_text(encoding="utf-8")
        parsed_html = md_parser.render(raw_md)
        body_html = post_process_html(parsed_html, page["dest"])

        # Insert diagrams if specified
        diagram_html = ""
        for diag in page["diagrams"]:
            diag_file = Path(diag).name
            diagram_html += f"""
<div class="diagram-card">
  <img src="{diag}" alt="{diag_file}" loading="lazy" />
  <div class="diagram-caption">Architectural Drawing: {diag_file}</div>
</div>
"""
        if diagram_html:
            # Place after first h1 or h2
            parts = body_html.split("</h1>", 1)
            if len(parts) == 2:
                body_html = parts[0] + "</h1>" + diagram_html + parts[1]
            else:
                body_html = diagram_html + body_html

        full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page["title"]} — Pergola 4x3m</title>
  <link rel="stylesheet" href="{CSS_REL_PATH}">
</head>
<body>
  {build_header(page["dest"])}
  <main class="page-container">
    {body_html}
  </main>
  {THEME_SCRIPT}
</body>
</html>
"""
        dest_path.write_text(full_html, encoding="utf-8")
        print(f"  ✓ Written: {page['dest']}")

def generate_unified_manual(md_parser):
    print("Generating unified printable manual (complete_build_manual.html)...")
    combined_body = """
<div style="text-align:center; padding: 40px 0 20px 0;">
  <h1 style="font-size:2.8rem; margin-bottom:8px;">🌲 4.0 m × 3.0 m Freestanding Pergola</h1>
  <p style="font-size:1.2rem; color:var(--brand); font-weight:600;">Complete Master Construction Handbook & Architectural Specifications</p>
  <p style="color:var(--text-muted);">Author: John Tobin & Antigravity Pair Programming | Location: Ireland/UK Patio Build</p>
</div>
<hr />
"""

    for idx, page in enumerate(PAGES):
        src_path = BASE_DIR / page["src"]
        if not src_path.exists():
            continue

        raw_md = src_path.read_text(encoding="utf-8")
        parsed_html = md_parser.render(raw_md)
        section_html = post_process_html(parsed_html, "complete_build_manual.html")

        # Diagram insertion for manual
        diagram_html = ""
        for diag in page["diagrams"]:
            diag_file = Path(diag).name
            diagram_html += f"""
<div class="diagram-card">
  <img src="{diag}" alt="{diag_file}" loading="lazy" />
  <div class="diagram-caption">Architectural Drawing: {diag_file}</div>
</div>
"""
        if diagram_html:
            parts = section_html.split("</h1>", 1)
            if len(parts) == 2:
                section_html = parts[0] + "</h1>" + diagram_html + parts[1]
            else:
                section_html = diagram_html + section_html

        page_break = ' class="page-break"' if idx > 0 else ""
        combined_body += f"""
<section id="section-{idx}"{page_break} style="margin-top: 40px;">
  {section_html}
</section>
<hr />
"""

    dest_path = BASE_DIR / "complete_build_manual.html"
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Complete Master Build Manual — 4x3m Pergola</title>
  <link rel="stylesheet" href="{CSS_REL_PATH}">
</head>
<body>
  {build_header("complete_build_manual.html")}
  <main class="page-container">
    {combined_body}
  </main>
  {THEME_SCRIPT}
</body>
</html>
"""
    dest_path.write_text(full_html, encoding="utf-8")
    print("  ✓ Written: complete_build_manual.html")

def main():
    md = create_markdown_parser()
    generate_individual_pages(md)
    generate_unified_manual(md)
    print("\nAll HTML documents generated successfully!")

if __name__ == "__main__":
    main()
