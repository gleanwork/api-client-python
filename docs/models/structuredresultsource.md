# StructuredResultSource

Source context for this result. Possible values depend on the result type.

## Example Usage

```python
from glean.api_client.models import StructuredResultSource

value = StructuredResultSource.EXPERT_DETECTION

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `EXPERT_DETECTION` | EXPERT_DETECTION   |
| `ENTITY_NLQ`       | ENTITY_NLQ         |
| `CALENDAR_EVENT`   | CALENDAR_EVENT     |
| `AGENT`            | AGENT              |