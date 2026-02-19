# Authentication

## Overview

Manage indexing API tokens.

### Available Operations

* [checkdatasourceauth](#checkdatasourceauth) - Check datasource authorization

## checkdatasourceauth

Returns all datasource instances that require per-user OAuth authorization
for the authenticated user, along with a transient auth token that can be
appended to auth URLs to complete OAuth flows.

Clients construct the full OAuth URL by combining the backend base URL,
the `authUrlRelativePath` from each instance, and the transient auth token:
`<backend>/<authUrlRelativePath>?transient_auth_token=<token>`.


### Example Usage

<!-- UsageSnippet language="python" operationID="checkdatasourceauth" method="post" path="/rest/api/v1/checkdatasourceauth" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.authentication.checkdatasourceauth()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CheckDatasourceAuthResponse](../../models/checkdatasourceauthresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |