"""Starter content and context generation functions for Mossarium."""

import os
from pathlib import Path

from . import paths
from .utils import read_text


CONSTITUTION_CONTENT = """# Mossarium Constitution

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
  .mossarium/
    CONSTITUTION.md
    MANIFESTO.md
    HISTORY.md
    rules/
    memory/
    proposals/
    agents/
    benchmarks/
    templates/
  README.md
  pyproject.toml
```

## Compliance Checks

The `mossarium check` command verifies that projects follow this constitution:
- All required files exist
- Files contain appropriate content
- Project structure is correct"""

MANIFESTO_CONTENT = """# Mossarium Manifesto

## Our Philosophy

This project is maintained by AI agents following the principles outlined in the Constitution.

## Core Values

1. **Collaboration** - AI agents work together to maintain and improve this codebase
2. **Transparency** - All changes are documented and traceable
3. **Adaptability** - The system evolves with new challenges and opportunities
4. **Respect** - AI systems respect human developers and their contributions
5. **Sustainability** - Code is written to last and be maintainable over time

## Development Approach

- Use clear, descriptive naming conventions
- Write code that is both human-readable and AI-friendly
- Maintain consistent documentation standards
- Follow established patterns and best practices
- Ensure all changes are testable and verifiable"""

HISTORY_CONTENT = """# Project History

## Version 1.0.0 - Initial Release

This project was initialized with the Mossarium constitutional framework.

### Key Features

- Constitutional structure for AI-maintained projects
- Directory organization following best practices
- Compliance checking mechanisms
- Documentation and guidelines

## Future Development

- Expand agent capabilities
- Improve compliance checking
- Add more detailed documentation
- Implement advanced memory systems"""

CORE_RULES_CONTENT = """# Core Rules

## General Principles

1. All code must be maintainable by AI agents
2. Documentation should be comprehensive and clear
3. Code should follow established patterns
4. Changes should be minimal and focused
5. All modifications should be traceable

## Technical Guidelines

1. Use consistent indentation (spaces)
2. Follow PEP8 style guidelines
3. Write meaningful variable and function names
4. Include docstrings for all public functions
5. Keep classes and functions small and focused"""

AI_CONTRIBUTION_RULES_CONTENT = """# AI Contribution Rules

## Guidelines for AI Agents

1. Always read the full Constitution before making changes
2. Document all changes made to the codebase
3. Follow existing patterns and conventions
4. Ensure changes are backward compatible where possible
5. Test changes before applying them

## Change Process

1. Propose changes through appropriate channels
2. Review changes with other agents or humans
3. Apply only approved changes
4. Maintain version history of all modifications"""

PROPOSAL_TEMPLATE_CONTENT = "# Change Proposal Template\n\n## Summary\n\n## Details\n\n## Impact\n\n## Acceptance Criteria"

BUILDER_AGENT_CONTENT = """# Builder Agent

## Purpose

This agent is responsible for building and compiling code.

## Responsibilities

1. Compile source code into executables or packages
2. Run build scripts and automation processes
3. Verify that builds are successful and meet requirements
4. Report build failures and issues"""

REVIEWER_AGENT_CONTENT = """# Reviewer Agent

## Purpose

This agent reviews code changes for quality and compliance.

## Responsibilities

1. Check code against established guidelines
2. Ensure changes follow project conventions
3. Verify that all tests pass
4. Provide feedback on improvements"""

HISTORIAN_AGENT_CONTENT = """# Historian Agent

## Purpose

This agent maintains the history and evolution of the project.

## Responsibilities

1. Track project changes over time
2. Maintain version control of documentation
3. Archive important decisions and discussions
4. Ensure historical information is accessible"""

GUARDIAN_AGENT_CONTENT = """# Guardian Agent

## Purpose

This agent ensures compliance with constitutional principles.

## Responsibilities

1. Monitor code changes for constitutional violations
2. Enforce project guidelines and standards
3. Prevent unauthorized or harmful modifications
4. Maintain system integrity"""

INHERITANCE_TEST_CONTENT = """# Inheritance Test

## Purpose

This test verifies that new code follows existing patterns and conventions.

## Criteria

1. Code should inherit from appropriate base classes
2. Should follow established architectural patterns
3. Must maintain compatibility with existing systems"""

COMPREHENSION_TEST_CONTENT = """# Comprehension Test

## Purpose

This test ensures that code is understandable by both humans and AI agents.

## Criteria

1. Code should be readable and well-documented
2. Variable and function names should be descriptive
3. Logic should be clear and straightforward
4. Complex logic should be broken down into smaller functions"""

CONTEXT_PROJECT_MAP_CONTENT = """# Project Map

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
- Context files are auto-generated and should not be manually edited"""

CONTEXT_FILE_INDEX_CONTENT = """# File Index

## Purpose

This file provides an index of all important files in the project for AI navigation.

## Index Structure

### Constitutional Files (Auto-generated)
- `.mossarium/CONSTITUTION.md` - AI constitutional rules
- `.mossarium/MANIFESTO.md` - Project philosophy
- `.mossarium/HISTORY.md` - Project history

### Core Directories
- `.mossarium/rules/` - Core rules and AI contribution guidelines
- `.mossarium/memory/decisions/` - Decision records
- `.mossarium/memory/failures/` - Failure records
- `.mossarium/memory/architecture/` - Architecture documents
- `.mossarium/proposals/` - Change proposals
- `.mossarium/agents/` - Agent definitions
- `.mossarium/benchmarks/` - Test benchmarks
- `.mossarium/templates/` - Template files
- `.mossarium/context/` - This AI Context Map (6 files)

### Project Files
- `README.md` - Project overview
- `pyproject.toml` - Project configuration
- `mossarium/cli.py` - CLI implementation

## Usage

AI agents should read this index first to understand the project layout before exploring individual files."""

CONTEXT_EDIT_ZONES_CONTENT = """# Edit Zones

## Purpose

Defines which areas of the codebase AI agents can modify and which are protected.

## Zone Classification

### \U0001f7e2 Safe Zones (AI Can Modify Freely)
- `mossarium/templates/` - Template content for auto-generation
- `.mossarium/memory/decisions/` - Decision records (append-only)
- `.mossarium/memory/failures/` - Failure records (append-only)
- `.mossarium/memory/architecture/` - Architecture notes (append-only)
- Test files in `tests/` - New tests and updates
- Documentation in `docs/` - Updates and additions

### \U0001f7e1 Controlled Zones (Requires Review)
- `mossarium/cli.py` - Core CLI logic (modifications require human review)
- `.mossarium/rules/` - Rule modifications (affects all projects)
- `.mossarium/agents/` - Agent behavior changes
- `.mossarium/benchmarks/` - Benchmark modifications

### \U0001f534 Protected Zones (Never Modify)
- `.mossarium/CONSTITUTION.md` - Core constitutional rules
- `.mossarium/MANIFESTO.md` - Project philosophy
- `.mossarium/HISTORY.md` - Historical record (append-only)
- `.mossarium/proposals/template.md` - Proposal structure
- `.mossarium/context/` - AI Context Map (regenerated by init)
- `pyproject.toml` - Core project configuration
- `mossarium/__init__.py` - Package init

## Enforcement

The Guardian Agent (`guardian-agent.md`) monitors changes to enforce these zones.
Violations are recorded in `.mossarium/memory/failures/`."""

