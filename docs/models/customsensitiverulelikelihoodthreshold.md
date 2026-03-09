# CustomSensitiveRuleLikelihoodThreshold

Likelihood threshold for BUILT_IN infotypes (e.g., LIKELY, VERY_LIKELY). Only applicable for BUILT_IN type.

## Example Usage

```python
from glean.api_client.models import CustomSensitiveRuleLikelihoodThreshold

value = CustomSensitiveRuleLikelihoodThreshold.LIKELY

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `LIKELY`        | LIKELY          |
| `VERY_LIKELY`   | VERY_LIKELY     |
| `POSSIBLE`      | POSSIBLE        |
| `UNLIKELY`      | UNLIKELY        |
| `VERY_UNLIKELY` | VERY_UNLIKELY   |