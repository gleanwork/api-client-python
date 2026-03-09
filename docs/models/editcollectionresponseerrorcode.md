# EditCollectionResponseErrorCode

## Example Usage

```python
from glean.api_client.models import EditCollectionResponseErrorCode

value = EditCollectionResponseErrorCode.NAME_EXISTS

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                        | Value                       |
| --------------------------- | --------------------------- |
| `NAME_EXISTS`               | NAME_EXISTS                 |
| `NOT_FOUND`                 | NOT_FOUND                   |
| `COLLECTION_PINNED`         | COLLECTION_PINNED           |
| `CONCURRENT_HIERARCHY_EDIT` | CONCURRENT_HIERARCHY_EDIT   |
| `HEIGHT_VIOLATION`          | HEIGHT_VIOLATION            |
| `WIDTH_VIOLATION`           | WIDTH_VIOLATION             |
| `NO_PERMISSIONS`            | NO_PERMISSIONS              |