# TimePoint


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `epoch_seconds`                                           | *Optional[int]*                                           | :heavy_minus_sign:                                        | Epoch seconds. Has precedence over daysFromNow.           |
| `days_from_now`                                           | *Optional[int]*                                           | :heavy_minus_sign:                                        | Number of days in the past, relative to the current date. |