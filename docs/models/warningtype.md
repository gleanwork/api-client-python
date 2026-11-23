# WarningType

The type of the warning.

## Example Usage

```python
from glean.api_client.models import WarningType

value = WarningType.LONG_QUERY

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                         | Value                        |
| ---------------------------- | ---------------------------- |
| `LONG_QUERY`                 | LONG_QUERY                   |
| `QUOTED_PUNCTUATION`         | QUOTED_PUNCTUATION           |
| `PUNCTUATION_ONLY`           | PUNCTUATION_ONLY             |
| `COPYPASTED_QUOTES`          | COPYPASTED_QUOTES            |
| `INVALID_OPERATOR`           | INVALID_OPERATOR             |
| `MAYBE_INVALID_FACET_QUERY`  | MAYBE_INVALID_FACET_QUERY    |
| `TOO_MANY_DATASOURCE_GROUPS` | TOO_MANY_DATASOURCE_GROUPS   |