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

if __name__ == "__main__":
    test_mossarium_init()
    test_mossarium_check()
    test_mossarium_help()
    print("All tests passed!")