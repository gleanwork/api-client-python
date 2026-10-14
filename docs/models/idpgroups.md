# IdpGroups

How to resolve effective usage limits when a user belongs to multiple IdP groups.


## Example Usage

```python
from glean.api_client.models import IdpGroups

value = IdpGroups.HIGHEST

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `HIGHEST` | HIGHEST   |
| `LOWEST`  | LOWEST    |