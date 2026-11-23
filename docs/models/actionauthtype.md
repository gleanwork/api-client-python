# ActionAuthType

Authentication mechanism used by an action pack.
  - `AUTH_USER_OAUTH`: Requires per-user OAuth consent to the third-party tool.
  - `AUTH_ADMIN`: Uses a service-account / admin-owned credential. End users do not authorize individually.
  - `AUTH_NONE`: Action pack requires no authentication.


## Example Usage

```python
from glean.api_client.models import ActionAuthType

value = ActionAuthType.AUTH_USER_OAUTH

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name              | Value             |
| ----------------- | ----------------- |
| `AUTH_USER_OAUTH` | AUTH_USER_OAUTH   |
| `AUTH_ADMIN`      | AUTH_ADMIN        |
| `AUTH_NONE`       | AUTH_NONE         |