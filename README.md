# Mossarium

**Mossarium is an AI constitution system for GitHub repositories.**

> **Mossarium does not make AI smarter.**
> **It makes repositories easier for AI to inherit.**

## Features

- `mossarium init` - Initialize project with complete constitutional structure + AI Context Map + Agent Activation files
- `mossarium check` - Check project compliance with constitutional requirements
- `mossarium brief` - Output a short AI project brief before editing
- `mossarium preflight` - Check whether the repository is ready for AI-assisted modification
- `mossarium audit` - Check whether a repository is ready for AI inheritance

## Installation

```bash
pip install -e .
```

## Usage

```bash
# Initialize a new project with constitutional files
# Now generates:
#   - constitutional structure (CONSTITUTION, MANIFESTO, HISTORY)
#   - memory structure (decisions, failures, architecture)
#   - proposal structure (templates)
#   - agent role files (builder, reviewer, historian, guardian)
#   - benchmark files (inheritance, comprehension)
#   - AI Context Map (6 files)
#   - Agent Activation files (AGENTS.md, QWEN.md)
mossarium init

# Check project compliance
# Verifies all constitutional files + AI Context Map exist
mossarium check

# Output a short AI project brief before editing
mossarium brief

# Check if the repository is ready for AI-assisted modification
mossarium preflight

# Check whether a repository is ready for AI inheritance
mossarium audit
```

## AI Context Map (v0.2)

Mossarium v0.2 adds an **AI Context Map** generated under:

```
.mossarium/context/
├── project-map.md       # High-level project structure & entry points
├── file-index.md        # Index of all important files for AI navigation
├── edit-zones.md        # Safe / controlled / protected modification zones
├── invariants.md        # System invariants that must never be violated
├── agent-protocol.md    # Interaction protocol for AI agents (read-first, propose-then-execute)
└── patch-mode.md        # Strict protocol for minimal, safe fixes
```

These files help AI agents understand **before modifying code**:

- **Project goals** — what the project is and how it's organized
- **File responsibilities** — which files do what
- **Editable zones** — where AI can safely make changes
- **Invariants** — rules that must never be broken
- **Agent protocol** — how agents coordinate (read-first, propose-then-execute)
- **Patch mode** — minimal, safe fix protocol

## Agent Activation Layer (v0.3)

Mossarium v0.3 adds an **Agent Activation Layer** so AI agents know what to read, what to obey, and what to avoid — without repeated human reminders.

### New Commands

- `mossarium brief` — Outputs a short AI Project Brief with project identity, required reading, forbidden actions, recommended workflow, and patch mode rules.
- `mossarium preflight` — Checks whether the repository is ready for AI-assisted modification by verifying required files exist, forbidden files are absent, and warning about local directories.

### Activation Files

`mossarium init` now also generates:

- `AGENTS.md` — Universal AI agent entry point telling any AI agent to run `mossarium brief` and follow Mossarium rules.
- `QWEN.md` — Project memory file for Qwen Code / local AI tools, containing full project context and development rules.

## Inheritance Audit (v0.4)

Mossarium v0.4 adds **Inheritance Audit**, a deterministic check that evaluates whether a repository is truly ready for AI inheritance — without calling any AI, without connecting to any network, and without auto-fixing anything.

### How the Commands Differ

- `mossarium check` — verifies structure (are constitutional files present?)
- `mossarium preflight` — verifies activation safety before editing (are activation files present? are forbidden files absent?)
- `mossarium audit` — verifies inheritance quality (are required files present? do context files have content? are semantic markers in place? are forbidden files absent?)

### Usage

```bash
mossarium audit
```

## What Mossarium Provides

Mossarium establishes an AI-readable constitution, history, memory, proposal process, inheritance checks, and an **AI Context Map** for software projects.

## Important Notes

This is **NOT**:
- A chatbot
- A programming language
- An AI coding agent
- A website or database
- An LLM API wrapper

## Core Principle

Mossarium gives software projects a constitution that future AI agents must read before changing code.