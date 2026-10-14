# PlatformAdminAgentFilterOperator

The only supported operator is EQUALS. Defaults to EQUALS.

## Example Usage

```python
from glean.api_client.models import PlatformAdminAgentFilterOperator

value = PlatformAdminAgentFilterOperator.EQUALS
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `EQUALS`     | EQUALS       |
| `NOT_EQUALS` | NOT_EQUALS   |
| `GT`         | GT           |
| `GTE`        | GTE          |
| `LT`         | LT           |
| `LTE`        | LTE          |