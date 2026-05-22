# CustomMetadataPropertyDefinitionPropertyType

The type of metadata key. This governs the search and faceting behavior.

## Example Usage

```python
from glean.api_client.models import CustomMetadataPropertyDefinitionPropertyType

value = CustomMetadataPropertyDefinitionPropertyType.TEXT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `TEXT`          | TEXT            |
| `PICKLIST`      | PICKLIST        |
| `TEXTLIST`      | TEXTLIST        |
| `MULTIPICKLIST` | MULTIPICKLIST   |