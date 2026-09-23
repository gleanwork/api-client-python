# PlatformAgentRunState

State of the persisted workflow execution. REQUIRES_INPUT is nonterminal.

## Example Usage

```python
from glean.api_client.models import PlatformAgentRunState

value = PlatformAgentRunState.QUEUED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `QUEUED`         | QUEUED           |
| `RUNNING`        | RUNNING          |
| `REQUIRES_INPUT` | REQUIRES_INPUT   |
| `SUCCEEDED`      | SUCCEEDED        |
| `FAILED`         | FAILED           |
| `CANCELLING`     | CANCELLING       |
| `CANCELLED`      | CANCELLED        |
| `EXPIRED`        | EXPIRED          |