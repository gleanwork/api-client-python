# InputOptionsTimePeriodType

Type of time period for which to run the report/policy. PAST_DAY is deprecated.

## Example Usage

```python
from glean.api_client.models import InputOptionsTimePeriodType

value = InputOptionsTimePeriodType.ALL_TIME

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `ALL_TIME`    | ALL_TIME      |
| `PAST_YEAR`   | PAST_YEAR     |
| `PAST_DAY`    | PAST_DAY      |
| `CUSTOM`      | CUSTOM        |
| `LAST_N_DAYS` | LAST_N_DAYS   |