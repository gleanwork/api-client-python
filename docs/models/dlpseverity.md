# DlpSeverity

Severity levels for DLP findings and analyses. FALSE_POSITIVE ranks below LOW and marks analyses that concluded every flagged entity is a detector false positive.

## Example Usage

```python
from glean.api_client.models import DlpSeverity

value = DlpSeverity.UNSPECIFIED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `UNSPECIFIED`    | UNSPECIFIED      |
| `LOW`            | LOW              |
| `MEDIUM`         | MEDIUM           |
| `HIGH`           | HIGH             |
| `FALSE_POSITIVE` | FALSE_POSITIVE   |