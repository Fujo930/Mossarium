# Mossarium

**Mossarium is an AI constitution system for GitHub repositories.**

> **Mossarium does not make AI smarter.**
> **It makes repositories easier for AI to inherit.**

## Features

- `mossarium init` - Initialize project with complete constitutional structure + AI Context Map
- `mossarium check` - Check project compliance with constitutional requirements

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
mossarium init

# Check project compliance
# Verifies all constitutional files + AI Context Map exist
mossarium check
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