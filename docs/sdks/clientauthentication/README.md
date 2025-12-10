# Client.Authentication

## Overview

### Available Operations

* [create_token](#create_token) - Create authentication token

## create_token

Creates an authentication token for the authenticated user. These are
specifically intended to be used with the [Web SDK](https://developers.glean.com/web).

Note: The tokens generated from this endpoint are **not** valid tokens
for use with the Client API (e.g. `/rest/api/v1/*`).


### Example Usage

<!-- UsageSnippet language="python" operationID="createauthtoken" method="post" path="/rest/api/v1/createauthtoken" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.authentication.create_token()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateAuthTokenResponse](../../models/createauthtokenresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |