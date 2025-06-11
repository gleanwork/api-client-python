# Visibilityoverrides
(*client.governance.documents.visibilityoverrides*)

## Overview

### Available Operations

* [list](#list) - Fetches documents visibility
* [create](#create) - Hide or unhide docs

## list

Fetches the visibility override status of the documents passed.

### Example Usage

```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.governance.documents.visibilityoverrides.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `doc_ids`                                                           | List[*str*]                                                         | :heavy_minus_sign:                                                  | List of doc-ids which will have their hide status fetched.          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetDocumentVisibilityOverridesResponse](../../models/getdocumentvisibilityoverridesresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## create

Sets the visibility-override state of the documents specified, effectively hiding or un-hiding documents.

### Example Usage

```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.governance.documents.visibilityoverrides.create()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `visibility_overrides`                                                                | List[[models.DocumentVisibilityOverride](../../models/documentvisibilityoverride.md)] | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.UpdateDocumentVisibilityOverridesResponse](../../models/updatedocumentvisibilityoverridesresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |