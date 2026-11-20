# DlpIssueStatus

Status of a DLP issue.

## Example Usage

```python
from glean.api_client.models import DlpIssueStatus

value = DlpIssueStatus.OPEN

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `OPEN`        | OPEN          |
| `CLOSED`      | CLOSED        |
| `IN_PROGRESS` | IN_PROGRESS   |
| `RESOLVED`    | RESOLVED      |