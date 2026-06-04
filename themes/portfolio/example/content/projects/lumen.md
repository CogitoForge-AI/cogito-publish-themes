---
title: Lumen
date: "2023-11-20"
summary: An open-source component library focused on accessibility and dark mode by default.
excerpt: An accessible, dark-mode-first open-source component library.
tags: [TypeScript, CSS, a11y]
tech: [TypeScript, React, CSS, Storybook]
live_url: https://example.com/lumen
repo: https://github.com/
---
Lumen is a small component library I maintain in the open. The guiding rule:
every component is keyboard-navigable and screen-reader-correct before it is
considered done, and dark mode is a first-class theme, not an afterthought.

## Highlights

- A token-driven theming layer that flips light/dark with one attribute.
- Components audited against WCAG 2.2 AA, with automated axe checks in CI.
- Zero runtime dependencies; ships as tree-shakeable ES modules.

## Outcome

Adopted by a handful of teams who needed accessible primitives without pulling in
a heavyweight design system.
