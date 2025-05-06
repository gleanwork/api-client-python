# IndexingShortcuts
(*indexing.shortcuts*)

## Overview

### Available Operations

* [bulk_index](#bulk_index) - Bulk index external shortcuts
* [upload](#upload) - Upload shortcuts

## bulk_index

Replaces all the currently indexed shortcuts using paginated batch API calls. Note that this endpoint is used for indexing shortcuts not hosted by Glean. If you want to upload shortcuts that would be hosted by Glean, please use the `/uploadshortcuts` endpoint. For information on what you can do with Golinks, which are Glean-hosted shortcuts, please refer to [this](https://help.glean.com/en/articles/5628838-how-go-links-work) page.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    g_client.indexing.shortcuts.bulk_index(upload_id="<id>", shortcuts=[
        {
            "input_alias": "<value>",
            "destination_url": "https://only-juggernaut.com/",
            "created_by": "<value>",
            "intermediate_url": "https://descriptive-electronics.name",
        },
    ])

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `upload_id`                                                                                              | *str*                                                                                                    | :heavy_check_mark:                                                                                       | Unique id that must be used for this bulk upload instance                                                |
| `shortcuts`                                                                                              | List[[models.ExternalShortcut](../../models/externalshortcut.md)]                                        | :heavy_check_mark:                                                                                       | Batch of shortcuts information                                                                           |
| `is_first_page`                                                                                          | *Optional[bool]*                                                                                         | :heavy_minus_sign:                                                                                       | true if this is the first page of the upload. Defaults to false                                          |
| `is_last_page`                                                                                           | *Optional[bool]*                                                                                         | :heavy_minus_sign:                                                                                       | true if this is the last page of the upload. Defaults to false                                           |
| `force_restart_upload`                                                                                   | *Optional[bool]*                                                                                         | :heavy_minus_sign:                                                                                       | Flag to discard previous upload attempts and start from scratch. Must be specified with isFirstPage=true |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## upload

Creates glean shortcuts for uploaded shortcuts info. Glean would host the shortcuts, and they can be managed in the knowledge tab once uploaded.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    g_client.indexing.shortcuts.upload(upload_id="<id>", shortcuts=[
        {
            "input_alias": "<value>",
            "destination_url": "https://needy-harp.name",
            "created_by": "<value>",
        },
    ])

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `upload_id`                                                                                              | *str*                                                                                                    | :heavy_check_mark:                                                                                       | Unique id that must be used for this bulk upload instance                                                |
| `shortcuts`                                                                                              | List[[models.IndexingShortcut](../../models/indexingshortcut.md)]                                        | :heavy_check_mark:                                                                                       | Batch of shortcuts information                                                                           |
| `is_first_page`                                                                                          | *Optional[bool]*                                                                                         | :heavy_minus_sign:                                                                                       | true if this is the first page of the upload. Defaults to false                                          |
| `is_last_page`                                                                                           | *Optional[bool]*                                                                                         | :heavy_minus_sign:                                                                                       | true if this is the last page of the upload. Defaults to false                                           |
| `force_restart_upload`                                                                                   | *Optional[bool]*                                                                                         | :heavy_minus_sign:                                                                                       | Flag to discard previous upload attempts and start from scratch. Must be specified with isFirstPage=true |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |