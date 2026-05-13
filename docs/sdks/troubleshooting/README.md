# Troubleshooting

## Overview

### Available Operations

* [post_api_index_v1_debug_datasource_document_events](#post_api_index_v1_debug_datasource_document_events) - Beta: Get document lifecycle events


## post_api_index_v1_debug_datasource_document_events

Retrieves lifecycle events for a specific document including upload time, index times and deletions. Rate limited to 1 request per minute per datasource. Currently in beta, might undergo breaking changes without prior notice.


### Example Usage

<!-- UsageSnippet language="python" operationID="post_/api/index/v1/debug/{datasource}/document/events" method="post" path="/api/index/v1/debug/{datasource}/document/events" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.troubleshooting.post_api_index_v1_debug_datasource_document_events(datasource="<value>", object_type="Article", doc_id="art123", start_date="2025-05-01", max_events=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        | Example                                                                                            |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `datasource`                                                                                       | *str*                                                                                              | :heavy_check_mark:                                                                                 | The datasource to which the document belongs                                                       |                                                                                                    |
| `object_type`                                                                                      | *str*                                                                                              | :heavy_check_mark:                                                                                 | Object type of the document to get lifecycle events for.                                           | Article                                                                                            |
| `doc_id`                                                                                           | *str*                                                                                              | :heavy_check_mark:                                                                                 | Glean Document ID within the datasource to get lifecycle events for.                               | art123                                                                                             |
| `start_date`                                                                                       | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | The start date for events to be fetched. Cannot be more than 30 days (default 7 days) in the past. | 2025-05-01                                                                                         |
| `max_events`                                                                                       | *Optional[int]*                                                                                    | :heavy_minus_sign:                                                                                 | Max number of events to be fetched. Cannot be more than 100 (default 20).                          | 50                                                                                                 |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |                                                                                                    |

### Response

**[models.DebugDocumentLifecycleResponse](../../models/debugdocumentlifecycleresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |