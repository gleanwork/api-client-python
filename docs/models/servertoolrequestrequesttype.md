# ServerToolRequestRequestType

The type of request made to the user.

## Example Usage

```python
from glean.api_client.models import ServerToolRequestRequestType

value = ServerToolRequestRequestType.EXECUTION

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                        | Value                       |
| --------------------------- | --------------------------- |
| `EXECUTION`                 | EXECUTION                   |
| `AUTHENTICATION_SUGGESTION` | AUTHENTICATION_SUGGESTION   |
| `VOTE_SUGGESTION`           | VOTE_SUGGESTION             |
| `SANDBOX_EGRESS`            | SANDBOX_EGRESS              |