# TokenEndpointAuthMethod

The OAuth 2.0 token endpoint authentication method (RFC 7591). Determines how the client authenticates when exchanging an authorization code for a token. client_secret_post sends credentials as form fields, client_secret_basic sends them via Authorization header, none omits client secret and relies on PKCE only. Values use lowercase to match the OAuth 2.0 wire format (RFC 7591 Section 2).

## Example Usage

```python
from glean.api_client.models import TokenEndpointAuthMethod

value = TokenEndpointAuthMethod.CLIENT_SECRET_POST

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                  | Value                 |
| --------------------- | --------------------- |
| `CLIENT_SECRET_POST`  | client_secret_post    |
| `CLIENT_SECRET_BASIC` | client_secret_basic   |
| `NONE`                | none                  |