# Indexing.CustomMetadata

## Overview

### Available Operations

* [upsert](#upsert) - Add or update custom metadata
* [delete](#delete) - Remove custom metadata
* [get_schema](#get_schema) - Retrieve metadata schema
* [upsert_schema](#upsert_schema) - Create or update metadata schema
* [delete_schema](#delete_schema) - Remove metadata schema

## upsert

Associates custom metadata with a specific document. Custom metadata enables you to enrich documents with additional structured information that can be used for search, filtering, and faceting.

### Example Usage

<!-- UsageSnippet language="python" operationID="put_/rest/api/index/document/{docId}/custom-metadata/{groupName}" method="put" path="/rest/api/index/document/{docId}/custom-metadata/{groupName}" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.indexing.custom_metadata.upsert(doc_id="<id>", group_name="<value>", custom_metadata=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `doc_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | Unique Glean identifier of the document                             |
| `group_name`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Name of the metadata group as specified while adding schema         |
| `custom_metadata`                                                   | List[[models.CustomProperty](../../models/customproperty.md)]       | :heavy_check_mark:                                                  | Array of custom metadata key-value pairs                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.SuccessResponse](../../models/successresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrorInfoResponse | 400, 401, 404, 429       | application/json         |
| errors.ErrorInfoResponse | 500                      | application/json         |
| errors.GleanError        | 4XX, 5XX                 | \*/\*                    |

## delete

Removes all custom metadata for the specified metadata group from a document.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete_/rest/api/index/document/{docId}/custom-metadata/{groupName}" method="delete" path="/rest/api/index/document/{docId}/custom-metadata/{groupName}" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.indexing.custom_metadata.delete(doc_id="<id>", group_name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `doc_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | Unique Glean identifier of the document                             |
| `group_name`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Name of the metadata group as specified while adding schema         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.SuccessResponse](../../models/successresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrorInfoResponse | 400, 401, 404, 429       | application/json         |
| errors.ErrorInfoResponse | 500                      | application/json         |
| errors.GleanError        | 4XX, 5XX                 | \*/\*                    |

## get_schema

Retrieves the current schema definition for a metadata group.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_/rest/api/index/custom-metadata/schema/{groupName}" method="get" path="/rest/api/index/custom-metadata/schema/{groupName}" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.indexing.custom_metadata.get_schema(group_name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `group_name`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Name of the metadata group schema                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.CustomMetadataSchema](../../models/custommetadataschema.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrorInfoResponse | 401, 404, 429            | application/json         |
| errors.ErrorInfoResponse | 500                      | application/json         |
| errors.GleanError        | 4XX, 5XX                 | \*/\*                    |

## upsert_schema

Defines or updates the schema for a metadata group. Schemas should be defined before indexing metadata.

### Example Usage

<!-- UsageSnippet language="python" operationID="put_/rest/api/index/custom-metadata/schema/{groupName}" method="put" path="/rest/api/index/custom-metadata/schema/{groupName}" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.indexing.custom_metadata.upsert_schema(group_name="<value>", metadata_keys=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `group_name`                                                                                      | *str*                                                                                             | :heavy_check_mark:                                                                                | Name of the metadata group schema                                                                 |
| `metadata_keys`                                                                                   | List[[models.CustomMetadataPropertyDefinition](../../models/custommetadatapropertydefinition.md)] | :heavy_check_mark:                                                                                | Array of metadata key definitions                                                                 |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |
| `server_url`                                                                                      | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | An optional server URL to use.                                                                    |

### Response

**[models.SuccessResponse](../../models/successresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrorInfoResponse | 400, 401, 409, 429       | application/json         |
| errors.ErrorInfoResponse | 500                      | application/json         |
| errors.GleanError        | 4XX, 5XX                 | \*/\*                    |

## delete_schema

Deletes the schema definition for a metadata group. This does not delete existing metadata values on documents.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete_/rest/api/index/custom-metadata/schema/{groupName}" method="delete" path="/rest/api/index/custom-metadata/schema/{groupName}" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.indexing.custom_metadata.delete_schema(group_name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `group_name`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Name of the metadata group schema                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.SuccessResponse](../../models/successresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrorInfoResponse | 400, 401, 404, 429       | application/json         |
| errors.ErrorInfoResponse | 500                      | application/json         |
| errors.GleanError        | 4XX, 5XX                 | \*/\*                    |