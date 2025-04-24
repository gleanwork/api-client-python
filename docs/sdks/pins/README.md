# Pins
(*client.pins*)

## Overview

### Available Operations

* [edit](#edit) - Update pin
* [get](#get) - Read pin
* [list](#list) - List pins
* [create](#create) - Create pin
* [remove](#remove) - Delete pin

## edit

Update an existing user-generated pin.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.pins.edit(audience_filters=[
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

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `x_scio_actas`                                                                                                               | *Optional[str]*                                                                                                              | :heavy_minus_sign:                                                                                                           | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).     |
| `x_glean_auth_type`                                                                                                          | *Optional[str]*                                                                                                              | :heavy_minus_sign:                                                                                                           | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                    |
| `queries`                                                                                                                    | List[*str*]                                                                                                                  | :heavy_minus_sign:                                                                                                           | The query strings for which the pinned result will show.                                                                     |
| `audience_filters`                                                                                                           | List[[models.FacetFilter](../../models/facetfilter.md)]                                                                      | :heavy_minus_sign:                                                                                                           | Filters which restrict who should see the pinned document. Values are taken from the corresponding filters in people search. |
| `id`                                                                                                                         | *Optional[str]*                                                                                                              | :heavy_minus_sign:                                                                                                           | The opaque id of the pin to be edited.                                                                                       |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |

### Response

**[models.PinDocument](../../models/pindocument.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## get

Read pin details given its ID.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.pins.get()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `id`                                                                                                                     | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | The opaque id of the pin to be fetched.                                                                                  |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.GetPinResponse](../../models/getpinresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## list

Lists all pins.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.pins.list(request_body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request_body`                                                                                                           | [models.ListpinsRequestBody](../../models/listpinsrequestbody.md)                                                        | :heavy_check_mark:                                                                                                       | List pins request                                                                                                        |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.ListPinsResponse](../../models/listpinsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## create

Pin a document as a result for a given search query.Pin results that are known to be a good match.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.pins.create(audience_filters=[
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

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `x_scio_actas`                                                                                                               | *Optional[str]*                                                                                                              | :heavy_minus_sign:                                                                                                           | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).     |
| `x_glean_auth_type`                                                                                                          | *Optional[str]*                                                                                                              | :heavy_minus_sign:                                                                                                           | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                    |
| `queries`                                                                                                                    | List[*str*]                                                                                                                  | :heavy_minus_sign:                                                                                                           | The query strings for which the pinned result will show.                                                                     |
| `audience_filters`                                                                                                           | List[[models.FacetFilter](../../models/facetfilter.md)]                                                                      | :heavy_minus_sign:                                                                                                           | Filters which restrict who should see the pinned document. Values are taken from the corresponding filters in people search. |
| `document_id`                                                                                                                | *Optional[str]*                                                                                                              | :heavy_minus_sign:                                                                                                           | The document to be pinned.                                                                                                   |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |

### Response

**[models.PinDocument](../../models/pindocument.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## remove

Unpin a previously pinned result.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.client.pins.remove()

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `id`                                                                                                                     | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | The opaque id of the pin to be unpinned.                                                                                 |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |