# ChatFileStatus

Current status of the file.

## Example Usage

```python
from glean.api_client.models import ChatFileStatus

value = ChatFileStatus.PROCESSING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `PROCESSING` | PROCESSING   |
| `PROCESSED`  | PROCESSED    |
| `FAILED`     | FAILED       |
| `DELETED`    | DELETED      |