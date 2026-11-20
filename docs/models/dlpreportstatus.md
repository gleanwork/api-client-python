# DlpReportStatus

The status of the policy/report. Only ACTIVE status will be picked for scans.

## Example Usage

```python
from glean.api_client.models import DlpReportStatus

value = DlpReportStatus.ACTIVE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `ACTIVE`    | ACTIVE      |
| `INACTIVE`  | INACTIVE    |
| `CANCELLED` | CANCELLED   |
| `NONE`      | NONE        |