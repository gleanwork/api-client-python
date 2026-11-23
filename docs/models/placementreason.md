# PlacementReason

Placement source for ranked feed results. ORGANIC means the card was emitted by normal feed ranking. PROMO means the card was inserted by the homepage cards promo framework. PINNED means the card was moved to the head of the ranked stack (e.g. knowledge-gap pilot cards).

## Example Usage

```python
from glean.api_client.models import PlacementReason

value = PlacementReason.ORGANIC

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `ORGANIC` | ORGANIC   |
| `PROMO`   | PROMO     |
| `PINNED`  | PINNED    |