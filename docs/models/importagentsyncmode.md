# ImportAgentSyncMode

Whether the imported version is staged (saved without updating the live version) or published directly to the live version.


## Example Usage

```python
from glean.api_client.models import ImportAgentSyncMode

value = ImportAgentSyncMode.STAGED
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `STAGED`    | STAGED      |
| `PUBLISHED` | PUBLISHED   |