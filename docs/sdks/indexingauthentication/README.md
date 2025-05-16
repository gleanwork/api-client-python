# IndexingAuthentication
(*indexing.authentication*)

## Overview

### Available Operations

* [rotate_token](#rotate_token) - Rotate token

## rotate_token

Rotates the secret value inside the Indexing API token and returns the new raw secret. All other properties of the token are unchanged. In order to rotate the secret value, include the token as the bearer token in the `/rotatetoken` request. Please refer to [Token rotation](https://developers.glean.com/docs/indexing_api_token_rotation/) documentation for more information.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    security=models.Security(
        act_as_bearer_token=os.getenv("GLEAN_ACT_AS_BEARER_TOKEN", ""),
    ),
) as g_client:

    res = g_client.indexing.authentication.rotate_token()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RotateTokenResponse](../../models/rotatetokenresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |