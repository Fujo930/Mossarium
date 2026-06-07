#!/usr/bin/env python3
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
