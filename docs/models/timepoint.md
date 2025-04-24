# TimePoint


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `epoch_seconds`                                                                       | *Optional[int]*                                                                       | :heavy_minus_sign:                                                                    | Epoch seconds. Has precedence over daysFromNow.                                       |
| `days_from_now`                                                                       | *Optional[int]*                                                                       | :heavy_minus_sign:                                                                    | The number of days from now. Specification relative to current time. Can be negative. |