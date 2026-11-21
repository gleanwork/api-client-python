# AgentExecutionStatus

The status of the run. One of 'error', 'success'.

## Example Usage

```python
from glean.api_client.models import AgentExecutionStatus

value = AgentExecutionStatus.ERROR

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `ERROR`   | error     |
| `SUCCESS` | success   |