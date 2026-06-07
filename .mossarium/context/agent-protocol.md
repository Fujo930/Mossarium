# Agent Protocol

## Purpose

Defines the interaction protocol for AI agents operating within this constitutional framework.

## Agent Roles

### Builder Agent
- **File**: `.mossarium/agents/builder-agent.md`
- **Actions**: Compile, build, verify builds
- **Constraints**: Only in Safe Zones (see edit-zones.md)

### Reviewer Agent
- **File**: `.mossarium/agents/reviewer-agent.md`
- **Actions**: Code review, guideline checking, test verification
- **Constraints**: Cannot modify Protected Zones

### Historian Agent
- **File**: `.mossarium/agents/historian-agent.md`
- **Actions**: Track changes, maintain version control, archive decisions
- **Constraints**: Append-only to memory directories

### Guardian Agent
- **File**: `.mossarium/agents/guardian-agent.md`
- **Actions**: Monitor compliance, enforce invariants, prevent violations
- **Constraints**: Reports violations, does not auto-fix Protected Zones

## Protocol Rules

1. **Read-First Protocol**: Every agent must read relevant context files before acting:
   - `project-map.md` - Understand structure
   - `file-index.md` - Locate files
   - `edit-zones.md` - Check modification permissions
   - `invariants.md` - Verify no invariant violations
   - `agent-protocol.md` - Follow role constraints
   - `patch-mode.md` - Understand change process

2. **Propose-Then-Execute**: All changes go through proposal system:
   - Create proposal in `.mossarium/proposals/`
   - Review by Reviewer Agent
   - Approval required for Controlled/Protected Zones
   - Guardian Agent validates invariants

3. **Memory Recording**: All significant actions recorded:
   - Decisions → `.mossarium/memory/decisions/`
   - Failures → `.mossarium/memory/failures/`
   - Architecture → `.mossarium/memory/architecture/`

4. **No Direct Context Edits**: Context files are read-only for agents
   - Regenerated only by `mossarium init`
   - Manual edits violate Invariants #4

<!-- MOSSARIUM:BEGIN AUTO-GENERATED -->
## Agent Protocol

### Before Editing

- run `mossarium brief`
- run `mossarium preflight`
- read required files
- identify task type
- choose Patch Mode for small changes

### After Editing

- run `pytest`
- run `mossarium check`
- run `mossarium audit`
- stop and wait for supervisor confirmation
<!-- MOSSARIUM:END AUTO-GENERATED -->
