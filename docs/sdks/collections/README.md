# Collections
(*client.collections*)

## Overview

### Available Operations

* [add_items](#add_items) - Add Collection item
* [create](#create) - Create Collection
* [delete](#delete) - Delete Collection
* [delete_item](#delete_item) - Delete Collection item
* [update](#update) - Update Collection
* [update_item](#update_item) - Update Collection item
* [retrieve](#retrieve) - Read Collection
* [list](#list) - List Collections

## add_items

Add items to a Collection.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.client.collections.add_items(collection_id=7742.68)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `collection_id`                                                                   | *float*                                                                           | :heavy_check_mark:                                                                | The ID of the Collection to add items to.                                         |
| `added_collection_item_descriptors`                                               | List[[models.CollectionItemDescriptor](../../models/collectionitemdescriptor.md)] | :heavy_minus_sign:                                                                | The CollectionItemDescriptors of the items being added.                           |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

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
from glean.utils import parse_datetime
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.client.collections.create(name="<value>", added_roles=[
        models.UserRoleSpecification(
            person=models.Person(
                name="George Clooney",
                obfuscated_id="abc123",
                related_documents=[
                    models.RelatedDocuments(
                        query_suggestion=models.QuerySuggestion(
                            query="app:github type:pull author:mortimer",
                            search_provider_info=models.SearchProviderInfo(
                                name="Google",
                                search_link_url_template="https://www.google.com/search?q={query}&hl=en",
                            ),
                            label="Mortimer's PRs",
                            datasource="github",
                            request_options=models.SearchRequestOptions(
                                datasource_filter="JIRA",
                                datasources_filter=[
                                    "JIRA",
                                ],
                                query_overrides_facet_filters=True,
                                facet_filters=[
                                    models.FacetFilter(
                                        field_name="type",
                                        values=[
                                            models.FacetFilterValue(
                                                value="Spreadsheet",
                                                relation_type=models.RelationType.EQUALS,
                                            ),
                                            models.FacetFilterValue(
                                                value="Presentation",
                                                relation_type=models.RelationType.EQUALS,
                                            ),
                                        ],
                                    ),
                                ],
                                facet_filter_sets=[
                                    models.FacetFilterSet(
                                        filters=[
                                            models.FacetFilter(
                                                field_name="type",
                                                values=[
                                                    models.FacetFilterValue(
                                                        value="Spreadsheet",
                                                        relation_type=models.RelationType.EQUALS,
                                                    ),
                                                    models.FacetFilterValue(
                                                        value="Presentation",
                                                        relation_type=models.RelationType.EQUALS,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    models.FacetFilterSet(
                                        filters=[
                                            models.FacetFilter(
                                                field_name="type",
                                                values=[
                                                    models.FacetFilterValue(
                                                        value="Spreadsheet",
                                                        relation_type=models.RelationType.EQUALS,
                                                    ),
                                                    models.FacetFilterValue(
                                                        value="Presentation",
                                                        relation_type=models.RelationType.EQUALS,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    models.FacetFilterSet(
                                        filters=[
                                            models.FacetFilter(
                                                field_name="type",
                                                values=[
                                                    models.FacetFilterValue(
                                                        value="Spreadsheet",
                                                        relation_type=models.RelationType.EQUALS,
                                                    ),
                                                    models.FacetFilterValue(
                                                        value="Presentation",
                                                        relation_type=models.RelationType.EQUALS,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                facet_bucket_size=977077,
                                auth_tokens=[
                                    models.AuthToken(
                                        access_token="123abc",
                                        datasource="gmail",
                                        scope="email profile https://www.googleapis.com/auth/gmail.readonly",
                                        token_type="Bearer",
                                        auth_user="1",
                                    ),
                                ],
                            ),
                            ranges=[
                                models.TextRange(
                                    start_index=86650,
                                    document=models.Document(
                                        metadata=models.DocumentMetadata(
                                            datasource="datasource",
                                            object_type="Feature Request",
                                            container="container",
                                            parent_id="JIRA_EN-1337",
                                            mime_type="mimeType",
                                            document_id="documentId",
                                            create_time=parse_datetime("2000-01-23T04:56:07.000Z"),
                                            update_time=parse_datetime("2000-01-23T04:56:07.000Z"),
                                            components=[
                                                "Backend",
                                                "Networking",
                                            ],
                                            status="[\"Done\"]",
                                            pins=[
                                                models.PinDocument(
                                                    audience_filters=[
                                                        models.FacetFilter(
                                                            field_name="type",
                                                            values=[
                                                                models.FacetFilterValue(
                                                                    value="Spreadsheet",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                                models.FacetFilterValue(
                                                                    value="Presentation",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    document_id="<id>",
                                                ),
                                            ],
                                            collections=[
                                                models.Collection(
                                                    name="<value>",
                                                    description="meaty dial elegantly while react",
                                                    audience_filters=[
                                                        models.FacetFilter(
                                                            field_name="type",
                                                            values=[
                                                                models.FacetFilterValue(
                                                                    value="Spreadsheet",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                                models.FacetFilterValue(
                                                                    value="Presentation",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    id=854591,
                                                    items=[
                                                        models.CollectionItem(
                                                            collection_id=697663,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                        models.CollectionItem(
                                                            collection_id=697663,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                        models.CollectionItem(
                                                            collection_id=697663,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            interactions=models.DocumentInteractions(
                                                reacts=[
                                                    models.Reaction(),
                                                    models.Reaction(),
                                                ],
                                                shares=[
                                                    models.Share(
                                                        num_days_ago=365776,
                                                    ),
                                                    models.Share(
                                                        num_days_ago=365776,
                                                    ),
                                                    models.Share(
                                                        num_days_ago=365776,
                                                    ),
                                                ],
                                            ),
                                            verification=models.Verification(
                                                state=models.State.DEPRECATED,
                                                metadata=models.VerificationMetadata(
                                                    reminders=[
                                                        models.Reminder(
                                                            assignee=models.Person(
                                                                name="George Clooney",
                                                                obfuscated_id="abc123",
                                                            ),
                                                            remind_at=268615,
                                                        ),
                                                    ],
                                                    last_reminder=models.Reminder(
                                                        assignee=models.Person(
                                                            name="George Clooney",
                                                            obfuscated_id="abc123",
                                                        ),
                                                        remind_at=423482,
                                                    ),
                                                ),
                                            ),
                                            shortcuts=[
                                                models.Shortcut(
                                                    input_alias="<value>",
                                                ),
                                                models.Shortcut(
                                                    input_alias="<value>",
                                                ),
                                                models.Shortcut(
                                                    input_alias="<value>",
                                                ),
                                            ],
                                            custom_data={
                                                "someCustomField": models.CustomDataValue(),
                                            },
                                        ),
                                    ),
                                ),
                            ],
                            input_details=models.SearchRequestInputDetails(
                                has_copy_paste=True,
                            ),
                        ),
                        results=[
                            models.SearchResult(
                                title="title",
                                url="https://example.com/foo/bar",
                                native_app_url="slack://foo/bar",
                                snippets=[
                                    models.SearchResultSnippet(
                                        snippet="snippet",
                                        mime_type="mimeType",
                                    ),
                                ],
                            ),
                        ],
                    ),
                    models.RelatedDocuments(
                        query_suggestion=models.QuerySuggestion(
                            query="app:github type:pull author:mortimer",
                            search_provider_info=models.SearchProviderInfo(
                                name="Google",
                                search_link_url_template="https://www.google.com/search?q={query}&hl=en",
                            ),
                            label="Mortimer's PRs",
                            datasource="github",
                            request_options=models.SearchRequestOptions(
                                datasource_filter="JIRA",
                                datasources_filter=[
                                    "JIRA",
                                ],
                                query_overrides_facet_filters=True,
                                facet_filters=[
                                    models.FacetFilter(
                                        field_name="type",
                                        values=[
                                            models.FacetFilterValue(
                                                value="Spreadsheet",
                                                relation_type=models.RelationType.EQUALS,
                                            ),
                                            models.FacetFilterValue(
                                                value="Presentation",
                                                relation_type=models.RelationType.EQUALS,
                                            ),
                                        ],
                                    ),
                                ],
                                facet_filter_sets=[
                                    models.FacetFilterSet(
                                        filters=[
                                            models.FacetFilter(
                                                field_name="type",
                                                values=[
                                                    models.FacetFilterValue(
                                                        value="Spreadsheet",
                                                        relation_type=models.RelationType.EQUALS,
                                                    ),
                                                    models.FacetFilterValue(
                                                        value="Presentation",
                                                        relation_type=models.RelationType.EQUALS,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    models.FacetFilterSet(
                                        filters=[
                                            models.FacetFilter(
                                                field_name="type",
                                                values=[
                                                    models.FacetFilterValue(
                                                        value="Spreadsheet",
                                                        relation_type=models.RelationType.EQUALS,
                                                    ),
                                                    models.FacetFilterValue(
                                                        value="Presentation",
                                                        relation_type=models.RelationType.EQUALS,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    models.FacetFilterSet(
                                        filters=[
                                            models.FacetFilter(
                                                field_name="type",
                                                values=[
                                                    models.FacetFilterValue(
                                                        value="Spreadsheet",
                                                        relation_type=models.RelationType.EQUALS,
                                                    ),
                                                    models.FacetFilterValue(
                                                        value="Presentation",
                                                        relation_type=models.RelationType.EQUALS,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                facet_bucket_size=977077,
                                auth_tokens=[
                                    models.AuthToken(
                                        access_token="123abc",
                                        datasource="gmail",
                                        scope="email profile https://www.googleapis.com/auth/gmail.readonly",
                                        token_type="Bearer",
                                        auth_user="1",
                                    ),
                                ],
                            ),
                            ranges=[
                                models.TextRange(
                                    start_index=86650,
                                    document=models.Document(
                                        metadata=models.DocumentMetadata(
                                            datasource="datasource",
                                            object_type="Feature Request",
                                            container="container",
                                            parent_id="JIRA_EN-1337",
                                            mime_type="mimeType",
                                            document_id="documentId",
                                            create_time=parse_datetime("2000-01-23T04:56:07.000Z"),
                                            update_time=parse_datetime("2000-01-23T04:56:07.000Z"),
                                            components=[
                                                "Backend",
                                                "Networking",
                                            ],
                                            status="[\"Done\"]",
                                            pins=[
                                                models.PinDocument(
                                                    audience_filters=[
                                                        models.FacetFilter(
                                                            field_name="type",
                                                            values=[
                                                                models.FacetFilterValue(
                                                                    value="Spreadsheet",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                                models.FacetFilterValue(
                                                                    value="Presentation",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    document_id="<id>",
                                                ),
                                            ],
                                            collections=[
                                                models.Collection(
                                                    name="<value>",
                                                    description="meaty dial elegantly while react",
                                                    audience_filters=[
                                                        models.FacetFilter(
                                                            field_name="type",
                                                            values=[
                                                                models.FacetFilterValue(
                                                                    value="Spreadsheet",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                                models.FacetFilterValue(
                                                                    value="Presentation",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    id=854591,
                                                    items=[
                                                        models.CollectionItem(
                                                            collection_id=697663,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                        models.CollectionItem(
                                                            collection_id=697663,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                        models.CollectionItem(
                                                            collection_id=697663,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            interactions=models.DocumentInteractions(
                                                reacts=[
                                                    models.Reaction(),
                                                    models.Reaction(),
                                                ],
                                                shares=[
                                                    models.Share(
                                                        num_days_ago=365776,
                                                    ),
                                                    models.Share(
                                                        num_days_ago=365776,
                                                    ),
                                                    models.Share(
                                                        num_days_ago=365776,
                                                    ),
                                                ],
                                            ),
                                            verification=models.Verification(
                                                state=models.State.DEPRECATED,
                                                metadata=models.VerificationMetadata(
                                                    reminders=[
                                                        models.Reminder(
                                                            assignee=models.Person(
                                                                name="George Clooney",
                                                                obfuscated_id="abc123",
                                                            ),
                                                            remind_at=268615,
                                                        ),
                                                    ],
                                                    last_reminder=models.Reminder(
                                                        assignee=models.Person(
                                                            name="George Clooney",
                                                            obfuscated_id="abc123",
                                                        ),
                                                        remind_at=423482,
                                                    ),
                                                ),
                                            ),
                                            shortcuts=[
                                                models.Shortcut(
                                                    input_alias="<value>",
                                                ),
                                                models.Shortcut(
                                                    input_alias="<value>",
                                                ),
                                                models.Shortcut(
                                                    input_alias="<value>",
                                                ),
                                            ],
                                            custom_data={
                                                "someCustomField": models.CustomDataValue(),
                                            },
                                        ),
                                    ),
                                ),
                            ],
                            input_details=models.SearchRequestInputDetails(
                                has_copy_paste=True,
                            ),
                        ),
                        results=[
                            models.SearchResult(
                                title="title",
                                url="https://example.com/foo/bar",
                                native_app_url="slack://foo/bar",
                                snippets=[
                                    models.SearchResultSnippet(
                                        snippet="snippet",
                                        mime_type="mimeType",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
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
                        models.DatasourceProfile(
                            datasource="github",
                            handle="<value>",
                        ),
                    ],
                    query_suggestions=models.QuerySuggestionList(
                        suggestions=[
                            models.QuerySuggestion(
                                query="app:github type:pull author:mortimer",
                                label="Mortimer's PRs",
                                datasource="github",
                            ),
                        ],
                    ),
                    invite_info=models.InviteInfo(
                        invites=[
                            models.ChannelInviteInfo(),
                            models.ChannelInviteInfo(),
                        ],
                    ),
                    custom_fields=[
                        models.CustomFieldData(
                            label="<value>",
                            values=[
                                models.CustomFieldValueStr(),
                                models.CustomFieldValueStr(),
                                models.CustomFieldValueStr(),
                            ],
                        ),
                        models.CustomFieldData(
                            label="<value>",
                            values=[
                                models.CustomFieldValueStr(),
                                models.CustomFieldValueStr(),
                                models.CustomFieldValueStr(),
                            ],
                        ),
                    ],
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
                        models.DatasourceProfile(
                            datasource="github",
                            handle="<value>",
                        ),
                    ],
                    query_suggestions=models.QuerySuggestionList(
                        suggestions=[
                            models.QuerySuggestion(
                                query="app:github type:pull author:mortimer",
                                label="Mortimer's PRs",
                                datasource="github",
                            ),
                        ],
                    ),
                    invite_info=models.InviteInfo(
                        invites=[
                            models.ChannelInviteInfo(),
                            models.ChannelInviteInfo(),
                        ],
                    ),
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
            role=models.UserRole.VIEWER,
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
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    g_client.client.collections.delete(ids=[
        930352,
        156719,
        25102,
    ])

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ids`                                                               | List[*int*]                                                         | :heavy_check_mark:                                                  | The IDs of the Collections to delete.                               |
| `allowed_datasource`                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The datasource allowed in the Collection to be deleted.             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

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
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.client.collections.delete_item(collection_id=6980.49, item_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `collection_id`                                                                                                       | *float*                                                                                                               | :heavy_check_mark:                                                                                                    | The ID of the Collection to remove an item in.                                                                        |
| `item_id`                                                                                                             | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | The item ID of the CollectionItem to remove from this Collection.                                                     |
| `document_id`                                                                                                         | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | The (optional) Glean Document ID of the CollectionItem to remove from this Collection if this is an indexed document. |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |

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
from glean.utils import parse_datetime
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.client.collections.update(name="<value>", id=671264, added_roles=[
        models.UserRoleSpecification(
            person=models.Person(
                name="George Clooney",
                obfuscated_id="abc123",
                related_documents=[
                    models.RelatedDocuments(
                        query_suggestion=models.QuerySuggestion(
                            query="app:github type:pull author:mortimer",
                            search_provider_info=models.SearchProviderInfo(
                                name="Google",
                                search_link_url_template="https://www.google.com/search?q={query}&hl=en",
                            ),
                            label="Mortimer's PRs",
                            datasource="github",
                            request_options=models.SearchRequestOptions(
                                datasource_filter="JIRA",
                                datasources_filter=[
                                    "JIRA",
                                ],
                                query_overrides_facet_filters=True,
                                facet_filters=[
                                    models.FacetFilter(
                                        field_name="type",
                                        values=[
                                            models.FacetFilterValue(
                                                value="Spreadsheet",
                                                relation_type=models.RelationType.EQUALS,
                                            ),
                                            models.FacetFilterValue(
                                                value="Presentation",
                                                relation_type=models.RelationType.EQUALS,
                                            ),
                                        ],
                                    ),
                                ],
                                facet_filter_sets=[
                                    models.FacetFilterSet(
                                        filters=[
                                            models.FacetFilter(
                                                field_name="type",
                                                values=[
                                                    models.FacetFilterValue(
                                                        value="Spreadsheet",
                                                        relation_type=models.RelationType.EQUALS,
                                                    ),
                                                    models.FacetFilterValue(
                                                        value="Presentation",
                                                        relation_type=models.RelationType.EQUALS,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    models.FacetFilterSet(
                                        filters=[
                                            models.FacetFilter(
                                                field_name="type",
                                                values=[
                                                    models.FacetFilterValue(
                                                        value="Spreadsheet",
                                                        relation_type=models.RelationType.EQUALS,
                                                    ),
                                                    models.FacetFilterValue(
                                                        value="Presentation",
                                                        relation_type=models.RelationType.EQUALS,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                facet_bucket_size=797260,
                                auth_tokens=[
                                    models.AuthToken(
                                        access_token="123abc",
                                        datasource="gmail",
                                        scope="email profile https://www.googleapis.com/auth/gmail.readonly",
                                        token_type="Bearer",
                                        auth_user="1",
                                    ),
                                ],
                            ),
                            ranges=[
                                models.TextRange(
                                    start_index=932928,
                                    document=models.Document(
                                        metadata=models.DocumentMetadata(
                                            datasource="datasource",
                                            object_type="Feature Request",
                                            container="container",
                                            parent_id="JIRA_EN-1337",
                                            mime_type="mimeType",
                                            document_id="documentId",
                                            create_time=parse_datetime("2000-01-23T04:56:07.000Z"),
                                            update_time=parse_datetime("2000-01-23T04:56:07.000Z"),
                                            components=[
                                                "Backend",
                                                "Networking",
                                            ],
                                            status="[\"Done\"]",
                                            pins=[
                                                models.PinDocument(
                                                    audience_filters=[
                                                        models.FacetFilter(
                                                            field_name="type",
                                                            values=[
                                                                models.FacetFilterValue(
                                                                    value="Spreadsheet",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                                models.FacetFilterValue(
                                                                    value="Presentation",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    document_id="<id>",
                                                ),
                                                models.PinDocument(
                                                    audience_filters=[
                                                        models.FacetFilter(
                                                            field_name="type",
                                                            values=[
                                                                models.FacetFilterValue(
                                                                    value="Spreadsheet",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                                models.FacetFilterValue(
                                                                    value="Presentation",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    document_id="<id>",
                                                ),
                                            ],
                                            collections=[
                                                models.Collection(
                                                    name="<value>",
                                                    description="how by extroverted excess kissingly scruple yearningly",
                                                    audience_filters=[
                                                        models.FacetFilter(
                                                            field_name="type",
                                                            values=[
                                                                models.FacetFilterValue(
                                                                    value="Spreadsheet",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                                models.FacetFilterValue(
                                                                    value="Presentation",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    id=416110,
                                                    items=[
                                                        models.CollectionItem(
                                                            collection_id=959645,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                        models.CollectionItem(
                                                            collection_id=959645,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                        models.CollectionItem(
                                                            collection_id=959645,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                    ],
                                                ),
                                                models.Collection(
                                                    name="<value>",
                                                    description="how by extroverted excess kissingly scruple yearningly",
                                                    audience_filters=[
                                                        models.FacetFilter(
                                                            field_name="type",
                                                            values=[
                                                                models.FacetFilterValue(
                                                                    value="Spreadsheet",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                                models.FacetFilterValue(
                                                                    value="Presentation",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    id=416110,
                                                    items=[
                                                        models.CollectionItem(
                                                            collection_id=959645,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                        models.CollectionItem(
                                                            collection_id=959645,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                        models.CollectionItem(
                                                            collection_id=959645,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            interactions=models.DocumentInteractions(
                                                reacts=[
                                                    models.Reaction(),
                                                    models.Reaction(),
                                                    models.Reaction(),
                                                ],
                                                shares=[
                                                    models.Share(
                                                        num_days_ago=927933,
                                                    ),
                                                    models.Share(
                                                        num_days_ago=927933,
                                                    ),
                                                    models.Share(
                                                        num_days_ago=927933,
                                                    ),
                                                ],
                                            ),
                                            verification=models.Verification(
                                                state=models.State.UNVERIFIED,
                                                metadata=models.VerificationMetadata(
                                                    reminders=[
                                                        models.Reminder(
                                                            assignee=models.Person(
                                                                name="George Clooney",
                                                                obfuscated_id="abc123",
                                                            ),
                                                            remind_at=353914,
                                                        ),
                                                        models.Reminder(
                                                            assignee=models.Person(
                                                                name="George Clooney",
                                                                obfuscated_id="abc123",
                                                            ),
                                                            remind_at=353914,
                                                        ),
                                                    ],
                                                    last_reminder=models.Reminder(
                                                        assignee=models.Person(
                                                            name="George Clooney",
                                                            obfuscated_id="abc123",
                                                        ),
                                                        remind_at=314497,
                                                    ),
                                                ),
                                            ),
                                            shortcuts=[
                                                models.Shortcut(
                                                    input_alias="<value>",
                                                ),
                                                models.Shortcut(
                                                    input_alias="<value>",
                                                ),
                                            ],
                                            custom_data={
                                                "someCustomField": models.CustomDataValue(),
                                            },
                                        ),
                                    ),
                                ),
                            ],
                            input_details=models.SearchRequestInputDetails(
                                has_copy_paste=True,
                            ),
                        ),
                        results=[
                            models.SearchResult(
                                title="title",
                                url="https://example.com/foo/bar",
                                native_app_url="slack://foo/bar",
                                snippets=[
                                    models.SearchResultSnippet(
                                        snippet="snippet",
                                        mime_type="mimeType",
                                    ),
                                ],
                            ),
                        ],
                    ),
                    models.RelatedDocuments(
                        query_suggestion=models.QuerySuggestion(
                            query="app:github type:pull author:mortimer",
                            search_provider_info=models.SearchProviderInfo(
                                name="Google",
                                search_link_url_template="https://www.google.com/search?q={query}&hl=en",
                            ),
                            label="Mortimer's PRs",
                            datasource="github",
                            request_options=models.SearchRequestOptions(
                                datasource_filter="JIRA",
                                datasources_filter=[
                                    "JIRA",
                                ],
                                query_overrides_facet_filters=True,
                                facet_filters=[
                                    models.FacetFilter(
                                        field_name="type",
                                        values=[
                                            models.FacetFilterValue(
                                                value="Spreadsheet",
                                                relation_type=models.RelationType.EQUALS,
                                            ),
                                            models.FacetFilterValue(
                                                value="Presentation",
                                                relation_type=models.RelationType.EQUALS,
                                            ),
                                        ],
                                    ),
                                ],
                                facet_filter_sets=[
                                    models.FacetFilterSet(
                                        filters=[
                                            models.FacetFilter(
                                                field_name="type",
                                                values=[
                                                    models.FacetFilterValue(
                                                        value="Spreadsheet",
                                                        relation_type=models.RelationType.EQUALS,
                                                    ),
                                                    models.FacetFilterValue(
                                                        value="Presentation",
                                                        relation_type=models.RelationType.EQUALS,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    models.FacetFilterSet(
                                        filters=[
                                            models.FacetFilter(
                                                field_name="type",
                                                values=[
                                                    models.FacetFilterValue(
                                                        value="Spreadsheet",
                                                        relation_type=models.RelationType.EQUALS,
                                                    ),
                                                    models.FacetFilterValue(
                                                        value="Presentation",
                                                        relation_type=models.RelationType.EQUALS,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                facet_bucket_size=797260,
                                auth_tokens=[
                                    models.AuthToken(
                                        access_token="123abc",
                                        datasource="gmail",
                                        scope="email profile https://www.googleapis.com/auth/gmail.readonly",
                                        token_type="Bearer",
                                        auth_user="1",
                                    ),
                                ],
                            ),
                            ranges=[
                                models.TextRange(
                                    start_index=932928,
                                    document=models.Document(
                                        metadata=models.DocumentMetadata(
                                            datasource="datasource",
                                            object_type="Feature Request",
                                            container="container",
                                            parent_id="JIRA_EN-1337",
                                            mime_type="mimeType",
                                            document_id="documentId",
                                            create_time=parse_datetime("2000-01-23T04:56:07.000Z"),
                                            update_time=parse_datetime("2000-01-23T04:56:07.000Z"),
                                            components=[
                                                "Backend",
                                                "Networking",
                                            ],
                                            status="[\"Done\"]",
                                            pins=[
                                                models.PinDocument(
                                                    audience_filters=[
                                                        models.FacetFilter(
                                                            field_name="type",
                                                            values=[
                                                                models.FacetFilterValue(
                                                                    value="Spreadsheet",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                                models.FacetFilterValue(
                                                                    value="Presentation",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    document_id="<id>",
                                                ),
                                                models.PinDocument(
                                                    audience_filters=[
                                                        models.FacetFilter(
                                                            field_name="type",
                                                            values=[
                                                                models.FacetFilterValue(
                                                                    value="Spreadsheet",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                                models.FacetFilterValue(
                                                                    value="Presentation",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    document_id="<id>",
                                                ),
                                            ],
                                            collections=[
                                                models.Collection(
                                                    name="<value>",
                                                    description="how by extroverted excess kissingly scruple yearningly",
                                                    audience_filters=[
                                                        models.FacetFilter(
                                                            field_name="type",
                                                            values=[
                                                                models.FacetFilterValue(
                                                                    value="Spreadsheet",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                                models.FacetFilterValue(
                                                                    value="Presentation",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    id=416110,
                                                    items=[
                                                        models.CollectionItem(
                                                            collection_id=959645,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                        models.CollectionItem(
                                                            collection_id=959645,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                        models.CollectionItem(
                                                            collection_id=959645,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                    ],
                                                ),
                                                models.Collection(
                                                    name="<value>",
                                                    description="how by extroverted excess kissingly scruple yearningly",
                                                    audience_filters=[
                                                        models.FacetFilter(
                                                            field_name="type",
                                                            values=[
                                                                models.FacetFilterValue(
                                                                    value="Spreadsheet",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                                models.FacetFilterValue(
                                                                    value="Presentation",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    id=416110,
                                                    items=[
                                                        models.CollectionItem(
                                                            collection_id=959645,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                        models.CollectionItem(
                                                            collection_id=959645,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                        models.CollectionItem(
                                                            collection_id=959645,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            interactions=models.DocumentInteractions(
                                                reacts=[
                                                    models.Reaction(),
                                                    models.Reaction(),
                                                    models.Reaction(),
                                                ],
                                                shares=[
                                                    models.Share(
                                                        num_days_ago=927933,
                                                    ),
                                                    models.Share(
                                                        num_days_ago=927933,
                                                    ),
                                                    models.Share(
                                                        num_days_ago=927933,
                                                    ),
                                                ],
                                            ),
                                            verification=models.Verification(
                                                state=models.State.UNVERIFIED,
                                                metadata=models.VerificationMetadata(
                                                    reminders=[
                                                        models.Reminder(
                                                            assignee=models.Person(
                                                                name="George Clooney",
                                                                obfuscated_id="abc123",
                                                            ),
                                                            remind_at=353914,
                                                        ),
                                                        models.Reminder(
                                                            assignee=models.Person(
                                                                name="George Clooney",
                                                                obfuscated_id="abc123",
                                                            ),
                                                            remind_at=353914,
                                                        ),
                                                    ],
                                                    last_reminder=models.Reminder(
                                                        assignee=models.Person(
                                                            name="George Clooney",
                                                            obfuscated_id="abc123",
                                                        ),
                                                        remind_at=314497,
                                                    ),
                                                ),
                                            ),
                                            shortcuts=[
                                                models.Shortcut(
                                                    input_alias="<value>",
                                                ),
                                                models.Shortcut(
                                                    input_alias="<value>",
                                                ),
                                            ],
                                            custom_data={
                                                "someCustomField": models.CustomDataValue(),
                                            },
                                        ),
                                    ),
                                ),
                            ],
                            input_details=models.SearchRequestInputDetails(
                                has_copy_paste=True,
                            ),
                        ),
                        results=[
                            models.SearchResult(
                                title="title",
                                url="https://example.com/foo/bar",
                                native_app_url="slack://foo/bar",
                                snippets=[
                                    models.SearchResultSnippet(
                                        snippet="snippet",
                                        mime_type="mimeType",
                                    ),
                                ],
                            ),
                        ],
                    ),
                    models.RelatedDocuments(
                        query_suggestion=models.QuerySuggestion(
                            query="app:github type:pull author:mortimer",
                            search_provider_info=models.SearchProviderInfo(
                                name="Google",
                                search_link_url_template="https://www.google.com/search?q={query}&hl=en",
                            ),
                            label="Mortimer's PRs",
                            datasource="github",
                            request_options=models.SearchRequestOptions(
                                datasource_filter="JIRA",
                                datasources_filter=[
                                    "JIRA",
                                ],
                                query_overrides_facet_filters=True,
                                facet_filters=[
                                    models.FacetFilter(
                                        field_name="type",
                                        values=[
                                            models.FacetFilterValue(
                                                value="Spreadsheet",
                                                relation_type=models.RelationType.EQUALS,
                                            ),
                                            models.FacetFilterValue(
                                                value="Presentation",
                                                relation_type=models.RelationType.EQUALS,
                                            ),
                                        ],
                                    ),
                                ],
                                facet_filter_sets=[
                                    models.FacetFilterSet(
                                        filters=[
                                            models.FacetFilter(
                                                field_name="type",
                                                values=[
                                                    models.FacetFilterValue(
                                                        value="Spreadsheet",
                                                        relation_type=models.RelationType.EQUALS,
                                                    ),
                                                    models.FacetFilterValue(
                                                        value="Presentation",
                                                        relation_type=models.RelationType.EQUALS,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    models.FacetFilterSet(
                                        filters=[
                                            models.FacetFilter(
                                                field_name="type",
                                                values=[
                                                    models.FacetFilterValue(
                                                        value="Spreadsheet",
                                                        relation_type=models.RelationType.EQUALS,
                                                    ),
                                                    models.FacetFilterValue(
                                                        value="Presentation",
                                                        relation_type=models.RelationType.EQUALS,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                facet_bucket_size=797260,
                                auth_tokens=[
                                    models.AuthToken(
                                        access_token="123abc",
                                        datasource="gmail",
                                        scope="email profile https://www.googleapis.com/auth/gmail.readonly",
                                        token_type="Bearer",
                                        auth_user="1",
                                    ),
                                ],
                            ),
                            ranges=[
                                models.TextRange(
                                    start_index=932928,
                                    document=models.Document(
                                        metadata=models.DocumentMetadata(
                                            datasource="datasource",
                                            object_type="Feature Request",
                                            container="container",
                                            parent_id="JIRA_EN-1337",
                                            mime_type="mimeType",
                                            document_id="documentId",
                                            create_time=parse_datetime("2000-01-23T04:56:07.000Z"),
                                            update_time=parse_datetime("2000-01-23T04:56:07.000Z"),
                                            components=[
                                                "Backend",
                                                "Networking",
                                            ],
                                            status="[\"Done\"]",
                                            pins=[
                                                models.PinDocument(
                                                    audience_filters=[
                                                        models.FacetFilter(
                                                            field_name="type",
                                                            values=[
                                                                models.FacetFilterValue(
                                                                    value="Spreadsheet",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                                models.FacetFilterValue(
                                                                    value="Presentation",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    document_id="<id>",
                                                ),
                                                models.PinDocument(
                                                    audience_filters=[
                                                        models.FacetFilter(
                                                            field_name="type",
                                                            values=[
                                                                models.FacetFilterValue(
                                                                    value="Spreadsheet",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                                models.FacetFilterValue(
                                                                    value="Presentation",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    document_id="<id>",
                                                ),
                                            ],
                                            collections=[
                                                models.Collection(
                                                    name="<value>",
                                                    description="how by extroverted excess kissingly scruple yearningly",
                                                    audience_filters=[
                                                        models.FacetFilter(
                                                            field_name="type",
                                                            values=[
                                                                models.FacetFilterValue(
                                                                    value="Spreadsheet",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                                models.FacetFilterValue(
                                                                    value="Presentation",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    id=416110,
                                                    items=[
                                                        models.CollectionItem(
                                                            collection_id=959645,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                        models.CollectionItem(
                                                            collection_id=959645,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                        models.CollectionItem(
                                                            collection_id=959645,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                    ],
                                                ),
                                                models.Collection(
                                                    name="<value>",
                                                    description="how by extroverted excess kissingly scruple yearningly",
                                                    audience_filters=[
                                                        models.FacetFilter(
                                                            field_name="type",
                                                            values=[
                                                                models.FacetFilterValue(
                                                                    value="Spreadsheet",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                                models.FacetFilterValue(
                                                                    value="Presentation",
                                                                    relation_type=models.RelationType.EQUALS,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    id=416110,
                                                    items=[
                                                        models.CollectionItem(
                                                            collection_id=959645,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                        models.CollectionItem(
                                                            collection_id=959645,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                        models.CollectionItem(
                                                            collection_id=959645,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            interactions=models.DocumentInteractions(
                                                reacts=[
                                                    models.Reaction(),
                                                    models.Reaction(),
                                                    models.Reaction(),
                                                ],
                                                shares=[
                                                    models.Share(
                                                        num_days_ago=927933,
                                                    ),
                                                    models.Share(
                                                        num_days_ago=927933,
                                                    ),
                                                    models.Share(
                                                        num_days_ago=927933,
                                                    ),
                                                ],
                                            ),
                                            verification=models.Verification(
                                                state=models.State.UNVERIFIED,
                                                metadata=models.VerificationMetadata(
                                                    reminders=[
                                                        models.Reminder(
                                                            assignee=models.Person(
                                                                name="George Clooney",
                                                                obfuscated_id="abc123",
                                                            ),
                                                            remind_at=353914,
                                                        ),
                                                        models.Reminder(
                                                            assignee=models.Person(
                                                                name="George Clooney",
                                                                obfuscated_id="abc123",
                                                            ),
                                                            remind_at=353914,
                                                        ),
                                                    ],
                                                    last_reminder=models.Reminder(
                                                        assignee=models.Person(
                                                            name="George Clooney",
                                                            obfuscated_id="abc123",
                                                        ),
                                                        remind_at=314497,
                                                    ),
                                                ),
                                            ),
                                            shortcuts=[
                                                models.Shortcut(
                                                    input_alias="<value>",
                                                ),
                                                models.Shortcut(
                                                    input_alias="<value>",
                                                ),
                                            ],
                                            custom_data={
                                                "someCustomField": models.CustomDataValue(),
                                            },
                                        ),
                                    ),
                                ),
                            ],
                            input_details=models.SearchRequestInputDetails(
                                has_copy_paste=True,
                            ),
                        ),
                        results=[
                            models.SearchResult(
                                title="title",
                                url="https://example.com/foo/bar",
                                native_app_url="slack://foo/bar",
                                snippets=[
                                    models.SearchResultSnippet(
                                        snippet="snippet",
                                        mime_type="mimeType",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
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
                        models.DatasourceProfile(
                            datasource="github",
                            handle="<value>",
                        ),
                        models.DatasourceProfile(
                            datasource="github",
                            handle="<value>",
                        ),
                    ],
                    query_suggestions=models.QuerySuggestionList(
                        suggestions=[
                            models.QuerySuggestion(
                                query="app:github type:pull author:mortimer",
                                label="Mortimer's PRs",
                                datasource="github",
                            ),
                        ],
                    ),
                    invite_info=models.InviteInfo(
                        invites=[
                            models.ChannelInviteInfo(),
                            models.ChannelInviteInfo(),
                            models.ChannelInviteInfo(),
                        ],
                    ),
                    custom_fields=[
                        models.CustomFieldData(
                            label="<value>",
                            values=[
                                models.CustomFieldValueStr(),
                                models.CustomFieldValueStr(),
                                models.CustomFieldValueStr(),
                            ],
                        ),
                    ],
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
                        models.DatasourceProfile(
                            datasource="github",
                            handle="<value>",
                        ),
                        models.DatasourceProfile(
                            datasource="github",
                            handle="<value>",
                        ),
                    ],
                    query_suggestions=models.QuerySuggestionList(
                        suggestions=[
                            models.QuerySuggestion(
                                query="app:github type:pull author:mortimer",
                                label="Mortimer's PRs",
                                datasource="github",
                            ),
                        ],
                    ),
                    invite_info=models.InviteInfo(
                        invites=[
                            models.ChannelInviteInfo(),
                            models.ChannelInviteInfo(),
                            models.ChannelInviteInfo(),
                        ],
                    ),
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

## update_item

Update the URL, Glean Document ID, description of an item within a Collection given its ID.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.client.collections.update_item(collection_id=142375, item_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `collection_id`                                                                     | *int*                                                                               | :heavy_check_mark:                                                                  | The ID of the Collection to edit CollectionItems in.                                |
| `item_id`                                                                           | *str*                                                                               | :heavy_check_mark:                                                                  | The ID of the CollectionItem to edit.                                               |
| `name`                                                                              | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | The optional name of the Collection item.                                           |
| `description`                                                                       | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | A helpful description of why this CollectionItem is in the Collection that it's in. |
| `icon`                                                                              | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | The emoji icon for this CollectionItem. Only used for Text type items.              |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.EditCollectionItemResponse](../../models/editcollectionitemresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## retrieve

Read the details of a Collection given its ID. Does not fetch items in this Collection.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.client.collections.retrieve(id=425335)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                     | Type                                                                                                                          | Required                                                                                                                      | Description                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                          | *int*                                                                                                                         | :heavy_check_mark:                                                                                                            | The ID of the Collection to be retrieved.                                                                                     |
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
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.client.collections.list(request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.ListCollectionsRequest](../../models/listcollectionsrequest.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.ListCollectionsResponse](../../models/listcollectionsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |