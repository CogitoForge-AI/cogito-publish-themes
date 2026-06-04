from __future__ import annotations

from pathlib import Path

from pyssg.presets import blog

# Demo site for the ``blog-minimal`` gallery theme. It vendors the theme that
# sits one directory up (``themes/themes/blog-minimal``) via an absolute ``layout``
# path, so the demo always tracks the theme it lives next to. The content is a
# small slice of the bundled ``examples/blog`` posts -- enough to exercise the
# paginated home, a single post, and the tag archive that drive the showcase
# screenshots.
_THEME = Path(__file__).resolve().parent.parent

config = blog(
    site={
        "title": "The Rendered Web",
        "description": "A blog-minimal demo: clean typography, posts, light/dark.",
    },
    layout=_THEME,
    posts_per_page=3,
)
