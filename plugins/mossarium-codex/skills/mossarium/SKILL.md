---
name: mossarium
description: Activate Mossarium before and after AI-assisted code changes; use brief, preflight, refresh, audit, and check to keep repository inheritance safe.
---

# Mossarium Codex Skill

## Project Identity

Mossarium is an AI constitution system for GitHub repositories.

## Core Slogan

Mossarium does not make AI smarter.
It makes repositories easier for AI to inherit.

## Before Editing

- Run `mossarium brief`
- Run `mossarium preflight`
- Run `mossarium refresh --check`
- Read `QWEN.md`
- Read `AGENTS.md`
- Read `.mossarium/context/project-map.md`
- Read `.mossarium/context/file-index.md`
- Read `.mossarium/context/invariants.md`
- Read `.mossarium/context/patch-mode.md`

## During Editing

- Use Patch Mode for bug fixes and small changes
- Modify only requested files
- Do not add unrequested features
- Do not redesign architecture
- Do not create `mossarium.py`
- Do not add `generate` or `export` commands

## After Editing

- Run `pytest`
- Run `mossarium refresh`
- Run `mossarium refresh --check`
- Run `mossarium audit`
- Run `mossarium check`
- Stop and wait for supervisor confirmation
