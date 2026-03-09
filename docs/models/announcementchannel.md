# AnnouncementChannel

This determines whether this is a Social Feed post or a regular announcement.

## Example Usage

```python
from glean.api_client.models import AnnouncementChannel

value = AnnouncementChannel.MAIN

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `MAIN`        | MAIN          |
| `SOCIAL_FEED` | SOCIAL_FEED   |