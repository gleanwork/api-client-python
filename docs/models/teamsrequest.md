# TeamsRequest


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `ids`                                                                          | List[*str*]                                                                    | :heavy_minus_sign:                                                             | The IDs of the teams to retrieve.                                              |
| `include_fields`                                                               | List[[models.TeamsRequestIncludeField](../models/teamsrequestincludefield.md)] | :heavy_minus_sign:                                                             | List of teams fields to return that aren't returned by default                 |