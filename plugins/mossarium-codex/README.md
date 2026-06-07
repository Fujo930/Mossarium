# Mossarium Codex Plugin

## What This Is

This plugin packages the Mossarium Codex Skill for Codex-style coding agents.

Mossarium is an AI constitution system for GitHub repositories.

## What It Installs

- **SKILL.md** — Mossarium protocol: what to run before, during, and after editing
- **preflight.py** — Pre-edit checklist (brief, preflight, refresh --check)
- **finish.py** — Post-edit checklist (pytest, refresh, audit, check)

## How to Test Locally

1. Install Mossarium: `pip install -e .`
2. Run `mossarium integrate codex` to scaffold the integration
3. Before editing: `mossarium brief` / `mossarium preflight` / `mossarium refresh --check`
4. After editing: `pytest` / `mossarium refresh` / `mossarium audit` / `mossarium check`

## Recommended Codex Workflow

- Run `mossarium brief` before editing
- Run `mossarium preflight` before editing
- Run `mossarium refresh --check` before editing
- Use Patch Mode for small changes
- After editing, run `pytest`, `mossarium refresh`, `mossarium audit`, and `mossarium check`

## Commands Used by the Skill

| Command | When |
|---|---|
| `mossarium brief` | Before editing |
| `mossarium preflight` | Before editing |
| `mossarium refresh --check` | Before editing |
| `mossarium refresh` | After editing |
| `mossarium audit` | After editing |
| `mossarium check` | After editing |

## Publication Status

This is a publication candidate scaffold, not an official public marketplace submission yet.
