#!/usr/bin/env python3
"""
Codemod script to restructure the glean package into a namespace structure.

This script moves all API client code from src/glean to src/glean/api_client,
making glean a namespace package and api_client the actual implementation.

It also detects if Speakeasy has regenerated files and automatically re-runs
the transformation.
"""

import shutil
import tempfile
import sys
from pathlib import Path
import re
from typing import List


class GleanRestructure:
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.src_dir = project_root / "src"
        self.glean_dir = self.src_dir / "glean"

    def update_imports_in_file(self, file_path: Path) -> bool:
        """Update import statements in a Python or Markdown file to use the new structure."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            original_content = content

            # Apply the actual import transformations
            transformations = [
                # from glean import X, Y, Z -> from glean.api_client import X, Y, Z
                (
                    r"from glean(?!\.api_client) import\s+",
                    r"from glean.api_client import ",
                ),
                # from glean.something import ... -> from glean.api_client.something import ...
                (r"from glean\.(?!api_client)([^.\s]+)", r"from glean.api_client.\1"),
                # import glean.something -> import glean.api_client.something
                (
                    r"import glean\.(?!api_client)([^.\s]+)",
                    r"import glean.api_client.\1",
                ),
                # String-based module paths in data structures (e.g. `_sub_sdk_map` in `sdks.py`)
                (r'"glean\.(?!api_client)([^."]+)"', r'"glean.api_client.\1"'),
                (r"'glean\.(?!api_client)([^.']+)'", r"'glean.api_client.\1'"),
            ]

            for pattern, replacement in transformations:
                content = re.sub(pattern, replacement, content)

            # Only write if content changed
            if content != original_content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Updated imports in: {file_path}")
                return True

            return False

        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return False

    def update_imports_in_moved_files(self, api_client_dir: Path):
        """Update internal imports within the moved api_client directory."""
        files_to_process = list(api_client_dir.rglob("*.py"))

        for file_path in files_to_process:
            self.update_imports_in_file(file_path)

    def get_files_to_move(self) -> List[Path]:
        """Get list of files/directories that would be moved."""
        files_to_move = []
        for item in self.glean_dir.iterdir():
            if item.name not in ["api_client", "__pycache__"]:
                files_to_move.append(item)
        return files_to_move

    def detect_speakeasy_regeneration(self) -> bool:
        """
        Detect if Speakeasy has regenerated files after our transformation.

        Returns True if regeneration is detected (i.e., there are files/dirs other than api_client)
        """
        api_client_dir = self.glean_dir / "api_client"

        if not api_client_dir.exists():
            # No api_client directory means we haven't run the transformation yet
            return False

        # Check if there are any files/directories other than api_client and __pycache__
        other_items = self.get_files_to_move()
        return len(other_items) > 0

    def move_files_to_api_client(self):
        """Move files from glean/ to glean/api_client/."""
        api_client_dir = self.glean_dir / "api_client"
        api_client_dir.mkdir(exist_ok=True)

        print("Moving files to api_client...")
        files_to_move = self.get_files_to_move()

        for item in files_to_move:
            dest = api_client_dir / item.name
            print(f"Moving {item} -> {dest}")
            shutil.move(str(item), str(dest))

    def update_project_imports(self):
        """Update imports in tests, examples, documentation, and other project files."""
        print("Updating imports in tests, examples, and documentation...")

        # Update test files
        tests_dir = self.project_root / "tests"
        if tests_dir.exists():
            for test_file in tests_dir.rglob("*.py"):
                self.update_imports_in_file(test_file)

        # Update example files
        examples_dir = self.project_root / "examples"
        if examples_dir.exists():
            for example_file in examples_dir.rglob("*.py"):
                self.update_imports_in_file(example_file)

        # Update any other Python files in the project root
        for py_file in self.project_root.glob("*.py"):
            self.update_imports_in_file(py_file)

        # Update markdown files with Python code snippets
        self.update_markdown_files()

    def update_markdown_files(self):
        """Update Python code snippets in markdown files."""
        print("Updating Python code snippets in markdown files...")

        # Find all markdown files in the project
        markdown_files = []

        # Check docs directory
        docs_dir = self.project_root / "docs"
        if docs_dir.exists():
            markdown_files.extend(docs_dir.rglob("*.md"))

        # Check root level markdown files
        markdown_files.extend(self.project_root.glob("*.md"))

        # Also check other common locations
        for dirname in ["examples", "tests"]:
            dir_path = self.project_root / dirname
            if dir_path.exists():
                markdown_files.extend(dir_path.rglob("*.md"))

        for md_file in markdown_files:
            if self.update_imports_in_file(md_file):
                print(f"Updated markdown file: {md_file}")

    def perform_restructure(self):
        """Perform the actual restructuring of files."""
        # Create a temporary backup
        temp_backup = tempfile.mkdtemp(prefix="glean_backup_")
        backup_glean = Path(temp_backup) / "glean"

        try:
            print(f"Creating backup at: {temp_backup}")
            shutil.copytree(self.glean_dir, backup_glean)
        except Exception as e:
            print(f"Error creating backup: {e}")
            sys.exit(1)

        try:
            # Move files to api_client
            self.move_files_to_api_client()

            # No need to create __init__.py - Python 3.3+ supports implicit namespace packages
            # The absence of __init__.py makes src/glean a namespace package automatically
            print("Using implicit namespace package (no __init__.py needed)")

            # Update imports in the moved files
            api_client_dir = self.glean_dir / "api_client"
            print("Updating imports in moved files...")
            self.update_imports_in_moved_files(api_client_dir)

            # Update imports in other parts of the project
            self.update_project_imports()

            print("\nRestructuring complete!")
            print(f"Backup created at: {temp_backup}")
            print("New structure:")
            print("  src/glean/             (implicit namespace package)")
            print("  src/glean/api_client/  (actual implementation)")

            print("\nTo use the restructured package:")
            print("  from glean.api_client import Glean")
            print("  # or")
            print("  import glean.api_client as glean")

            print(f"\nIf anything goes wrong, you can restore from: {temp_backup}")

        except Exception as e:
            print(f"Error during restructuring: {e}")
            print(f"Restoring from backup: {temp_backup}")

            # Restore from backup
            backup_glean = Path(temp_backup) / "glean"
            if self.glean_dir.exists():
                shutil.rmtree(self.glean_dir)
            shutil.copytree(backup_glean, self.glean_dir)

            sys.exit(1)

    def run(self):
        """Main entry point for the restructuring process."""
        if not self.glean_dir.exists():
            print(
                "Error: src/glean directory not found. Run this script from the project root."
            )
            sys.exit(1)

        print("Checking for Speakeasy regeneration...")

        speakeasy_regenerated = self.detect_speakeasy_regeneration()
        api_client_dir = self.glean_dir / "api_client"

        if speakeasy_regenerated:
            print(
                "🔄 Detected Speakeasy regeneration - files found outside api_client/"
            )
            print(
                "This means Speakeasy has regenerated the client after our transformation."
            )
            print(
                "Removing old api_client/ and re-running transformation from scratch..."
            )
            if api_client_dir.exists():
                shutil.rmtree(api_client_dir)
                print(f"Removed {api_client_dir}")

        print("Starting restructure...")
        print(f"Project root: {self.project_root}")
        print(f"Source dir: {self.src_dir}")
        print(f"Glean dir: {self.glean_dir}")
        self.perform_restructure()


def main():
    # Get the project root (should be run from project root)
    project_root = Path.cwd()

    restructurer = GleanRestructure(project_root)
    restructurer.run()


if __name__ == "__main__":
    main()
