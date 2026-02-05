# Client.Pins

## Overview

### Available Operations

* [update](#update) - Update pin
* [retrieve](#retrieve) - Read pin
* [list](#list) - List pins
* [create](#create) - Create pin
* [remove](#remove) - Delete pin

## update

Update an existing user-generated pin.

### Example Usage

<!-- UsageSnippet language="python" operationID="editpin" method="post" path="/rest/api/v1/editpin" -->
```python
from glean.api_client import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.pins.update(audience_filters=[
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
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |
| `queries`                                                                                                                                                                                           | List[*str*]                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                  | The query strings for which the pinned result will show.                                                                                                                                            |
| `audience_filters`                                                                                                                                                                                  | List[[models.FacetFilter](../../models/facetfilter.md)]                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                  | Filters which restrict who should see the pinned document. Values are taken from the corresponding filters in people search.                                                                        |
| `id`                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The opaque id of the pin to be edited.                                                                                                                                                              |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Response

**[models.PinDocument](../../models/pindocument.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## retrieve

Read pin details given its ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="getpin" method="post" path="/rest/api/v1/getpin" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.pins.retrieve()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |
| `id`                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The opaque id of the pin to be fetched.                                                                                                                                                             |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Response

**[models.GetPinResponse](../../models/getpinresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## list

Lists all pins.

### Example Usage

<!-- UsageSnippet language="python" operationID="listpins" method="post" path="/rest/api/v1/listpins" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.pins.list(request_body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request_body`                                                                                                                                                                                      | [models.ListpinsRequestBody](../../models/listpinsrequestbody.md)                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                  | List pins request                                                                                                                                                                                   |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Response

**[models.ListPinsResponse](../../models/listpinsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## create

Pin a document as a result for a given search query.Pin results that are known to be a good match.

### Example Usage

<!-- UsageSnippet language="python" operationID="pin" method="post" path="/rest/api/v1/pin" -->
```python
from glean.api_client import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.pins.create(audience_filters=[
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
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |
| `queries`                                                                                                                                                                                           | List[*str*]                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                  | The query strings for which the pinned result will show.                                                                                                                                            |
| `audience_filters`                                                                                                                                                                                  | List[[models.FacetFilter](../../models/facetfilter.md)]                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                  | Filters which restrict who should see the pinned document. Values are taken from the corresponding filters in people search.                                                                        |
| `document_id`                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The document to be pinned.                                                                                                                                                                          |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Response

**[models.PinDocument](../../models/pindocument.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## remove

Unpin a previously pinned result.

### Example Usage

<!-- UsageSnippet language="python" operationID="unpin" method="post" path="/rest/api/v1/unpin" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    glean.client.pins.remove()

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |
| `id`                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The opaque id of the pin to be unpinned.                                                                                                                                                            |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |