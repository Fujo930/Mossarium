# Project Map

## Overview

This document provides a high-level map of the project structure and key components.

## Directory Structure

```
project/
  .mossarium/          # Constitutional framework
  src/                 # Source code (language-specific)
  tests/               # Test files
  docs/                # Documentation
  config/              # Configuration files
```

## Key Entry Points

- **Main CLI**: `mossarium/cli.py` - Entry point for all commands
- **Constitution**: `.mossarium/CONSTITUTION.md` - Core rules
- **Memory**: `.mossarium/memory/` - Decisions, failures, architecture
- **Agents**: `.mossarium/agents/` - AI agent definitions
- **Context**: `.mossarium/context/` - This AI Context Map

## Component Relationships

- `mossarium init` creates the full `.mossarium/` structure
- `mossarium check` verifies constitutional compliance
- Context files are auto-generated and should not be manually edited

<!-- MOSSARIUM:BEGIN AUTO-GENERATED -->
## Project Map

Mossarium is an AI constitution system for GitHub repositories.

### Known Commands

- `mossarium init`
- `mossarium check`
- `mossarium brief`
- `mossarium preflight`
- `mossarium audit`
- `mossarium refresh`

### Important Directories

- `mossarium/` — CLI implementation modules
- `tests/` — Test suite
- `.mossarium/` — Constitutional framework
- `.mossarium/context/` — AI Context Map

### Main Implementation Files

- `mossarium/cli.py` — CLI entry point and command dispatch
- `tests/test_cli.py` — Behaviour tests

### AI Inheritance Workflow

1. Run `mossarium brief` to understand the project
2. Run `mossarium preflight` to check readiness
3. Read `.mossarium/context/` files for context
4. Identify task type and choose Patch Mode for small changes
5. After changes, run `pytest`, `mossarium check`, `mossarium audit`
<!-- MOSSARIUM:END AUTO-GENERATED -->
