# Policies
(*client.governance.data.policies*)

## Overview

### Available Operations

* [retrieve](#retrieve) - Gets specified Policy.
* [update](#update) - Updates an existing policy.
* [list](#list) - Lists policies.
* [create](#create) - Creates new policy.
* [download](#download) - Downloads violations CSV for policy.

## retrieve

Fetches the specified policy version, or the latest if no version is provided.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    security=models.Security(
        act_as_bearer_token=os.getenv("GLEAN_ACT_AS_BEARER_TOKEN", ""),
    ),
) as g_client:

    res = g_client.client.governance.data.policies.retrieve(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                  | Type                                                                                                                                                       | Required                                                                                                                                                   | Description                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                       | *str*                                                                                                                                                      | :heavy_check_mark:                                                                                                                                         | The id of the policy to fetch.                                                                                                                             |
| `version`                                                                                                                                                  | *Optional[int]*                                                                                                                                            | :heavy_minus_sign:                                                                                                                                         | The version of the policy to fetch. Each time a policy is updated, the older version is still stored. If this is left empty, the latest policy is fetched. |
| `retries`                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                           | :heavy_minus_sign:                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                        |

### Response

**[models.GetDlpReportResponse](../../models/getdlpreportresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## update

Updates an existing policy.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    security=models.Security(
        act_as_bearer_token=os.getenv("GLEAN_ACT_AS_BEARER_TOKEN", ""),
    ),
) as g_client:

    res = g_client.client.governance.data.policies.update(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `id`                                                                            | *str*                                                                           | :heavy_check_mark:                                                              | The id of the policy to fetch.                                                  |
| `config`                                                                        | [Optional[models.DlpConfig]](../../models/dlpconfig.md)                         | :heavy_minus_sign:                                                              | Detailed configuration of what documents and sensitive content will be scanned. |
| `frequency`                                                                     | [Optional[models.DlpFrequency]](../../models/dlpfrequency.md)                   | :heavy_minus_sign:                                                              | Interval between scans. DAILY is deprecated.                                    |
| `status`                                                                        | [Optional[models.DlpReportStatus]](../../models/dlpreportstatus.md)             | :heavy_minus_sign:                                                              | The status of the policy/report. Only ACTIVE status will be picked for scans.   |
| `auto_hide_docs`                                                                | *Optional[bool]*                                                                | :heavy_minus_sign:                                                              | The new autoHideDoc boolean the policy will be updated to if provided.          |
| `report_name`                                                                   | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | The new name of the policy if provided.                                         |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.UpdateDlpReportResponse](../../models/updatedlpreportresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## list

Lists policies with filtering.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    security=models.Security(
        act_as_bearer_token=os.getenv("GLEAN_ACT_AS_BEARER_TOKEN", ""),
    ),
) as g_client:

    res = g_client.client.governance.data.policies.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `auto_hide`                                                         | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Filter to return reports with a given value of auto-hide.           |
| `frequency`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Filter to return reports with a given frequency.                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListDlpReportsResponse](../../models/listdlpreportsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## create

Creates a new policy with specified specifications and returns its id.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    security=models.Security(
        act_as_bearer_token=os.getenv("GLEAN_ACT_AS_BEARER_TOKEN", ""),
    ),
) as g_client:

    res = g_client.client.governance.data.policies.create()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.CreateDlpReportRequest](../../models/createdlpreportrequest.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.CreateDlpReportResponse](../../models/createdlpreportresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## download

Downloads CSV violations report for a specific policy id. This does not support continuous policies.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    security=models.Security(
        act_as_bearer_token=os.getenv("GLEAN_ACT_AS_BEARER_TOKEN", ""),
    ),
) as g_client:

    res = g_client.client.governance.data.policies.download(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The id of the policy to download violations for.                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[str](../../models/.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |