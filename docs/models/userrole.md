# UserRole

A user's role with respect to a specific document.

## Example Usage

```python
from glean.api_client.models import UserRole

value = UserRole.OWNER

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `OWNER`            | OWNER              |
| `VIEWER`           | VIEWER             |
| `ANSWER_MODERATOR` | ANSWER_MODERATOR   |
| `EDITOR`           | EDITOR             |
| `VERIFIER`         | VERIFIER           |