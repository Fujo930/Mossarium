import os
import tempfile
import shutil
from pathlib import Path
import subprocess
import sys

def test_mossarium_init():
    """Test that mossarium init creates the required files."""
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)
            
            # Run mossarium init
            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            
            assert result.returncode == 0, f"mossarium init failed: {result.stderr}"
            
            # Check that .mossarium directory was created
            mossarium_dir = Path(".mossarium")
            assert mossarium_dir.exists(), ".mossarium directory should be created"
            
            # Check that required files exist
            required_files = ["CONSTITUTION.md", "MANIFESTO.md", "HISTORY.md"]
            for filename in required_files:
                file_path = mossarium_dir / filename
                assert file_path.exists(), f"{filename} should be created"
                
        finally:
            os.chdir(original_cwd)

def test_mossarium_check():
    """Test that mossarium check verifies compliance."""
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)
            
            # First run init to create files
            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            
            assert result.returncode == 0, f"mossarium init failed: {result.stderr}"
            
            # Run mossarium check
            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "check"
            ], capture_output=True, text=True)
            
            assert result.returncode == 0, f"mossarium check failed: {result.stderr}"
            assert "Project compliance check passed" in result.stdout
            
        finally:
            os.chdir(original_cwd)

def test_mossarium_help():
    """Test that mossarium shows help when no arguments are provided."""
    result = subprocess.run([
        sys.executable, "-m", "mossarium.cli"
    ], capture_output=True, text=True)

    assert result.returncode == 0
    assert "usage:" in result.stdout


def test_mossarium_init_creates_context_files():
    """Test that mossarium init creates all 6 context files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            # Run mossarium init
            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)

            assert result.returncode == 0, f"mossarium init failed: {result.stderr}"

            # Check that all 6 context files exist
            context_dir = Path(".mossarium/context")
            assert context_dir.exists(), ".mossarium/context directory should be created"

            context_files = [
                "project-map.md",
                "file-index.md",
                "edit-zones.md",
                "invariants.md",
                "agent-protocol.md",
                "patch-mode.md"
            ]

            for filename in context_files:
                file_path = context_dir / filename
                assert file_path.exists(), f"context/{filename} should be created"
                # Verify content is not empty
                assert file_path.stat().st_size > 0, f"context/{filename} should not be empty"

        finally:
            os.chdir(original_cwd)


def test_mossarium_check_validates_context_files():
    """Test that mossarium check verifies context files exist."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            # Initialize first
            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            # Run mossarium check
            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "check"
            ], capture_output=True, text=True)

            assert result.returncode == 0, f"mossarium check failed: {result.stderr}"
            assert "Project compliance check passed" in result.stdout

        finally:
            os.chdir(original_cwd)


def test_mossarium_check_fails_on_missing_context_file():
    """Test that mossarium check fails with MISSING when context file is deleted."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            # Initialize first
            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            # Delete one context file
            context_file = Path(".mossarium/context/project-map.md")
            context_file.unlink()

            # Run mossarium check - should fail
            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "check"
            ], capture_output=True, text=True)

            assert result.returncode != 0, "mossarium check should fail with missing context file"
            assert "MISSING" in result.stdout, "Output should contain MISSING"
            assert "project-map.md" in result.stdout, "Output should mention missing file"

        finally:
            os.chdir(original_cwd)


def test_mossarium_init_twice_does_not_crash():
    """Test that running mossarium init twice doesn't crash."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            # First init
            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0, f"First init failed: {result.stderr}"

            # Second init - should not crash
            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0, f"Second init failed: {result.stderr}"

            # Verify all context files still exist and have content
            context_dir = Path(".mossarium/context")
            context_files = [
                "project-map.md",
                "file-index.md",
                "edit-zones.md",
                "invariants.md",
                "agent-protocol.md",
                "patch-mode.md"
            ]

            for filename in context_files:
                file_path = context_dir / filename
                assert file_path.exists(), f"context/{filename} should still exist after second init"
                assert file_path.stat().st_size > 0, f"context/{filename} should not be empty"

        finally:
            os.chdir(original_cwd)


def test_mossarium_init_fills_missing_context_files():
    """Test that mossarium init fills in missing context files on partial structure."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            # First init
            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            # Delete some context files
            context_dir = Path(".mossarium/context")
            for filename in ["project-map.md", "file-index.md"]:
                (context_dir / filename).unlink()

            # Run init again - should fill in missing files
            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0, f"Init on partial structure failed: {result.stderr}"

            # Verify all context files exist
            for filename in [
                "project-map.md",
                "file-index.md",
                "edit-zones.md",
                "invariants.md",
                "agent-protocol.md",
                "patch-mode.md"
            ]:
                file_path = context_dir / filename
                assert file_path.exists(), f"context/{filename} should be recreated"
                assert file_path.stat().st_size > 0, f"context/{filename} should not be empty"

        finally:
            os.chdir(original_cwd)

def test_mossarium_brief_exits_successfully():
    """Test that mossarium brief exits successfully."""
    result = subprocess.run([
        sys.executable, "-m", "mossarium.cli", "brief"
    ], capture_output=True, text=True)
    assert result.returncode == 0, f"mossarium brief failed: {result.stderr}"


def test_mossarium_brief_contains_required_sections():
    """Test that mossarium brief output contains required sections."""
    result = subprocess.run([
        sys.executable, "-m", "mossarium.cli", "brief"
    ], capture_output=True, text=True)
    assert result.returncode == 0
    output = result.stdout
    assert "Mossarium" in output, "Brief should mention Mossarium"
    assert "REQUIRED READING" in output, "Brief should have REQUIRED READING section"
    assert "PATCH MODE REMINDER" in output, "Brief should have PATCH MODE REMINDER section"
    assert "QWEN.md" in output, "Brief should list QWEN.md"
    assert ".mossarium/context/project-map.md" in output, "Brief should list project-map.md"
    assert "Do not create mossarium.py" in output, "Brief should forbid mossarium.py"


def test_mossarium_preflight_passes_after_init():
    """Test that mossarium preflight passes after mossarium init."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            # Run mossarium init first
            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0, f"mossarium init failed: {result.stderr}"

            # Create README.md (required by preflight but not created by init)
            Path("README.md").write_text("# Test Project\n")

            # Run mossarium preflight
            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "preflight"
            ], capture_output=True, text=True)
            assert result.returncode == 0, f"mossarium preflight failed: {result.stderr}"
            assert "Mossarium preflight passed" in result.stdout

        finally:
            os.chdir(original_cwd)


def test_mossarium_preflight_fails_if_qwen_missing():
    """Test that mossarium preflight fails if QWEN.md is missing."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            # Run mossarium init first
            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            # Create README.md so only QWEN.md is missing
            Path("README.md").write_text("# Test Project\n")

            # Delete QWEN.md
            Path("QWEN.md").unlink()

            # Run mossarium preflight - should fail
            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "preflight"
            ], capture_output=True, text=True)
            assert result.returncode != 0, "preflight should fail when QWEN.md is missing"
            assert "QWEN.md" in result.stdout, "preflight should mention missing QWEN.md"

        finally:
            os.chdir(original_cwd)


def test_mossarium_preflight_fails_if_root_mossarium_py_exists():
    """Test that mossarium preflight fails if root mossarium.py exists."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            # Run mossarium init first
            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            # Create README.md (required by preflight)
            Path("README.md").write_text("# Test Project\n")

            # Create forbidden mossarium.py
            Path("mossarium.py").touch()

            # Use python -c with sys.path fix to avoid mossarium.py shadowing
            result = subprocess.run([
                sys.executable, "-c",
                "import sys; sys.path = [p for p in sys.path if p]; from mossarium.cli import main; sys.argv=['mossarium','preflight']; main()"
            ], capture_output=True, text=True)
            assert result.returncode != 0, "preflight should fail when mossarium.py exists"
            assert "mossarium.py" in result.stdout, "preflight should mention mossarium.py"

        finally:
            os.chdir(original_cwd)


def test_mossarium_init_creates_agents_and_qwen_md():
    """Test that mossarium init creates AGENTS.md and QWEN.md if missing."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            assert Path("AGENTS.md").exists(), "AGENTS.md should be created by init"
            assert Path("QWEN.md").exists(), "QWEN.md should be created by init"

        finally:
            os.chdir(original_cwd)


def test_mossarium_init_does_not_overwrite_existing_agents_or_qwen():
    """Test that mossarium init does not overwrite existing AGENTS.md or QWEN.md."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            # Create AGENTS.md with custom content before init
            custom_agents = "Custom AGENTS.md content"
            Path("AGENTS.md").write_text(custom_agents)

            # Create QWEN.md with custom content before init
            custom_qwen = "Custom QWEN.md content"
            Path("QWEN.md").write_text(custom_qwen)

            # Run mossarium init
            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            # Verify existing files were NOT overwritten
            assert Path("AGENTS.md").read_text() == custom_agents, \
                "Existing AGENTS.md should not be overwritten"
            assert Path("QWEN.md").read_text() == custom_qwen, \
                "Existing QWEN.md should not be overwritten"

        finally:
            os.chdir(original_cwd)


def test_mossarium_audit_exits_successfully_after_init():
    """Test that mossarium audit exits successfully after mossarium init."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            # Create README.md and HISTORY.md (required by audit, not created by init)
            Path("README.md").write_text("# Test\nMossarium\nAI Context Map\nAgent Activation Layer\n")
            Path("HISTORY.md").write_text("# History\n")

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "audit"
            ], capture_output=True, text=True)
            assert result.returncode == 0, f"mossarium audit failed: {result.stderr}"

        finally:
            os.chdir(original_cwd)


def test_mossarium_audit_contains_header():
    """Test that mossarium audit output contains the expected header."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            Path("README.md").write_text("# Test\nMossarium\nAI Context Map\nAgent Activation Layer\n")
            Path("HISTORY.md").write_text("# History\n")

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "audit"
            ], capture_output=True, text=True)
            assert "Mossarium Inheritance Audit" in result.stdout, \
                "Audit output should contain header"

        finally:
            os.chdir(original_cwd)


def test_mossarium_audit_contains_result():
    """Test that mossarium audit output contains Result: PASS or PASS WITH WARNINGS."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            Path("README.md").write_text("# Test\nMossarium\nAI Context Map\nAgent Activation Layer\n")
            Path("HISTORY.md").write_text("# History\n")

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "audit"
            ], capture_output=True, text=True)
            assert result.returncode == 0
            output = result.stdout
            assert ("Result: PASS" in output), \
                f"Audit output should contain Result: PASS or PASS WITH WARNINGS, got: {output}"

        finally:
            os.chdir(original_cwd)


def test_mossarium_audit_fails_if_readme_missing():
    """Test that mossarium audit fails if README.md is missing."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            # Create HISTORY.md but NOT README.md
            Path("HISTORY.md").write_text("# History\n")

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "audit"
            ], capture_output=True, text=True)
            assert result.returncode != 0, "audit should fail when README.md is missing"
            assert "README.md" in result.stdout, "audit should mention missing README.md"

        finally:
            os.chdir(original_cwd)


def test_mossarium_audit_fails_if_qwen_missing():
    """Test that mossarium audit fails if QWEN.md is missing."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            Path("README.md").write_text("# Test\nMossarium\nAI Context Map\nAgent Activation Layer\n")
            Path("HISTORY.md").write_text("# History\n")

            # Delete QWEN.md
            Path("QWEN.md").unlink()

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "audit"
            ], capture_output=True, text=True)
            assert result.returncode != 0, "audit should fail when QWEN.md is missing"
            assert "QWEN.md" in result.stdout, "audit should mention missing QWEN.md"

        finally:
            os.chdir(original_cwd)


def test_mossarium_audit_fails_if_root_mossarium_py_exists():
    """Test that mossarium audit fails if root mossarium.py exists."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            Path("README.md").write_text("# Test\nMossarium\nAI Context Map\nAgent Activation Layer\n")
            Path("HISTORY.md").write_text("# History\n")

            # Create forbidden mossarium.py
            Path("mossarium.py").touch()

            # Use python -c with sys.path fix to avoid mossarium.py shadowing
            result = subprocess.run([
                sys.executable, "-c",
                "import sys; sys.path = [p for p in sys.path if p]; from mossarium.cli import main; sys.argv=['mossarium','audit']; main()"
            ], capture_output=True, text=True)
            assert result.returncode != 0, "audit should fail when mossarium.py exists"
            assert "mossarium.py" in result.stdout, "audit should mention mossarium.py"

        finally:
            os.chdir(original_cwd)


def test_mossarium_audit_warns_if_qwen_dir_exists():
    """Test that mossarium audit warns if .qwen/ exists but does not fail."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            Path("README.md").write_text("# Test\nMossarium\nAI Context Map\nAgent Activation Layer\n")
            Path("HISTORY.md").write_text("# History\n")

            # Create .qwen/ directory
            Path(".qwen").mkdir(exist_ok=True)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "audit"
            ], capture_output=True, text=True)
            # Should still pass (WARN only), not fail
            assert result.returncode == 0, \
                f"audit should not fail because of .qwen/, got: {result.stdout}"
            assert ".qwen/" in result.stdout, "audit should warn about .qwen/"

        finally:
            os.chdir(original_cwd)


def test_mossarium_audit_fails_if_context_project_map_empty():
    """Test that mossarium audit fails if .mossarium/context/project-map.md is empty."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            Path("README.md").write_text("# Test\nMossarium\nAI Context Map\nAgent Activation Layer\n")
            Path("HISTORY.md").write_text("# History\n")

            # Empty the project-map.md file
            Path(".mossarium/context/project-map.md").write_text("")

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "audit"
            ], capture_output=True, text=True)
            assert result.returncode != 0, "audit should fail when project-map.md is empty"
            assert "empty" in result.stdout.lower(), "audit should mention empty file"

        finally:
            os.chdir(original_cwd)


def test_mossarium_audit_does_not_fail_on_warnings_only():
    """Test that mossarium audit passes with warnings when only WARN items exist."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            # Create files with content but missing some semantic markers
            Path("README.md").write_text("# Test\nMossarium\n")
            Path("HISTORY.md").write_text("# History\n")

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "audit"
            ], capture_output=True, text=True)
            # Should pass with warnings (missing AI Context Map / Agent Activation Layer in README)
            assert result.returncode == 0, \
                f"audit should not fail on warnings only, got exit {result.returncode}: {result.stdout}"

        finally:
            os.chdir(original_cwd)


def test_mossarium_refresh_exits_successfully():
    """Test that mossarium refresh exits successfully."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "refresh"
            ], capture_output=True, text=True)
            assert result.returncode == 0, f"mossarium refresh failed: {result.stderr}"

        finally:
            os.chdir(original_cwd)


def test_mossarium_refresh_creates_managed_sections():
    """Test that mossarium refresh creates managed sections with markers."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "refresh"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            for filename in ["project-map.md", "file-index.md", "edit-zones.md",
                             "invariants.md", "agent-protocol.md", "patch-mode.md"]:
                content = Path(f".mossarium/context/{filename}").read_text(encoding="utf-8")
                assert "<!-- MOSSARIUM:BEGIN AUTO-GENERATED -->" in content, \
                    f"{filename} should contain managed section begin marker"
                assert "<!-- MOSSARIUM:END AUTO-GENERATED -->" in content, \
                    f"{filename} should contain managed section end marker"

        finally:
            os.chdir(original_cwd)


def test_mossarium_refresh_preserves_user_content():
    """Test that refresh preserves user content outside managed sections."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            # Add user content before the managed section
            pm_path = Path(".mossarium/context/project-map.md")
            original = pm_path.read_text(encoding="utf-8")
            user_header = "# My Custom Project Notes\n\nThis is user content.\n\n"
            pm_path.write_text(user_header + original, encoding="utf-8")

            # Refresh
            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "refresh"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            # Verify user content preserved
            new_content = pm_path.read_text(encoding="utf-8")
            assert "My Custom Project Notes" in new_content, \
                "User content outside managed section should be preserved"
            assert "This is user content" in new_content, \
                "User content outside managed section should be preserved"

        finally:
            os.chdir(original_cwd)


def test_mossarium_refresh_check_passes_after_refresh():
    """Test that refresh --check passes immediately after refresh."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "refresh"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "refresh", "--check"
            ], capture_output=True, text=True)
            assert result.returncode == 0, \
                f"refresh --check should pass after refresh: {result.stdout}"
            assert "up to date" in result.stdout.lower()

        finally:
            os.chdir(original_cwd)


def test_mossarium_refresh_check_fails_on_stale():
    """Test that refresh --check fails if a managed section is manually changed."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "refresh"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            # Tamper with a managed section
            pm_path = Path(".mossarium/context/project-map.md")
            content = pm_path.read_text(encoding="utf-8")
            pm_path.write_text(content.replace("Mossarium", "Something Else"), encoding="utf-8")

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "refresh", "--check"
            ], capture_output=True, text=True)
            assert result.returncode != 0, \
                "refresh --check should fail when managed section is tampered"

        finally:
            os.chdir(original_cwd)


def test_mossarium_refresh_file_index_contains_key_files():
    """Test that file-index.md contains mossarium/cli.py after refresh."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "refresh"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            content = Path(".mossarium/context/file-index.md").read_text(encoding="utf-8")
            assert "mossarium/cli.py" in content, \
                "file-index.md should contain mossarium/cli.py"

        finally:
            os.chdir(original_cwd)


def test_mossarium_refresh_project_map_contains_refresh():
    """Test that project-map.md contains mossarium refresh after refresh."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "refresh"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            content = Path(".mossarium/context/project-map.md").read_text(encoding="utf-8")
            assert "mossarium refresh" in content, \
                "project-map.md should contain mossarium refresh"

        finally:
            os.chdir(original_cwd)


def test_mossarium_refresh_excludes_noise_in_file_index():
    """Test that refresh does not include excluded dirs/patterns in file-index."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "refresh"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            content = Path(".mossarium/context/file-index.md").read_text(encoding="utf-8")
            # Must not include noise paths
            assert ".venv" not in content, "file-index should not include .venv"
            assert ".pytest_cache" not in content, "file-index should not include .pytest_cache"
            assert "__pycache__" not in content, "file-index should not include __pycache__"
            assert ".qwen" not in content, "file-index should not include .qwen"
            assert ".pyc" not in content, "file-index should not include .pyc"

        finally:
            os.chdir(original_cwd)


def test_mossarium_integrate_codex_exits_successfully():
    """Test that mossarium integrate codex exits successfully."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "integrate", "codex"
            ], capture_output=True, text=True)
            assert result.returncode == 0, f"integrate codex failed: {result.stderr}"

        finally:
            os.chdir(original_cwd)


def test_mossarium_integrate_codex_creates_files():
    """Test that mossarium integrate codex creates all required files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "integrate", "codex"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            assert Path(".codex/skills/mossarium/SKILL.md").exists(), \
                "SKILL.md should be created"
            assert Path(".codex/skills/mossarium/scripts/preflight.py").exists(), \
                "preflight.py should be created"
            assert Path(".codex/skills/mossarium/scripts/finish.py").exists(), \
                "finish.py should be created"

        finally:
            os.chdir(original_cwd)


def test_mossarium_integrate_codex_skill_contains_required_content():
    """Test that SKILL.md contains required Mossarium references."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "integrate", "codex"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            content = Path(".codex/skills/mossarium/SKILL.md").read_text(encoding="utf-8")
            assert "Mossarium Codex Skill" in content
            assert "mossarium brief" in content
            assert "mossarium preflight" in content
            assert "mossarium refresh --check" in content
            assert "mossarium audit" in content
            assert "Patch Mode" in content
            # v0.6.1: YAML frontmatter
            assert "name: mossarium" in content
            assert "description:" in content

        finally:
            os.chdir(original_cwd)


def test_mossarium_integrate_codex_does_not_overwrite_skill():
    """Test that integrate codex does not overwrite existing SKILL.md."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "integrate", "codex"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            # Modify SKILL.md with custom content
            custom = "Custom Codex skill content"
            Path(".codex/skills/mossarium/SKILL.md").write_text(custom, encoding="utf-8")

            # Run integrate again — should not overwrite
            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "integrate", "codex"
            ], capture_output=True, text=True)
            assert result.returncode == 0
            assert Path(".codex/skills/mossarium/SKILL.md").read_text(encoding="utf-8") == custom

        finally:
            os.chdir(original_cwd)


def test_mossarium_integrate_codex_twice_does_not_crash():
    """Test that running integrate codex twice does not crash."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "integrate", "codex"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "integrate", "codex"
            ], capture_output=True, text=True)
            assert result.returncode == 0, \
                f"second integrate codex should not crash: {result.stderr}"

        finally:
            os.chdir(original_cwd)


def test_mossarium_help_includes_integrate():
    """Test that mossarium --help includes integrate."""
    result = subprocess.run([
        sys.executable, "-m", "mossarium.cli", "--help"
    ], capture_output=True, text=True)
    assert result.returncode == 0
    assert "integrate" in result.stdout, "--help should include integrate command"


