# Mossarium

**Mossarium is an AI constitution system for GitHub repositories.**

> Mossarium does not make AI smarter.  
> It makes repositories easier for AI to inherit.

---

## Commands

| Command | What It Does |
|---|---|
| `mossarium init` | Initialize a project with constitutional structure, AI Context Map, and activation files |
| `mossarium check` | Verify structural compliance (are all required files present?) |
| `mossarium brief` | Print a short AI project brief before editing |
| `mossarium preflight` | Check activation safety before modifying code |
| `mossarium audit` | Full inheritance-quality audit (files, content, semantics, safety) |
| `mossarium refresh` | Refresh AI Context Map from current repository state |
| `mossarium refresh --check` | Check whether the context map is stale |
| `mossarium integrate codex` | Install Codex local integration scaffold |

---

## Installation

```bash
pip install -e .
```

## Quick Start

```bash
mossarium init        # Set up a new project
mossarium brief       # Read the AI project brief
mossarium preflight   # Verify repo is ready for AI work
mossarium check       # Check constitutional compliance
mossarium audit       # Run full inheritance audit
mossarium refresh     # Update AI Context Map
```

---

## Capabilities by Version

### v0.1 — AI Constitution

The foundation. `mossarium init` creates the `.mossarium/` directory with rules, memory, proposals, agents, benchmarks, and templates. `mossarium check` verifies every required file and directory exists.

### v0.2 — AI Context Map

Six auto-generated files under `.mossarium/context/` give AI agents a complete picture of the project *before* they modify anything:

| File | Purpose |
|---|---|
| `project-map.md` | High-level project structure and entry points |
| `file-index.md` | Index of key files and their responsibilities |
| `edit-zones.md` | Safe, controlled, and protected modification zones |
| `invariants.md` | Rules that must never be broken |
| `agent-protocol.md` | Read-first, propose-then-execute protocol |
| `patch-mode.md` | Minimal, safe fix protocol |

### v0.3 — Agent Activation Layer

AI agents no longer need repeated human reminders. Two new commands and two activation files make the rules self-discovering:

| Command | Purpose |
|---|---|
| `mossarium brief` | Outputs project identity, required reading, forbidden actions, workflow, and patch-mode rules |
| `mossarium preflight` | Checks required files, forbidden files, and warns about local directories |

`mossarium init` now also generates:

- `AGENTS.md` — Universal AI agent entry point
- `QWEN.md` — Project memory for Qwen Code / local AI tools

### v0.4 — Inheritance Audit

A deterministic audit that checks whether a repository is truly ready for AI inheritance — no AI calls, no network, no auto-fix.

```
$ mossarium audit

Mossarium Inheritance Audit

[OK]  Required file: README.md
[OK]  Context file has content: invariants.md
[WARN] Local directory found: .venv/

Result: PASS WITH WARNINGS
```

**How the commands differ:**

| Command | Checks |
|---|---|
| `mossarium check` | Structure — are constitutional files present? |
| `mossarium preflight` | Activation safety — are activation files present? forbidden files absent? |
| `mossarium audit` | Inheritance quality — required files, context content, semantic markers, forbidden patterns |

### v0.5 — Context Refresh Engine

Mossarium v0.5 adds **Context Refresh**, moving from static AI memory to maintainable AI memory. `mossarium refresh` scans the repository and updates managed sections inside the AI Context Map — while preserving any user-written content outside those sections.

| Command | Purpose |
|---|---|
| `mossarium refresh` | Regenerate AI Context Map from current repository state |
| `mossarium refresh --check` | Report whether the context map is stale (exit code only, no writes) |

Managed sections use `<!-- MOSSARIUM:BEGIN AUTO-GENERATED -->` markers so
Mossarium can safely update context without touching user-authored notes.

### v0.6 — Codex Integration Layer

Mossarium v0.6 adds **Codex Integration**, moving from manual CLI usage toward agent-integrated workflow. `mossarium integrate codex` installs a local Codex skill scaffold under `.codex/skills/mossarium/` so Codex-style coding agents can activate Mossarium before and after editing.

| File | Purpose |
|---|---|
| `.codex/skills/mossarium/SKILL.md` | Mossarium protocol for Codex agents |
| `.codex/skills/mossarium/scripts/preflight.py` | Pre-edit checklist (brief, preflight, refresh --check) |
| `.codex/skills/mossarium/scripts/finish.py` | Post-edit checklist (pytest, refresh, audit, check) |

---

## What Mossarium Provides

Mossarium gives every repository a self-describing layer that AI agents can read before acting: constitution, history, memory, proposals, agent roles, benchmarks, context map, activation files, and inheritance audit.

## Development

Mossarium modules are split for AI maintainability:

| Module | Responsibility |
|---|---|
| `mossarium/cli.py` | CLI dispatch only (~52 lines) |
| `mossarium/init.py` | Project initialization |
| `mossarium/check.py` | Compliance checking |
| `mossarium/brief.py` | AI project brief |
| `mossarium/preflight.py` | Activation safety check |
| `mossarium/audit.py` | Inheritance audit |
| `mossarium/refresh.py` | Context refresh engine |
| `mossarium/content.py` | Starter content and generators |
| `mossarium/paths.py` | Centralised path definitions |
| `mossarium/utils.py` | Shared helpers |

When modifying Mossarium, prefer focused modules and avoid growing `mossarium/cli.py` unless changing CLI dispatch.

## What Mossarium Is NOT

- Not a chatbot
- Not a programming language
- Not a generic coding agent
- Not a website or database
- Not an LLM API wrapper

## Core Principle

> Mossarium does not make AI smarter. It makes repositories easier for AI to inherit.
