# EventStrategyName

The name of method used to surface relevant data for a given calendar event.

## Example Usage

```python
from glean.api_client.models import EventStrategyName

value = EventStrategyName.CUSTOMER_CARD

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `CUSTOMER_CARD`      | customerCard         |
| `NEWS`               | news                 |
| `CALL`               | call                 |
| `EMAIL`              | email                |
| `MEETING_NOTES`      | meetingNotes         |
| `LINKED_IN`          | linkedIn             |
| `RELEVANT_DOCUMENTS` | relevantDocuments    |
| `CHAT_FOLLOW_UPS`    | chatFollowUps        |
| `CONVERSATIONS`      | conversations        |