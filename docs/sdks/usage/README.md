# Admin.Usage

## Overview

### Available Operations

* [get_settings](#get_settings) - Get usage settings
* [update_settings](#update_settings) - Update usage settings

## get_settings

Retrieve workspace-wide policy from the same configuration used by Billing. Group resolution uses the configured policy and its backend defaults; business justification is currently optional. No per-user settings are read, and updated_at is omitted because no policy-update timestamp is available. Requires admin.usage.settings:read and permission to read workspace billing; a global administrator role is not required.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-admin-usage-settings-get" method="get" path="/api/admin/usage/settings" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.admin.usage.get_settings()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlatformUsageSettingsResponse](../../models/platformusagesettingsresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 429      | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## update_settings

Assign workspace-wide usage policy. Assignment is currently unavailable until a writer to authoritative Billing configuration is integrated. The backend config platform.usageSettingsWritesEnabled is disabled by default; enabling it alone does not implement assignment, and an authorized request still returns 503 without changing configuration or persisting a second copy of policy. Requires admin.usage.settings:write and permission to edit workspace billing; a global administrator role is not required.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-admin-usage-settings-update" method="patch" path="/api/admin/usage/settings" -->
```python
from glean.api_client import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.admin.usage.update_settings(request={
        "multiple_membership_resolution": {
            "per_member": {
                "idp_groups": models.IdpGroups.HIGHEST,
            },
        },
        "limit_increase_requests": {
            "business_justification": models.BusinessJustification.REQUIRED,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                 | [models.PlatformUsageSettingsUpdateRequestUnion](../../models/platformusagesettingsupdaterequestunion.md) | :heavy_check_mark:                                                                                        | The request object to use for the request.                                                                |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.PlatformUsageSettingsResponse](../../models/platformusagesettingsresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 413, 429 | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |