# PlatformSkillUpdateStatus

Activation to apply for the authenticated caller. For the owner, this updates the skill's stored status. For any other caller, it updates only that caller's setting.


## Example Usage

```python
from glean.api_client.models import PlatformSkillUpdateStatus

value = PlatformSkillUpdateStatus.ENABLED
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `ENABLED`  | ENABLED    |
| `DISABLED` | DISABLED   |