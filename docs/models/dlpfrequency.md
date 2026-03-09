# DlpFrequency

Interval between scans. DAILY is deprecated.

## Example Usage

```python
from glean.api_client.models import DlpFrequency

value = DlpFrequency.ONCE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `ONCE`       | ONCE         |
| `DAILY`      | DAILY        |
| `WEEKLY`     | WEEKLY       |
| `CONTINUOUS` | CONTINUOUS   |
| `NONE`       | NONE         |