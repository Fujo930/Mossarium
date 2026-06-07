# AGENTS.md - AI Agent Activation File

This repository uses Mossarium, an AI constitution system for GitHub repositories.

## Before Editing

- Run `mossarium brief`
- Run `mossarium preflight`
- Run `mossarium refresh --check`

## After Significant Changes

- Run `mossarium refresh`
- Run `pytest`
- Run `mossarium audit`

## Required Reading

Before modifying code, read these Mossarium files:

- `.mossarium/CONSTITUTION.md`
- `.mossarium/context/project-map.md`
- `.mossarium/context/file-index.md`
- `.mossarium/context/invariants.md`
- `.mossarium/context/patch-mode.md`

## Rules

- Use Patch Mode for bug fixes or small changes
- Do not create `mossarium.py` in the root directory
- Do not add `generate` or `export` commands
- Do not manually modify `.mossarium/` as a substitute for changing init/check
- When modifying Mossarium, prefer focused modules and avoid growing `mossarium/cli.py` unless changing CLI dispatch
- Stop after completing the requested task
- Wait for supervisor confirmation

## If Using Codex

- Run `mossarium integrate codex` once
- Before editing, follow the Mossarium Codex Skill:
  - Run `mossarium brief`
  - Run `mossarium preflight`
  - Run `mossarium refresh --check`
- After editing:
  - Run `pytest`
  - Run `mossarium refresh`
  - Run `mossarium audit`
  - Run `mossarium check`

## Quick Start

```bash
mossarium brief           # Read the AI project brief
mossarium preflight       # Check repository readiness
mossarium refresh --check # Verify context is current
mossarium check           # Verify compliance
mossarium audit           # Full inheritance audit
```
