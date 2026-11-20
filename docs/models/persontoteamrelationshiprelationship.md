# PersonToTeamRelationshipRelationship

The team member's relationship to the team. This defaults to MEMBER if not set.

## Example Usage

```python
from glean.api_client.models import PersonToTeamRelationshipRelationship

value = PersonToTeamRelationshipRelationship.MEMBER

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `MEMBER`           | MEMBER             |
| `MANAGER`          | MANAGER            |
| `LEAD`             | LEAD               |
| `POINT_OF_CONTACT` | POINT_OF_CONTACT   |
| `OTHER`            | OTHER              |