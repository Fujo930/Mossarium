"""Codex integration installer for Mossarium."""

import json
from pathlib import Path

from . import paths
from . import content as c
from .utils import ensure_dir, read_text


def _write_if_missing(filepath: str, content: str) -> str:
    """Write content to filepath if it doesn't exist. Returns 'CREATED' or 'SKIPPED'."""
    p = Path(filepath)
    if p.exists():
        return "SKIPPED"
    p.write_text(content, encoding="utf-8")
    return "CREATED"


def validate_codex_plugin_package() -> tuple[bool, list[str]]:
    """Validate the Codex plugin package scaffold.
    Returns (ok, issues) where ok is True if all checks pass."""
    issues = []

    # plugin.json
    pj = Path(paths.PLUGIN_JSON_FILE)
    if not pj.exists():
        issues.append(f"MISSING: {paths.PLUGIN_JSON_FILE}")
    else:
        try:
            data = json.loads(pj.read_text(encoding="utf-8"))
            for field in ["name", "version", "description", "skills"]:
                if field not in data:
                    issues.append(f"MISSING field in plugin.json: {field}")
            if data.get("skills") != "./skills/":
                issues.append(f"plugin.json skills should be './skills/', got: {data.get('skills')}")
        except json.JSONDecodeError:
            issues.append(f"INVALID JSON: {paths.PLUGIN_JSON_FILE}")

    # Plugin SKILL.md
    ps = Path(paths.PLUGIN_SKILL_FILE)
    if not ps.exists():
        issues.append(f"MISSING: {paths.PLUGIN_SKILL_FILE}")
    else:
        content = read_text(ps)
        if "name: mossarium" not in content:
            issues.append("SKILL.md missing frontmatter: name: mossarium")
        if "description:" not in content:
            issues.append("SKILL.md missing frontmatter: description:")

    # Plugin scripts
    for sp in [paths.PLUGIN_PREFLIGHT, paths.PLUGIN_FINISH]:
        if not Path(sp).exists():
            issues.append(f"MISSING: {sp}")

    # Plugin README
    if not Path(paths.PLUGIN_README).exists():
        issues.append(f"MISSING: {paths.PLUGIN_README}")

    # marketplace.json
    mf = Path(paths.MARKETPLACE_FILE)
    if not mf.exists():
        issues.append(f"MISSING: {paths.MARKETPLACE_FILE}")
    else:
        try:
            mdata = json.loads(mf.read_text(encoding="utf-8"))
            path_val = mdata.get("plugins", [{}])[0].get("source", {}).get("path", "")
            if path_val != "./plugins/mossarium-codex":
                issues.append(f"marketplace.json should point to ./plugins/mossarium-codex, got: {path_val}")
        except (json.JSONDecodeError, IndexError, KeyError):
            issues.append(f"INVALID: {paths.MARKETPLACE_FILE}")

    return (len(issues) == 0, issues)


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

    # Summary
    print()
    print(f"  Local skill scaffold:    {paths.CODEX_SKILL_DIR}/")
    print(f"  Plugin package scaffold: {paths.PLUGIN_DIR}/")
    print(f"  Repo marketplace scaffold:{paths.MARKETPLACE_FILE}")

    # Publication readiness check (v0.6.2)
    ok, issues = validate_codex_plugin_package()
    if ok:
        print(f"  Publication readiness:    OK")
    else:
        print(f"  Publication readiness:    WARN ({len(issues)} issue(s))")
        for issue in issues:
            print(f"    - {issue}")
