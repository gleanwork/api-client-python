# ~~Role~~

DEPRECATED - use permissions instead. Viewer's role on the specific document.

> :warning: **DEPRECATED**: Deprecated on 2026-02-05, removal scheduled for 2026-10-15: Use permissions instead.

## Example Usage

```python
from glean.api_client.models import Role

value = Role.ANSWER_MODERATOR

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `ANSWER_MODERATOR` | ANSWER_MODERATOR   |
| `OWNER`            | OWNER              |
| `VIEWER`           | VIEWER             |