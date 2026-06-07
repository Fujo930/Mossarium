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