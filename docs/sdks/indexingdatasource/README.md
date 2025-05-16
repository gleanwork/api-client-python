# IndexingDatasource
(*indexing.datasource*)

## Overview

### Available Operations

* [status](#status) - Beta: Get datasource status


## status

Gather information about the datasource's overall status. Currently in beta, might undergo breaking changes without prior notice.

Tip: Refer to the [Troubleshooting tutorial](https://developers.glean.com/docs/indexing_api/indexing_api_troubleshooting/) for more information.


### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    security=models.Security(
        api_token=os.getenv("GLEAN_API_TOKEN", ""),
    ),
) as g_client:

    res = g_client.indexing.datasource.status(datasource="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The datasource to get debug status for.                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DebugDatasourceStatusResponse](../../models/debugdatasourcestatusresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |