# Mossarium Constitution

## Introduction

This constitution establishes the guidelines and conventions for software projects maintained by AI systems. It serves as a reference for maintaining consistency, quality, and clarity in codebases.

## AI Constitutional Rules

1. **AI-Agent Readiness**: All code must be structured to allow AI agents to read and understand the project's purpose, history, and current state before making any changes.

2. **Constitutional Compliance**: Any AI agent modifying code must first read and understand the constitution in its entirety.

3. **Change Proposals**: All modifications must be proposed through a process that allows for review by other agents or humans.

4. **History Preservation**: The project's history must be maintained in a way that AI agents can understand past decisions and reasoning.

5. **Memory System**: The project must have an accessible memory system that AI agents can reference when making decisions.

6. **Inheritance Checks**: Any new code or changes must be checked against existing constitutional principles.

7. **Code Readability**: Code must be written in a way that is understandable to both humans and AI systems.

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