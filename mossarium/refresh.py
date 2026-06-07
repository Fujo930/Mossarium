"""refresh command — context refresh engine management."""

import os
import sys
from pathlib import Path

from . import content as c
from . import paths
from .utils import read_text

MANAGED_BEGIN = "<!-- MOSSARIUM:BEGIN AUTO-GENERATED -->"
MANAGED_END = "<!-- MOSSARIUM:END AUTO-GENERATED -->"


def _get_project_files():
    """Return a sorted list of project file paths, using git ls-files or fallback."""
    import subprocess as sp
    try:
        result = sp.run(["git", "ls-files"], capture_output=True, text=True, timeout=10)
        if result.returncode == 0 and result.stdout.strip():
            return sorted(result.stdout.strip().splitlines())
    except Exception:
        pass

    files = []
    for root, dirs, filenames in os.walk("."):
        dirs[:] = [d for d in dirs if d not in paths.EXCLUDED_SCAN_DIRS]
        for fn in filenames:
            if fn.endswith(".pyc"):
                continue
            rel = os.path.relpath(os.path.join(root, fn), ".")
            parts = Path(rel).parts
            if any(p in paths.EXCLUDED_SCAN_DIRS for p in parts):
                continue
            files.append(rel.replace("\\", "/"))
    return sorted(files)


def _managed_replace(filepath: str, new_section: str) -> bool:
    """Replace content between MANAGED_BEGIN and MANAGED_END markers.
    Returns True if the file was modified."""
    p = Path(filepath)
    if not p.exists():
        return False

    content = read_text(filepath)
    begin_idx = content.find(MANAGED_BEGIN)
    end_idx = content.find(MANAGED_END)

    new_block = f"{MANAGED_BEGIN}\n{new_section.rstrip()}\n{MANAGED_END}"

    if begin_idx != -1 and end_idx != -1 and end_idx > begin_idx:
        new_content = content[:begin_idx] + new_block + content[end_idx + len(MANAGED_END):]
        if new_content != content:
            p.write_text(new_content, encoding="utf-8")
            return True
        return False
    else:
        if not content.endswith("\n"):
            content += "\n"
        new_content = content + "\n" + new_block + "\n"
        p.write_text(new_content, encoding="utf-8")
        return True


def _read_managed_section(filepath: str) -> str:
    """Return the content between managed markers, or empty string."""
    content = read_text(filepath)
    begin_idx = content.find(MANAGED_BEGIN)
    end_idx = content.find(MANAGED_END)
    if begin_idx != -1 and end_idx != -1 and end_idx > begin_idx:
        return content[begin_idx + len(MANAGED_BEGIN):end_idx].strip()
    return ""


CONTEXT_GENERATORS = {
    ".mossarium/context/file-index.md": lambda: c.generate_file_index(_get_project_files()),
    ".mossarium/context/project-map.md": c.generate_project_map,
    ".mossarium/context/edit-zones.md": c.generate_edit_zones,
    ".mossarium/context/invariants.md": c.generate_invariants,
    ".mossarium/context/agent-protocol.md": c.generate_agent_protocol,
    ".mossarium/context/patch-mode.md": c.generate_patch_mode,
}


def refresh_project():
    """Refresh AI Context Map managed sections from current repository state."""
    updated = 0
    for filepath, generator in CONTEXT_GENERATORS.items():
        new_section = generator()
        changed = _managed_replace(filepath, new_section)
        if changed:
            print(f"Refreshed: {filepath}")
            updated += 1
        else:
            print(f"Up to date: {filepath}")
    if updated == 0:
        print("Context map is up to date.")
    else:
        print(f"{updated} context file(s) refreshed.")


def check_refresh():
    """Check whether managed sections are stale. Exits non-zero if any differ."""
    stale = 0
    for filepath, generator in CONTEXT_GENERATORS.items():
        expected = generator()
        actual = _read_managed_section(filepath)
        if actual != expected.rstrip():
            print(f"STALE: {filepath}")
            stale += 1
    if stale:
        print(f"{stale} context file(s) are out of date.")
        sys.exit(1)
    else:
        print("Context map is up to date.")
