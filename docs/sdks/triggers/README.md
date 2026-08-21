# Triggers

## Overview

### Available Operations

* [create](#create) - Create trigger
* [list](#list) - List triggers
* [get](#get) - Get trigger
* [update](#update) - Update trigger
* [delete](#delete) - Delete trigger
* [search_events](#search_events) - Search events for a trigger
* [list_presets](#list_presets) - List trigger presets
* [get_preset](#get_preset) - Get trigger preset
* [list_preset_input_values](#list_preset_input_values) - Search trigger preset input values
* [search_preset_events](#search_preset_events) - Search events for a trigger preset

## create

Create a trigger from a preset and return it with its signing secret.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-triggers-create" method="post" path="/api/triggers" -->
```python
from glean.api_client import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.triggers.create(preset_id="GITHUB_1", delivery={
        "webhook_url": "https://customer.app/webhook",
        "auth": {
            "type": models.PlatformTriggerAuthType.BEARER,
            "secret": "secret_test_123",
        },
    }, description="Reviews I am tagged on, sent to my team's review channel", inputs={
        "repository": "acme/payments-api",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               | Example                                                                   |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `preset_id`                                                               | *str*                                                                     | :heavy_check_mark:                                                        | ID of the preset to instantiate.                                          | GITHUB_1                                                                  |
| `delivery`                                                                | [models.PlatformTriggerDelivery](../../models/platformtriggerdelivery.md) | :heavy_check_mark:                                                        | N/A                                                                       |                                                                           |
| `description`                                                             | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | Optional note describing this trigger.                                    | Reviews I am tagged on, sent to my team's review channel                  |
| `inputs`                                                                  | Dict[str, *Any*]                                                          | :heavy_minus_sign:                                                        | Values for the preset's inputs.                                           | {<br/>"repository": "acme/payments-api"<br/>}                             |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |                                                                           |

### Response

**[models.PlatformTriggerCreateResponse](../../models/platformtriggercreateresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.PlatformProblemDetailError      | 400, 401, 403, 404, 408, 409, 413, 429 | application/problem+json               |
| errors.PlatformProblemDetailError      | 500, 503                               | application/problem+json               |
| errors.GleanError                      | 4XX, 5XX                               | \*/\*                                  |

## list

List triggers owned by the authenticated caller.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-triggers-list" method="get" path="/api/triggers" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.triggers.list(page_size=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum number of triggers to return.                               |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Opaque pagination cursor from a previous response.                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlatformTriggerListResponse](../../models/platformtriggerlistresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 408, 429           | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## get

Retrieve a trigger owned by the authenticated caller.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-triggers-get" method="get" path="/api/triggers/{trigger_id}" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.triggers.get(trigger_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `trigger_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the trigger to retrieve.                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlatformTriggerGetResponse](../../models/platformtriggergetresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 429      | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## update

Update a trigger.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-triggers-update" method="patch" path="/api/triggers/{trigger_id}" -->
```python
from glean.api_client import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.triggers.update(trigger_id="<id>", status=models.PlatformTriggerStatus.ENABLED, description="Reviews I am tagged on, sent to my team's review channel", inputs={
        "repository": "acme/payments-api",
    }, delivery={
        "webhook_url": "https://customer.app/webhook",
        "auth": {
            "type": models.PlatformTriggerAuthType.BEARER,
            "secret": "secret_test_123",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         | Example                                                                             |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `trigger_id`                                                                        | *str*                                                                               | :heavy_check_mark:                                                                  | ID of the trigger to update.                                                        |                                                                                     |
| `status`                                                                            | [Optional[models.PlatformTriggerStatus]](../../models/platformtriggerstatus.md)     | :heavy_minus_sign:                                                                  | Current trigger lifecycle state.                                                    | ENABLED                                                                             |
| `description`                                                                       | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | Optional note describing this trigger.                                              | Reviews I am tagged on, sent to my team's review channel                            |
| `inputs`                                                                            | Dict[str, *Any*]                                                                    | :heavy_minus_sign:                                                                  | Values for the preset's inputs.                                                     | {<br/>"repository": "acme/payments-api"<br/>}                                       |
| `delivery`                                                                          | [Optional[models.PlatformTriggerDelivery]](../../models/platformtriggerdelivery.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |                                                                                     |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |                                                                                     |

### Response

**[models.PlatformTriggerGetResponse](../../models/platformtriggergetresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 413, 429 | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## delete

Delete a trigger.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-triggers-delete" method="delete" path="/api/triggers/{trigger_id}" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    glean.triggers.delete(trigger_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `trigger_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the trigger to delete.                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 429      | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## search_events

Search recent content events an existing trigger matches. Read-only — no webhook delivery is made. Covers the last seven days.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-triggers-events-search" method="post" path="/api/triggers/{trigger_id}/events/search" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.triggers.search_events(trigger_id="<id>", page_size=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `trigger_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | ID of the trigger whose events to search.                           |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum number of events to return.                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlatformTriggerEventSearchResponse](../../models/platformtriggereventsearchresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 413, 429 | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## list_presets

List the trigger presets available to the caller. A preset is a curated content-trigger template (e.g. a new Jira ticket) which is passed when creating a trigger.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-trigger-presets-list" method="get" path="/api/trigger-presets" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.triggers.list_presets(page_size=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Restrict results to presets for a single datasource (e.g. github).  |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum number of presets to return.                                |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Opaque pagination cursor from a previous response.                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlatformTriggerPresetListResponse](../../models/platformtriggerpresetlistresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 408, 429           | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## get_preset

Retrieve a single trigger preset by id.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-trigger-presets-get" method="get" path="/api/trigger-presets/{preset_id}" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.triggers.get_preset(preset_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `preset_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | ID of the preset to retrieve.                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlatformTriggerPresetGetResponse](../../models/platformtriggerpresetgetresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 429      | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## list_preset_input_values

Return up to 300 selectable values for a single picklist input on a preset. Results are intended for typeahead selection and are not cursor-paginated. When `is_truncated` is true, refine `query` to narrow the result set.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-trigger-presets-input-values-list" method="get" path="/api/trigger-presets/{preset_id}/input-values" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.triggers.list_preset_input_values(preset_id="<id>", field="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `preset_id`                                                                                                          | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | ID of the preset the input belongs to.                                                                               |
| `field`                                                                                                              | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | Field identifier of the input whose values to list.                                                                  |
| `query`                                                                                                              | *Optional[str]*                                                                                                      | :heavy_minus_sign:                                                                                                   | Prefix filter over the input's option values, for typeahead. Matching is on the option value, not its display name.<br/> |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |

### Response

**[models.PlatformTriggerPresetInputValueListResponse](../../models/platformtriggerpresetinputvaluelistresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 429      | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## search_preset_events

Search recent content events an unsaved trigger built from this preset would match, to preview it before creating the trigger. Read-only — no trigger is created and no webhook delivery is made. Covers the last seven days.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-trigger-presets-events-search" method="post" path="/api/trigger-presets/{preset_id}/events/search" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.triggers.search_preset_events(preset_id="<id>", inputs={
        "repository": "acme/payments-api",
    }, page_size=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `preset_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | ID of the preset to preview.                                        |                                                                     |
| `inputs`                                                            | Dict[str, *str*]                                                    | :heavy_minus_sign:                                                  | Values for the preset's input fields, keyed by field name.<br/>     | {<br/>"repository": "acme/payments-api"<br/>}                       |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum number of events to return.                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PlatformTriggerEventSearchResponse](../../models/platformtriggereventsearchresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 413, 429 | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |