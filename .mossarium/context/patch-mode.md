# Patch Mode

## Purpose

Defines the strict protocol for applying fixes and small changes to the codebase.

## When to Use Patch Mode

- Bug fixes (not new features)
- Small corrections (typos, logic errors)
- Compliance fixes (missing files, invariant violations)
- Reverting unintended changes

## Patch Mode Rules

1. **Scope Limitation**
   - Modify only the specific file(s) related to the issue
   - Do not refactor unrelated code
   - Do not add new features
   - Do not rewrite documentation unnecessarily

2. **Read-Only Context**
   - Must read existing context files first
   - Do not modify any `.mossarium/context/` files
   - Changes to context only via `mossarium init`

3. **Verification Steps**
   - Run `pytest` after changes
   - Run `mossarium check` to verify compliance
   - All tests must pass
   - No new MISSING items

4. **Prohibited in Patch Mode**
   - ❌ Adding new CLI commands
   - ❌ Modifying `pyproject.toml` entry points
   - ❌ Creating `mossarium.py` in root
   - ❌ Changing context file structure
   - ❌ Rewriting CONSTITUTION.md, MANIFESTO.md, HISTORY.md
   - ❌ Modifying test files to hide failures

5. **Completion Checklist**
   - [ ] Issue fixed in minimal scope
   - [ ] `pytest` passes
   - [ ] `mossarium check` shows "Project compliance check passed"
   - [ ] No invariant violations
   - [ ] Stop and wait for supervisor confirmation

<!-- MOSSARIUM:BEGIN AUTO-GENERATED -->
## Patch Mode Rules

- Read only relevant files
- Make the smallest safe change
- Do not rewrite unrelated documentation
- Do not add unrequested features
- Do not redesign architecture
- Run the smallest relevant tests
- Stop after verification
<!-- MOSSARIUM:END AUTO-GENERATED -->
