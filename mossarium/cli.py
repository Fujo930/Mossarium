#!/usr/bin/env python3
"""
Mossarium - A constitutional system for AI-maintained software projects
"""

import argparse
import os
import sys
from pathlib import Path

def init_project():
    """Initialize a project with constitutional files."""
    # Create .mossarium directory if it doesn't exist
    mossarium_dir = Path(".mossarium")
    mossarium_dir.mkdir(exist_ok=True)

    # Create all required subdirectories and files
    # Create rules directory structure
    rules_dir = mossarium_dir / "rules"
    rules_dir.mkdir(parents=True, exist_ok=True)

    # Create memory directory structure with .gitkeep files
    memory_dir = mossarium_dir / "memory"
    decisions_dir = memory_dir / "decisions"
    failures_dir = memory_dir / "failures"
    architecture_dir = memory_dir / "architecture"

    decisions_dir.mkdir(parents=True, exist_ok=True)
    failures_dir.mkdir(parents=True, exist_ok=True)
    architecture_dir.mkdir(parents=True, exist_ok=True)

    # Create proposals directory structure
    proposals_dir = mossarium_dir / "proposals"
    proposals_dir.mkdir(parents=True, exist_ok=True)

    # Create agents directory structure
    agents_dir = mossarium_dir / "agents"
    agents_dir.mkdir(parents=True, exist_ok=True)

    # Create benchmarks directory structure
    benchmarks_dir = mossarium_dir / "benchmarks"
    benchmarks_dir.mkdir(parents=True, exist_ok=True)

    # Create templates directory structure
    templates_dir = mossarium_dir / "templates"
    templates_dir.mkdir(parents=True, exist_ok=True)

    # Create context directory structure
    context_dir = mossarium_dir / "context"
    context_dir.mkdir(parents=True, exist_ok=True)

    # Create the required files in .mossarium root
    files_to_create = {
        "CONSTITUTION.md": None,  # Will be created with default content
        "MANIFESTO.md": None,    # Will be created with default content
        "HISTORY.md": None       # Will be created with default content
    }

    # Create the core rule files in rules directory
    core_rules_file = rules_dir / "core-rules.md"
    ai_contribution_rules_file = rules_dir / "ai-contribution-rules.md"

    # Create the memory subdirectories with .gitkeep files
    decisions_gitkeep = decisions_dir / ".gitkeep"
    failures_gitkeep = failures_dir / ".gitkeep"
    architecture_gitkeep = architecture_dir / ".gitkeep"

    # Create the proposal template file
    proposal_template_file = proposals_dir / "template.md"

    # Create agent files
    builder_agent_file = agents_dir / "builder-agent.md"
    reviewer_agent_file = agents_dir / "reviewer-agent.md"
    historian_agent_file = agents_dir / "historian-agent.md"
    guardian_agent_file = agents_dir / "guardian-agent.md"

    # Create benchmark files
    inheritance_test_file = benchmarks_dir / "inheritance-test.md"
    comprehension_test_file = benchmarks_dir / "comprehension-test.md"

    # Create meaningful default content for root files
    constitution_content = """# Mossarium Constitution

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
    
    manifesto_content = """# Mossarium Manifesto

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
    
    history_content = """# Project History

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

    # Create meaningful default content for all files
    root_files_content = {
        "CONSTITUTION.md": constitution_content,
        "MANIFESTO.md": manifesto_content,
        "HISTORY.md": history_content
    }

    # Create core rule files with default content
    core_rules_content = """# Core Rules

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
    
    ai_contribution_rules_content = """# AI Contribution Rules

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
    
    # Create all root files with proper content
    for filename, content in root_files_content.items():
        file_path = mossarium_dir / filename
        if not file_path.exists():
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

    # Create core rule files with default content
    if not core_rules_file.exists():
        with open(core_rules_file, 'w', encoding='utf-8') as f:
            f.write(core_rules_content)
            
    if not ai_contribution_rules_file.exists():
        with open(ai_contribution_rules_file, 'w', encoding='utf-8') as f:
            f.write(ai_contribution_rules_content)

    # Create .gitkeep files for memory directories
    if not decisions_gitkeep.exists():
        with open(decisions_gitkeep, 'w', encoding='utf-8') as f:
            pass  # Empty file
            
    if not failures_gitkeep.exists():
        with open(failures_gitkeep, 'w', encoding='utf-8') as f:
            pass  # Empty file
            
    if not architecture_gitkeep.exists():
        with open(architecture_gitkeep, 'w', encoding='utf-8') as f:
            pass  # Empty file

    # Create proposal template file
    if not proposal_template_file.exists():
        with open(proposal_template_file, 'w', encoding='utf-8') as f:
            f.write("# Change Proposal Template\n\n## Summary\n\n## Details\n\n## Impact\n\n## Acceptance Criteria")

    # Create agent files with default content
    builder_agent_content = """# Builder Agent

## Purpose

This agent is responsible for building and compiling code.

## Responsibilities

1. Compile source code into executables or packages
2. Run build scripts and automation processes
3. Verify that builds are successful and meet requirements
4. Report build failures and issues"""

    reviewer_agent_content = """# Reviewer Agent

## Purpose

This agent reviews code changes for quality and compliance.

## Responsibilities

1. Check code against established guidelines
2. Ensure changes follow project conventions
3. Verify that all tests pass
4. Provide feedback on improvements"""
    
    historian_agent_content = """# Historian Agent

## Purpose

This agent maintains the history and evolution of the project.

## Responsibilities

1. Track project changes over time
2. Maintain version control of documentation
3. Archive important decisions and discussions
4. Ensure historical information is accessible"""

    guardian_agent_content = """# Guardian Agent

## Purpose

This agent ensures compliance with constitutional principles.

## Responsibilities

1. Monitor code changes for constitutional violations
2. Enforce project guidelines and standards
3. Prevent unauthorized or harmful modifications
4. Maintain system integrity"""
    
    if not builder_agent_file.exists():
        with open(builder_agent_file, 'w', encoding='utf-8') as f:
            f.write(builder_agent_content)
            
    if not reviewer_agent_file.exists():
        with open(reviewer_agent_file, 'w', encoding='utf-8') as f:
            f.write(reviewer_agent_content)
            
    if not historian_agent_file.exists():
        with open(historian_agent_file, 'w', encoding='utf-8') as f:
            f.write(historian_agent_content)
            
    if not guardian_agent_file.exists():
        with open(guardian_agent_file, 'w', encoding='utf-8') as f:
            f.write(guardian_agent_content)

    # Create benchmark files with default content
    inheritance_test_content = """# Inheritance Test

## Purpose

This test verifies that new code follows existing patterns and conventions.

## Criteria

1. Code should inherit from appropriate base classes
2. Should follow established architectural patterns
3. Must maintain compatibility with existing systems"""
    
    comprehension_test_content = """# Comprehension Test

## Purpose

This test ensures that code is understandable by both humans and AI agents.

## Criteria

1. Code should be readable and well-documented
2. Variable and function names should be descriptive
3. Logic should be clear and straightforward
4. Complex logic should be broken down into smaller functions"""
    
    if not inheritance_test_file.exists():
        with open(inheritance_test_file, 'w', encoding='utf-8') as f:
            f.write(inheritance_test_content)
            
    if not comprehension_test_file.exists():
        with open(comprehension_test_file, 'w', encoding='utf-8') as f:
            f.write(comprehension_test_content)

    # Create AI Context Map files
    context_files = {
        "project-map.md": """# Project Map

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
- Context files are auto-generated and should not be manually edited""",

        "file-index.md": """# File Index

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

AI agents should read this index first to understand the project layout before exploring individual files.""",

        "edit-zones.md": """# Edit Zones

## Purpose

Defines which areas of the codebase AI agents can modify and which are protected.

## Zone Classification

### 🟢 Safe Zones (AI Can Modify Freely)
- `mossarium/templates/` - Template content for auto-generation
- `.mossarium/memory/decisions/` - Decision records (append-only)
- `.mossarium/memory/failures/` - Failure records (append-only)
- `.mossarium/memory/architecture/` - Architecture notes (append-only)
- Test files in `tests/` - New tests and updates
- Documentation in `docs/` - Updates and additions

### 🟡 Controlled Zones (Requires Review)
- `mossarium/cli.py` - Core CLI logic (modifications require human review)
- `.mossarium/rules/` - Rule modifications (affects all projects)
- `.mossarium/agents/` - Agent behavior changes
- `.mossarium/benchmarks/` - Benchmark modifications