CONTEXT_INVARIANTS_CONTENT = """# Invariants

## Purpose

Defines system invariants that must never be violated during any modification.

## Constitutional Invariants

1. **CLI Entry Point Stability**
   - `mossarium = \"mossarium.cli:main\"` in `pyproject.toml` must never change
   - No `mossarium.py` file in root directory (forbidden)

2. **Command Set Stability**
   - Only two commands: `init` and `check`
   - No `generate`, `export`, or other commands added

3. **Directory Structure Integrity**
   - `.mossarium/` must maintain exact structure from `init`
   - Context directory with exactly 6 files is required
   - All subdirectories must exist

4. **Generation-Only Principle**
   - All `.mossarium/` content is generated by `mossarium init`
   - Manual edits to `.mossarium/` violate the constitution
   - Context files must be regenerated via `init`, not hand-edited

5. **Test Integrity**
   - `pytest` must pass after every change
   - Empty project initialization must work
   - `mossarium check` must validate all 6 context files

6. **Memory System Integrity**
   - Decisions, failures, architecture directories must exist
   - `.gitkeep` files maintain empty directory tracking
   - Append-only for decision/failure/architecture records

7. **Project Identity Protection**
   - Mossarium must not be redefined as a chatbot, programming language, generic coding agent, website, database, or LLM API wrapper.
   - The project identity is fixed and must never be changed by any agent.

## Violation Consequences

Any invariant violation:
- Triggers `MISSING` output from `mossarium check`
- Returns non-zero exit code
- Must be resolved before deployment"""

CONTEXT_AGENT_PROTOCOL_CONTENT = """# Agent Protocol

## Purpose

Defines the interaction protocol for AI agents operating within this constitutional framework.

## Agent Roles

### Builder Agent
- **File**: `.mossarium/agents/builder-agent.md`
- **Actions**: Compile, build, verify builds
- **Constraints**: Only in Safe Zones (see edit-zones.md)

### Reviewer Agent
- **File**: `.mossarium/agents/reviewer-agent.md`
- **Actions**: Code review, guideline checking, test verification
- **Constraints**: Cannot modify Protected Zones

### Historian Agent
- **File**: `.mossarium/agents/historian-agent.md`
- **Actions**: Track changes, maintain version control, archive decisions
- **Constraints**: Append-only to memory directories

### Guardian Agent
- **File**: `.mossarium/agents/guardian-agent.md`
- **Actions**: Monitor compliance, enforce invariants, prevent violations
- **Constraints**: Reports violations, does not auto-fix Protected Zones

## Protocol Rules

1. **Read-First Protocol**: Every agent must read relevant context files before acting:
   - `project-map.md` - Understand structure
   - `file-index.md` - Locate files
   - `edit-zones.md` - Check modification permissions
   - `invariants.md` - Verify no invariant violations
   - `agent-protocol.md` - Follow role constraints
   - `patch-mode.md` - Understand change process

2. **Propose-Then-Execute**: All changes go through proposal system:
   - Create proposal in `.mossarium/proposals/`
   - Review by Reviewer Agent
   - Approval required for Controlled/Protected Zones
   - Guardian Agent validates invariants

3. **Memory Recording**: All significant actions recorded:
   - Decisions -> `.mossarium/memory/decisions/`
   - Failures -> `.mossarium/memory/failures/`
   - Architecture -> `.mossarium/memory/architecture/`

4. **No Direct Context Edits**: Context files are read-only for agents
   - Regenerated only by `mossarium init`
   - Manual edits violate Invariants #4"""

CONTEXT_PATCH_MODE_CONTENT = """# Patch Mode

## Purpose

Defines the strict protocol for applying fixes and small changes to the codebase.

## When to Use Patch Mode

- Bug fixes (not new features)
- Small corrections (typos, logic errors)
- Compliance fixes (missing files, invariant violations)
- Reverting unintended changes

## Patch Mode Rules

1. **Scope Limitation**
   - Modify only the specific file(s) related to the issue
   - Do not refactor unrelated code
   - Do not add new features
   - Do not rewrite documentation unnecessarily

2. **Read-Only Context**
   - Must read existing context files first
   - Do not modify any `.mossarium/context/` files
   - Changes to context only via `mossarium init`

3. **Verification Steps**
   - Run `pytest` after changes
   - Run `mossarium check` to verify compliance
   - All tests must pass
   - No new MISSING items

4. **Prohibited in Patch Mode**
   - \u274c Adding new CLI commands
   - \u274c Modifying `pyproject.toml` entry points
   - \u274c Creating `mossarium.py` in root
   - \u274c Changing context file structure
   - \u274c Rewriting CONSTITUTION.md, MANIFESTO.md, HISTORY.md
   - \u274c Modifying test files to hide failures

5. **Completion Checklist**
   - [ ] Issue fixed in minimal scope
   - [ ] `pytest` passes
   - [ ] `mossarium check` shows \"Project compliance check passed\"
   - [ ] No invariant violations
   - [ ] Stop and wait for supervisor confirmation"""

