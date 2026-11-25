# PlatformAgentContentTriggerFilterOperator

Operator of a content trigger filter.

## Example Usage

```python
from glean.api_client.models import PlatformAgentContentTriggerFilterOperator

value = PlatformAgentContentTriggerFilterOperator.IS_ONE_OF

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `IS_ONE_OF`     | IS_ONE_OF       |
| `IS_NOT_ONE_OF` | IS_NOT_ONE_OF   |
| `CONTAINS`      | CONTAINS        |
| `FIELD_CHANGED` | FIELD_CHANGED   |