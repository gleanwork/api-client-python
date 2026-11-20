# ToolServerAuthStatus

Authentication status for the calling user.

## Example Usage

```python
from glean.api_client.models import ToolServerAuthStatus

value = ToolServerAuthStatus.AWAITING_AUTH

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `AWAITING_AUTH` | AWAITING_AUTH   |
| `AUTHORIZED`    | AUTHORIZED      |