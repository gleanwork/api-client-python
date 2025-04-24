# CustomerMetadata


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `datasource_id`                                                   | *Optional[str]*                                                   | :heavy_minus_sign:                                                | The user visible id of the salesforce customer account.           |
| `custom_data`                                                     | Dict[str, [models.CustomDataValue](../models/customdatavalue.md)] | :heavy_minus_sign:                                                | Custom fields specific to individual datasources                  |