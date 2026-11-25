# DocumentVisibility

The level of visibility of the document as understood by our system.

## Example Usage

```python
from glean.api_client.models import DocumentVisibility

value = DocumentVisibility.PRIVATE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                         | Value                        |
| ---------------------------- | ---------------------------- |
| `PRIVATE`                    | PRIVATE                      |
| `SPECIFIC_PEOPLE_AND_GROUPS` | SPECIFIC_PEOPLE_AND_GROUPS   |
| `DOMAIN_LINK`                | DOMAIN_LINK                  |
| `DOMAIN_VISIBLE`             | DOMAIN_VISIBLE               |
| `PUBLIC_LINK`                | PUBLIC_LINK                  |
| `PUBLIC_VISIBLE`             | PUBLIC_VISIBLE               |