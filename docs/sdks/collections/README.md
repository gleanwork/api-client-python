# Collections
(*client.collections*)

## Overview

### Available Operations

* [add_items](#add_items) - Add Collection item
* [create](#create) - Create Collection
* [delete](#delete) - Delete Collection
* [delete_item](#delete_item) - Delete Collection item
* [update](#update) - Update Collection
* [edit_item](#edit_item) - Update Collection item
* [get](#get) - Read Collection
* [list](#list) - List Collections

## add_items

Add items to a Collection.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.collections.add_items(collection_id=6460.15)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `collection_id`                                                                                                          | *float*                                                                                                                  | :heavy_check_mark:                                                                                                       | The ID of the Collection to add items to.                                                                                |
| `x_glean_act_as`                                                                                                         | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `added_collection_item_descriptors`                                                                                      | List[[models.CollectionItemDescriptor](../../models/collectionitemdescriptor.md)]                                        | :heavy_minus_sign:                                                                                                       | The CollectionItemDescriptors of the items being added.                                                                  |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.AddCollectionItemsResponse](../../models/addcollectionitemsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## create

Create a publicly visible (empty) Collection of documents.

### Example Usage

```python
from datetime import date
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.collections.create(name="<value>", added_roles=[
        models.UserRoleSpecification(
            person=models.Person(
                name="George Clooney",
                obfuscated_id="abc123",
                related_documents=[],
                metadata=models.PersonMetadata(
                    type=models.PersonMetadataType.FULL_TIME,
                    title="Actor",
                    department="Movies",
                    email="george@example.com",
                    location="Hollywood, CA",
                    phone="6505551234",
                    photo_url="https://example.com/george.jpg",
                    start_date=date.fromisoformat("2000-01-23"),
                    datasource_profile=[
                        models.DatasourceProfile(
                            datasource="github",
                            handle="<value>",
                        ),
                    ],
                    query_suggestions=models.QuerySuggestionList(
                        suggestions=[],
                    ),
                    invite_info=models.InviteInfo(
                        invites=[],
                    ),
                    custom_fields=[],
                    badges=[
                        models.Badge(
                            key="deployment_name_new_hire",
                            display_name="New hire",
                            icon_config=models.IconConfig(
                                color="#343CED",
                                key="person_icon",
                                icon_type=models.IconType.GLYPH,
                                name="user",
                            ),
                        ),
                    ],
                ),
            ),
            role=models.UserRole.OWNER,
        ),
        models.UserRoleSpecification(
            role=models.UserRole.VERIFIER,
        ),
    ], removed_roles=[
        models.UserRoleSpecification(
            person=models.Person(
                name="George Clooney",
                obfuscated_id="abc123",
                metadata=models.PersonMetadata(
                    type=models.PersonMetadataType.FULL_TIME,
                    title="Actor",
                    department="Movies",
                    email="george@example.com",
                    location="Hollywood, CA",
                    phone="6505551234",
                    photo_url="https://example.com/george.jpg",
                    start_date=date.fromisoformat("2000-01-23"),
                    datasource_profile=[
                        models.DatasourceProfile(
                            datasource="github",
                            handle="<value>",
                        ),
                    ],
                    query_suggestions=models.QuerySuggestionList(),
                    invite_info=models.InviteInfo(),
                    badges=[
                        models.Badge(
                            key="deployment_name_new_hire",
                            display_name="New hire",
                            icon_config=models.IconConfig(
                                color="#343CED",
                                key="person_icon",
                                icon_type=models.IconType.GLYPH,
                                name="user",
                            ),
                        ),
                    ],
                ),
            ),
            role=models.UserRole.VERIFIER,
        ),
        models.UserRoleSpecification(
            role=models.UserRole.ANSWER_MODERATOR,
        ),
        models.UserRoleSpecification(
            role=models.UserRole.OWNER,
        ),
    ], audience_filters=[
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

| Parameter                                                                                                                                                 | Type                                                                                                                                                      | Required                                                                                                                                                  | Description                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                                                    | *str*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                        | The unique name of the Collection.                                                                                                                        |
| `x_glean_act_as`                                                                                                                                          | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).                                  |
| `x_glean_auth_type`                                                                                                                                       | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                                                 |
| `description`                                                                                                                                             | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | A brief summary of the Collection's contents.                                                                                                             |
| `added_roles`                                                                                                                                             | List[[models.UserRoleSpecification](../../models/userrolespecification.md)]                                                                               | :heavy_minus_sign:                                                                                                                                        | A list of added user roles for the Collection.                                                                                                            |
| `removed_roles`                                                                                                                                           | List[[models.UserRoleSpecification](../../models/userrolespecification.md)]                                                                               | :heavy_minus_sign:                                                                                                                                        | A list of removed user roles for the Collection.                                                                                                          |
| `audience_filters`                                                                                                                                        | List[[models.FacetFilter](../../models/facetfilter.md)]                                                                                                   | :heavy_minus_sign:                                                                                                                                        | Filters which restrict who should see this Collection. Values are taken from the corresponding filters in people search.                                  |
| `icon`                                                                                                                                                    | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | The emoji icon of this Collection.                                                                                                                        |
| `admin_locked`                                                                                                                                            | *Optional[bool]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                        | Indicates whether edits are allowed for everyone or only admins.                                                                                          |
| `parent_id`                                                                                                                                               | *Optional[int]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | The parent of this Collection, or 0 if it's a top-level Collection.                                                                                       |
| `thumbnail`                                                                                                                                               | [Optional[models.Thumbnail]](../../models/thumbnail.md)                                                                                                   | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `allowed_datasource`                                                                                                                                      | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | The datasource type this Collection can hold.                                                                                                             |
| `new_next_item_id`                                                                                                                                        | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | The (optional) ItemId of the next CollectionItem in sequence. If omitted, will be added to the end of the Collection. Only used if parentId is specified. |
| `retries`                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                          | :heavy_minus_sign:                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                       |

### Response

**[models.CreateCollectionResponse](../../models/createcollectionresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.CollectionError | 422                    | application/json       |
| errors.GleanError      | 4XX, 5XX               | \*/\*                  |

## delete

Delete a Collection given the Collection's ID.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.client.collections.delete(ids=[
        698486,
        386564,
    ])

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `ids`                                                                                                                    | List[*int*]                                                                                                              | :heavy_check_mark:                                                                                                       | The IDs of the Collections to delete.                                                                                    |
| `x_glean_act_as`                                                                                                         | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `allowed_datasource`                                                                                                     | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | The datasource allowed in the Collection to be deleted.                                                                  |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.CollectionError | 422                    | application/json       |
| errors.GleanError      | 4XX, 5XX               | \*/\*                  |

## delete_item

Delete a single item from a Collection.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.collections.delete_item(collection_id=1357.59, item_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `collection_id`                                                                                                          | *float*                                                                                                                  | :heavy_check_mark:                                                                                                       | The ID of the Collection to remove an item in.                                                                           |
| `item_id`                                                                                                                | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | The item ID of the CollectionItem to remove from this Collection.                                                        |
| `x_glean_act_as`                                                                                                         | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `document_id`                                                                                                            | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | The (optional) Glean Document ID of the CollectionItem to remove from this Collection if this is an indexed document.    |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.DeleteCollectionItemResponse](../../models/deletecollectionitemresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## update

Update the properties of an existing Collection.

### Example Usage

```python
from datetime import date
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.collections.update(name="<value>", id=720396, added_roles=[
        models.UserRoleSpecification(
            person=models.Person(
                name="George Clooney",
                obfuscated_id="abc123",
                related_documents=[],
                metadata=models.PersonMetadata(
                    type=models.PersonMetadataType.FULL_TIME,
                    title="Actor",
                    department="Movies",
                    email="george@example.com",
                    location="Hollywood, CA",
                    phone="6505551234",
                    photo_url="https://example.com/george.jpg",
                    start_date=date.fromisoformat("2000-01-23"),
                    datasource_profile=[
                        models.DatasourceProfile(
                            datasource="github",
                            handle="<value>",
                        ),
                    ],
                    query_suggestions=models.QuerySuggestionList(
                        suggestions=[],
                    ),
                    invite_info=models.InviteInfo(
                        invites=[],
                    ),
                    custom_fields=[],
                    badges=[
                        models.Badge(
                            key="deployment_name_new_hire",
                            display_name="New hire",
                            icon_config=models.IconConfig(
                                color="#343CED",
                                key="person_icon",
                                icon_type=models.IconType.GLYPH,
                                name="user",
                            ),
                        ),
                    ],
                ),
            ),
            role=models.UserRole.ANSWER_MODERATOR,
        ),
        models.UserRoleSpecification(
            role=models.UserRole.EDITOR,
        ),
        models.UserRoleSpecification(
            role=models.UserRole.ANSWER_MODERATOR,
        ),
    ], removed_roles=[
        models.UserRoleSpecification(
            person=models.Person(
                name="George Clooney",
                obfuscated_id="abc123",
                metadata=models.PersonMetadata(
                    type=models.PersonMetadataType.FULL_TIME,
                    title="Actor",
                    department="Movies",
                    email="george@example.com",
                    location="Hollywood, CA",
                    phone="6505551234",
                    photo_url="https://example.com/george.jpg",
                    start_date=date.fromisoformat("2000-01-23"),
                    datasource_profile=[
                        models.DatasourceProfile(
                            datasource="github",
                            handle="<value>",
                        ),
                    ],
                    query_suggestions=models.QuerySuggestionList(),
                    invite_info=models.InviteInfo(),
                    badges=[
                        models.Badge(
                            key="deployment_name_new_hire",
                            display_name="New hire",
                            icon_config=models.IconConfig(
                                color="#343CED",
                                key="person_icon",
                                icon_type=models.IconType.GLYPH,
                                name="user",
                            ),
                        ),
                    ],
                ),
            ),
            role=models.UserRole.ANSWER_MODERATOR,
        ),
    ], audience_filters=[
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

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `name`                                                                                                                   | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | The unique name of the Collection.                                                                                       |
| `id`                                                                                                                     | *int*                                                                                                                    | :heavy_check_mark:                                                                                                       | The ID of the Collection to modify.                                                                                      |
| `x_glean_act_as`                                                                                                         | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `description`                                                                                                            | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | A brief summary of the Collection's contents.                                                                            |
| `added_roles`                                                                                                            | List[[models.UserRoleSpecification](../../models/userrolespecification.md)]                                              | :heavy_minus_sign:                                                                                                       | A list of added user roles for the Collection.                                                                           |
| `removed_roles`                                                                                                          | List[[models.UserRoleSpecification](../../models/userrolespecification.md)]                                              | :heavy_minus_sign:                                                                                                       | A list of removed user roles for the Collection.                                                                         |
| `audience_filters`                                                                                                       | List[[models.FacetFilter](../../models/facetfilter.md)]                                                                  | :heavy_minus_sign:                                                                                                       | Filters which restrict who should see this Collection. Values are taken from the corresponding filters in people search. |
| `icon`                                                                                                                   | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | The emoji icon of this Collection.                                                                                       |
| `admin_locked`                                                                                                           | *Optional[bool]*                                                                                                         | :heavy_minus_sign:                                                                                                       | Indicates whether edits are allowed for everyone or only admins.                                                         |
| `parent_id`                                                                                                              | *Optional[int]*                                                                                                          | :heavy_minus_sign:                                                                                                       | The parent of this Collection, or 0 if it's a top-level Collection.                                                      |
| `thumbnail`                                                                                                              | [Optional[models.Thumbnail]](../../models/thumbnail.md)                                                                  | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |
| `allowed_datasource`                                                                                                     | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | The datasource type this Collection can hold.                                                                            |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.EditCollectionResponse](../../models/editcollectionresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.CollectionError | 422                    | application/json       |
| errors.GleanError      | 4XX, 5XX               | \*/\*                  |

## edit_item

Update the URL, Glean Document ID, description of an item within a Collection given its ID.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.collections.edit_item(collection_id=795203, item_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `collection_id`                                                                                                          | *int*                                                                                                                    | :heavy_check_mark:                                                                                                       | The ID of the Collection to edit CollectionItems in.                                                                     |
| `item_id`                                                                                                                | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | The ID of the CollectionItem to edit.                                                                                    |
| `x_glean_act_as`                                                                                                         | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `name`                                                                                                                   | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | The optional name of the Collection item.                                                                                |
| `description`                                                                                                            | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | A helpful description of why this CollectionItem is in the Collection that it's in.                                      |
| `icon`                                                                                                                   | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | The emoji icon for this CollectionItem. Only used for Text type items.                                                   |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.EditCollectionItemResponse](../../models/editcollectionitemresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## get

Read the details of a Collection given its ID. Does not fetch items in this Collection.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.collections.get(id=700347)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                     | Type                                                                                                                          | Required                                                                                                                      | Description                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                          | *int*                                                                                                                         | :heavy_check_mark:                                                                                                            | The ID of the Collection to be retrieved.                                                                                     |
| `x_glean_act_as`                                                                                                              | *Optional[str]*                                                                                                               | :heavy_minus_sign:                                                                                                            | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).      |
| `x_glean_auth_type`                                                                                                           | *Optional[str]*                                                                                                               | :heavy_minus_sign:                                                                                                            | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                     |
| `with_items`                                                                                                                  | *Optional[bool]*                                                                                                              | :heavy_minus_sign:                                                                                                            | Whether or not to include the Collection Items in this Collection. Only request if absolutely required, as this is expensive. |
| `with_hierarchy`                                                                                                              | *Optional[bool]*                                                                                                              | :heavy_minus_sign:                                                                                                            | Whether or not to include the top level Collection in this Collection's hierarchy.                                            |
| `allowed_datasource`                                                                                                          | *Optional[str]*                                                                                                               | :heavy_minus_sign:                                                                                                            | The datasource allowed in the Collection returned.                                                                            |
| `retries`                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                              | :heavy_minus_sign:                                                                                                            | Configuration to override the default retry behavior of the client.                                                           |

### Response

**[models.GetCollectionResponse](../../models/getcollectionresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## list

List all existing Collections.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.collections.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `x_glean_act_as`                                                                                                         | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `include_audience`                                                                                                       | *Optional[bool]*                                                                                                         | :heavy_minus_sign:                                                                                                       | Whether to include the audience filters with the listed Collections.                                                     |
| `include_roles`                                                                                                          | *Optional[bool]*                                                                                                         | :heavy_minus_sign:                                                                                                       | Whether to include the editor roles with the listed Collections.                                                         |
| `allowed_datasource`                                                                                                     | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | The datasource type this Collection can hold.<br/>ANSWERS - for Collections representing answer boards                   |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.ListCollectionsResponse](../../models/listcollectionsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |