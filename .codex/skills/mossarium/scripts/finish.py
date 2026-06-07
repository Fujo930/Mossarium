#!/usr/bin/env python3
"""Mossarium Codex finish — run after editing."""
import subprocess
import sys

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
sys.exit(exit_code)
