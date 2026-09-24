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

CSS_STYLES = """
:root {
  --bg-primary: #ffffff;
  --bg-secondary: #f8fafc;
  --bg-tertiary: #f1f5f9;
  --text-primary: #0f172a;
  --text-secondary: #475569;
  --text-muted: #64748b;
  --border: #e2e8f0;
  --border-subtle: #cbd5e1;
  --brand: #d97706;
  --brand-hover: #b45309;
  --brand-light: #fef3c7;
  --accent-blue: #0284c7;
  --accent-green: #059669;
  --accent-purple: #7c3aed;
  --accent-red: #dc2626;
  --code-bg: #0f172a;
  --code-text: #f8fafc;
  --card-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.08), 0 2px 4px -2px rgb(0 0 0 / 0.06);
}

[data-theme="dark"] {
  --bg-primary: #0b1120;
  --bg-secondary: #0f172a;
  --bg-tertiary: #1e293b;
  --text-primary: #f8fafc;
  --text-secondary: #cbd5e1;
  --text-muted: #94a3b8;
  --border: #334155;
  --border-subtle: #475569;
  --brand: #f59e0b;
  --brand-hover: #d97706;
  --brand-light: #78350f40;
  --accent-blue: #38bdf8;
  --accent-green: #34d399;
  --accent-purple: #a78bfa;
  --accent-red: #f87171;
  --code-bg: #030712;
  --code-text: #f8fafc;
  --card-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.3);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  line-height: 1.65;
  color: var(--text-primary);
  background-color: var(--bg-primary);
  transition: background-color 0.2s, color 0.2s;
  padding-bottom: 80px;
}

/* Header & Navigation */
header.site-header {
  position: sticky;
  top: 0;
  z-index: 100;
  background-color: var(--bg-secondary);
  border-bottom: 1px solid var(--border);
  box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.05);
}

.header-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 12px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
}

.logo-area {
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  color: var(--text-primary);
  font-weight: 700;
  font-size: 1.15rem;
}

.logo-icon {
  font-size: 1.4rem;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 6px;
  flex-wrap: wrap;
}

.nav-item {
  text-decoration: none;
  color: var(--text-secondary);
  font-size: 0.88rem;
  font-weight: 500;
  padding: 6px 12px;
  border-radius: 6px;
  transition: all 0.15s ease-in-out;
}

.nav-item:hover {
  background-color: var(--bg-tertiary);
  color: var(--brand);
}

.nav-item.active {
  background-color: var(--brand);
  color: #ffffff;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.btn-action {
  background: var(--bg-tertiary);
  border: 1px solid var(--border);
  color: var(--text-primary);
  padding: 6px 12px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.85rem;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  text-decoration: none;
  transition: all 0.15s;
}

.btn-action:hover {
  border-color: var(--brand);
  color: var(--brand);
}

.btn-action-primary {
  background-color: var(--brand);
  color: #fff;
  border-color: var(--brand);
}

.btn-action-primary:hover {
  background-color: var(--brand-hover);
  color: #fff;
}

/* Main Layout */
.page-container {
  max-width: 980px;
  margin: 32px auto;
  padding: 0 24px;
}

/* Typography */
h1 {
  font-size: 2.2rem;
  line-height: 1.25;
  color: var(--text-primary);
  margin-top: 10px;
  margin-bottom: 16px;
  font-weight: 800;
  letter-spacing: -0.02em;
}

h2 {
  font-size: 1.5rem;
  line-height: 1.3;
  color: var(--text-primary);
  margin-top: 36px;
  margin-bottom: 16px;
  padding-bottom: 8px;
  border-bottom: 1px solid var(--border);
  font-weight: 700;
}

h3 {
  font-size: 1.2rem;
  margin-top: 24px;
  margin-bottom: 12px;
  color: var(--text-primary);
  font-weight: 600;
}

p {
  margin-bottom: 16px;
  color: var(--text-secondary);
}

hr {
  border: 0;
  border-top: 1px solid var(--border);
  margin: 32px 0;
}

ul, ol {
  margin-left: 24px;
  margin-bottom: 18px;
  color: var(--text-secondary);
}

li {
  margin-bottom: 6px;
}

a {
  color: var(--accent-blue);
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

/* Tables */
.table-wrapper {
  overflow-x: auto;
  margin: 20px 0 28px 0;
  border: 1px solid var(--border);
  border-radius: 8px;
  box-shadow: var(--card-shadow);
  background: var(--bg-primary);
}

table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
  font-size: 0.92rem;
}

thead th {
  background-color: var(--bg-secondary);
  color: var(--text-primary);
  font-weight: 600;
  padding: 12px 16px;
  border-bottom: 2px solid var(--border);
  white-space: nowrap;
}

tbody td {
  padding: 10px 16px;
  border-bottom: 1px solid var(--border);
  color: var(--text-secondary);
}

tbody tr:last-child td {
  border-bottom: none;
}

tbody tr:nth-child(even) {
  background-color: var(--bg-secondary);
}

tbody tr:hover {
  background-color: var(--bg-tertiary);
}

/* Code & Pre Blocks */
pre {
  background-color: var(--code-bg);
  color: var(--code-text);
  padding: 18px 20px;
  border-radius: 8px;
  overflow-x: auto;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
  font-size: 0.88rem;
  line-height: 1.5;
  margin: 18px 0 24px 0;
  border: 1px solid var(--border-subtle);
}

code {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 0.88em;
  background-color: var(--bg-tertiary);
  color: var(--brand);
  padding: 2px 6px;
  border-radius: 4px;
}

pre code {
  background-color: transparent;
  color: inherit;
  padding: 0;
}

/* Callouts */
.callout {
  border-left: 4px solid;
  border-radius: 6px;
  padding: 16px 20px;
  margin: 20px 0;
  background-color: var(--bg-secondary);
}

.callout-header {
  font-weight: 700;
  font-size: 0.95rem;
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.callout-body {
  font-size: 0.92rem;
  color: var(--text-secondary);
}

.callout-body p:last-child {
  margin-bottom: 0;
}

.callout-note {
  border-color: var(--accent-blue);
  background-color: var(--bg-secondary);
}
.callout-note .callout-header { color: var(--accent-blue); }

.callout-tip {
  border-color: var(--accent-green);
  background-color: var(--bg-secondary);
}
.callout-tip .callout-header { color: var(--accent-green); }

.callout-important {
  border-color: var(--accent-purple);
  background-color: var(--bg-secondary);
}
.callout-important .callout-header { color: var(--accent-purple); }

.callout-warning, .callout-caution {
  border-color: var(--accent-red);
  background-color: var(--bg-secondary);
}
.callout-warning .callout-header, .callout-caution .callout-header { color: var(--accent-red); }

/* Task lists */
.contains-task-list {
  list-style: none;
  margin-left: 4px;
}

.task-list-item-checkbox {
  margin-right: 8px;
  accent-color: var(--brand);
  transform: scale(1.15);
}

/* SVG Diagram Containers */
.diagram-card {
  margin: 28px 0;
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 16px;
  box-shadow: var(--card-shadow);
  text-align: center;
}

.diagram-card img, .diagram-card svg {
  max-width: 100%;
  height: auto;
  border-radius: 4px;
}

.diagram-caption {
  font-size: 0.85rem;
  color: var(--text-muted);
  margin-top: 10px;
  font-weight: 500;
}

/* Math rendering */
.math-inline {
  font-family: "Cambria Math", "Latin Modern Math", serif;
  font-style: italic;
  padding: 0 4px;
  color: var(--brand);
}

/* Print Styles */
@media print {
  header.site-header, .no-print, .btn-action {
    display: none !important;
  }
  body {
    background: #fff !important;
    color: #000 !important;
    font-size: 11pt;
    line-height: 1.4;
  }
  .page-container {
    max-width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
  }
  .table-wrapper {
    box-shadow: none !important;
    border: 1px solid #ccc !important;
    page-break-inside: avoid;
  }
  thead th {
    background-color: #eee !important;
    color: #000 !important;
  }
  tr, img, svg, .diagram-card {
    page-break-inside: avoid;
  }
  h1, h2, h3 {
    page-break-after: avoid;
    color: #000 !important;
  }
  .page-break {
    page-break-before: always;
  }
}
"""

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
  <style>{CSS_STYLES}</style>
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
  <style>{CSS_STYLES}</style>
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
