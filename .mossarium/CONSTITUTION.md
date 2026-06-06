# Mossarium Constitution

## Introduction

This constitution establishes the guidelines and conventions for software projects maintained by AI systems. It serves as a reference for maintaining consistency, quality, and clarity in codebases.

## Core Principles

1. **Documentation First** - All code changes must be documented
2. **Consistency** - Follow established patterns and conventions
3. **Minimalism** - Keep solutions simple and avoid over-engineering
4. **Testability** - Ensure all code can be tested effectively
5. **Maintainability** - Write code that is easy to understand and modify

## Project Structure

### Required Files
- `README.md` - Project overview and usage instructions
- `.mossarium/CONSTITUTION.md` - This document
- `.mossarium/MANIFESTO.md` - Project philosophy
- `.mossarium/HISTORY.md` - Project history and evolution
- `pyproject.toml` - Project configuration

### Directory Structure
```
project/
├── .mossarium/
│   ├── CONSTITUTION.md
│   ├── MANIFESTO.md
│   └── HISTORY.md
├── README.md
└── pyproject.toml
```

## Compliance Checks

The `mossarium check` command verifies that projects follow this constitution:
- All required files exist
- Files contain appropriate content
- Project structure is correct