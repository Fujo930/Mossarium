#!/usr/bin/env python3
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
