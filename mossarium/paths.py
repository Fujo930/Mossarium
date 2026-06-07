"""Centralised path definitions for Mossarium."""

# --- Root Mossarium directory ---
MOSSARIUM_DIR = ".mossarium"

# --- Required root files in .mossarium ---
ROOT_FILES = ["CONSTITUTION.md", "MANIFESTO.md", "HISTORY.md"]

# --- Required directories inside .mossarium ---
REQUIRED_DIRS = [
    "rules",
    "memory/decisions",
    "memory/failures",
    "memory/architecture",
    "proposals",
    "agents",
    "benchmarks",
    "templates",
    "context",
]

# --- Files required inside subdirectories (for check) ---
FILES_IN_DIRS = [
    ("rules/core-rules.md", "core-rules.md"),
    ("rules/ai-contribution-rules.md", "ai-contribution-rules.md"),
    ("memory/decisions/.gitkeep", ".gitkeep"),
    ("memory/failures/.gitkeep", ".gitkeep"),
    ("memory/architecture/.gitkeep", ".gitkeep"),
    ("proposals/template.md", "template.md"),
    ("agents/builder-agent.md", "builder-agent.md"),
    ("agents/reviewer-agent.md", "reviewer-agent.md"),
    ("agents/historian-agent.md", "historian-agent.md"),
    ("agents/guardian-agent.md", "guardian-agent.md"),
    ("benchmarks/inheritance-test.md", "inheritance-test.md"),
    ("benchmarks/comprehension-test.md", "comprehension-test.md"),
    ("context/project-map.md", "project-map.md"),
    ("context/file-index.md", "file-index.md"),
    ("context/edit-zones.md", "edit-zones.md"),
    ("context/invariants.md", "invariants.md"),
    ("context/agent-protocol.md", "agent-protocol.md"),
    ("context/patch-mode.md", "patch-mode.md"),
]

# --- Context files (full relative from .mossarium) ---
CONTEXT_FILES = [
    "project-map.md",
    "file-index.md",
    "edit-zones.md",
    "invariants.md",
    "agent-protocol.md",
    "patch-mode.md",
]

CONTEXT_DIR = ".mossarium/context"

# --- Required files for preflight ---
PREFLIGHT_REQUIRED = [
    "QWEN.md",
    "README.md",
    ".mossarium/CONSTITUTION.md",
    ".mossarium/HISTORY.md",
    ".mossarium/context/project-map.md",
    ".mossarium/context/file-index.md",
    ".mossarium/context/invariants.md",
    ".mossarium/context/patch-mode.md",
]

# --- Required files for audit ---
AUDIT_REQUIRED = [
    "README.md",
    "HISTORY.md",
    "QWEN.md",
    "AGENTS.md",
    ".mossarium/CONSTITUTION.md",
    ".mossarium/HISTORY.md",
    ".mossarium/context/project-map.md",
    ".mossarium/context/file-index.md",
    ".mossarium/context/edit-zones.md",
    ".mossarium/context/invariants.md",
    ".mossarium/context/agent-protocol.md",
    ".mossarium/context/patch-mode.md",
]

# --- Context files that must be non-empty (for audit) ---
AUDIT_CONTEXT_FILES = [
    ".mossarium/context/project-map.md",
    ".mossarium/context/file-index.md",
    ".mossarium/context/edit-zones.md",
    ".mossarium/context/invariants.md",
    ".mossarium/context/agent-protocol.md",
    ".mossarium/context/patch-mode.md",
]

# --- Forbidden files (FAIL) ---
FORBIDDEN_FAIL = [
    "mossarium.py",
    "tests/README.md",
]

# --- Warning-only local directories ---
WARN_DIRS = [
    ".qwen/",
    ".venv/",
    ".pytest_cache/",
    "__pycache__/",
]

# --- Directories/patterns excluded from file scanning ---
EXCLUDED_SCAN = [
    ".git", ".venv", ".pytest_cache", "__pycache__", ".qwen",
    "build", "dist",
]

EXCLUDED_SCAN_DIRS = {".git", ".venv", ".pytest_cache", "__pycache__", ".qwen", "build", "dist"}

# --- Codex integration paths ---
CODEX_SKILL_DIR = ".codex/skills/mossarium"
CODEX_SCRIPTS_DIR = ".codex/skills/mossarium/scripts"
CODEX_SKILL_FILE = ".codex/skills/mossarium/SKILL.md"
CODEX_PREFLIGHT_SCRIPT = ".codex/skills/mossarium/scripts/preflight.py"
CODEX_FINISH_SCRIPT = ".codex/skills/mossarium/scripts/finish.py"