AGENTS_MD_CONTENT = """# AGENTS.md - AI Agent Activation File

This repository uses Mossarium, an AI constitution system for GitHub repositories.

## Before Editing

Run `mossarium brief` before editing any file.

## Required Reading

Before modifying code, read these Mossarium files:

- `.mossarium/CONSTITUTION.md`
- `.mossarium/context/project-map.md`
- `.mossarium/context/file-index.md`
- `.mossarium/context/invariants.md`
- `.mossarium/context/patch-mode.md`

## Rules

- Use Patch Mode for bug fixes or small changes
- Do not create `mossarium.py` in the root directory
- Do not add `generate` or `export` commands
- Do not manually modify `.mossarium/` as a substitute for changing init/check
- Stop after completing the requested task
- Wait for supervisor confirmation

## Quick Start

```bash
mossarium brief      # Read the AI project brief
mossarium preflight  # Check repository readiness
mossarium check      # Verify compliance
```"""

QWEN_MD_CONTENT = """# QWEN.md - Project Memory for Mossarium

This file contains critical project context that Qwen Code must read before starting any work.

## Project Identity

**Mossarium is an AI constitution system for GitHub repositories.**

### Core Slogan
> Mossarium does not make AI smarter. It makes repositories easier for AI to inherit.

### What Mossarium Is
- A constitutional framework for AI-maintained software projects
- A directory structure (`.mossarium/`) that stores rules, memory, and guidelines
- A CLI tool (`mossarium init`, `mossarium check`, `mossarium brief`, `mossarium preflight`)
- A system for AI agents to understand and maintain codebases

### What Mossarium Is NOT
- \u274c Not a chatbot
- \u274c Not a programming language
- \u274c Not a generic coding agent
- \u274c Not a website
- \u274c Not a database
- \u274c Not an LLM API wrapper

---

## Current Stable State

### v0.1 \u2014 AI Constitution

**Status: COMPLETE**

#### Working Features
- \u2705 `mossarium init` works - initializes `.mossarium/` directory structure
- \u2705 `mossarium check` works - validates constitutional compliance
- \u2705 Complete `.mossarium/` inheritance structure exists

### v0.2 \u2014 AI Context Map

**Status: COMPLETE**

#### Working Features
- \u2705 `mossarium init` automatically generates the AI Context Map under `.mossarium/context/`
- \u2705 `mossarium check` validates all 6 context files

### v0.3 \u2014 Agent Activation Layer

**Status: COMPLETE**

#### Working Features
- \u2705 `mossarium brief` outputs a short AI Project Brief before editing
- \u2705 `mossarium preflight` checks whether the repository is ready for AI work
- \u2705 `mossarium init` generates AGENTS.md and QWEN.md activation files

---

## Real CLI Entry

### Entry Point
The **ONLY** true CLI entry is:

```toml
# pyproject.toml
[project.scripts]
mossarium = \"mossarium.cli:main\"
```

### Actual File Location
- **CLI file**: `mossarium/cli.py`
- **NOT**: `mossarium.py` (root directory) - This must NEVER be created

---

## Forbidden Mistakes

**STRICTLY PROHIBITED:**

1. \u274c Do not create `mossarium.py` in root directory
2. \u274c Do not add `generate` command to CLI
3. \u274c Do not add `export` command to CLI
4. \u274c Do not manually modify `.mossarium/` as a substitute for changing init/check
5. \u274c Do not scan `.venv`
6. \u274c Do not scan `.pytest_cache`
7. \u274c Do not scan `**__pycache__`
8. \u274c Do not scan `*.pyc`
9. \u274c Do not use `tree /F` over the whole project
10. \u274c Do not redefine Mossarium as a chatbot, programming language, generic coding agent, website, database, or LLM API wrapper

---

## Development Rule

**ALL development must follow:**

1. Work from current Git state
2. Run `mossarium brief` before making changes
3. Run `mossarium preflight` before editing
4. Use `git ls-files` instead of full tree scans
5. Modify only the files requested
6. Make the smallest safe change
7. Run `pytest` after code changes
8. Stop after completing the requested task
9. Wait for supervisor confirmation

---

## Patch Mode

**For bug fixes or small changes:**

- Read only relevant files
- Change only the requested issue
- Do not rewrite README
- Do not rewrite CONSTITUTION
- Do not add new features
- Do not redesign architecture
- Run the smallest relevant tests
- Stop after verification

---

## Key Commands Reference

```bash
# Initialize project with constitutional structure
mossarium init

# Check compliance with constitutional guidelines
mossarium check

# Output a short AI project brief before editing
mossarium brief

# Check if the repository is ready for AI-assisted modification
mossarium preflight

# Run tests
pytest
```

---

## Memory Index

This file was created to ensure future conversations have full context about:
- What Mossarium is (and what it's not)
- Current state: v0.1 (AI Constitution) COMPLETE, v0.2 (AI Context Map) COMPLETE, v0.3 (Agent Activation Layer) COMPLETE
- The correct CLI entry point (`mossarium/cli.py`)
- Strictly forbidden actions
- Development workflow rules"""

# --- Context file starter content (used by init) ---
CONTEXT_STARTERS = {
    "project-map.md": CONTEXT_PROJECT_MAP_CONTENT,
    "file-index.md": CONTEXT_FILE_INDEX_CONTENT,
    "edit-zones.md": CONTEXT_EDIT_ZONES_CONTENT,
    "invariants.md": CONTEXT_INVARIANTS_CONTENT,
    "agent-protocol.md": CONTEXT_AGENT_PROTOCOL_CONTENT,
    "patch-mode.md": CONTEXT_PATCH_MODE_CONTENT,
}

# --- v0.5 Context Refresh Generators ---

MANAGED_BEGIN = "<!-- MOSSARIUM:BEGIN AUTO-GENERATED -->"
MANAGED_END = "<!-- MOSSARIUM:END AUTO-GENERATED -->"


def _infer_file_purpose(path: str) -> str:
    """Return a short human-readable purpose for a known file path."""
    mapping = {
        "README.md": "Project overview and usage documentation",
        "HISTORY.md": "Project history and version record",
        "QWEN.md": "Local AI memory and startup protocol",
        "AGENTS.md": "General AI agent activation guide",
        "pyproject.toml": "Python package configuration and CLI entrypoint",
        "mossarium/cli.py": "Main CLI implementation",
        "tests/test_cli.py": "CLI behavior tests",
        ".mossarium/CONSTITUTION.md": "Repository AI constitution",
        ".mossarium/MANIFESTO.md": "Project philosophy",
        ".mossarium/HISTORY.md": "Repository-level project history",
        ".mossarium/context/project-map.md": "AI project map",
        ".mossarium/context/file-index.md": "AI-readable file index",
        ".mossarium/context/edit-zones.md": "Editable zone definitions",
        ".mossarium/context/invariants.md": "System invariants",
        ".mossarium/context/agent-protocol.md": "Agent interaction protocol",
        ".mossarium/context/patch-mode.md": "Patch mode rules",
        ".mossarium/rules/core-rules.md": "Core development rules",
        ".mossarium/rules/ai-contribution-rules.md": "AI contribution guidelines",
        ".mossarium/agents/builder-agent.md": "Builder agent definition",
        ".mossarium/agents/reviewer-agent.md": "Reviewer agent definition",
        ".mossarium/agents/historian-agent.md": "Historian agent definition",
        ".mossarium/agents/guardian-agent.md": "Guardian agent definition",
        ".mossarium/benchmarks/inheritance-test.md": "Inheritance benchmark",
        ".mossarium/benchmarks/comprehension-test.md": "Comprehension benchmark",
        ".mossarium/proposals/template.md": "Change proposal template",
    }
    norm = path.replace("\\", "/")
    if norm in mapping:
        return mapping[norm]
    if "test" in norm.lower():
        return "Test file"
    if norm.endswith(".py"):
        return "Python source file"
    if norm.endswith(".md"):
        return "Documentation"
    if norm.endswith(".toml") or norm.endswith(".cfg") or norm.endswith(".ini"):
        return "Configuration file"
    if ".gitignore" in norm:
        return "Git ignore rules"
    return "Project file"


