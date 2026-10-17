# PlatformOAuthTokenEndpointAuthMethod

How an OAuth client authenticates to the token endpoint.

## Example Usage

```python
from glean.api_client.models import PlatformOAuthTokenEndpointAuthMethod

value = PlatformOAuthTokenEndpointAuthMethod.CLIENT_SECRET_BASIC

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                  | Value                 |
| --------------------- | --------------------- |
| `CLIENT_SECRET_BASIC` | CLIENT_SECRET_BASIC   |
| `CLIENT_SECRET_POST`  | CLIENT_SECRET_POST    |
| `NO_AUTHENTICATION`   | NO_AUTHENTICATION     |
| `PRIVATE_KEY_JWT`     | PRIVATE_KEY_JWT       |
| `TLS_CLIENT_AUTH`     | TLS_CLIENT_AUTH       |