# ExecutionMode

REQUEST_BOUND preserves the existing wait/stream behavior. DURABLE starts a fresh, persisted execution with a 30-minute execution timeout and returns immediately. DURABLE requires stream to be false or omitted and does not accept metadata.chat_session_id. It does not bypass tool approval requirements or provide automatic QE-crash resumption. Expiry is read-triggered: the next GET of the run marks an active turn FAILED if more than 40 minutes have passed since the turn was accepted. There is no periodic sweep, so the stored run can remain RUNNING until it is read. Expiry never replays execution or expires approval-paused runs, and failure does not prove that external tool work has stopped.


## Example Usage

```python
from glean.api_client.models import ExecutionMode

value = ExecutionMode.REQUEST_BOUND
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `REQUEST_BOUND` | REQUEST_BOUND   |
| `DURABLE`       | DURABLE         |