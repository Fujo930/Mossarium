"""brief command — output a short AI project brief before editing."""

BRIEF = """===============================================================================
MOSSARIUM AI PROJECT BRIEF
===============================================================================

1. PROJECT IDENTITY

Mossarium is an AI constitution system for GitHub repositories.

2. CORE SLOGAN

Mossarium does not make AI smarter.
It makes repositories easier for AI to inherit.

3. REQUIRED READING

Before editing any file, read:

  * QWEN.md
  * README.md
  * .mossarium/CONSTITUTION.md
  * .mossarium/HISTORY.md
  * .mossarium/context/project-map.md
  * .mossarium/context/file-index.md
  * .mossarium/context/invariants.md
  * .mossarium/context/patch-mode.md

4. FORBIDDEN ACTIONS

  * Do not create mossarium.py
  * Do not add generate command
  * Do not add export command
  * Do not manually modify .mossarium/ as a substitute for init/check changes
  * Do not scan .venv, .pytest_cache, **pycache**, or *.pyc
  * Do not redefine Mossarium as a chatbot, programming language,
    generic coding agent, website, database, or LLM API wrapper

5. RECOMMENDED WORKFLOW

  * Run mossarium brief before editing
  * Read required files
  * Identify task type
  * Use Patch Mode for bug fixes or small changes
  * Modify only requested files
  * Run pytest after code changes
  * Stop and wait for supervisor confirmation

6. PATCH MODE REMINDER

  * Read only relevant files
  * Make the smallest safe change
  * Do not rewrite unrelated documentation
  * Do not add unrequested features
  * Do not redesign architecture

==============================================================================="""


def brief_project():
    """Output a short AI Project Brief for AI agents before editing."""
    print(BRIEF)
