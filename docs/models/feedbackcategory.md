# FeedbackCategory

The feature category to which the feedback applies. These should be broad product areas such as Announcements, Answers, Search, etc. rather than specific components or UI treatments within those areas.

## Example Usage

```python
from glean.api_client.models import FeedbackCategory

value = FeedbackCategory.ANNOUNCEMENT
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `ANNOUNCEMENT` | ANNOUNCEMENT   |
| `ANSWERS`      | ANSWERS        |
| `ARTIFACTS`    | ARTIFACTS      |
| `AUTOCOMPLETE` | AUTOCOMPLETE   |
| `COLLECTIONS`  | COLLECTIONS    |
| `FEED`         | FEED           |
| `SEARCH`       | SEARCH         |
| `CHAT`         | CHAT           |
| `NTP`          | NTP            |
| `WORKFLOWS`    | WORKFLOWS      |
| `SUMMARY`      | SUMMARY        |
| `GENERAL`      | GENERAL        |
| `PRISM`        | PRISM          |
| `PROMPTS`      | PROMPTS        |