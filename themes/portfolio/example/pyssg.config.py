"""Demo site for the ``portfolio`` gallery theme.

It vendors the theme one directory up (``themes/themes/portfolio``) via an absolute
``layout`` path. The home page (``content/index.md``) carries the hero, skills,
and social links in its frontmatter; ``content/projects/*.md`` become a
``projects`` collection rendered as a grid at ``/projects/`` with a detail page
each. Plugins are assembled by hand (no preset) so the project collection and its
templates are wired exactly.
"""

from __future__ import annotations

from pathlib import Path

from pyssg import Config
from pyssg.plugins import (
    CollectionSpec,
    Pagination,
    asset_copy,
    collections,
    content_meta,
    directory_loader,
    frontmatter,
    highlight,
    markdown,
    nav,
    permalink,
    render,
    sitemap,
)

_THEME = Path(__file__).resolve().parent.parent

# Projects -> a grid at /projects/, newest first.
_projects = CollectionSpec(
    name="projects",
    select=lambda item: item.section == "projects",
    sort_key=lambda item: item.date,
    reverse=True,
    pagination=Pagination(size=50, route="/projects/", template="projects.html.j2"),
    title="Projects",
)

config = Config(
    content_dir="content",
    output_dir="dist",
    layout=_THEME,
    site={
        "title": "Ada Quokka",
        "description": "Portfolio of Ada Quokka, product engineer.",
    },
    plugins=[
        directory_loader(),
        frontmatter(),
        markdown(),
        highlight(),
        content_meta(),
        permalink(),
        nav(),
        collections(_projects),
        sitemap(),
        asset_copy(),
        render(),
    ],
)
