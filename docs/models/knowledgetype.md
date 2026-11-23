# KnowledgeType

Indicates the kind of knowledge a tool would access or modify.

## Example Usage

```python
from glean.api_client.models import KnowledgeType

value = KnowledgeType.NEUTRAL_KNOWLEDGE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                | Value               |
| ------------------- | ------------------- |
| `NEUTRAL_KNOWLEDGE` | NEUTRAL_KNOWLEDGE   |
| `COMPANY_KNOWLEDGE` | COMPANY_KNOWLEDGE   |
| `WORLD_KNOWLEDGE`   | WORLD_KNOWLEDGE     |