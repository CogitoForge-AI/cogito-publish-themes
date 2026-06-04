# landing -- style notes

The stylesheet (`assets/style.css`) is **original** to pyssg: hand-written plain
CSS, not compiled from any upstream theme's SCSS, and the layout/markup are
original too. The design is *inspired by* the common product/SaaS landing-page
archetype (a centered hero with an eyebrow pill and dual CTAs, a feature grid, a
numbered "how it works" section, and a closing call-to-action band) rather than
reproducing a specific theme.

Because the CSS is original there is no `THEME-LICENSE` (the repository LICENSE
applies) and there is no SCSS build step -- pyssg ships only the static CSS.

## Typography

Body text uses **Inter**, loaded at runtime from the privacy-friendly
[Bunny Fonts](https://fonts.bunny.net) CDN. No font binaries are committed and
the build output is unaffected (the `<head>` only emits a `<link>`), so two
builds stay byte-identical. Override the `<head>` or the `--font` variable to
self-host or swap the font.
