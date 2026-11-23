# UserReferenceDefinition

Describes how a user is referenced in a document. The user can be referenced by email or by a datasource specific id.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `email`                                                                      | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `datasource_user_id`                                                         | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | some datasources refer to the user by the datasource user id in the document |
| `name`                                                                       | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |