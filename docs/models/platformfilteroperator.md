# PlatformFilterOperator

Supported filter operator.

## Example Usage

```python
from glean.api_client.models import PlatformFilterOperator

value = PlatformFilterOperator.EQUALS

# Open enum: unrecognized values are captured as UnrecognizedStr
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