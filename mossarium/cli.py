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

    # Create default content for root files
    default_content = "# Default Content\n\nThis is the default content for this file.\n"

    # Create all files with default content if they don't exist
    files_to_create_paths = [
        core_rules_file,
        ai_contribution_rules_file,
        decisions_gitkeep,
        failures_gitkeep,
        architecture_gitkeep,
        proposal_template_file,
        builder_agent_file,
        reviewer_agent_file,
        historian_agent_file,
        guardian_agent_file,
        inheritance_test_file,
        comprehension_test_file
    ]

    # Create root files with default content
    for filename, template_path in files_to_create.items():
        file_path = mossarium_dir / filename
        if not file_path.exists():
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(default_content)

    # Create all other files with default content
    for file_path in files_to_create_paths:
        if not file_path.exists():
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(default_content)

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