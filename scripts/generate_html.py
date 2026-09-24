#!/usr/bin/env python3
"""HTML Documentation Generator for 4.0 m x 3.0 m Freestanding Pergola Project.

Converts Markdown documentation files into styled, responsive HTML pages with navigation,
print styles, embedded SVG diagrams, and a unified all-in-one printable manual.
"""

import dataclasses
import pathlib
import re

import markdown_it
import mdit_py_plugins.dollarmath
import mdit_py_plugins.tasklists

BASE_DIR: pathlib.Path = pathlib.Path(__file__).resolve().parent.parent
CSS_REL_PATH: str = "css/styles.css"


@dataclasses.dataclass(frozen=True)
class PageConfig:
    """Configuration for a documentation page.

    Attributes:
        src: Source markdown filename relative to BASE_DIR.
        dest: Destination HTML filename relative to BASE_DIR.
        title: Full page title for the HTML document head.
        short_title: Short title for navigation menu items.
        diagrams: List of SVG diagram paths to embed in this page.
    """

    src: str
    dest: str
    title: str
    short_title: str
    diagrams: list[str] = dataclasses.field(default_factory=list)


PAGES: list[PageConfig] = [
    PageConfig(
        src="README.md",
        dest="index.html",
        title="Master Overview & Plan",
        short_title="Overview",
        diagrams=["diagrams/elevation_and_plan.svg"],
    ),
    PageConfig(
        src="01_PROJECT_SPECIFICATIONS.md",
        dest="01_PROJECT_SPECIFICATIONS.html",
        title="01 — Project Specifications",
        short_title="01 Specs",
        diagrams=["diagrams/elevation_and_plan.svg"],
    ),
    PageConfig(
        src="02_BILL_OF_MATERIALS.md",
        dest="02_BILL_OF_MATERIALS.html",
        title="02 — Bill of Materials (BOM)",
        short_title="02 Materials",
    ),
    PageConfig(
        src="03_CUT_LIST_AND_TIMBER_OPTIMIZATION.md",
        dest="03_CUT_LIST_AND_TIMBER_OPTIMIZATION.html",
        title="03 — Cut List & Timber Optimization",
        short_title="03 Cut List",
    ),
    PageConfig(
        src="04_JOINERY_AND_CONNECTION_DETAILS.md",
        dest="04_JOINERY_AND_CONNECTION_DETAILS.html",
        title="04 — Joinery & Connection Details",
        short_title="04 Joinery",
        diagrams=["diagrams/joinery_details.svg"],
    ),
    PageConfig(
        src="05_STEP_BY_STEP_BUILD_GUIDE.md",
        dest="05_STEP_BY_STEP_BUILD_GUIDE.html",
        title="05 — Step-by-Step Construction Guide",
        short_title="05 Build Guide",
    ),
    PageConfig(
        src="06_TOOL_AND_SAFETY_CHECKLIST.md",
        dest="06_TOOL_AND_SAFETY_CHECKLIST.html",
        title="06 — Tool & Safety Checklist",
        short_title="06 Tools",
    ),
]

THEME_SCRIPT: str = """
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


def create_markdown_parser() -> markdown_it.MarkdownIt:
    """Creates and configures a MarkdownIt parser with required extensions.

    Returns:
        A configured markdown_it.MarkdownIt parser instance.
    """
    md: markdown_it.MarkdownIt = markdown_it.MarkdownIt("commonmark")
    _ = md.enable("table")
    _ = md.enable("strikethrough")
    _ = mdit_py_plugins.tasklists.tasklists_plugin(md)
    _ = mdit_py_plugins.dollarmath.dollarmath_plugin(md)
    return md


def post_process_html(html_content: str, current_page_dest: str = "") -> str:
    """Post-processes rendered HTML with tables, callouts, links, and math formatting.

    Args:
        html_content: Raw HTML rendered from Markdown.
        current_page_dest: Target HTML filename for reference during post-processing.

    Returns:
        Cleaned and enriched HTML string.
    """
    _ = current_page_dest
    processed: str = re.sub(
        r"(<table>.*?</table>)",
        r'<div class="table-wrapper">\1</div>',
        html_content,
        flags=re.DOTALL,
    )

    alert_types: dict[str, tuple[str, str, str]] = {
        "NOTE": ("callout-note", "ℹ️", "Note"),
        "TIP": ("callout-tip", "💡", "Tip"),
        "IMPORTANT": ("callout-important", "📌", "Important"),
        "WARNING": ("callout-warning", "⚠️", "Warning"),
        "CAUTION": ("callout-caution", "🛑", "Caution"),
    }

    def replace_alert(match: re.Match[str]) -> str:
        kind: str = match.group(1).upper()
        body: str = match.group(2).strip()
        css_class, icon, label = alert_types.get(
            kind, ("callout-note", "ℹ️", kind.capitalize())
        )
        return (
            f'<div class="callout {css_class}">'
            + f'<div class="callout-header"><span class="callout-icon">{icon}</span> {label}</div>'
            + f'<div class="callout-body"><p>{body}</p></div>'
            + "</div>"
        )

    alert_pattern: re.Pattern[str] = re.compile(
        r"<blockquote>\s*<p>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]"
        + r"\s*<br\s*/?>?\s*(.*?)</p>\s*</blockquote>",
        re.DOTALL | re.IGNORECASE,
    )
    processed = alert_pattern.sub(replace_alert, processed)

    alert_pattern_simple: re.Pattern[str] = re.compile(
        r"<blockquote>\s*<p>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*(.*?)</p>\s*</blockquote>",
        re.DOTALL | re.IGNORECASE,
    )
    processed = alert_pattern_simple.sub(replace_alert, processed)

    def rewrite_link(match: re.Match[str]) -> str:
        href: str = match.group(1)
        filename: str = href.split("/")[-1]
        if filename == "README.md":
            return 'href="index.html"'
        if filename.endswith(".md"):
            return f'href="{filename[:-3]}.html"'
        return match.group(0)

    processed = re.sub(r'href="([^"]+\.md)"', rewrite_link, processed)

    processed = re.sub(
        r'<span class="math inline">\\sqrt\{(.*?)\}</span>',
        r'<span class="math-inline">√(\1)</span>',
        processed,
    )
    processed = re.sub(
        r'<span class="math inline">(.*?)</span>',
        r'<span class="math-inline">\1</span>',
        processed,
    )

    return processed


def build_header(current_dest: str) -> str:
    """Builds the top navigation header bar HTML.

    Args:
        current_dest: Destination filename of the current page being built.

    Returns:
        HTML string of the header navigation element.
    """
    nav_items: list[str] = []
    for page in PAGES:
        active_class: str = " active" if page.dest == current_dest else ""
        nav_items.append(
            f'<a href="{page.dest}" class="nav-item{active_class}">{page.short_title}</a>'
        )

    all_in_one_active: str = (
        " active" if current_dest == "complete_build_manual.html" else ""
    )
    nav_items.append(
        f'<a href="complete_build_manual.html" class="nav-item{all_in_one_active}" '
        + 'style="font-weight:700; color:var(--brand);">📖 Full Manual</a>'
    )

    nav_html: str = "\n".join(nav_items)

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


def render_markdown(md_parser: markdown_it.MarkdownIt, text: str) -> str:
    """Renders markdown text to HTML using the provided parser.

    Args:
        md_parser: Configured MarkdownIt parser instance.
        text: Raw markdown string.

    Returns:
        Rendered HTML string.
    """
    rendered: str = md_parser.render(text)  # pyright: ignore[reportAny]
    return rendered


def generate_individual_pages(md_parser: markdown_it.MarkdownIt) -> None:
    """Generates standalone HTML files for each configured Markdown document.

    Args:
        md_parser: Configured MarkdownIt parser instance.
    """
    print("Generating individual HTML pages...")
    for page in PAGES:
        src_path: pathlib.Path = BASE_DIR / page.src
        dest_path: pathlib.Path = BASE_DIR / page.dest

        if not src_path.exists():
            print(f"Warning: {src_path} does not exist, skipping.")
            continue

        raw_md: str = src_path.read_text(encoding="utf-8")
        parsed_html: str = render_markdown(md_parser, raw_md)
        body_html: str = post_process_html(parsed_html, page.dest)

        diagram_html: str = ""
        for diag in page.diagrams:
            diag_file: str = pathlib.Path(diag).name
            diagram_html += f"""
