"""Shared utility helpers used across Mossarium modules."""

import os
from pathlib import Path


def ensure_dir(path: str | Path):
    """Create directory with parents if it doesn't exist."""
    Path(path).mkdir(parents=True, exist_ok=True)


def write_if_missing(filepath: str | Path, content: str):
    """Write content to filepath only if it does not already exist."""
    p = Path(filepath)
    if not p.exists():
        p.write_text(content, encoding="utf-8")


def write_if_missing_bytes(filepath: str | Path, content: str):
    """Write content to filepath only if it does not already exist (utf-8)."""
    p = Path(filepath)
    if not p.exists():
        p.write_text(content, encoding="utf-8")


def read_text(filepath: str | Path) -> str:
    """Read a file as UTF-8 text."""
    p = Path(filepath)
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8", errors="ignore")


def file_has_content(filepath: str | Path) -> bool:
    """Return True if the file exists and is non-empty."""
    p = Path(filepath)
    return p.exists() and p.stat().st_size > 0
