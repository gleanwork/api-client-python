# ClientShortcuts
(*client.shortcuts*)

## Overview

### Available Operations

* [create](#create) - Create shortcut
* [delete](#delete) - Delete shortcut
* [retrieve](#retrieve) - Read shortcut
* [list](#list) - List shortcuts
* [update](#update) - Update shortcut

## create

Create a user-generated shortcut that contains an alias and destination URL.

### Example Usage

```python
from datetime import date
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.shortcuts.create(data={
        "added_roles": [
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
        ],
        "removed_roles": [
            models.UserRoleSpecification(
                role=models.UserRole.VERIFIER,
            ),
            models.UserRoleSpecification(
                role=models.UserRole.ANSWER_MODERATOR,
            ),
            models.UserRoleSpecification(
                role=models.UserRole.OWNER,
            ),
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `data`                                                                        | [models.ShortcutMutableProperties](../../models/shortcutmutableproperties.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.CreateShortcutResponse](../../models/createshortcutresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## delete

Delete an existing user-generated shortcut.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.client.shortcuts.delete(id=545907)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | The opaque id of the user generated content.                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## retrieve

Read a particular shortcut's details given its ID.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.shortcuts.retrieve(request={
        "alias": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.GetShortcutRequestUnion](../../models/getshortcutrequestunion.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.GetShortcutResponse](../../models/getshortcutresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## list

List shortcuts editable/owned by the currently authenticated user.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.shortcuts.list(page_size=10, filters=[
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

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           | Example                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page_size`                                                                                                                                                                           | *int*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | N/A                                                                                                                                                                                   | 10                                                                                                                                                                                    |
| `include_fields`                                                                                                                                                                      | List[[models.ListShortcutsPaginatedRequestIncludeField](../../models/listshortcutspaginatedrequestincludefield.md)]                                                                   | :heavy_minus_sign:                                                                                                                                                                    | Array of fields/data to be included in response that are not included by default                                                                                                      |                                                                                                                                                                                       |
| `cursor`                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | A token specifying the position in the overall results to start at. Received from the endpoint and iterated back. Currently being used as page no (as we implement offset pagination) |                                                                                                                                                                                       |
| `filters`                                                                                                                                                                             | List[[models.FacetFilter](../../models/facetfilter.md)]                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | A list of filters for the query. An AND is assumed between different filters. We support filters on Go Link name, author, department and type.                                        |                                                                                                                                                                                       |
| `sort`                                                                                                                                                                                | [Optional[models.SortOptions]](../../models/sortoptions.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |                                                                                                                                                                                       |
| `query`                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | Search query that should be a substring in atleast one of the fields (alias , inputAlias, destinationUrl, description). Empty query does not filter shortcuts.                        |                                                                                                                                                                                       |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |                                                                                                                                                                                       |

### Response

**[models.ListShortcutsPaginatedResponse](../../models/listshortcutspaginatedresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## update

Updates the shortcut with the given ID.

### Example Usage

```python
from datetime import date
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.shortcuts.update(id=857478, added_roles=[
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
                        models.DatasourceProfile(
                            datasource="github",
                            handle="<value>",
                        ),
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
            role=models.UserRole.EDITOR,
        ),
        models.UserRoleSpecification(
            role=models.UserRole.ANSWER_MODERATOR,
        ),
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `id`                                                                                              | *int*                                                                                             | :heavy_check_mark:                                                                                | The opaque id of the user generated content.                                                      |
| `input_alias`                                                                                     | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | Link text following go/ prefix as entered by the user.                                            |
| `destination_url`                                                                                 | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | Destination URL for the shortcut.                                                                 |
| `destination_document_id`                                                                         | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | Glean Document ID for the URL, if known.                                                          |
| `description`                                                                                     | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | A short, plain text blurb to help people understand the intent of the shortcut.                   |
| `unlisted`                                                                                        | *Optional[bool]*                                                                                  | :heavy_minus_sign:                                                                                | Whether this shortcut is unlisted or not. Unlisted shortcuts are visible to author + admins only. |
| `url_template`                                                                                    | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | For variable shortcuts, contains the URL template; note, `destinationUrl` contains default URL.   |
| `added_roles`                                                                                     | List[[models.UserRoleSpecification](../../models/userrolespecification.md)]                       | :heavy_minus_sign:                                                                                | A list of user roles added for the Shortcut.                                                      |
| `removed_roles`                                                                                   | List[[models.UserRoleSpecification](../../models/userrolespecification.md)]                       | :heavy_minus_sign:                                                                                | A list of user roles removed for the Shortcut.                                                    |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.UpdateShortcutResponse](../../models/updateshortcutresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |