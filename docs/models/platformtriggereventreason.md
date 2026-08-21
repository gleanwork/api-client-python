# PlatformTriggerEventReason

Why the event fired.

## Example Usage

```python
from glean.api_client.models import PlatformTriggerEventReason

value = PlatformTriggerEventReason.CREATED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                     | Value                    |
| ------------------------ | ------------------------ |
| `CREATED`                | CREATED                  |
| `UPDATED`                | UPDATED                  |
| `DELETED`                | DELETED                  |
| `MEETS_CONDITION`        | MEETS_CONDITION          |
| `ASSIGNED`               | ASSIGNED                 |
| `UNASSIGNED`             | UNASSIGNED               |
| `LABELED`                | LABELED                  |
| `UNLABELED`              | UNLABELED                |
| `REVIEW_REQUESTED`       | REVIEW_REQUESTED         |
| `REVIEW_REQUEST_REMOVED` | REVIEW_REQUEST_REMOVED   |
| `READY_FOR_REVIEW`       | READY_FOR_REVIEW         |
| `CONVERTED_TO_DRAFT`     | CONVERTED_TO_DRAFT       |
| `WEBHOOK_UPDATED`        | WEBHOOK_UPDATED          |