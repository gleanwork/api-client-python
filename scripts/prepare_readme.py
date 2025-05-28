"""
Prepare README for PyPI publication.

This script processes README.md to create README-PYPI.md with PyPI-compatible formatting:
- Converts relative URLs to absolute GitHub URLs so links work on PyPI
- Updates pyproject.toml to reference the PyPI-ready README file

The original README.md remains unchanged for GitHub display, while README-PYPI.md
is used for package publishing to ensure all documentation links function properly
on the PyPI package page.
"""

import re


def update_pyproject_readme_path():
    """Update pyproject.toml to point to the PyPI readme file."""
    pyproject_path = "pyproject.toml"

    try:
        with open(pyproject_path, "r", encoding="utf-8") as f:
            content = f.read()

        updated_content = re.sub(
            r'readme\s*=\s*"README\.md"', 'readme = "README-PYPI.md"', content
        )

        if updated_content != content:
            with open(pyproject_path, "w", encoding="utf-8") as f:
                f.write(updated_content)
            print("Updated pyproject.toml to use README-PYPI.md")
        else:
            print("No changes needed in pyproject.toml")

    except Exception as e:
        print(f"Failed to update pyproject.toml: {e}")


try:
    with open("README.md", "r", encoding="utf-8") as rh:
        readme_contents = rh.read()
        GITHUB_URL = "https://github.com/gleanwork/api-client-python.git"
        GITHUB_URL = (
            GITHUB_URL[: -len(".git")] if GITHUB_URL.endswith(".git") else GITHUB_URL
        )
        # links on PyPI should have absolute URLs
        readme_contents = re.sub(
            r"(\[[^\]]+\]\()((?!https?:)[^\)]+)(\))",
            lambda m: m.group(1)
            + GITHUB_URL
            + "/blob/master/"
            + m.group(2)
            + m.group(3),
            readme_contents,
        )

        with open("README-PYPI.md", "w", encoding="utf-8") as wh:
            wh.write(readme_contents)

        print("Successfully created README-PYPI.md")
        update_pyproject_readme_path()

except Exception as e:
    print("Failed to update README.md to use absolute URLs for PyPi")
    print(e)
