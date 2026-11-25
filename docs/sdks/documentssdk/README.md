# Documents

## Overview

### Available Operations

* [get_by_url](#get_by_url) - Get document by URL
* [get_by_id](#get_by_id) - Get document by ID
* [batch](#batch) - Batch get documents

## get_by_url

Retrieve one permission-visible indexed document by URL. The url is the lookup key that Platform search returns. Many URLs can resolve to one document. The response is a single document, not a list. The returned url is the permalink and may differ from the submitted URL. Gmail and Outlook search results and chat citations carry caller-specific IDs that get document by ID cannot resolve, so retrieve them by URL here. A Gmail or Outlook URL that Platform search returned can still return 404, as it can with legacy getdocuments. Retrieving search results is best-effort parity with legacy getdocuments. Federated results and go-link shortcut documents are not retrievable in this release.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-documents-get-by-url" method="get" path="/api/documents" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN"),
) as glean:

    res = glean.documents.get_by_url(url="{url}")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         | Example                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `url`                                                                                                                               | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | URL of the document to retrieve.                                                                                                    | {url}                                                                                                                               |
| `include`                                                                                                                           | List[[models.PlatformDocumentInclude](../../models/platformdocumentinclude.md)]                                                     | :heavy_minus_sign:                                                                                                                  | Optional field groups to add to each found document. Each value only adds fields; it does not change which documents are returned.<br/> |                                                                                                                                     |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |                                                                                                                                     |

### Response

**[models.PlatformDocumentGetResponse](../../models/platformdocumentgetresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 429      | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## get_by_id

Retrieve one permission-visible indexed document by its Glean store ID. Gmail and Outlook search results and chat citations can carry caller-specific IDs that this operation cannot resolve. Try get document by URL for those documents. URL lookup does not resolve every Gmail or Outlook result.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-documents-get" method="get" path="/api/documents/{document_id}" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN"),
) as glean:

    res = glean.documents.get_by_id(document_id="{document_id}")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         | Example                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `document_id`                                                                                                                       | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | Indexed Glean store ID. For a Gmail or Outlook citation with a caller-specific ID, try get document by URL instead.<br/>            | {document_id}                                                                                                                       |
| `include`                                                                                                                           | List[[models.PlatformDocumentInclude](../../models/platformdocumentinclude.md)]                                                     | :heavy_minus_sign:                                                                                                                  | Optional field groups to add to each found document. Each value only adds fields; it does not change which documents are returned.<br/> |                                                                                                                                     |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |                                                                                                                                     |

### Response

**[models.PlatformDocumentGetResponse](../../models/platformdocumentgetresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 429      | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## batch

Retrieve up to 100 permission-visible indexed documents by URL or document_id. Found items are in results. Complete misses are warnings correlated by index. Incomplete store work fails the whole request. Retrieving search results is best-effort parity with legacy getdocuments. Gmail and Outlook caller-specific citation IDs are not accepted as document_id selectors. Use URL selectors for them. A Gmail or Outlook URL can still return a resource_not_found warning. Federated results and go-link shortcut documents are not retrievable in this release.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-documents-batch" method="post" path="/api/documents/batch" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN"),
) as glean:

    res = glean.documents.batch(document_specs=[
        {
            "document_id": "{document_id}",
        },
        {
            "url": "https://company.atlassian.net/wiki/spaces/ENG/pages/12345",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                | Type                                                                                                                                                                                     | Required                                                                                                                                                                                 | Description                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `document_specs`                                                                                                                                                                         | List[[models.PlatformDocumentsBatchRequestDocumentSpec](../../models/platformdocumentsbatchrequestdocumentspec.md)]                                                                      | :heavy_check_mark:                                                                                                                                                                       | Selectors to retrieve. Each item is exactly one of document_id or url.                                                                                                                   |
| `include`                                                                                                                                                                                | List[[models.PlatformDocumentInclude](../../models/platformdocumentinclude.md)]                                                                                                          | :heavy_minus_sign:                                                                                                                                                                       | Optional field groups applied to every document in results. CONTENT adds content to every found document. Each value only adds fields; it does not change which documents are returned.<br/> |
| `retries`                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                      |

### Response

**[models.PlatformDocumentsBatchResponse](../../models/platformdocumentsbatchresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 413, 429 | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |