"""init command — initialize a project with Mossarium constitutional structure."""

from pathlib import Path

from . import content as c
from . import paths
from .utils import write_if_missing, ensure_dir


def init_project():
    """Initialize a project with constitutional files."""
    mossarium_dir = Path(".mossarium")
    mossarium_dir.mkdir(exist_ok=True)

    # Create all subdirectories
    ensure_dir(mossarium_dir / "rules")
    ensure_dir(mossarium_dir / "memory/decisions")
    ensure_dir(mossarium_dir / "memory/failures")
    ensure_dir(mossarium_dir / "memory/architecture")
    ensure_dir(mossarium_dir / "proposals")
    ensure_dir(mossarium_dir / "agents")
    ensure_dir(mossarium_dir / "benchmarks")
    ensure_dir(mossarium_dir / "templates")
    ensure_dir(mossarium_dir / "context")

    # Root constitutional files
    write_if_missing(mossarium_dir / "CONSTITUTION.md", c.CONSTITUTION_CONTENT)
    write_if_missing(mossarium_dir / "MANIFESTO.md", c.MANIFESTO_CONTENT)
    write_if_missing(mossarium_dir / "HISTORY.md", c.HISTORY_CONTENT)

    # Rules
    write_if_missing(mossarium_dir / "rules/core-rules.md", c.CORE_RULES_CONTENT)
    write_if_missing(mossarium_dir / "rules/ai-contribution-rules.md", c.AI_CONTRIBUTION_RULES_CONTENT)

    # Memory .gitkeep files
    for p in ["memory/decisions/.gitkeep", "memory/failures/.gitkeep", "memory/architecture/.gitkeep"]:
        f = mossarium_dir / p
        if not f.exists():
            f.touch()

    # Proposal template
    write_if_missing(mossarium_dir / "proposals/template.md", c.PROPOSAL_TEMPLATE_CONTENT)

    # Agent files
    write_if_missing(mossarium_dir / "agents/builder-agent.md", c.BUILDER_AGENT_CONTENT)
    write_if_missing(mossarium_dir / "agents/reviewer-agent.md", c.REVIEWER_AGENT_CONTENT)
    write_if_missing(mossarium_dir / "agents/historian-agent.md", c.HISTORIAN_AGENT_CONTENT)
    write_if_missing(mossarium_dir / "agents/guardian-agent.md", c.GUARDIAN_AGENT_CONTENT)

    # Benchmark files
    write_if_missing(mossarium_dir / "benchmarks/inheritance-test.md", c.INHERITANCE_TEST_CONTENT)
    write_if_missing(mossarium_dir / "benchmarks/comprehension-test.md", c.COMPREHENSION_TEST_CONTENT)

    # Context files
    for fname in paths.CONTEXT_FILES:
        ctx = getattr(c, f"CONTEXT_{fname.replace('-', '_').replace('.md', '').upper()}_CONTENT", "")
        write_if_missing(mossarium_dir / "context" / fname, ctx)

    # Activation files
    write_if_missing("AGENTS.md", c.AGENTS_MD_CONTENT)
    write_if_missing("QWEN.md", c.QWEN_MD_CONTENT)

    print("Project initialized with complete constitutional structure.")