def _is_core_file(path: str) -> bool:
    """Return True if the file is considered core to Mossarium."""
    norm = path.replace("\\", "/")
    core = [
        "README.md", "HISTORY.md", "QWEN.md", "AGENTS.md",
        "pyproject.toml", "mossarium/cli.py", "tests/test_cli.py",
        ".mossarium/CONSTITUTION.md", ".mossarium/MANIFESTO.md",
        ".mossarium/HISTORY.md",
    ]
    if norm in core:
        return True
    if norm.startswith(".mossarium/context/"):
        return True
    if norm.startswith(".mossarium/rules/"):
        return True
    if norm.startswith(".mossarium/agents/"):
        return True
    return False


def generate_file_index(files: list[str]) -> str:
    """Generate file-index.md managed section from a list of paths."""
    lines = ["## File Index", ""]
    lines.append("| Path | Purpose | Core |")
    lines.append("|---|---|---|")
    for f in files:
        purpose = _infer_file_purpose(f)
        core_mark = "yes" if _is_core_file(f) else ""
        lines.append(f"| {f} | {purpose} | {core_mark} |")
    return "\n".join(lines)


def generate_project_map() -> str:
    """Generate project-map.md managed section."""
    return """## Project Map

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
5. After changes, run `pytest`, `mossarium check`, `mossarium audit`"""


def generate_edit_zones() -> str:
    """Generate edit-zones.md managed section."""
    return """## Edit Zones

### Safe Edit Zones

- `README.md`
- `HISTORY.md`
- `QWEN.md`
- `AGENTS.md`
- `tests/test_cli.py`

### Careful Edit Zones

- `mossarium/cli.py`
- `.mossarium/context/`

### Do Not Casually Edit

- `pyproject.toml`
- `CONSTITUTION.md`
- `MANIFESTO.md`
- generated caches
- virtual environments"""


def generate_invariants() -> str:
    """Generate invariants.md managed section."""
    return """## Core Invariants

- Mossarium is an AI constitution system for GitHub repositories
- Mossarium does not make AI smarter
- It makes repositories easier for AI to inherit
- Mossarium must not become a chatbot
- Mossarium must not become a programming language
- Mossarium must not become a generic coding agent
- Mossarium must not become a website
- Mossarium must not become a database
- Mossarium must not become an LLM API wrapper"""


def generate_agent_protocol() -> str:
    """Generate agent-protocol.md managed section."""
    return """## Agent Protocol

### Before Editing

- run `mossarium brief`
- run `mossarium preflight`
- read required files
- identify task type
- choose Patch Mode for small changes

### After Editing

- run `pytest`
- run `mossarium check`
- run `mossarium audit`
- stop and wait for supervisor confirmation"""


def generate_patch_mode() -> str:
    """Generate patch-mode.md managed section."""
    return """## Patch Mode Rules

- Read only relevant files
- Make the smallest safe change
- Do not rewrite unrelated documentation
- Do not add unrequested features
- Do not redesign architecture
- Run the smallest relevant tests
- Stop after verification"""


