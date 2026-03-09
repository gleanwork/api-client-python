# Datasources

## Overview

Manage datasources.

### Available Operations

* [get_datasource_instance_configuration](#get_datasource_instance_configuration) - Get datasource instance configuration
* [update_datasource_instance_configuration](#update_datasource_instance_configuration) - Update datasource instance configuration

## get_datasource_instance_configuration

Gets the greenlisted configuration values for a datasource instance. Returns only configuration keys that are exposed via the public API greenlist.


### Example Usage

<!-- UsageSnippet language="python" operationID="getDatasourceInstanceConfiguration" method="get" path="/rest/api/v1/configure/datasources/{datasourceId}/instances/{instanceId}" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.datasources.get_datasource_instance_configuration(datasource_id="o365sharepoint", instance_id="o365sharepoint_abc123")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The datasource type identifier (e.g. o365sharepoint)                | o365sharepoint                                                      |
| `instance_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The datasource instance identifier                                  | o365sharepoint_abc123                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DatasourceConfigurationResponse](../../models/datasourceconfigurationresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400, 403, 404        | application/json     |
| errors.GleanError    | 4XX, 5XX             | \*/\*                |

## update_datasource_instance_configuration

Updates the greenlisted configuration values for a datasource instance. Only configuration keys that are exposed via the public API greenlist may be set. Returns the full greenlisted configuration after the update is applied.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateDatasourceInstanceConfiguration" method="patch" path="/rest/api/v1/configure/datasources/{datasourceId}/instances/{instanceId}" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.datasources.update_datasource_instance_configuration(datasource_id="o365sharepoint", instance_id="o365sharepoint_abc123", configuration={
        "values": {

        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               | Example                                                                                   |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `datasource_id`                                                                           | *str*                                                                                     | :heavy_check_mark:                                                                        | The datasource type identifier (e.g. o365sharepoint)                                      | o365sharepoint                                                                            |
| `instance_id`                                                                             | *str*                                                                                     | :heavy_check_mark:                                                                        | The datasource instance identifier                                                        | o365sharepoint_abc123                                                                     |
| `configuration`                                                                           | [models.DatasourceInstanceConfiguration](../../models/datasourceinstanceconfiguration.md) | :heavy_check_mark:                                                                        | Configuration for a datasource instance                                                   |                                                                                           |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |                                                                                           |

### Response

**[models.DatasourceConfigurationResponse](../../models/datasourceconfigurationresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400, 403, 404        | application/json     |
| errors.GleanError    | 4XX, 5XX             | \*/\*                |