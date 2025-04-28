# Troubleshooting
(*indexing.troubleshooting*)

## Overview

### Available Operations

* [get_datasource_status](#get_datasource_status) - Beta: Get datasource status

* [post_document_debug](#post_document_debug) - Beta: Get document information

* [post_documents_debug](#post_documents_debug) - Beta: Get information of a batch of documents

* [debug_user](#debug_user) - Beta: Get user information

* [check_access](#check_access) - Check document access
* [~~get_status~~](#get_status) - Get document upload and indexing status :warning: **Deprecated**
* [~~get_document_count~~](#get_document_count) - Get document count :warning: **Deprecated**
* [~~get_user_count~~](#get_user_count) - Get user count :warning: **Deprecated**

## get_datasource_status

Gather information about the datasource's overall status. Currently in beta, might undergo breaking changes without prior notice.

Tip: Refer to the [Troubleshooting tutorial](https://developers.glean.com/docs/indexing_api/indexing_api_troubleshooting/) for more information.


### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.indexing.troubleshooting.get_datasource_status(datasource="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The datasource to get debug status for.                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DebugDatasourceStatusResponse](../../models/debugdatasourcestatusresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## post_document_debug

Gives various information that would help in debugging related to a particular document. Currently in beta, might undergo breaking changes without prior notice.

Tip: Refer to the [Troubleshooting tutorial](https://developers.glean.com/docs/indexing_api/indexing_api_troubleshooting/) for more information.


### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.indexing.troubleshooting.post_document_debug(datasource="<value>", object_type="Article", doc_id="art123")

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

## post_documents_debug

Gives various information that would help in debugging related to a batch of documents. Currently in beta, might undergo breaking changes without prior notice.

Tip: Refer to the [Troubleshooting tutorial](https://developers.glean.com/docs/indexing_api/indexing_api_troubleshooting/) for more information.


### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.indexing.troubleshooting.post_documents_debug(datasource="<value>", debug_documents=[
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

## debug_user

Gives various information that would help in debugging related to a particular user. Currently in beta, might undergo breaking changes without prior notice.

Tip: Refer to the [Troubleshooting tutorial](https://developers.glean.com/docs/indexing_api/indexing_api_troubleshooting/) for more information.


### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.indexing.troubleshooting.debug_user(datasource="<value>", email="u1@foo.com")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The datasource to which the user belongs                            |                                                                     |
| `email`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Email ID of the user to get the status for                          | u1@foo.com                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DebugUserResponse](../../models/debuguserresponse.md)**

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
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.indexing.troubleshooting.check_access(datasource="<value>", object_type="<value>", doc_id="<id>", user_email="<value>")

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

## ~~get_status~~

Intended for debugging/validation. Fetches the current upload and indexing status of documents.

Tip: Use [/debug/{datasource}/document](https://developers.glean.com/docs/indexing_api/indexing_api_troubleshooting/#debug-datasource-document) for richer information.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.indexing.troubleshooting.get_status(datasource="<value>", object_type="<value>", doc_id="<id>")

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

## ~~get_document_count~~

Fetches document count for the specified custom datasource.

Tip: Use [/debug/{datasource}/status](https://developers.glean.com/docs/indexing_api/indexing_api_troubleshooting/#debug-datasource-status) for richer information.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.indexing.troubleshooting.get_document_count(datasource="<value>")

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

## ~~get_user_count~~

Fetches user count for the specified custom datasource.

Tip: Use [/debug/{datasource}/status](https://developers.glean.com/docs/indexing_api/indexing_api_troubleshooting/#debug-datasource-status) for richer information.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.indexing.troubleshooting.get_user_count(datasource="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Datasource name for which user count is needed.                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetUserCountResponse](../../models/getusercountresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |