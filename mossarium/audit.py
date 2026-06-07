"""audit command — check whether a repository is ready for AI inheritance."""

import sys
from pathlib import Path

from . import paths
from .utils import read_text, file_has_content


def audit():
    """Check whether a repository is ready for AI inheritance."""
    print("Mossarium Inheritance Audit")
    print()

    failed = False
    warnings = False

    # --- Required Files ---
    for filepath in paths.AUDIT_REQUIRED:
        if Path(filepath).exists():
            print(f"[OK] Required file: {filepath}")
        else:
            print(f"[FAIL] Required file missing: {filepath}")
            failed = True

    # --- Context Files Must Not Be Empty ---
    for filepath in paths.AUDIT_CONTEXT_FILES:
        p = Path(filepath)
        if p.exists():
            if p.stat().st_size == 0:
                print(f"[FAIL] Context file is empty: {filepath}")
                failed = True
            else:
                print(f"[OK] Context file has content: {filepath}")

    # --- Semantic Checks (WARN only) ---
    # README.md
    readme_path = Path("README.md")
    if readme_path.exists():
        content = read_text(readme_path)
        for marker, label in [
            ("Mossarium", "Mossarium"),
            ("AI Context Map", "AI Context Map"),
            ("Agent Activation Layer", "Agent Activation Layer"),
        ]:
            if marker in content:
                print(f"[OK] README.md mentions {label}")
            else:
                print(f"[WARN] README.md does not mention {label}")
                warnings = True

    # QWEN.md
    qwen_path = Path("QWEN.md")
    if qwen_path.exists():
        content = read_text(qwen_path)
        for needle, label in [
            ("mossarium/cli.py", "mossarium/cli.py"),
            ("Do not create mossarium.py", "'Do not create mossarium.py'"),
            ("Do not add generate command", "'Do not add generate command'"),
            ("Do not add export command", "'Do not add export command'"),
            ("Patch Mode", "'Patch Mode'"),
        ]:
            if needle in content:
                print(f"[OK] QWEN.md contains {label}")
            else:
                print(f"[WARN] QWEN.md does not contain {label}")
                warnings = True

    # AGENTS.md
    agents_path = Path("AGENTS.md")
    if agents_path.exists():
        content = read_text(agents_path)
        for needle, label in [
            ("mossarium brief", "'mossarium brief'"),
            ("mossarium preflight", "'mossarium preflight'"),
            ("Patch Mode", "'Patch Mode'"),
        ]:
            if needle in content:
                print(f"[OK] AGENTS.md contains {label}")
            else:
                print(f"[WARN] AGENTS.md does not contain {label}")
                warnings = True

    # invariants.md
    inv_path = Path(".mossarium/context/invariants.md")
    if file_has_content(inv_path):
        content = read_text(inv_path).lower()
        terms = ["chatbot", "programming language", "generic coding agent",
                 "website", "database", "LLM API wrapper"]
        found = [t for t in terms if t.lower() in content]
        if len(found) >= 2:
            print("[OK] invariants.md covers identity constraints")
        else:
            print(f"[WARN] invariants.md should cover identity constraints (found {len(found)}/2)")
            warnings = True

    # patch-mode.md
    pm_path = Path(".mossarium/context/patch-mode.md")
    if file_has_content(pm_path):
        content = read_text(pm_path)
        if any(t in content for t in ["smallest safe change", "minimal patch", "Patch Mode"]):
            print("[OK] patch-mode.md defines patch protocol")
        else:
            print("[WARN] patch-mode.md should define patch protocol")
            warnings = True

    # --- Forbidden Files ---
    for filepath in paths.FORBIDDEN_FAIL:
        if Path(filepath).exists():
            print(f"[FAIL] Forbidden file exists: {filepath}")
            failed = True
        else:
            print(f"[OK] No forbidden file: {filepath}")

    for dirpath in paths.WARN_DIRS:
        p = Path(dirpath)
        if p.exists() and p.is_dir():
            print(f"[WARN] Local directory found: {dirpath}")
            warnings = True

    # *.pyc outside cache dirs
    pyc_all = list(Path(".").rglob("*.pyc"))
    pyc_bad = [f for f in pyc_all
               if ".venv" not in str(f)
               and ".pytest_cache" not in str(f)
               and "__pycache__" not in str(f)]
    if pyc_bad:
        print("[WARN] *.pyc files found outside cache dirs")
        warnings = True

    # --- Result ---
    print()
    if failed:
        print("Result: FAIL")
        sys.exit(1)
    elif warnings:
        print("Result: PASS WITH WARNINGS")
    else:
        print("Result: PASS")
