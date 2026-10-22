# PlatformOAuthClientType

Whether an OAuth client can keep a secret.

## Example Usage

```python
from glean.api_client.models import PlatformOAuthClientType

value = PlatformOAuthClientType.CONFIDENTIAL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `CONFIDENTIAL` | CONFIDENTIAL   |
| `PUBLIC`       | PUBLIC         |