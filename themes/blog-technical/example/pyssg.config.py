from __future__ import annotations

from pathlib import Path

from pyssg.presets import blog

# Demo site for the ``blog-technical`` gallery theme (PaperMod-style). It vendors
# the theme one directory up (``themes/themes/blog-technical``) via an absolute
# ``layout`` path. The posts carry headings, tags, and code blocks so the demo
# shows off the theme's table of contents, reading time, tag chips, and
# code-copy buttons in the showcase screenshots.
_THEME = Path(__file__).resolve().parent.parent

config = blog(
    site={
        "title": "The Rendered Web",
        "description": "A blog-technical demo: TOC, tags, reading time, code copy.",
    },
    layout=_THEME,
    posts_per_page=3,
)
