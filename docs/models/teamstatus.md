# TeamStatus

whether this team is fully processed or there are still unprocessed operations that'll affect it

## Example Usage

```python
from glean.api_client.models import TeamStatus

value = TeamStatus.PROCESSED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                  | Value                 |
| --------------------- | --------------------- |
| `PROCESSED`           | PROCESSED             |
| `QUEUED_FOR_CREATION` | QUEUED_FOR_CREATION   |
| `QUEUED_FOR_DELETION` | QUEUED_FOR_DELETION   |