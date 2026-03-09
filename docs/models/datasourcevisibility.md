# DatasourceVisibility

The visibility of the datasource, an enum of VISIBLE_TO_ALL, VISIBLE_TO_TEST_GROUP, NOT_VISIBLE

## Example Usage

```python
from glean.api_client.models import DatasourceVisibility

value = DatasourceVisibility.ENABLED_FOR_ALL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                     | Value                    |
| ------------------------ | ------------------------ |
| `ENABLED_FOR_ALL`        | ENABLED_FOR_ALL          |
| `ENABLED_FOR_TEST_GROUP` | ENABLED_FOR_TEST_GROUP   |
| `NOT_ENABLED`            | NOT_ENABLED              |