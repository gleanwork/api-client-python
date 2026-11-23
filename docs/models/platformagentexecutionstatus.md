# PlatformAgentExecutionStatus

Status of the agent run.

## Example Usage

```python
from glean.api_client.models import PlatformAgentExecutionStatus

value = PlatformAgentExecutionStatus.ERROR

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `ERROR`   | error     |
| `SUCCESS` | success   |