# ProcessingHistoryEvent

Processing history event for a datasource


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `start_time`                                                                 | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | The start time of the processing in ISO 8601 format                          | 2021-08-06T17:58:01.000Z                                                     |
| `end_time`                                                                   | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | The end time of the processing in ISO 8601 format, 'NA' if still in progress | 2021-08-06T18:58:01.000Z                                                     |