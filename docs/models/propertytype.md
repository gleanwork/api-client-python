# PropertyType

The type of custom property - this governs the search and faceting behavior. Note that MULTIPICKLIST is not yet supported.

## Example Usage

```python
from glean.api_client.models import PropertyType

value = PropertyType.TEXT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `TEXT`          | TEXT            |
| `DATE`          | DATE            |
| `INT`           | INT             |
| `USERID`        | USERID          |
| `PICKLIST`      | PICKLIST        |
| `TEXTLIST`      | TEXTLIST        |
| `MULTIPICKLIST` | MULTIPICKLIST   |