# Restructuring Script

This directory contains a script to restructure the glean package from:

```
src/glean/          # All implementation files
```

To:

```
src/glean/          # Implicit namespace package (no __init__.py)
src/glean/api_client/   # All implementation files moved here
```

## Usage

### Analyze what would change (recommended first step)

```bash
python scripts/restructure_to_namespace.py --dry-run
```

This shows you:

- Which files would be moved
- Which import statements would be updated
- Current state of the transformation

### Perform the restructuring

```bash
python scripts/restructure_to_namespace.py
```

This script:

- **Detects Speakeasy regeneration** and automatically handles it
- Creates a backup and moves all files
- Uses implicit namespace packages (no `__init__.py` needed)
- Can be run multiple times safely
- Updates all import statements throughout the codebase

## Smart Speakeasy Integration

The script automatically detects when Speakeasy has regenerated files:

1. **First run**: Moves everything to `api_client/`
2. **After Speakeasy regeneration**: Detects new files in `src/glean/`, removes old `api_client/`, and re-runs the transformation
3. **Subsequent runs**: Detects already-transformed structure and skips

This means you can safely run the script as part of your build process!

## Examples

```bash
# First, see what would be changed
python scripts/restructure_to_namespace.py --dry-run

# If it looks good, perform the restructuring
python scripts/restructure_to_namespace.py

# Safe to run multiple times - it will detect and handle various states
python scripts/restructure_to_namespace.py  # Skips if already done
python scripts/restructure_to_namespace.py  # Auto-detects Speakeasy regeneration
```

## What the restructuring does

1. **Creates a backup** of the current `src/glean` directory
2. **Moves all files** from `src/glean/` to `src/glean/api_client/`
3. **Creates an implicit namespace package** (no `__init__.py` - Python 3.3+ feature)
4. **Updates all import statements** in tests, examples, and internal files
5. **Handles Speakeasy regeneration** automatically

## After restructuring

Users will need to update their imports:

### Before

```python
from glean import Glean, models, errors
from glean.utils import parse_datetime
```

### After

```python
from glean.api_client import Glean, models, errors
from glean.api_client.utils import parse_datetime
```

## Workflow Integration

You can integrate this into your build process:

```bash
# In your build script or CI
speakeasy generate  # Regenerates files to src/glean/
python scripts/restructure_to_namespace.py  # Automatically detects and re-transforms
```

## Recovery

If something goes wrong, the script provides the path to the backup directory:

```bash
rm -rf src/glean
cp -r /path/to/backup/glean src/glean
```

## Testing after restructuring

```bash
# Run tests
python -m pytest

# Try importing
python -c "from glean.api_client import Glean; print('Success!')"
```

