from __future__ import annotations

from pathlib import Path

from pyssg.presets import docs

# Demo site for the ``docs-technical`` gallery theme (docsy-style). It vendors
# the theme one directory up (``themes/themes/docs-technical``) via an absolute
# ``layout`` path. The content is a tiny handbook -- a landing page plus a couple
# of cross-linked guide and reference pages -- enough to show the left nav
# sidebar, "on this page" TOC, breadcrumbs, prev/next, and backlinks that this
# theme is built around.
_THEME = Path(__file__).resolve().parent.parent

config = docs(
    site={
        "title": "Widgetizer",
        "description": "Documentation for the Widgetizer toolkit.",
    },
    layout=_THEME,
)
