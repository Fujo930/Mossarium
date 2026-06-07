# Mossarium History

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