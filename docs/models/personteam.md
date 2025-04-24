# PersonTeam

Use `id` if you index teams via Glean, and use `name` and `externalLink` if you want to use your own team pages


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `id`                                                                            | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Unique identifier                                                               |
| `name`                                                                          | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Team name                                                                       |
| `external_link`                                                                 | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Link to a team page on the internet or your company's intranet                  |
| `relationship`                                                                  | [Optional[models.PersonTeamRelationship]](../models/personteamrelationship.md)  | :heavy_minus_sign:                                                              | The team member's relationship to the team. This defaults to MEMBER if not set. |
| `join_date`                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)            | :heavy_minus_sign:                                                              | The team member's start date                                                    |