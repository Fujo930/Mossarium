"""check command — verify project compliance with constitutional guidelines."""

import sys
from pathlib import Path

from . import paths


def check_compliance():
    """Check project compliance with constitutional guidelines."""
    mossarium_dir = Path(paths.MOSSARIUM_DIR)
    if not mossarium_dir.exists():
        print("MISSING")
        sys.exit(1)

    missing = []

    # Required root files
    for filename in paths.ROOT_FILES:
        if not (mossarium_dir / filename).exists():
            missing.append(filename)

    # Required directories
    for d in paths.REQUIRED_DIRS:
        if not (mossarium_dir / d).exists():
            missing.append(d)

    # Required files in subdirectories
    for rel_path, display in paths.FILES_IN_DIRS:
        if not (mossarium_dir / rel_path).exists():
            missing.append(display)

    if missing:
        print(f"MISSING: {', '.join(missing)}")
        sys.exit(1)

    # Check root files are not empty
    for filename in paths.ROOT_FILES:
        fp = mossarium_dir / filename
        if fp.stat().st_size == 0:
            print(f"ERROR: {filename} is empty.")
            sys.exit(1)

    print("Project compliance check passed")