### 🔴 Protected Zones (Never Modify)
- `.mossarium/CONSTITUTION.md` - Core constitutional rules
- `.mossarium/MANIFESTO.md` - Project philosophy
- `.mossarium/HISTORY.md` - Historical record (append-only)
- `.mossarium/proposals/template.md` - Proposal structure
- `.mossarium/context/` - AI Context Map (regenerated by init)
- `pyproject.toml` - Core project configuration
- `mossarium/__init__.py` - Package init

## Enforcement

The Guardian Agent (`guardian-agent.md`) monitors changes to enforce these zones.
Violations are recorded in `.mossarium/memory/failures/`.""",

        "invariants.md": """# Invariants

## Purpose

Defines system invariants that must never be violated during any modification.

## Constitutional Invariants

1. **CLI Entry Point Stability**
   - `mossarium = "mossarium.cli:main"` in `pyproject.toml` must never change
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

## Violation Consequences

Any invariant violation:
- Triggers `MISSING` output from `mossarium check`
- Returns non-zero exit code
- Must be resolved before deployment""",

        "agent-protocol.md": """# Agent Protocol

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
   - Decisions → `.mossarium/memory/decisions/`
   - Failures → `.mossarium/memory/failures/`
   - Architecture → `.mossarium/memory/architecture/`

4. **No Direct Context Edits**: Context files are read-only for agents
   - Regenerated only by `mossarium init`
   - Manual edits violate Invariants #4""",

        "patch-mode.md": """# Patch Mode

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
   - ❌ Adding new CLI commands
   - ❌ Modifying `pyproject.toml` entry points
   - ❌ Creating `mossarium.py` in root
   - ❌ Changing context file structure
   - ❌ Rewriting CONSTITUTION.md, MANIFESTO.md, HISTORY.md
   - ❌ Modifying test files to hide failures

5. **Completion Checklist**
   - [ ] Issue fixed in minimal scope
   - [ ] `pytest` passes
   - [ ] `mossarium check` shows "Project compliance check passed"
   - [ ] No invariant violations
   - [ ] Stop and wait for supervisor confirmation""",
    }

    for filename, content in context_files.items():
        file_path = context_dir / filename
        if not file_path.exists():
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

    # Create Agent Activation files in project root (v0.3)
    agents_md_content = """# AGENTS.md - AI Agent Activation File

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
```
"""

    qwen_md_content = """# QWEN.md - Project Memory for Mossarium

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
- ❌ Not a chatbot
- ❌ Not a programming language
- ❌ Not a generic coding agent
- ❌ Not a website
- ❌ Not a database
- ❌ Not an LLM API wrapper

---

## Current Stable State

### v0.1 — AI Constitution

**Status: COMPLETE**

#### Working Features
- ✅ `mossarium init` works - initializes `.mossarium/` directory structure
- ✅ `mossarium check` works - validates constitutional compliance
- ✅ Complete `.mossarium/` inheritance structure exists

### v0.2 — AI Context Map

**Status: COMPLETE**

#### Working Features
- ✅ `mossarium init` automatically generates the AI Context Map under `.mossarium/context/`
- ✅ `mossarium check` validates all 6 context files

### v0.3 — Agent Activation Layer

**Status: COMPLETE**

#### Working Features
- ✅ `mossarium brief` outputs a short AI Project Brief before editing
- ✅ `mossarium preflight` checks whether the repository is ready for AI work
- ✅ `mossarium init` generates AGENTS.md and QWEN.md activation files

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

1. ❌ Do not create `mossarium.py` in root directory
2. ❌ Do not add `generate` command to CLI
3. ❌ Do not add `export` command to CLI
4. ❌ Do not manually modify `.mossarium/` as a substitute for changing init/check
5. ❌ Do not scan `.venv`
6. ❌ Do not scan `.pytest_cache`
7. ❌ Do not scan `**__pycache__`
8. ❌ Do not scan `*.pyc`
9. ❌ Do not use `tree /F` over the whole project
10. ❌ Do not redefine Mossarium as a chatbot, programming language, generic coding agent, website, database, or LLM API wrapper

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
- Development workflow rules
"""

    # Create AGENTS.md if it doesn't exist
    agents_md_path = Path("AGENTS.md")
    if not agents_md_path.exists():
        with open(agents_md_path, 'w', encoding='utf-8') as f:
            f.write(agents_md_content)

    # Create QWEN.md if it doesn't exist
    qwen_md_path = Path("QWEN.md")
    if not qwen_md_path.exists():
        with open(qwen_md_path, 'w', encoding='utf-8') as f:
            f.write(qwen_md_content)

    print("Project initialized with complete constitutional structure.")

def check_compliance():
    """Check project compliance with constitutional guidelines."""
    # Check if .mossarium directory exists
    mossarium_dir = Path(".mossarium")
    if not mossarium_dir.exists():
        print("MISSING")
        sys.exit(1)

    # List of required root files
    required_files = ["CONSTITUTION.md", "MANIFESTO.md", "HISTORY.md"]

    missing_files = []
    for filename in required_files:
        file_path = mossarium_dir / filename
        if not file_path.exists():
            missing_files.append(filename)

    # Check directory structure
    required_dirs = [
        "rules",
        "memory/decisions",
        "memory/failures",
        "memory/architecture",
        "proposals",
        "agents",
        "benchmarks",
        "templates",
        "context"
    ]

    missing_dirs = []
    for dir_path in required_dirs:
        full_path = mossarium_dir / dir_path
        if not full_path.exists():
            missing_dirs.append(dir_path)

    # Check specific files in directories
    required_files_in_dirs = [
        ("rules/core-rules.md", "core-rules.md"),
        ("rules/ai-contribution-rules.md", "ai-contribution-rules.md"),
        ("memory/decisions/.gitkeep", ".gitkeep"),
        ("memory/failures/.gitkeep", ".gitkeep"),
        ("memory/architecture/.gitkeep", ".gitkeep"),
        ("proposals/template.md", "template.md"),
        ("agents/builder-agent.md", "builder-agent.md"),
        ("agents/reviewer-agent.md", "reviewer-agent.md"),
        ("agents/historian-agent.md", "historian-agent.md"),
        ("agents/guardian-agent.md", "guardian-agent.md"),
        ("benchmarks/inheritance-test.md", "inheritance-test.md"),
        ("benchmarks/comprehension-test.md", "comprehension-test.md"),
        ("context/project-map.md", "project-map.md"),
        ("context/file-index.md", "file-index.md"),
        ("context/edit-zones.md", "edit-zones.md"),
        ("context/invariants.md", "invariants.md"),
        ("context/agent-protocol.md", "agent-protocol.md"),
        ("context/patch-mode.md", "patch-mode.md")
    ]

    missing_files_in_dirs = []
    for dir_file_path, display_name in required_files_in_dirs:
        full_path = mossarium_dir / dir_file_path
        if not full_path.exists():
            missing_files_in_dirs.append(display_name)

    all_missing = missing_files + missing_dirs + missing_files_in_dirs

    if all_missing:
        print(f"MISSING: {', '.join(all_missing)}")
        sys.exit(1)

    # Check that files are not empty
    for filename in required_files:
        file_path = mossarium_dir / filename
        if file_path.stat().st_size == 0:
            print(f"ERROR: {filename} is empty.")
            sys.exit(1)

    print("Project compliance check passed")

def brief_project():
    """Output a short AI Project Brief for AI agents before editing."""
    brief = """===============================================================================
MOSSARIUM AI PROJECT BRIEF
===============================================================================

1. PROJECT IDENTITY

Mossarium is an AI constitution system for GitHub repositories.

2. CORE SLOGAN

Mossarium does not make AI smarter.
It makes repositories easier for AI to inherit.

3. REQUIRED READING

Before editing any file, read:

  * QWEN.md
  * README.md
  * .mossarium/CONSTITUTION.md
  * .mossarium/HISTORY.md
  * .mossarium/context/project-map.md
  * .mossarium/context/file-index.md
  * .mossarium/context/invariants.md
  * .mossarium/context/patch-mode.md

4. FORBIDDEN ACTIONS

  * Do not create mossarium.py
  * Do not add generate command
  * Do not add export command
  * Do not manually modify .mossarium/ as a substitute for init/check changes
  * Do not scan .venv, .pytest_cache, **pycache**, or *.pyc
  * Do not redefine Mossarium as a chatbot, programming language,
    generic coding agent, website, database, or LLM API wrapper

5. RECOMMENDED WORKFLOW

  * Run mossarium brief before editing
  * Read required files
  * Identify task type
  * Use Patch Mode for bug fixes or small changes
  * Modify only requested files
  * Run pytest after code changes
  * Stop and wait for supervisor confirmation

6. PATCH MODE REMINDER

  * Read only relevant files
  * Make the smallest safe change
  * Do not rewrite unrelated documentation
  * Do not add unrequested features
  * Do not redesign architecture

==============================================================================="""
    print(brief)

def preflight():
    """Check whether the repository is ready for AI-assisted modification."""
    required_files = [
        "QWEN.md",
        "README.md",
        ".mossarium/CONSTITUTION.md",
        ".mossarium/HISTORY.md",
        ".mossarium/context/project-map.md",
        ".mossarium/context/file-index.md",
        ".mossarium/context/invariants.md",
        ".mossarium/context/patch-mode.md",
    ]

    forbidden_files = [
        "mossarium.py",
        "tests/README.md",
    ]

    warn_dirs = [
        ".qwen/",
        ".venv/",
        ".pytest_cache/",
        "**pycache**/",
    ]

    failed = False

    # Check required files
    for filepath in required_files:
        p = Path(filepath)
        if not p.exists():
            print(f"FAIL: Required file missing: {filepath}")
            failed = True

    # Check forbidden files
    for filepath in forbidden_files:
        p = Path(filepath)
        if p.exists():
            print(f"FAIL: Forbidden file exists: {filepath}")
            failed = True

    # Check warning-only directories
    for dirpath in warn_dirs:
        p = Path(dirpath)
        if p.exists() and p.is_dir():
            print(f"WARN: Local directory found: {dirpath}")

    if failed:
        sys.exit(1)

    print("Mossarium preflight passed")

def audit():
    """Check whether a repository is ready for AI inheritance."""
    print("Mossarium Inheritance Audit")
    print()

    failed = False
    warnings = False

    # --- Required Files ---
    required_files = [
        "README.md",
        "HISTORY.md",
        "QWEN.md",
        "AGENTS.md",
        ".mossarium/CONSTITUTION.md",
        ".mossarium/HISTORY.md",
        ".mossarium/context/project-map.md",
        ".mossarium/context/file-index.md",
        ".mossarium/context/edit-zones.md",
        ".mossarium/context/invariants.md",
        ".mossarium/context/agent-protocol.md",
        ".mossarium/context/patch-mode.md",
    ]

    for filepath in required_files:
        p = Path(filepath)
        if p.exists():
            print(f"[OK] Required file: {filepath}")
        else:
            print(f"[FAIL] Required file missing: {filepath}")
            failed = True

    # --- Context Files Must Not Be Empty ---
    context_files = [
        ".mossarium/context/project-map.md",
        ".mossarium/context/file-index.md",
        ".mossarium/context/edit-zones.md",
        ".mossarium/context/invariants.md",
        ".mossarium/context/agent-protocol.md",
        ".mossarium/context/patch-mode.md",
    ]

    for filepath in context_files:
        p = Path(filepath)
        if p.exists():
            if p.stat().st_size == 0:
                print(f"[FAIL] Context file is empty: {filepath}")
                failed = True
            else:
                print(f"[OK] Context file has content: {filepath}")

    # --- Semantic Checks (WARN only) ---

    # README.md checks
    readme_path = Path("README.md")
    if readme_path.exists():
        readme_content = readme_path.read_text(encoding='utf-8', errors='ignore')
        if "Mossarium" in readme_content:
            print("[OK] README.md mentions Mossarium")
        else:
            print("[WARN] README.md does not mention Mossarium")
            warnings = True
        if "AI Context Map" in readme_content:
            print("[OK] README.md mentions AI Context Map")
        else:
            print("[WARN] README.md does not mention AI Context Map")
            warnings = True
        if "Agent Activation Layer" in readme_content:
            print("[OK] README.md mentions Agent Activation Layer")
        else:
            print("[WARN] README.md does not mention Agent Activation Layer")
            warnings = True

    # QWEN.md checks
    qwen_path = Path("QWEN.md")
    if qwen_path.exists():
        qwen_content = qwen_path.read_text(encoding='utf-8', errors='ignore')
        qwen_checks = [
            ("mossarium/cli.py", "mossarium/cli.py"),
            ("Do not create mossarium.py", "'Do not create mossarium.py'"),
            ("Do not add generate command", "'Do not add generate command'"),
            ("Do not add export command", "'Do not add export command'"),
            ("Patch Mode", "'Patch Mode'"),
        ]
        for needle, label in qwen_checks:
            if needle in qwen_content:
                print(f"[OK] QWEN.md contains {label}")
            else:
                print(f"[WARN] QWEN.md does not contain {label}")
                warnings = True

    # AGENTS.md checks
    agents_path = Path("AGENTS.md")
    if agents_path.exists():
        agents_content = agents_path.read_text(encoding='utf-8', errors='ignore')
        agents_checks = [
            ("mossarium brief", "'mossarium brief'"),
            ("mossarium preflight", "'mossarium preflight'"),
            ("Patch Mode", "'Patch Mode'"),
        ]
        for needle, label in agents_checks:
            if needle in agents_content:
                print(f"[OK] AGENTS.md contains {label}")
            else:
                print(f"[WARN] AGENTS.md does not contain {label}")
                warnings = True

    # invariants.md: must contain at least 2 of the identity-forbidden terms
    invariants_path = Path(".mossarium/context/invariants.md")
    if invariants_path.exists() and invariants_path.stat().st_size > 0:
        inv_content = invariants_path.read_text(encoding='utf-8', errors='ignore')
        identity_terms = [
            "chatbot",
            "programming language",
            "generic coding agent",
            "website",
            "database",
            "LLM API wrapper",
        ]
        found_terms = [t for t in identity_terms if t.lower() in inv_content.lower()]
        if len(found_terms) >= 2:
            print(f"[OK] invariants.md covers identity constraints")
        else:
            print(f"[WARN] invariants.md should cover identity constraints (found {len(found_terms)}/2)")
            warnings = True

    # patch-mode.md: must contain one of the patch terms
    patch_mode_path = Path(".mossarium/context/patch-mode.md")
    if patch_mode_path.exists() and patch_mode_path.stat().st_size > 0:
        pm_content = patch_mode_path.read_text(encoding='utf-8', errors='ignore')
        patch_terms = ["smallest safe change", "minimal patch", "Patch Mode"]
        if any(t in pm_content for t in patch_terms):
            print("[OK] patch-mode.md defines patch protocol")
        else:
            print("[WARN] patch-mode.md should define patch protocol")
            warnings = True

    # --- Forbidden Files ---
    forbidden_fail = [
        "mossarium.py",
        "tests/README.md",
    ]

    for filepath in forbidden_fail:
        p = Path(filepath)
        if p.exists():
            print(f"[FAIL] Forbidden file exists: {filepath}")
            failed = True
        else:
            print(f"[OK] No forbidden file: {filepath}")

    forbidden_warn = [
        ".qwen/",
        ".venv/",
        ".pytest_cache/",
        "__pycache__/",
    ]

    for dirpath in forbidden_warn:
        p = Path(dirpath)
        if p.exists() and p.is_dir():
            print(f"[WARN] Local directory found: {dirpath}")
            warnings = True

    # Check for *.pyc files
    pyc_files = list(Path(".").rglob("*.pyc"))
    # Filter out .venv and .pytest_cache
    pyc_filtered = [f for f in pyc_files if ".venv" not in str(f) and ".pytest_cache" not in str(f) and "__pycache__" not in str(f)]
    if pyc_filtered:
        print(f"[WARN] *.pyc files found outside cache dirs")
        warnings = True

    # --- Result ---
    print()
    if failed:
        print("Result: FAIL")
        sys.exit(1)
    elif warnings:
        print("Result: PASS WITH WARNINGS")
    else:
        print("Result: PASS")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description="Mossarium - Constitutional system for AI-maintained software projects")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # init command
    init_parser = subparsers.add_parser("init", help="Initialize project with constitutional files")

    # check command
    check_parser = subparsers.add_parser("check", help="Check project compliance with constitutional guidelines")

    # brief command
    brief_parser = subparsers.add_parser("brief", help="Output a short AI project brief before editing")

    # preflight command
    preflight_parser = subparsers.add_parser("preflight", help="Check if the repository is ready for AI-assisted modification")

    # audit command
    audit_parser = subparsers.add_parser("audit", help="Check whether a repository is ready for AI inheritance")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    if args.command == "init":
        init_project()
    elif args.command == "check":
        check_compliance()
    elif args.command == "brief":
        brief_project()
    elif args.command == "preflight":
        preflight()
    elif args.command == "audit":
        audit()

if __name__ == "__main__":
    main()