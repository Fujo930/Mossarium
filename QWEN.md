# QWEN.md - Project Memory for Mossarium

This file contains critical project context that Qwen Code must read before starting any work.

## Project Identity

**Mossarium is an AI constitution system for GitHub repositories.**

### Core Slogan
> Mossarium does not make AI smarter. It makes repositories easier for AI to inherit.

### What Mossarium Is
- A constitutional framework for AI-maintained software projects
- A directory structure (`.mossarium/`) that stores rules, memory, and guidelines
- A CLI tool (`mossarium init`, `mossarium check`)
- A system for AI agents to understand and maintain codebases

### What Mossarium Is NOT
- ❌ Not a chatbot
- ❌ Not a programming language
- ❌ Not a generic coding agent
- ❌ Not a website
- ❌ Not a database
- ❌ Not an LLM API wrapper

---

## Current Stable State

### v0.1 — AI Constitution

**Status: COMPLETE**

#### Working Features
- ✅ `mossarium init` works - initializes `.mossarium/` directory structure
- ✅ `mossarium check` works - validates constitutional compliance
- ✅ `pytest passes` - all tests pass
- ✅ Empty project initialization works
- ✅ Complete `.mossarium/` inheritance structure exists

#### Project Structure (v0.1)
```
.mossarium/
├── CONSTITUTION.md      # AI constitutional rules
├── MANIFESTO.md         # Project philosophy
├── HISTORY.md           # Project history
├── rules/
│   ├── core-rules.md
│   └── ai-contribution-rules.md
├── memory/
│   ├── decisions/
│   │   └── .gitkeep
│   ├── failures/
│   │   └── .gitkeep
│   └── architecture/
│       └── .gitkeep
├── proposals/
│   └── template.md
├── agents/
│   ├── builder-agent.md
│   ├── reviewer-agent.md
│   ├── historian-agent.md
│   └── guardian-agent.md
├── benchmarks/
│   ├── inheritance-test.md
│   └── comprehension-test.md
└── templates/
```

### v0.2 — AI Context Map

**Status: COMPLETE**

#### Working Features
- ✅ `mossarium init` automatically generates the AI Context Map under `.mossarium/context/`
- ✅ `mossarium check` validates all 6 context files; missing any outputs `MISSING` and returns non-zero exit code
- ✅ `pytest` includes v0.2 context tests; currently 8 passed
- ✅ `README.md` and `HISTORY.md` record v0.2 — AI Context Map

#### `.mossarium/context/` Structure (v0.2)
```
.mossarium/context/
├── project-map.md       # High-level project structure and entry points
├── file-index.md        # Index of key files and their purposes
├── edit-zones.md        # Which files are safe to edit and how
├── invariants.md        # Rules that must never be broken
├── agent-protocol.md    # How AI agents should operate in this repository
└── patch-mode.md        # Rules for small, focused patches

---

## Real CLI Entry

### Entry Point
The **ONLY** true CLI entry is:

```toml
# pyproject.toml
[project.scripts]
mossarium = "mossarium.cli:main"
```

### Actual File Location
- **CLI file**: `mossarium/cli.py`
- **NOT**: `mossarium.py` (root directory) - This must NEVER be created

---

## Forbidden Mistakes

**STRICTLY PROHIBITED:**

1. ❌ Do not create `mossarium.py` in root directory
2. ❌ Do not add `generate` command to CLI
3. ❌ Do not add `export` command to CLI
4. ❌ Do not manually modify `.mossarium/` as a substitute for changing init/check
5. ❌ Do not scan `.venv`
6. ❌ Do not scan `.pytest_cache`
7. ❌ Do not scan `**__pycache__`
8. ❌ Do not scan `*.pyc`
9. ❌ Do not use `tree /F` over the whole project
10. ❌ Do not redefine Mossarium as a chatbot, programming language, generic coding agent, website, database, or LLM API wrapper

---

## Development Rule

**ALL development must follow:**

1. Work from current Git state
2. Run `git status --short` before changes
3. Use `git ls-files` instead of full tree scans
4. Modify only the files requested
5. Make the smallest safe change
6. Run `pytest` after code changes
7. Stop after completing the requested task
8. Wait for supervisor confirmation

---

## Patch Mode

**For bug fixes or small changes:**

- Read only relevant files
- Change only the requested issue
- Do not rewrite README
- Do not rewrite CONSTITUTION
- Do not add new features
- Do not redesign architecture
- Run the smallest relevant tests
- Stop after verification

---

## v0.3 Goal (NEXT PLANNED WORK)

**Goal: Agent Activation Layer**

### Problem
AI agents currently need repeated human reminders about which files to read,
which rules to follow, and which mistakes to avoid.

### Solution
`mossarium brief` / `mossarium preflight` will automatically tell the agent
what to read, what to obey, and what to avoid — without human prompting.

**Note:** This is NOT yet implemented. Do not create these commands.

---

## Key Commands Reference

```bash
# Initialize project with constitutional structure
mossarium init

# Check compliance with constitutional guidelines
mossarium check

# Run tests
pytest
```

---

## Memory Index

This file was created to ensure future conversations have full context about:
- What Mossarium is (and what it's not)
- Current state: v0.1 (AI Constitution) COMPLETE, v0.2 (AI Context Map) COMPLETE
- Next planned: v0.3 (Agent Activation Layer)
- The correct CLI entry point (`mossarium/cli.py`)
- Strictly forbidden actions
- Development workflow rules
