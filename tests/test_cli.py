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

            # Run mossarium preflight - should fail
            # Use direct file path to avoid mossarium.py shadowing the package
            import mossarium.cli
            cli_path = str(Path(mossarium.cli.__file__).resolve())
            result = subprocess.run([
                sys.executable, cli_path, "preflight"
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

            # Use direct file path to avoid mossarium.py shadowing the package
            import mossarium.cli
            cli_path = str(Path(mossarium.cli.__file__).resolve())
            result = subprocess.run([
                sys.executable, cli_path, "audit"
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


if __name__ == "__main__":
    test_mossarium_init()
    test_mossarium_check()
    test_mossarium_help()
    print("All tests passed!")