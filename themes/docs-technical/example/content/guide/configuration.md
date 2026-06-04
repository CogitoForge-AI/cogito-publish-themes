---
title: Configuration
description: Tune Widgetizer with a small, predictable set of options.
tags: [guide, config]
---
Widgetizer reads an optional `widgetizer.toml` from the project root. Every
option has a sensible default, so the file is only as long as your overrides.

## Project options

```toml
[project]
name = "my-widgets"
out_dir = "build"
```

- **`name`** -- labels the build output; defaults to the directory name.
- **`out_dir`** -- where built widgets are written; defaults to `build`.

## Validation rules

```toml
[validate]
strict = true
max_size = "256kb"
```

Strict mode turns warnings into errors, which is what you want in CI. See
[[Getting started]] to create the project this file configures.

## Precedence

Command-line flags override `widgetizer.toml`, which overrides the built-in
defaults. The full flag list lives in the [[CLI reference]].
