"""Demo site for the ``landing`` gallery theme.

It vendors the theme one directory up (``themes/themes/landing``) via an absolute
``layout`` path. The home page (``content/index.md``) carries the hero, feature
grid, steps, and closing CTA entirely in its frontmatter; a second page
(``content/pricing.md``) shows the generic inner-page template. Plugins are
assembled by hand (no preset) because a marketing site needs no blog/collection
machinery.
"""

from __future__ import annotations

from pathlib import Path

from pyssg import Config
from pyssg.plugins import (
    asset_copy,
    content_meta,
    directory_loader,
    frontmatter,
    markdown,
    nav,
    permalink,
    render,
    sitemap,
)

_THEME = Path(__file__).resolve().parent.parent

config = Config(
    content_dir="content",
    output_dir="dist",
    layout=_THEME,
    site={
        "title": "Driftless",
        "description": "Ship static sites without the busywork.",
    },
    plugins=[
        directory_loader(),
        frontmatter(),
        markdown(),
        content_meta(),
        permalink(),
        nav(),
        sitemap(),
        asset_copy(),
        render(),
    ],
)