<div class="diagram-card">
  <img src="{diag}" alt="{diag_file}" loading="lazy" />
  <div class="diagram-caption">Architectural Drawing: {diag_file}</div>
</div>
"""
        if diagram_html:
            parts: list[str] = body_html.split("</h1>", 1)
            if len(parts) == 2:
                body_html = parts[0] + "</h1>" + diagram_html + parts[1]
            else:
                body_html = diagram_html + body_html

        full_html: str = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page.title} — Pergola 4x3m</title>
  <link rel="stylesheet" href="{CSS_REL_PATH}">
</head>
<body>
  {build_header(page.dest)}
  <main class="page-container">
    {body_html}
  </main>
  {THEME_SCRIPT}
</body>
</html>
"""
        _ = dest_path.write_text(full_html, encoding="utf-8")
        print(f"  ✓ Written: {page.dest}")


def generate_unified_manual(md_parser: markdown_it.MarkdownIt) -> None:
    """Generates complete_build_manual.html combining all sections into one document.

    Args:
        md_parser: Configured MarkdownIt parser instance.
    """
    print("Generating unified printable manual (complete_build_manual.html)...")
    combined_body: str = """
<div style="text-align:center; padding: 40px 0 20px 0;">
  <h1 style="font-size:2.8rem; margin-bottom:8px;">🌲 4.0 m × 3.0 m Freestanding Pergola</h1>
  <p style="font-size:1.2rem; color:var(--brand); font-weight:600;">Complete Master Construction Handbook & Architectural Specifications</p>
  <p style="color:var(--text-muted);">Author: John Tobin & Antigravity Pair Programming | Location: Ireland/UK Patio Build</p>
</div>
<hr />
"""

    for idx, page in enumerate(PAGES):
        src_path: pathlib.Path = BASE_DIR / page.src
        if not src_path.exists():
            continue

        raw_md: str = src_path.read_text(encoding="utf-8")
        parsed_html: str = render_markdown(md_parser, raw_md)
        section_html: str = post_process_html(parsed_html, "complete_build_manual.html")

        diagram_html: str = ""
        for diag in page.diagrams:
            diag_file: str = pathlib.Path(diag).name
            diagram_html += f"""
<div class="diagram-card">
  <img src="{diag}" alt="{diag_file}" loading="lazy" />
  <div class="diagram-caption">Architectural Drawing: {diag_file}</div>
</div>
"""
        if diagram_html:
            parts: list[str] = section_html.split("</h1>", 1)
            if len(parts) == 2:
                section_html = parts[0] + "</h1>" + diagram_html + parts[1]
            else:
                section_html = diagram_html + section_html

        page_break: str = ' class="page-break"' if idx > 0 else ""
        combined_body += f"""
<section id="section-{idx}"{page_break} style="margin-top: 40px;">
  {section_html}
</section>
<hr />
"""

    dest_path: pathlib.Path = BASE_DIR / "complete_build_manual.html"
    full_html: str = f"""<!DOCTYPE html>
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
    _ = dest_path.write_text(full_html, encoding="utf-8")
    print("  ✓ Written: complete_build_manual.html")


def main() -> None:
    """Main entry point for generating the HTML documentation."""
    md: markdown_it.MarkdownIt = create_markdown_parser()
    generate_individual_pages(md)
    generate_unified_manual(md)
    print("\nAll HTML documents generated successfully!")


if __name__ == "__main__":
    main()
