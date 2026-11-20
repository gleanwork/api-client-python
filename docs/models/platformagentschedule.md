# PlatformAgentSchedule

Wall-clock schedule for INPUT_FORM and CHAT_MESSAGE agents.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `frequency`                                                                          | *str*                                                                                | :heavy_check_mark:                                                                   | Five-field Unix cron expression, for example `0 9 * * 1-5`.                          |
| `timezone`                                                                           | *str*                                                                                | :heavy_check_mark:                                                                   | IANA time zone name, for example `America/Los_Angeles`.                              |
| `start_at`                                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects)                 | :heavy_minus_sign:                                                                   | ISO 8601 timestamp with an explicit offset before which the schedule stays dormant.<br/> |