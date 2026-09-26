# PlatformSkillStatus

The caller's effective activation. The owner sees the skill's stored status. Another caller sees their personal setting, or DISABLED when they have none. DRAFT is the stored draft state and is not set by update. Effective activation may also reflect workspace governance policy.


## Example Usage

```python
from glean.api_client.models import PlatformSkillStatus

value = PlatformSkillStatus.DRAFT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `DRAFT`    | DRAFT      |
| `ENABLED`  | ENABLED    |
| `DISABLED` | DISABLED   |