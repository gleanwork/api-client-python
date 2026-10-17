# PlatformOAuthGrantType

An OAuth grant type.

## Example Usage

```python
from glean.api_client.models import PlatformOAuthGrantType

value = PlatformOAuthGrantType.AUTHORIZATION_CODE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `AUTHORIZATION_CODE` | AUTHORIZATION_CODE   |
| `CLIENT_CREDENTIALS` | CLIENT_CREDENTIALS   |
| `REFRESH_TOKEN`      | REFRESH_TOKEN        |
| `DEVICE_CODE`        | DEVICE_CODE          |
| `TOKEN_EXCHANGE`     | TOKEN_EXCHANGE       |
| `JWT_BEARER`         | JWT_BEARER           |