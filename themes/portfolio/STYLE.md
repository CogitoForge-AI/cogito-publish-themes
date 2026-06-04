# portfolio -- style notes

The stylesheet (`assets/style.css`) is **original** to pyssg: it is hand-written
plain CSS, not compiled from any upstream theme's SCSS, and the layout/markup are
original too. The design is *inspired by* the common personal-portfolio
archetype (hero with avatar + role, an about section, a skills chip row, and a
project grid backed by detail pages) rather than reproducing a specific theme.

Because the CSS is original there is no `THEME-LICENSE` (the repository LICENSE
applies) and there is no SCSS build step -- pyssg ships only the static CSS.

## Typography

Body text uses **Inter**, loaded at runtime from the privacy-friendly
[Bunny Fonts](https://fonts.bunny.net) CDN (a drop-in, GDPR-friendly Google Fonts
mirror). No font binaries are committed, and the build output is unaffected: the
`<head>` only emits a `<link>`, so two builds remain byte-identical. A site that
prefers to self-host or swap the font can override the `<head>` or restyle
`--font` in its own layer.
