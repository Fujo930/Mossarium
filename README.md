# Mossarium

**Mossarium is an AI constitution system for GitHub repositories.**

> Mossarium does not make AI smarter.  
> It makes repositories easier for AI to inherit.

---

## What Problem Does Mossarium Solve?

AI coding agents are powerful, but they need context. Without a shared protocol, every human has to repeatedly remind every agent which files to read, which rules to obey, and which mistakes to avoid.

Mossarium gives every repository a **self-describing layer** that AI agents can read before acting. One `mossarium init` and the rules are in the repo — not in the chat transcript.

---

## Commands

| Command | What It Does |
|---|---|
| `mossarium init` | Initialize a project with constitutional structure, AI Context Map, and activation files |
| `mossarium check` | Verify structural compliance (are all required files present?) |
| `mossarium brief` | Print a short AI project brief before editing |
| `mossarium preflight` | Check activation safety before modifying code |
| `mossarium audit` | Full inheritance-quality audit (files, content, semantics, safety) |
| `mossarium refresh` | Regenerate AI Context Map from current repository state |
| `mossarium refresh --check` | Check whether the context map is stale (no writes) |
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

## How It Works

### AI Memory Layer

`mossarium init` creates a `.mossarium/` directory that every AI agent can read before touching code:

```
.mossarium/
├── CONSTITUTION.md          # AI constitutional rules
├── MANIFESTO.md             # Project philosophy
├── HISTORY.md               # Project history
├── rules/                   # Core rules + AI contribution guidelines
├── memory/                  # Decisions, failures, architecture records
├── proposals/               # Change proposal templates
├── agents/                  # Builder, reviewer, historian, guardian roles
├── benchmarks/              # Inheritance + comprehension tests
└── context/                 # AI Context Map (6 auto-generated files)
```

The **AI Context Map** under `.mossarium/context/` gives agents a complete picture of the project *before* they modify anything:

| File | Purpose |
|---|---|
| `project-map.md` | High-level project structure and entry points |
| `file-index.md` | Index of key files and their responsibilities |
| `edit-zones.md` | Safe, controlled, and protected modification zones |
| `invariants.md` | Rules that must never be broken |
| `agent-protocol.md` | Read-first, propose-then-execute protocol |
| `patch-mode.md` | Minimal, safe fix protocol |

### Agent Activation Layer

AI agents discover the rules automatically — no more repeated human reminders:

- `mossarium brief` — Print a one-page project brief with identity, required reading, forbidden actions, and workflow.
- `mossarium preflight` — Check that all activation files are present and no forbidden files exist.
- `AGENTS.md` — Universal entry point for any AI agent.
- `QWEN.md` — Project memory for Qwen Code and local AI tools.

### Quality Assurance

Three commands form a safety net, each at a different layer:

| Command | Layer | What It Checks |
|---|---|---|
| `mossarium check` | Structure | Are constitutional files present? |
| `mossarium preflight` | Activation | Are activation files present? Forbidden files absent? |
| `mossarium audit` | Inheritance | Required files, context quality, semantic markers, forbidden patterns |

`mossarium audit` is fully deterministic — no AI calls, no network, no auto-fix.

### Memory Maintenance

Projects change. The AI Context Map must stay in sync. `mossarium refresh` scans the repository and updates managed sections inside the six context files — while preserving any user-written content outside those sections.

Managed sections use `<!-- MOSSARIUM:BEGIN AUTO-GENERATED -->` markers so Mossarium can safely update generated content without touching user-authored notes.

### Platform Integrations

Mossarium is designed to work with any AI coding platform.

| Platform | Status |
|---|---|
| **Codex** | ✅ Supported — `mossarium integrate codex` installs a local skill scaffold, plugin package, and repo-scoped marketplace |
| **Claude Code** | 🔜 Planned |
| **GitHub Copilot** | 🔜 Planned |
| **Qwen Code** | 🔜 Planned (already ships QWEN.md) |
| **Other agents** | Compatible via AGENTS.md + `.mossarium/context/` |

Codex integration generates:

| Path | Purpose |
|---|---|
| `.codex/skills/mossarium/SKILL.md` | Mossarium protocol for Codex agents |
| `.codex/skills/mossarium/scripts/preflight.py` | Pre-edit checklist |
| `.codex/skills/mossarium/scripts/finish.py` | Post-edit checklist |
| `plugins/mossarium-codex/` | Publication-candidate plugin package |
| `.agents/plugins/marketplace.json` | Repo-scoped local marketplace |

This is a publication candidate — not yet an official public marketplace submission.

---

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

---

## What Mossarium Is NOT

- Not a chatbot
- Not a programming language
- Not a generic coding agent
- Not a website or database
- Not an LLM API wrapper

## Core Principle

> Mossarium does not make AI smarter. It makes repositories easier for AI to inherit.
