# Restructuring Script

This directory contains a script to restructure the glean package from:

```
src/glean/              # All implementation files
```

To:

```
src/glean/              # Implicit namespace package (no __init__.py)
src/glean/api_client/   # All implementation files moved here
```

## Usage

```bash
python scripts/restructure_to_namespace.py
```

This script:

- Detects Speakeasy regeneration and automatically handles it
- Creates a backup and moves all files
- Uses implicit namespace packages (no `__init__.py` needed)
- Can be run multiple times safely
- Updates all import statements throughout the codebase

## Speakeasy Integration

The script automatically detects when Speakeasy has regenerated files:

1. **First run**: Moves everything to `api_client/`
2. **After Speakeasy regeneration**: Detects new files in `src/glean/`, removes old `api_client/`, and re-runs the transformation
3. **Subsequent runs**: Detects already-transformed structure and skips

## What the restructuring does

1. **Creates a backup** of the current `src/glean` directory
2. **Moves all files** from `src/glean/` to `src/glean/api_client/`
3. **Creates an implicit namespace package** (no `__init__.py` - Python 3.3+ feature)
4. **Updates all import statements** in tests, examples, and internal files

## Workflow Integration

The repository includes a GitHub Actions workflow (`.github/workflows/patch-speakeasy-pr.yml`) that automatically runs the restructuring script.

- **Triggers**: Runs on PRs with "Update SDK - Generate" in the title (Speakeasy PRs) or manual dispatch
- **Process**: Automatically runs the restructuring script when Speakeasy regenerates the SDK
- **Auto-commit**: Commits and pushes the restructured files back to the same PR branch

This means Speakeasy PRs are automatically transformed to the namespace
structure without manual intervention.
