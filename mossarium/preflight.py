"""preflight command — check if the repository is ready for AI-assisted modification."""

import sys
from pathlib import Path

from . import paths


def preflight():
    """Check whether the repository is ready for AI-assisted modification."""
    failed = False

    for filepath in paths.PREFLIGHT_REQUIRED:
        if not Path(filepath).exists():
            print(f"FAIL: Required file missing: {filepath}")
            failed = True

    for filepath in paths.FORBIDDEN_FAIL:
        if Path(filepath).exists():
            print(f"FAIL: Forbidden file exists: {filepath}")
            failed = True

    for dirpath in paths.WARN_DIRS:
        p = Path(dirpath)
        if p.exists() and p.is_dir():
            print(f"WARN: Local directory found: {dirpath}")

    if failed:
        sys.exit(1)

    print("Mossarium preflight passed")
