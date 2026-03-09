# UpdateDatasourceConfigurationRequest

Request to update greenlisted configuration values for a datasource instance. Only keys that are exposed via the public API greenlist may be set.



## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `configuration`                                                                        | [models.DatasourceInstanceConfiguration](../models/datasourceinstanceconfiguration.md) | :heavy_check_mark:                                                                     | Configuration for a datasource instance                                                |