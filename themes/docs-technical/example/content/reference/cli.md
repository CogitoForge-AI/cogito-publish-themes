---
title: CLI reference
description: Every Widgetizer command and the flags it accepts.
tags: [reference, cli]
---
The `widgetizer` command groups its work into a handful of subcommands. This
page is the exhaustive list; for a guided introduction read [[Getting started]].

## `widgetizer build`

Compile one or more widget files into the output directory.

```bash
widgetizer build [FILES...] [--out DIR] [--strict]
```

- **`FILES`** -- widget files to build; defaults to every `*.widget` found.
- **`--out DIR`** -- override the configured output directory.
- **`--strict`** -- treat validation warnings as errors.

## `widgetizer validate`

Check widget files without writing any output.

```bash
widgetizer validate [FILES...]
```

## `widgetizer --version`

Print the installed version and exit. Configuration for these commands is
described in [[Configuration]].
