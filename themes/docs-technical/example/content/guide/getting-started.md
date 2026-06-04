---
title: Getting started
description: Install Widgetizer and shape your first widget in under a minute.
tags: [guide, install]
---
This page takes you from an empty directory to a validated widget. It assumes
nothing beyond a recent Python and a terminal.

## Install

Widgetizer ships as a single package:

```bash
pip install widgetizer
```

Verify the install by printing the version:

```bash
widgetizer --version
```

## Shape your first widget

A widget is just a small declarative file. Create `hello.widget`:

```toml
name = "hello"
shape = "rounded"
color = "#30638e"
```

Then build it:

```bash
widgetizer build hello.widget
```

## Next steps

Once the basics work, tune the defaults in [[Configuration]] or look up a
command in the [[CLI reference]].
