# PlatformUserFilterOperator

The only supported operator is EQUALS. Defaults to EQUALS.

## Example Usage

```python
from glean.api_client.models import PlatformUserFilterOperator

value = PlatformUserFilterOperator.EQUALS
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