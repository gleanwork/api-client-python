# IndexingDocuments
(*indexing.documents*)

## Overview

### Available Operations

* [add_or_update](#add_or_update) - Index document
* [index](#index) - Index documents
* [bulk_index](#bulk_index) - Bulk index documents
* [process_all](#process_all) - Schedules the processing of uploaded documents
* [delete](#delete) - Delete document
* [debug](#debug) - Beta: Get document information

* [debug_many](#debug_many) - Beta: Get information of a batch of documents

* [check_access](#check_access) - Check document access
* [~~status~~](#status) - Get document upload and indexing status :warning: **Deprecated**
* [~~count~~](#count) - Get document count :warning: **Deprecated**

## add_or_update

Adds a document to the index or updates an existing document.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    g_client.indexing.documents.add_or_update(document=models.DocumentDefinition(
        datasource="<value>",
    ))

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `document`                                                                                                      | [models.DocumentDefinition](../../models/documentdefinition.md)                                                 | :heavy_check_mark:                                                                                              | Indexable document structure                                                                                    |
| `version`                                                                                                       | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | Version number for document for optimistic concurrency control. If absent or 0 then no version checks are done. |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## index

Adds or updates multiple documents in the index. Please refer to the [bulk indexing](https://developers.glean.com/docs/indexing_api_bulk_indexing/#choosing-indexdocuments-vs-bulkindexdocuments) documentation for an explanation of when to use this endpoint.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    g_client.indexing.documents.index(datasource="<value>", documents=[
        models.DocumentDefinition(
            datasource="<value>",
        ),
    ])

    # Use the SDK ...

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `datasource`                                                          | *str*                                                                 | :heavy_check_mark:                                                    | Datasource of the documents                                           |
| `documents`                                                           | List[[models.DocumentDefinition](../../models/documentdefinition.md)] | :heavy_check_mark:                                                    | Batch of documents being added/updated                                |
| `upload_id`                                                           | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Optional id parameter to identify and track a batch of documents.     |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## bulk_index

Replaces the documents in a datasource using paginated batch API calls. Please refer to the [bulk indexing](https://developers.glean.com/docs/indexing_api_bulk_indexing/#bulk-upload-model) documentation for an explanation of how to use bulk endpoints.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    g_client.indexing.documents.bulk_index(upload_id="<id>", datasource="<value>", documents=[
        models.DocumentDefinition(
            datasource="<value>",
        ),
    ])

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `upload_id`                                                                                                                                                                           | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | Unique id that must be used for this bulk upload instance                                                                                                                             |
| `datasource`                                                                                                                                                                          | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | Datasource of the documents                                                                                                                                                           |
| `documents`                                                                                                                                                                           | List[[models.DocumentDefinition](../../models/documentdefinition.md)]                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | Batch of documents for the datasource                                                                                                                                                 |
| `is_first_page`                                                                                                                                                                       | *Optional[bool]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | true if this is the first page of the upload. Defaults to false                                                                                                                       |
| `is_last_page`                                                                                                                                                                        | *Optional[bool]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | true if this is the last page of the upload. Defaults to false                                                                                                                        |
| `force_restart_upload`                                                                                                                                                                | *Optional[bool]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Flag to discard previous upload attempts and start from scratch. Must be specified with isFirstPage=true                                                                              |
| `disable_stale_document_deletion_check`                                                                                                                                               | *Optional[bool]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | True if older documents need to be force deleted after the upload completes. Defaults to older documents being deleted asynchronously. This must only be set when `isLastPage = true` |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## process_all

Schedules the immediate processing of documents uploaded through the indexing API. By default the uploaded documents will be processed asynchronously but this API can be used to schedule processing of all documents on demand.

If a `datasource` parameter is specified, processing is limited to that custom datasource. Without it, processing applies to all documents across all custom datasources.
#### Rate Limits
This endpoint is rate-limited to one usage every 3 hours. Exceeding this limit results in a 429 response code. Here's how the rate limit works:
1. Calling `/processalldocuments` for datasource `foo` prevents another call for `foo` for 3 hours.
2. Calling `/processalldocuments` for datasource `foo` doesn't affect immediate calls for `bar`.
3. Calling `/processalldocuments` for all datasources prevents any datasource calls for 3 hours.
4. Calling `/processalldocuments` for datasource `foo` doesn't affect immediate calls for all datasources.

For more frequent document processing, contact Glean support.


### Example Usage

```python
from glean import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    g_client.indexing.documents.process_all()

    # Use the SDK ...

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.ProcessAllDocumentsRequest](../../models/processalldocumentsrequest.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## delete

Deletes the specified document from the index. Succeeds if document is not present.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    g_client.indexing.documents.delete(datasource="<value>", object_type="<value>", id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `datasource`                                                                                                    | *str*                                                                                                           | :heavy_check_mark:                                                                                              | datasource of the document                                                                                      |
| `object_type`                                                                                                   | *str*                                                                                                           | :heavy_check_mark:                                                                                              | object type of the document                                                                                     |
| `id`                                                                                                            | *str*                                                                                                           | :heavy_check_mark:                                                                                              | The id of the document                                                                                          |
| `version`                                                                                                       | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | Version number for document for optimistic concurrency control. If absent or 0 then no version checks are done. |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## debug

Gives various information that would help in debugging related to a particular document. Currently in beta, might undergo breaking changes without prior notice.

Tip: Refer to the [Troubleshooting tutorial](https://developers.glean.com/docs/indexing_api/indexing_api_troubleshooting/) for more information.


### Example Usage

```python
from glean import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.indexing.documents.debug(datasource="<value>", object_type="Article", doc_id="art123")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The datasource to which the document belongs                        |                                                                     |
| `object_type`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Object type of the document to get the status for.                  | Article                                                             |
| `doc_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | Glean Document ID within the datasource to get the status for.      | art123                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DebugDocumentResponse](../../models/debugdocumentresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## debug_many

Gives various information that would help in debugging related to a batch of documents. Currently in beta, might undergo breaking changes without prior notice.

Tip: Refer to the [Troubleshooting tutorial](https://developers.glean.com/docs/indexing_api/indexing_api_troubleshooting/) for more information.


### Example Usage

```python
from glean import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.indexing.documents.debug_many(datasource="<value>", debug_documents=[
        {
            "object_type": "Article",
            "doc_id": "art123",
        },
        {
            "object_type": "Article",
            "doc_id": "art123",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `datasource`                                                              | *str*                                                                     | :heavy_check_mark:                                                        | The datasource to which the document belongs                              |
| `debug_documents`                                                         | List[[models.DebugDocumentRequest](../../models/debugdocumentrequest.md)] | :heavy_check_mark:                                                        | Documents to fetch debug information for                                  |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.DebugDocumentsResponse](../../models/debugdocumentsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## check_access

Check if a given user has access to access a document in a custom datasource

Tip: Refer to the [Troubleshooting tutorial](https://developers.glean.com/docs/indexing_api/indexing_api_troubleshooting/) for more information.


### Example Usage

```python
from glean import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.indexing.documents.check_access(datasource="<value>", object_type="<value>", doc_id="<id>", user_email="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Datasource of document to check access for.                         |
| `object_type`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Object type of document to check access for.                        |
| `doc_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | Glean Document ID to check access for.                              |
| `user_email`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Email of user to check access for.                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CheckDocumentAccessResponse](../../models/checkdocumentaccessresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## ~~status~~

Intended for debugging/validation. Fetches the current upload and indexing status of documents.

Tip: Use [/debug/{datasource}/document](https://developers.glean.com/docs/indexing_api/indexing_api_troubleshooting/#debug-datasource-document) for richer information.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.indexing.documents.status(datasource="<value>", object_type="<value>", doc_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Datasource to get fetch document status for                         |
| `object_type`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Object type of the document to get the status for                   |
| `doc_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | Glean Document ID within the datasource to get the status for.      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetDocumentStatusResponse](../../models/getdocumentstatusresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## ~~count~~

Fetches document count for the specified custom datasource.

Tip: Use [/debug/{datasource}/status](https://developers.glean.com/docs/indexing_api/indexing_api_troubleshooting/#debug-datasource-status) for richer information.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.indexing.documents.count(datasource="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Datasource name for which document count is needed.                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetDocumentCountResponse](../../models/getdocumentcountresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |