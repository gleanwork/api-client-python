# PlatformSkillSyncStatus

Current external-source sync status.

## Example Usage

```python
from glean.api_client.models import PlatformSkillSyncStatus

value = PlatformSkillSyncStatus.UP_TO_DATE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `UP_TO_DATE`       | UP_TO_DATE         |
| `UPDATE_AVAILABLE` | UPDATE_AVAILABLE   |
| `SYNC_FAILED`      | SYNC_FAILED        |