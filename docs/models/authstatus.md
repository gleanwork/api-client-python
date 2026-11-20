# AuthStatus

The per-user authorization status for a datasource.

## Example Usage

```python
from glean.api_client.models import AuthStatus

value = AuthStatus.DISABLED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `DISABLED`      | DISABLED        |
| `AWAITING_AUTH` | AWAITING_AUTH   |
| `AUTHORIZED`    | AUTHORIZED      |
| `STALE_OAUTH`   | STALE_OAUTH     |
| `SEG_MIGRATION` | SEG_MIGRATION   |