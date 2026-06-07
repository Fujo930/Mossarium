# Mossarium History

## v0.6.2 — Codex Plugin Publication Candidate

v0.6.2 validates and polishes the Codex plugin package scaffold toward publication readiness.

- `validate_codex_plugin_package()` checks plugin.json, SKILL.md, scripts, README, marketplace.json
- Plugin README expanded with sections: What This Is, How to Test Locally, Recommended Workflow, Commands, Publication Status
- Scripts use `sys.exit(main())` pattern with safety comments
- Both SKILL.md copies verified consistent
- 5 new tests; 46 total

## v0.6.1 — Codex Packaging Readiness

v0.6.1 adds Codex plugin packaging scaffolds to `mossarium integrate codex`, preparing Mossarium for future Codex plugin marketplace submission.

### New Scaffolds
- Plugin package candidate: `plugins/mossarium-codex/` with `.codex-plugin/plugin.json`, skill copy, scripts copy, and README
- Repo-scoped marketplace: `.agents/plugins/marketplace.json` pointing to the plugin package
- SKILL.md now includes YAML frontmatter with `name` and `description` fields per Codex spec

### Compatibility
v0.6.0's local skill scaffold (`.codex/skills/mossarium/`) is fully preserved.

### Changes in v0.6.1
- `mossarium integrate codex` extended to create plugin package and marketplace scaffolds
- SKILL.md updated with YAML frontmatter
- `mossarium/content.py` extended with plugin.json, plugin README, and marketplace.json content
- `mossarium/paths.py` extended with plugin and marketplace paths
- 3 new tests: plugin package creation, plugin.json validity, marketplace.json validity
- All previous 38 tests still pass; total 41 tests

## v0.6.0 — Codex Integration Layer

Mossarium v0.6 introduces `mossarium integrate codex`.

It creates a local Codex integration scaffold under `.codex/skills/mossarium/` so Codex-style coding agents can activate Mossarium before and after editing — without requiring developers to manually run CLI commands.

### New Command
- `mossarium integrate codex` — Installs a local Codex skill with SKILL.md, preflight.py, and finish.py

### Generated Files
- `.codex/skills/mossarium/SKILL.md` — Mossarium protocol for Codex agents
- `.codex/skills/mossarium/scripts/preflight.py` — Runs brief, preflight, refresh --check before editing
- `.codex/skills/mossarium/scripts/finish.py` — Runs pytest, refresh, audit, check after editing

### Changes in v0.6
- `mossarium integrate codex` command added
- `mossarium/integrations.py` module created
- Codex content added to `mossarium/content.py`
- 6 new tests covering integration install, file creation, content checks, idempotence, and help output
- All previous 32 tests still pass; total 38 tests

## v0.5.1 — Internal Refactor for AI Maintainability

v0.5.1 splits the large CLI implementation into focused modules without changing any public behavior.

### New Module Structure

| Module | Purpose |
|---|---|
| `mossarium/cli.py` | CLI dispatch only (1577 → 52 lines) |
| `mossarium/init.py` | Project initialization |
| `mossarium/check.py` | Compliance checking |
| `mossarium/brief.py` | AI project brief |
| `mossarium/preflight.py` | Activation safety check |
| `mossarium/audit.py` | Inheritance audit |
| `mossarium/refresh.py` | Context refresh engine |
| `mossarium/content.py` | Starter content and generators |
| `mossarium/paths.py` | Centralised path definitions |
| `mossarium/utils.py` | Shared helpers |

All 32 tests pass with zero behavior changes. Future agents should prefer editing focused modules instead of expanding `mossarium/cli.py`.

## v0.5.0 — Context Refresh Engine

**AI memory must stay in sync with the repository it describes.**

Mossarium v0.5 introduces `mossarium refresh` and `mossarium refresh --check`.

It moves Mossarium from static AI memory to maintainable AI memory. `mossarium refresh` scans the current repository and updates managed sections inside the six AI Context Map files — using `<!-- MOSSARIUM:BEGIN AUTO-GENERATED -->` markers to replace generated content while preserving all user-written content outside those sections.

### New Commands
- `mossarium refresh` — Regenerates AI Context Map from current repository state
- `mossarium refresh --check` — Reports STALE for any managed section that differs from expected output; exits non-zero without writing files

### Design
- Managed sections allow Mossarium to safely update context without touching user-authored notes
- File scanning uses `git ls-files` with a safe directory-walk fallback
- Excludes `.git/`, `.venv/`, `.pytest_cache/`, `__pycache__/`, `.qwen/`, `build/`, `dist/`, `*.egg-info/`, `*.pyc`

### Changes in v0.5
- `mossarium refresh` command added
- `mossarium refresh --check` command added
- Six context file generators implemented (file-index, project-map, edit-zones, invariants, agent-protocol, patch-mode)
- 8 new tests covering refresh, managed sections, user content preservation, --check pass/fail, file-index content, and noise exclusion
- All previous 24 tests still pass; total 32 tests

## v0.4.0 — Inheritance Audit

**Structure and activation are not enough. A repository must prove it is ready for AI inheritance.**

Mossarium v0.4 introduces `mossarium audit`, a deterministic audit command that checks whether a repository is ready for AI inheritance. It evaluates required files, context file quality, semantic markers in activation files, forbidden file patterns, and known AI failure indicators — without calling any AI, without connecting to any network, and without auto-fixing anything.

### New Command
- `mossarium audit` — Performs a full inheritance audit with [OK], [WARN], and [FAIL] markers, producing Result: PASS, PASS WITH WARNINGS, or FAIL.

### Audit Checks
- 12 required files (README, HISTORY, QWEN, AGENTS, constitution, 6 context files)
- Context file content (all 6 must be non-empty)
- Semantic markers (README mentions Mossarium/AI Context Map/Agent Activation Layer, QWEN contains key prohibitions, AGENTS contains brief/preflight/Patch Mode, invariants covers identity constraints, patch-mode defines patch protocol)
- Forbidden files (mossarium.py, tests/README.md → FAIL; .qwen/, .venv/, .pytest_cache/, __pycache__/, *.pyc → WARN)

### Changes in v0.4
- `mossarium audit` command added with deterministic inheritance checks
- 10 new tests covering audit happy path, missing files, forbidden files, empty context, warnings-only, and .qwen/ directory
- All previous 15 tests still pass; total 24 tests

## v0.3.0 — Agent Activation Layer

**AI agents shouldn't need repeated human reminders to know what to read.**

Mossarium v0.3 introduces an **Agent Activation Layer** that tells AI agents what to read, what to obey, and what to avoid — without human prompting.

### New Commands
- `mossarium brief` — Outputs a short AI Project Brief with project identity, required reading, forbidden actions, recommended workflow, and patch mode rules.
- `mossarium preflight` — Checks whether the repository is ready for AI-assisted modification. Verifies required files exist, forbidden files are absent, and warns about local directories.

### Activation Files
- `AGENTS.md` — Universal AI agent entry point, generated by `mossarium init`.
- `QWEN.md` — Project memory file for Qwen Code / local AI tools, generated by `mossarium init`.

### Changes in v0.3
- `mossarium brief` command added
- `mossarium preflight` command added
- `mossarium init` now generates AGENTS.md and QWEN.md in project root (if not present)
- Both AGENTS.md and QWEN.md are never overwritten if they already exist
- Tests extended: brief exits successfully, brief contains required sections, preflight passes after init, preflight fails on missing QWEN.md, preflight fails on mossarium.py, init creates activation files, init preserves existing activation files

It moves Mossarium from passive project memory toward active agent activation.

## v0.2.0 — AI Context Map

**AI creates files quickly, but safely modifying inherited code is slow.**

Mossarium v0.2 introduces an **AI Context Map** generated under `.mossarium/context/` with six files:

- `project-map.md` — High-level project structure and entry points
- `file-index.md` — Index of all important files for AI navigation
- `edit-zones.md` — Safe / controlled / protected modification zones
- `invariants.md` — System invariants that must never be violated
- `agent-protocol.md` — Read-first, propose-then-execute interaction protocol
- `patch-mode.md` — Minimal, safe fix protocol

These files help AI agents understand **before modifying code**:
- Project goals and organization
- File responsibilities
- Editable zones and protected areas
- Invariants that must never be broken
- Agent coordination protocol
- Patch mode for minimal fixes

### Changes in v0.2
- `mossarium init` now auto-generates full AI Context Map (6 files)
- `mossarium check` validates all 6 context files exist
- Tests extended to cover context file creation, validation, missing file detection, idempotent init, and partial structure completion

## Version 0.1 (2026)

Initial release of Mossarium, a constitutional system for AI-maintained software projects.

### Features

- `mossarium init` command to initialize project with constitutional files
- `mossarium check` command to verify project compliance
- Basic directory structure and file creation
- Support for Python CLI using argparse

### Development

This tool was created to provide a standardized approach to maintaining software projects that are primarily managed by AI systems. It establishes a foundation of conventions and documentation that make AI maintenance more predictable and reliable.

The initial version focuses on the core functionality needed to establish and verify project constitutional compliance.