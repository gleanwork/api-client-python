# AuthHeaderType

Defines the header structure for sending the API key or token to the server. Defaults to AUTHORIZATION_BEARER. Select the specific header format the server expects for transmitting the key.

## Example Usage

```python
from glean.api_client.models import AuthHeaderType

value = AuthHeaderType.AUTHORIZATION_BEARER

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                    | Value                   |
| ----------------------- | ----------------------- |
| `AUTHORIZATION_BEARER`  | AUTHORIZATION_BEARER    |
| `AUTHORIZATION_TOKEN`   | AUTHORIZATION_TOKEN     |
| `AUTHORIZATION_API_KEY` | AUTHORIZATION_API_KEY   |
| `X_API_KEY`             | X_API_KEY               |