# ProcessingState

The current state of the upload, an enum of UNAVAILABLE, UPLOAD STARTED, UPLOAD IN PROGRESS, UPLOAD COMPLETED, DELETION PAUSED, INDEXING COMPLETED

## Example Usage

```python
from glean.api_client.models import ProcessingState

value = ProcessingState.UNAVAILABLE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `UNAVAILABLE`        | UNAVAILABLE          |
| `UPLOAD_STARTED`     | UPLOAD STARTED       |
| `UPLOAD_IN_PROGRESS` | UPLOAD IN PROGRESS   |
| `UPLOAD_COMPLETED`   | UPLOAD COMPLETED     |
| `DELETION_PAUSED`    | DELETION PAUSED      |
| `INDEXING_COMPLETED` | INDEXING COMPLETED   |