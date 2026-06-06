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
        "templates"
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
        ("benchmarks/comprehension-test.md", "comprehension-test.md")
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

def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description="Mossarium - Constitutional system for AI-maintained software projects")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # init command
    init_parser = subparsers.add_parser("init", help="Initialize project with constitutional files")

    # check command
    check_parser = subparsers.add_parser("check", help="Check project compliance with constitutional guidelines")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    if args.command == "init":
        init_project()
    elif args.command == "check":
        check_compliance()

if __name__ == "__main__":
    main()