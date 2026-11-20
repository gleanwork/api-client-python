# TimeRangeFilterTimePeriodType

The type of time period for which to filter findings.

## Example Usage

```python
from glean.api_client.models import TimeRangeFilterTimePeriodType

value = TimeRangeFilterTimePeriodType.PAST_DAY

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `PAST_DAY`   | PAST_DAY     |
| `PAST_WEEK`  | PAST_WEEK    |
| `PAST_MONTH` | PAST_MONTH   |
| `PAST_YEAR`  | PAST_YEAR    |
| `CUSTOM`     | CUSTOM       |