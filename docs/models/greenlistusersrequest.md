# GreenlistUsersRequest

Describes the request body of the /betausers API call


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `datasource`                                                                        | *str*                                                                               | :heavy_check_mark:                                                                  | Datasource which needs to be made visible to users specified in the `emails` field. |
| `emails`                                                                            | List[*str*]                                                                         | :heavy_check_mark:                                                                  | The emails of the beta users                                                        |