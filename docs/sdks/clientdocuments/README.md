# Client.Documents

## Overview

### Available Operations

* [retrieve_permissions](#retrieve_permissions) - Read document permissions
* [retrieve](#retrieve) - Read documents
* [retrieve_by_facets](#retrieve_by_facets) - Read documents by facets
* [summarize](#summarize) - Summarize documents

## retrieve_permissions

Read the emails of all users who have access to the given document.

### Example Usage

<!-- UsageSnippet language="python" operationID="getdocpermissions" method="post" path="/rest/api/v1/getdocpermissions" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.documents.retrieve_permissions()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The Glean Document ID to retrieve permissions for.                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetDocPermissionsResponse](../../models/getdocpermissionsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## retrieve

Read the documents including metadata (does not include enhanced metadata via `/documentmetadata`) for the given list of Glean Document IDs or URLs specified in the request.

### Example Usage

<!-- UsageSnippet language="python" operationID="getdocuments" method="post" path="/rest/api/v1/getdocuments" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.documents.retrieve()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GetDocumentsRequest](../../models/getdocumentsrequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetDocumentsResponse](../../models/getdocumentsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## retrieve_by_facets

Read the documents including metadata (does not include enhanced metadata via `/documentmetadata`) macthing the given facet conditions.

### Example Usage

<!-- UsageSnippet language="python" operationID="getdocumentsbyfacets" method="post" path="/rest/api/v1/getdocumentsbyfacets" -->
```python
from glean.api_client import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.documents.retrieve_by_facets(request={
        "filter_sets": [
            {
                "filters": [
                    {
                        "field_name": "type",
                        "values": [
                            {
                                "value": "Spreadsheet",
                                "relation_type": models.RelationType.EQUALS,
                            },
                            {
                                "value": "Presentation",
                                "relation_type": models.RelationType.EQUALS,
                            },
                        ],
                    },
                ],
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.GetDocumentsByFacetsRequest](../../models/getdocumentsbyfacetsrequest.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.GetDocumentsByFacetsResponse](../../models/getdocumentsbyfacetsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## summarize

Generate an AI summary of the requested documents.

### Example Usage

<!-- UsageSnippet language="python" operationID="summarize" method="post" path="/rest/api/v1/summarize" -->
```python
from glean.api_client import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.documents.summarize(document_specs=[
        {
            "ugc_type": models.DocumentSpecUgcType2.CHATS,
            "ugc_id": "<id>",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `document_specs`                                                                            | List[[models.DocumentSpecUnion](../../models/documentspecunion.md)]                         | :heavy_check_mark:                                                                          | Specifications of documents to summarize                                                    |
| `timestamp`                                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)                        | :heavy_minus_sign:                                                                          | The ISO 8601 timestamp associated with the client request.                                  |
| `query`                                                                                     | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | Optional query that the summary should be about                                             |
| `preferred_summary_length`                                                                  | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | Optional length of summary output. If not given, defaults to 500 chars.                     |
| `tracking_token`                                                                            | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | An opaque token that represents this particular result. To be used for /feedback reporting. |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.SummarizeResponse](../../models/summarizeresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |