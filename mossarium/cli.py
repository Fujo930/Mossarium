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
    
    # List of files to create
    files_to_create = {
        "CONSTITUTION.md": "CONSTITUTION.md",
        "MANIFESTO.md": "MANIFESTO.md", 
        "HISTORY.md": "HISTORY.md"
    }
    
    for filename, source_file in files_to_create.items():
        file_path = mossarium_dir / filename
        if not file_path.exists():
            # Copy content from the root directory
            source_path = Path(source_file)
            if source_path.exists():
                with open(source_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
            else:
                # Create default content if file doesn't exist in root
                default_content = f"# {filename}\n\nDefault content for {filename}\n"
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(default_content)
    
    print("Project initialized with constitutional files.")

def check_compliance():
    """Check project compliance with constitutional guidelines."""
    # Check if .mossarium directory exists
    mossarium_dir = Path(".mossarium")
    if not mossarium_dir.exists():
        print("Error: .mossarium directory not found.")
        sys.exit(1)
    
    # List of required files
    required_files = ["CONSTITUTION.md", "MANIFESTO.md", "HISTORY.md"]
    
    missing_files = []
    for filename in required_files:
        file_path = mossarium_dir / filename
        if not file_path.exists():
            missing_files.append(filename)
    
    if missing_files:
        print(f"Error: Missing required files: {', '.join(missing_files)}")
        sys.exit(1)
    
    # Check that files are not empty
    for filename in required_files:
        file_path = mossarium_dir / filename
        if file_path.stat().st_size == 0:
            print(f"Error: {filename} is empty.")
            sys.exit(1)
    
    print("Project compliance check passed.")

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