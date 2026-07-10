# GrantScope

Scope of the approval grant. Only applicable when isGranted is true and requestType is EXECUTION.


## Example Usage

```python
from glean.api_client.models import GrantScope

value = GrantScope.CURRENT_REQUEST

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name              | Value             |
| ----------------- | ----------------- |
| `CURRENT_REQUEST` | CURRENT_REQUEST   |
| `CURRENT_SESSION` | CURRENT_SESSION   |
| `ALWAYS`          | ALWAYS            |