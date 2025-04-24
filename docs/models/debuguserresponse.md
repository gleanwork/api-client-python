# DebugUserResponse

Describes the response body of the /debug/{datasource}/user API call


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `status`                                                                         | [Optional[models.UserStatusResponse]](../models/userstatusresponse.md)           | :heavy_minus_sign:                                                               | Describes the user status response body                                          |
| `uploaded_groups`                                                                | List[[models.DatasourceGroupDefinition](../models/datasourcegroupdefinition.md)] | :heavy_minus_sign:                                                               | List of groups the user is a member of, as uploaded via permissions API.         |