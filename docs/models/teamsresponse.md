# TeamsResponse


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `results`                                                            | List[[models.Team](../models/team.md)]                               | :heavy_minus_sign:                                                   | A Team and a deep copy of all its members for each ID in the request |
| `errors`                                                             | List[*str*]                                                          | :heavy_minus_sign:                                                   | A list of IDs that could not be found.                               |