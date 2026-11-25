# DocumentVisibilityOverrideOverride

The visibility-override state of the document.

## Example Usage

```python
from glean.api_client.models import DocumentVisibilityOverrideOverride

value = DocumentVisibilityOverrideOverride.NONE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                         | Value                        |
| ---------------------------- | ---------------------------- |
| `NONE`                       | NONE                         |
| `HIDE_FROM_ALL`              | HIDE_FROM_ALL                |
| `HIDE_FROM_GROUPS`           | HIDE_FROM_GROUPS             |
| `HIDE_FROM_ALL_EXCEPT_OWNER` | HIDE_FROM_ALL_EXCEPT_OWNER   |