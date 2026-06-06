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

if __name__ == "__main__":
    test_mossarium_init()
    test_mossarium_check()
    test_mossarium_help()
    print("All tests passed!")