"""Configuration for the Cogito Publish Themes gallery -- a themes.gohugo.io-style showcase.

The gallery is itself a Cogito Publish site (dogfooding). Each theme has a showcase page
under ``content/showcase/<slug>.md``; a ``themes`` collection turns those pages
into the home grid (``/``), and the per-theme detail page lives at
``/showcase/<slug>/``. Each theme's screenshots are mounted from
``<slug>/screenshots/`` into ``/screenshots/<slug>/`` so the gallery can show
them without copying the binaries into this site tree.
"""

from __future__ import annotations

from pyssg import Config
from pyssg.plugins import (
    CollectionSpec,
    Pagination,
    asset_copy,
    collections,
    content_meta,
    directory_loader,
    frontmatter,
    markdown,
    nav,
    permalink,
    render,
    sitemap,
)

# Every theme that has a showcase page must also be listed here so its committed
# screenshots (``themes/<slug>/screenshots/``) are published under
# ``/screenshots/<slug>/``.
_THEMES = ["blog-minimal", "blog-technical", "docs-technical", "portfolio", "landing"]
_SCREENSHOT_MOUNTS = [(f"themes/{slug}/screenshots", f"/screenshots/{slug}") for slug in _THEMES]

# The home grid: a single page listing every showcase entry, sorted by title.
_gallery = CollectionSpec(
    name="themes",
    select=lambda item: item.section == "showcase",
    sort_key=lambda item: item.title.lower(),
    pagination=Pagination(size=100, route="/", template="index.html.j2"),
    title="Cogito Publish Themes",
)

config = Config(
    content_dir="content",
    output_dir="dist",
    layout="layouts/gallery",
    base_url="https://publish-themes.cogito-ai.org",
    site={
        "title": "Cogito Publish Themes",
        "description": "A gallery of ready-to-use themes for Cogito Publish.",
    },
    plugins=[
        directory_loader(),
        frontmatter(),
        markdown(),
        content_meta(),
        permalink(),
        nav(),
        collections(_gallery),
        sitemap(),
        asset_copy(mounts=_SCREENSHOT_MOUNTS),
        render(),
    ],
)
