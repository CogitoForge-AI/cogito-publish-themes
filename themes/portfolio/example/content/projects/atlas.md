---
title: Atlas
date: "2024-09-01"
summary: A self-serve analytics layer that turns SQL into shareable, versioned dashboards.
excerpt: Self-serve analytics -- SQL in, versioned dashboards out.
tags: [Python, DuckDB, React]
tech: [Python, FastAPI, DuckDB, React, TypeScript]
live_url: https://example.com/atlas
repo: https://github.com/
---
Atlas lets non-engineers explore a warehouse without waiting on the data team. A
query is just a file: it is versioned in git, reviewed like code, and rendered as
an interactive dashboard at build time.

## What I built

- A query compiler that validates SQL against the live schema and caches results
  per content hash.
- A React dashboard runtime with cross-filtering and shareable URLs.
- A permissions model that maps warehouse roles to dashboard visibility.

## Outcome

Cut the average "I have a question" turnaround from two days to ten minutes, and
removed the data team from the critical path for routine reporting.
