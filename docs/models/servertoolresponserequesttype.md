# ServerToolResponseRequestType

The type of request made to the user.

## Example Usage

```python
from glean.api_client.models import ServerToolResponseRequestType

value = ServerToolResponseRequestType.EXECUTION

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                        | Value                       |
| --------------------------- | --------------------------- |
| `EXECUTION`                 | EXECUTION                   |
| `AUTHENTICATION_SUGGESTION` | AUTHENTICATION_SUGGESTION   |
| `VOTE_SUGGESTION`           | VOTE_SUGGESTION             |