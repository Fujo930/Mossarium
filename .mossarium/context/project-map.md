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

### Project Identity

Mossarium is an AI constitution system for GitHub repositories.

### Known Commands

- `mossarium init`
- `mossarium check`
- `mossarium brief`
- `mossarium preflight`
- `mossarium audit`
- `mossarium refresh`

### Important Directories

- `.mossarium/` — Constitutional framework root
- `.mossarium/context/` — AI Context Map
- `.mossarium/rules/` — Core rules
- `.mossarium/agents/` — Agent definitions
- `.mossarium/memory/` — Decisions, failures, architecture
- `mossarium/` — CLI implementation
- `tests/` — Test suite

### Main Implementation Files

- `mossarium/cli.py` — All CLI commands
- `tests/test_cli.py` — Behavior tests

### AI Inheritance Workflow

1. Run `mossarium brief` before editing
2. Run `mossarium preflight` to verify readiness
3. Read required files
4. Identify task type
5. Use Patch Mode for small changes
6. Run `pytest` after code changes
7. Run `mossarium audit` to verify inheritance quality
8. Stop and wait for supervisor confirmation
<!-- MOSSARIUM:END AUTO-GENERATED -->
