# PlatformSkillSourcePreviewFailureCode

Stable machine-readable reason a discovered entry was excluded.

## Example Usage

```python
from glean.api_client.models import PlatformSkillSourcePreviewFailureCode

value = PlatformSkillSourcePreviewFailureCode.INVALID_SKILL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `INVALID_SKILL`      | INVALID_SKILL        |
| `SKILL_FETCH_FAILED` | SKILL_FETCH_FAILED   |