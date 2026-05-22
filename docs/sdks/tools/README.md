# Tools

## Overview

### Available Operations

* [get_action_pack_auth_status](#get_action_pack_auth_status) - Get end-user authentication status for an action pack.
* [authorize_action_pack](#authorize_action_pack) - Start the OAuth authorization flow for an action pack.

## get_action_pack_auth_status

Reports whether the calling user is already authenticated against the third-party
tool backing the specified action pack. Intended for headless / server-driven clients
that render an "Authorize" prompt when the user has not yet consented to the tool.


### Example Usage

<!-- UsageSnippet language="python" operationID="getActionPackAuthStatus" method="get" path="/rest/api/v1/actions/actionpack/{actionPackId}/auth" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.tools.get_action_pack_auth_status(action_pack_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `action_pack_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | ID of the action pack to query or authorize.                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ActionPackAuthStatusResponse](../../models/actionpackauthstatusresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## authorize_action_pack

Starts the third-party OAuth flow for the specified action pack and returns the
redirect URL that the client should navigate the end user to. After the OAuth
callback completes, the user's browser is redirected back to `returnUrl` with a
status query parameter (`?glean_action_auth=success|error&actionPackId=...`).

`returnUrl` must match the tenant's configured return URL allowlist; otherwise the
request is rejected with 400.


### Example Usage

<!-- UsageSnippet language="python" operationID="authorizeActionPack" method="post" path="/rest/api/v1/actions/actionpack/{actionPackId}/auth" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.tools.authorize_action_pack(action_pack_id="<id>", return_url="https://merry-allocation.org/")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `action_pack_id`                                                                                                                                                               | *str*                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                             | ID of the action pack to query or authorize.                                                                                                                                   |
| `return_url`                                                                                                                                                                   | *str*                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                             | URL on the customer's domain to redirect the end user's browser back to after the third-party OAuth<br/>callback completes. Must be present in the tenant's return URL allowlist.<br/> |
| `retries`                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                               | :heavy_minus_sign:                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                            |

### Response

**[models.AuthorizeActionPackResponse](../../models/authorizeactionpackresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |