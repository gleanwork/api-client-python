# AuthConfigStatus

Auth status of the tool.

## Example Usage

```python
from glean.api_client.models import AuthConfigStatus

value = AuthConfigStatus.AWAITING_AUTH

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `AWAITING_AUTH` | AWAITING_AUTH   |
| `AUTHORIZED`    | AUTHORIZED      |
| `AUTH_DISABLED` | AUTH_DISABLED   |