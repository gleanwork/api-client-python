# IndexAuthentication
(*index.authentication*)

## Overview

### Available Operations

* [rotate_token](#rotate_token) - Rotate token

## rotate_token

Rotates the secret value inside the Indexing API token and returns the new raw secret. All other properties of the token are unchanged. In order to rotate the secret value, include the token as the bearer token in the `/rotatetoken` request. Please refer to [Token rotation](https://developers.glean.com/docs/indexing_api_token_rotation/) documentation for more information.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.index.authentication.rotate_token()

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