# ChatStatus

The status of the Chat.

## Example Usage

```python
from glean.api_client.models import ChatStatus

value = ChatStatus.SUCCESS

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `SUCCESS`     | SUCCESS       |
| `ERROR`       | ERROR         |
| `IN_PROGRESS` | IN_PROGRESS   |
| `CANCELLED`   | CANCELLED     |