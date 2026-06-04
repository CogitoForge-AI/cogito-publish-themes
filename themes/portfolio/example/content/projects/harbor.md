---
title: Harbor
date: "2024-04-12"
summary: A deployment dashboard that makes rollbacks a one-click, audited operation.
excerpt: A deployment dashboard where rollbacks are one click and fully audited.
tags: [Go, React, Kubernetes]
tech: [Go, gRPC, React, Kubernetes]
live_url: https://example.com/harbor
repo: https://github.com/
---
Harbor is the control plane a small team uses to ship to production with
confidence. Every deploy is an immutable record; rolling back is selecting a
previous record and pressing one button.

## Highlights

- A streaming activity log built on gRPC server-streaming.
- Progressive rollouts with automatic halt on error-rate regressions.
- An audit trail that answers "who changed what, when" without spelunking logs.

## Outcome

Mean time to recovery dropped sharply once rollback stopped being a scary,
manual `kubectl` session.
