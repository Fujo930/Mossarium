"""Codex integration installer for Mossarium."""

from pathlib import Path

from . import paths
from . import content as c
from .utils import ensure_dir


def _write_if_missing(filepath: str, content: str) -> str:
    """Write content to filepath if it doesn't exist. Returns 'CREATED' or 'SKIPPED'."""
    p = Path(filepath)
    if p.exists():
        return "SKIPPED"
    p.write_text(content, encoding="utf-8")
    return "CREATED"


def install_codex_integration():
    """Install Codex local integration scaffold under .codex/skills/mossarium/."""
    ensure_dir(paths.CODEX_SKILL_DIR)
    ensure_dir(paths.CODEX_SCRIPTS_DIR)

    results = []

    # SKILL.md
    status = _write_if_missing(paths.CODEX_SKILL_FILE, c.CODEX_SKILL_CONTENT)
    results.append((status, paths.CODEX_SKILL_FILE))

    # preflight.py
    status = _write_if_missing(paths.CODEX_PREFLIGHT_SCRIPT, c.CODEX_PREFLIGHT_SCRIPT)
    results.append((status, paths.CODEX_PREFLIGHT_SCRIPT))

    # finish.py
    status = _write_if_missing(paths.CODEX_FINISH_SCRIPT, c.CODEX_FINISH_SCRIPT)
    results.append((status, paths.CODEX_FINISH_SCRIPT))

    for status, path in results:
        if status == "CREATED":
            print(f"  CREATED: {path}")
        else:
            print(f"  SKIPPED existing: {path}")

    created_count = sum(1 for s, _ in results if s == "CREATED")
    if created_count == 0:
        print("\nCodex integration already present.")
    else:
        print(f"\nCodex integration installed.")
