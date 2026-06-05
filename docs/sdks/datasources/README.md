# Datasources

## Overview

Manage datasources.

### Available Operations

* [get_datasource_instance_configuration](#get_datasource_instance_configuration) - Get datasource instance configuration
* [update_datasource_instance_configuration](#update_datasource_instance_configuration) - Update datasource instance configuration
* [get_datasource_credential_status](#get_datasource_credential_status) - Get datasource instance credential status
* [rotate_datasource_credentials](#rotate_datasource_credentials) - Rotate datasource instance credentials

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

## get_datasource_credential_status

Returns the current credential status for a datasource instance. Access is limited to callers with the ADMIN scope; the handler enforces this check.


### Example Usage

<!-- UsageSnippet language="python" operationID="getDatasourceCredentialStatus" method="get" path="/rest/api/v1/datasource/{datasourceInstanceId}/credentialstatus" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.datasources.get_datasource_credential_status(datasource_instance_id="o365sharepoint_abc123")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `datasource_instance_id`                                             | *str*                                                                | :heavy_check_mark:                                                   | The full datasource instance identifier (e.g. o365sharepoint_abc123) | o365sharepoint_abc123                                                |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |                                                                      |

### Response

**[models.DatasourceCredentialStatusResponse](../../models/datasourcecredentialstatusresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400, 403, 404        | application/json     |
| errors.GleanError    | 4XX, 5XX             | \*/\*                |

## rotate_datasource_credentials

Rotates the credentials that a datasource instance uses to connect to its upstream system. Replaces the active credential material with the supplied values and returns the credential status after rotation. Access is limited to callers with the ADMIN scope; the handler enforces this check.
Only keys recognized as credential material for the datasource type may be set in `credentials.values` (e.g. `clientSecret`, `apiToken`, `privateKey`, depending on the configured auth method). Unrecognized keys, or keys that correspond to non-credential configuration, cause a 400; other instance configuration must be updated via PATCH /configure/datasources/{datasourceId}/instances/{instanceId}.


### Example Usage

<!-- UsageSnippet language="python" operationID="rotateDatasourceCredentials" method="post" path="/rest/api/v1/datasource/{datasourceInstanceId}/credentials" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.datasources.rotate_datasource_credentials(datasource_instance_id="o365sharepoint_abc123", credentials={
        "values": {
            "key": {},
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               | Example                                                                                   |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `datasource_instance_id`                                                                  | *str*                                                                                     | :heavy_check_mark:                                                                        | The full datasource instance identifier (e.g. o365sharepoint_abc123)                      | o365sharepoint_abc123                                                                     |
| `credentials`                                                                             | [models.DatasourceInstanceConfiguration](../../models/datasourceinstanceconfiguration.md) | :heavy_check_mark:                                                                        | Configuration for a datasource instance                                                   |                                                                                           |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |                                                                                           |

### Response

**[models.DatasourceCredentialStatusResponse](../../models/datasourcecredentialstatusresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400, 403, 404        | application/json     |
| errors.GleanError    | 4XX, 5XX             | \*/\*                |