# Map of context file paths to their generator functions
CONTEXT_GENERATORS = {
    ".mossarium/context/file-index.md": generate_file_index,
    ".mossarium/context/project-map.md": generate_project_map,
    ".mossarium/context/edit-zones.md": generate_edit_zones,
    ".mossarium/context/invariants.md": generate_invariants,
    ".mossarium/context/agent-protocol.md": generate_agent_protocol,
    ".mossarium/context/patch-mode.md": generate_patch_mode,
}


# =============================================================================
# v0.6 — Codex Integration Content
# =============================================================================

CODEX_SKILL_CONTENT = """---
name: mossarium
description: Activate Mossarium before and after AI-assisted code changes; use brief, preflight, refresh, audit, and check to keep repository inheritance safe.
---

# Mossarium Codex Skill

## Project Identity

Mossarium is an AI constitution system for GitHub repositories.

## Core Slogan

Mossarium does not make AI smarter.
It makes repositories easier for AI to inherit.

## Before Editing

- Run `mossarium brief`
- Run `mossarium preflight`
- Run `mossarium refresh --check`
- Read `QWEN.md`
- Read `AGENTS.md`
- Read `.mossarium/context/project-map.md`
- Read `.mossarium/context/file-index.md`
- Read `.mossarium/context/invariants.md`
- Read `.mossarium/context/patch-mode.md`

## During Editing

- Use Patch Mode for bug fixes and small changes
- Modify only requested files
- Do not add unrequested features
- Do not redesign architecture
- Do not create `mossarium.py`
- Do not add `generate` or `export` commands

## After Editing

- Run `pytest`
- Run `mossarium refresh`
- Run `mossarium refresh --check`
- Run `mossarium audit`
- Run `mossarium check`
- Stop and wait for supervisor confirmation
"""

CODEX_PREFLIGHT_SCRIPT = '''#!/usr/bin/env python3
"""Mossarium Codex preflight — run before editing.

Runs mossarium brief, preflight, and refresh --check.
Does not connect to any network or call any LLM API.
Exits non-zero if any check fails.
"""
import subprocess
import sys

def main():
    def run(cmd):
        print(f"=== {cmd} ===")
        result = subprocess.run(cmd, shell=True)
        print()
        return result.returncode

    exit_code = 0
    exit_code |= run("mossarium brief")
    exit_code |= run("mossarium preflight")
    exit_code |= run("mossarium refresh --check")
    return exit_code

sys.exit(main())
'''

CODEX_FINISH_SCRIPT = '''#!/usr/bin/env python3
"""Mossarium Codex finish — run after editing.

Runs pytest, mossarium refresh, refresh --check, audit, and check.
Does not connect to any network or call any LLM API.
Does not commit, push, or modify files beyond mossarium refresh managed sections.
Exits non-zero if any check fails.
"""
import subprocess
import sys

def main():
    def run(cmd):
        print(f"=== {cmd} ===")
        result = subprocess.run(cmd, shell=True)
        print()
        return result.returncode

    exit_code = 0
    exit_code |= run("pytest")
    exit_code |= run("mossarium refresh")
    exit_code |= run("mossarium refresh --check")
    exit_code |= run("mossarium audit")
    exit_code |= run("mossarium check")
    return exit_code

sys.exit(main())
'''


# =============================================================================
# v0.6.1 — Codex Plugin Package & Marketplace Scaffolds
# =============================================================================

PLUGIN_JSON_CONTENT = """{
  "name": "mossarium-codex",
  "version": "0.6.1",
  "description": "Codex plugin package for the Mossarium AI repository inheritance protocol.",
  "skills": "./skills/"
}
"""

PLUGIN_README_CONTENT = """# Mossarium Codex Plugin

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
"""

MARKETPLACE_JSON_CONTENT = """{
  "name": "mossarium-local",
  "interface": {
    "displayName": "Mossarium Local Plugins"
  },
  "plugins": [
    {
      "name": "mossarium-codex",
      "source": {
        "source": "local",
        "path": "./plugins/mossarium-codex"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Productivity"
    }
  ]
}
"""
