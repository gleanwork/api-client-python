# DatasourceCredentialStatus

Lifecycle state of the credentials installed for a datasource instance. Mirrors the internal admin Status enum so the handler can surface the same health signals already tracked today. EXPIRING_SOON is represented as VALID_WITH_WARNINGS (with detail in `message`); EXPIRED is surfaced as INVALID plus a non-null `expiresAt` in the past.


## Example Usage

```python
from glean.api_client.models import DatasourceCredentialStatus

value = DatasourceCredentialStatus.VALID

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                  | Value                 |
| --------------------- | --------------------- |
| `VALID`               | VALID                 |
| `VALID_WITH_WARNINGS` | VALID_WITH_WARNINGS   |
| `VALIDATING`          | VALIDATING            |
| `INVALID`             | INVALID               |
| `MISSING`             | MISSING               |