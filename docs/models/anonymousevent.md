# AnonymousEvent

A generic, light-weight calendar event.


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `time`                                                                           | [Optional[models.TimeInterval]](../models/timeinterval.md)                       | :heavy_minus_sign:                                                               | N/A                                                                              |
| `event_type`                                                                     | [Optional[models.AnonymousEventEventType]](../models/anonymouseventeventtype.md) | :heavy_minus_sign:                                                               | The nature of the event, for example "out of office".                            |