def test_mossarium_integrate_codex_creates_plugin_package():
    """Test that integrate codex creates the plugin package scaffold."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "integrate", "codex"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            assert Path("plugins/mossarium-codex/.codex-plugin/plugin.json").exists()
            assert Path("plugins/mossarium-codex/skills/mossarium/SKILL.md").exists()
            assert Path("plugins/mossarium-codex/skills/mossarium/scripts/preflight.py").exists()
            assert Path("plugins/mossarium-codex/skills/mossarium/scripts/finish.py").exists()
            assert Path("plugins/mossarium-codex/README.md").exists()

        finally:
            os.chdir(original_cwd)


def test_mossarium_integrate_codex_plugin_json_is_valid():
    """Test that plugin.json is valid JSON with required fields."""
    import json
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "integrate", "codex"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            data = json.loads(Path("plugins/mossarium-codex/.codex-plugin/plugin.json").read_text(encoding="utf-8"))
            assert data["name"] == "mossarium-codex"
            assert data["version"] == "0.6.1"
            assert data["skills"] == "./skills/"

        finally:
            os.chdir(original_cwd)


def test_mossarium_integrate_codex_marketplace_is_valid():
    """Test that marketplace.json is valid JSON and points to plugin."""
    import json
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "integrate", "codex"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            data = json.loads(Path(".agents/plugins/marketplace.json").read_text(encoding="utf-8"))
            assert data["plugins"][0]["source"]["path"] == "./plugins/mossarium-codex"

        finally:
            os.chdir(original_cwd)


def test_mossarium_integrate_codex_output_mentions_scaffolds():
    """Test integrate codex output mentions all scaffold paths and readiness."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "integrate", "codex"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            assert "Local skill scaffold" in result.stdout
            assert "Plugin package scaffold" in result.stdout
            assert "Repo marketplace scaffold" in result.stdout
            assert "Publication readiness" in result.stdout

        finally:
            os.chdir(original_cwd)


def test_mossarium_integrate_codex_plugin_readme_has_sections():
    """Test plugin README contains required sections."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "integrate", "codex"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            content = Path("plugins/mossarium-codex/README.md").read_text(encoding="utf-8")
            assert "publication candidate" in content
            assert "How to Test Locally" in content
            assert "Recommended Codex Workflow" in content

        finally:
            os.chdir(original_cwd)


def test_mossarium_integrate_codex_both_skills_consistent():
    """Test both SKILL.md files contain required markers."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "integrate", "codex"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            for skill_path in [".codex/skills/mossarium/SKILL.md",
                               "plugins/mossarium-codex/skills/mossarium/SKILL.md"]:
                content = Path(skill_path).read_text(encoding="utf-8")
                assert "name: mossarium" in content, f"{skill_path} missing name"
                assert "description:" in content, f"{skill_path} missing description"
                assert "Before Editing" in content, f"{skill_path} missing Before Editing"
                assert "After Editing" in content, f"{skill_path} missing After Editing"
                assert "Patch Mode" in content, f"{skill_path} missing Patch Mode"
                assert "mossarium refresh --check" in content, f"{skill_path} missing refresh --check"

        finally:
            os.chdir(original_cwd)


def test_mossarium_integrate_codex_scripts_use_main_pattern():
    """Test preflight.py and finish.py use sys.exit(main()) pattern."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "integrate", "codex"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            for script in [".codex/skills/mossarium/scripts/preflight.py",
                           ".codex/skills/mossarium/scripts/finish.py"]:
                content = Path(script).read_text(encoding="utf-8")
                assert "subprocess.run" in content, f"{script} missing subprocess.run"
                assert "sys.exit(main())" in content, f"{script} missing sys.exit(main())"

        finally:
            os.chdir(original_cwd)


def test_mossarium_integrate_codex_readiness_passes():
    """Test that validate_codex_plugin_package returns OK after integrate."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "init"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            result = subprocess.run([
                sys.executable, "-m", "mossarium.cli", "integrate", "codex"
            ], capture_output=True, text=True)
            assert result.returncode == 0

            from mossarium.integrations import validate_codex_plugin_package
            ok, issues = validate_codex_plugin_package()
            assert ok, f"readiness should pass, issues: {issues}"

        finally:
            os.chdir(original_cwd)


if __name__ == "__main__":
    test_mossarium_init()
    test_mossarium_check()
    test_mossarium_help()
    print("All tests passed!")