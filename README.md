# PySSG theme gallery

This directory is a **gallery of standalone themes** for PySSG. Unlike the
built-in themes under `pyssg/themes/` (which ship inside the `pyssg` wheel),
themes here are **source-only**: they are not packaged or installed with PySSG.
They are meant to be adopted into a site by vendoring (copy the theme directory
into your project) and pointing `Config.layout` at it.

It is **also a PySSG site itself**: `themes/` builds into a
[themes.gohugo.io](https://themes.gohugo.io/)-style **showcase** (built with
PySSG, dogfooding) published at **https://themes-pyssg.nkthanh.dev**. See
[The showcase site](#the-showcase-site) below.

```python
# pyssg.config.py -- after copying themes/themes/blog-technical into your site as ./theme
from pyssg.presets import blog

config = blog(site={"title": "My Blog"}, layout="theme")
```

`Config.layout` accepts a `str` path (resolved relative to the site directory)
or an absolute `Path`, so a vendored theme is referenced the same way as any
local layout package.

## Theme layout

Each theme is a layout package:

```
<theme>/
  layout.toml          # manifest: name, version, default_template, [options]
  templates/           # Jinja2 templates (*.html.j2)
  assets/              # css/js/fonts copied to /assets/ in the output
  i18n/                # UI string tables (en.toml, ...); a site can override them
  THEME-LICENSE        # upstream license when the theme is adapted from another
```

## Configuration

Themes expose configurable options through the **theme configuration API**. A
theme declares its option defaults in the `layout.toml` `[options]` table; a site
overrides any of them via `Config.theme`. Resolution is `theme defaults <-
Config.theme`, and the result is available to templates as `theme.*`.

```toml
# layout.toml
[options]
default_theme = "auto"   # color scheme: "auto" | "light" | "dark"
accent = "#0b66c3"
show_toc = true
```

```python
config.theme = {"default_theme": "dark", "accent": "#e25555"}
```

The mechanism is standardized; the **option vocabulary is per-theme**, so read
each theme's own option list. Keys a theme does not declare are still passed
through to templates but trigger a non-fatal warning (typo guard). For
cross-theme consistency, theme authors are encouraged -- not required -- to reuse
conventional names where they apply, currently:

| Convention | Meaning |
| --- | --- |
| `default_theme` | Initial color scheme: `"auto"`, `"light"`, or `"dark"`. |
| `accent` | Primary accent color. |

## Themes

| Theme | Adapted from | Notes |
| --- | --- | --- |
| `blog-minimal` | [hugo-coder](https://github.com/luizdepra/hugo-coder) (MIT) | Minimal blog: clean typography, post list + post page, light/dark toggle. |
| `blog-technical` | [hugo-PaperMod](https://github.com/adityatelange/hugo-PaperMod) (MIT) | Technical blog: TOC, tags, reading time, code copy, light/dark toggle. |
| `docs-technical` | [docsy](https://github.com/google/docsy) (layout reference; CSS original) | Technical docs: navbar, left nav sidebar, "on this page" TOC, breadcrumbs, prev/next. |
| `portfolio` | original (CSS + layout) | Personal portfolio/resume: hero, about, skills, project grid + detail pages. |
| `landing` | original (CSS + layout) | Product/SaaS landing: hero, feature grid, "how it works", closing CTA. |

Themes whose stylesheet is compiled offline from upstream SCSS document the exact
source commit and reproduction command in their `STYLE.md` (the PySSG build never
compiles SCSS; only the static CSS is shipped).

## The showcase site

`themes/` doubles as a PySSG site that renders the gallery above into a browsable
showcase. Its pieces:

```
themes/
  pyssg.config.py            # the gallery site config (a "themes" collection -> home grid)
  content/showcase/          # one Markdown page per theme (card + detail page)
  layouts/gallery/           # the gallery's own layout (templates + CSS)
  themes/<theme>/screenshots/  # 5 committed screenshots per theme, embedded by the gallery
  themes/<theme>/example/      # a minimal demo site per theme (also the screenshot source)
  wrangler.jsonc             # Cloudflare Worker ("pyssg-themes") for the deploy
```

Adding a theme to the showcase is three steps: drop its screenshots under
`themes/<theme>/screenshots/`, add a `content/showcase/<theme>.md` page (the frontmatter
carries the category, source links, feature list, and screenshot URLs), and add
the theme's slug to `_THEMES` in `pyssg.config.py` so its screenshots are mounted
into the output.

### Build and preview locally

```bash
uv run pyssg --site themes serve     # the gallery at http://127.0.0.1:8000
uv run pyssg --site themes build     # one-shot build into themes/dist
```

Each theme also ships a demo you can run on its own:

```bash
uv run pyssg --site themes/themes/<theme>/example serve
```

### Regenerating screenshots

Screenshots are committed source assets (not build output). Each theme has five
under `<theme>/screenshots/` -- a home/list view, a content view, an archive
view, a dark-mode view, and a mobile view -- captured from the theme's
`example/` demo at a uniform viewport. Rebuild a theme's demo
(`pyssg --site themes/themes/<theme>/example build`), serve its `dist/`, and recapture
with your headless browser of choice, overwriting the files in place.

### Deployment

A push to `main` that touches `themes/**` triggers
`.github/workflows/deploy-themes.yml`, which builds the site and runs
`wrangler deploy` against the `pyssg-themes` Worker (see `wrangler.jsonc`),
exactly like the docs deploy. The custom domain `themes-pyssg.nkthanh.dev` is
attached to that Worker through the Cloudflare dashboard (Workers route / custom
domain) -- a one-time setup outside this repo.
