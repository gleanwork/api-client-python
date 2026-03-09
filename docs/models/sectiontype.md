# SectionType

Type of the section. This defines how the section should be interpreted and rendered in the digest.

## Example Usage

```python
from glean.api_client.models import SectionType

value = SectionType.CHANNEL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `CHANNEL`  | CHANNEL    |
| `MENTIONS` | MENTIONS   |
| `TOPIC`    | TOPIC      |