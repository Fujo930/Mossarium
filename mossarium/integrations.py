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
    """Install Codex local integration scaffold under .codex/skills/mossarium/
    plus plugin package scaffold under plugins/mossarium-codex/
    plus repo-scoped marketplace under .agents/plugins/."""

    # --- Local skill scaffold (v0.6.0) ---
    ensure_dir(paths.CODEX_SKILL_DIR)
    ensure_dir(paths.CODEX_SCRIPTS_DIR)

    results = []

    results.append((_write_if_missing(paths.CODEX_SKILL_FILE, c.CODEX_SKILL_CONTENT), paths.CODEX_SKILL_FILE))
    results.append((_write_if_missing(paths.CODEX_PREFLIGHT_SCRIPT, c.CODEX_PREFLIGHT_SCRIPT), paths.CODEX_PREFLIGHT_SCRIPT))
    results.append((_write_if_missing(paths.CODEX_FINISH_SCRIPT, c.CODEX_FINISH_SCRIPT), paths.CODEX_FINISH_SCRIPT))

    # --- Plugin package scaffold (v0.6.1) ---
    ensure_dir(paths.PLUGIN_CODEX_DIR)
    ensure_dir(paths.PLUGIN_SKILL_DIR)
    ensure_dir(paths.PLUGIN_SCRIPTS_DIR)

    results.append((_write_if_missing(paths.PLUGIN_JSON_FILE, c.PLUGIN_JSON_CONTENT), paths.PLUGIN_JSON_FILE))
    results.append((_write_if_missing(paths.PLUGIN_SKILL_FILE, c.CODEX_SKILL_CONTENT), paths.PLUGIN_SKILL_FILE))
    results.append((_write_if_missing(paths.PLUGIN_PREFLIGHT, c.CODEX_PREFLIGHT_SCRIPT), paths.PLUGIN_PREFLIGHT))
    results.append((_write_if_missing(paths.PLUGIN_FINISH, c.CODEX_FINISH_SCRIPT), paths.PLUGIN_FINISH))
    results.append((_write_if_missing(paths.PLUGIN_README, c.PLUGIN_README_CONTENT), paths.PLUGIN_README))

    # --- Marketplace scaffold (v0.6.1) ---
    ensure_dir(paths.MARKETPLACE_DIR)
    results.append((_write_if_missing(paths.MARKETPLACE_FILE, c.MARKETPLACE_JSON_CONTENT), paths.MARKETPLACE_FILE))

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
        print(f"  local skill scaffold:  {paths.CODEX_SKILL_DIR}/")
        print(f"  plugin package:        {paths.PLUGIN_DIR}/")
        print(f"  marketplace scaffold:  {paths.MARKETPLACE_FILE}")
