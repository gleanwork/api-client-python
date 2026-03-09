# ResponseHint

Hints for the response content.

## Example Usage

```python
from glean.api_client.models import ResponseHint

value = ResponseHint.ALL_RESULT_COUNTS

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                  | Value                 |
| --------------------- | --------------------- |
| `ALL_RESULT_COUNTS`   | ALL_RESULT_COUNTS     |
| `FACET_RESULTS`       | FACET_RESULTS         |
| `QUERY_METADATA`      | QUERY_METADATA        |
| `RESULTS`             | RESULTS               |
| `SPELLCHECK_METADATA` | SPELLCHECK_METADATA   |