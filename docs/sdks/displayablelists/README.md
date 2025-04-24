# DisplayableLists
(*client.displayable_lists*)

## Overview

### Available Operations

* [create](#create) - Create displayable lists
* [delete](#delete) - Delete displayable lists
* [get](#get) - Read displayable lists
* [update](#update) - Update displayable lists

## create

Create one or more lists that can be display on the home page.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.displayable_lists.create(items=[
        {
            "config": {
                "audience_filters": [
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
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `items`                                                                                                                  | List[[models.DisplayableList](../../models/displayablelist.md)]                                                          | :heavy_check_mark:                                                                                                       | N/A                                                                                                                      |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.CreateDisplayableListsResponse](../../models/createdisplayablelistsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## delete

Delete one or more displayable lists.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.client.displayable_lists.delete(ids=[
        698486,
        386564,
    ])

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `ids`                                                                                                                    | List[*int*]                                                                                                              | :heavy_check_mark:                                                                                                       | N/A                                                                                                                      |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## get

Read the details of the displayable lists with the given IDs.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.displayable_lists.get(ids=[
        558834,
        544221,
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `ids`                                                                                                                    | List[*int*]                                                                                                              | :heavy_check_mark:                                                                                                       | N/A                                                                                                                      |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.GetDisplayableListsResponse](../../models/getdisplayablelistsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## update

Update one or more displayable lists with all fields from request fields.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.displayable_lists.update(items=[
        {
            "config": {
                "audience_filters": [
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
        },
        {
            "config": {
                "audience_filters": [
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
        },
        {
            "config": {
                "audience_filters": [
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
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `items`                                                                                                                  | List[[models.DisplayableList](../../models/displayablelist.md)]                                                          | :heavy_check_mark:                                                                                                       | N/A                                                                                                                      |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.UpdateDisplayableListsResponse](../../models/updatedisplayablelistsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |