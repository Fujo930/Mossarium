#!/usr/bin/env python3
"""Mossarium Codex preflight — run before editing."""
import subprocess
import sys

def run(cmd):
    print(f"=== {cmd} ===")
    result = subprocess.run(cmd, shell=True)
    print()
    return result.returncode

exit_code = 0
exit_code |= run("mossarium brief")
exit_code |= run("mossarium preflight")
exit_code |= run("mossarium refresh --check")
sys.exit(exit_code)
