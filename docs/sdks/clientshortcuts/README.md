# ClientShortcuts
(*client.shortcuts*)

## Overview

### Available Operations

* [create](#create) - Create shortcut
* [delete](#delete) - Delete shortcut
* [get](#get) - Read shortcut
* [get_similar](#get_similar) - Get similar shortcuts
* [list](#list) - List shortcuts
* [preview](#preview) - Preview shortcut
* [update](#update) - Update shortcut
* [upload](#upload) - Upload shortcuts

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

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `data`                                                                                                                   | [models.ShortcutMutableProperties](../../models/shortcutmutableproperties.md)                                            | :heavy_check_mark:                                                                                                       | N/A                                                                                                                      |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

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

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                     | *int*                                                                                                                    | :heavy_check_mark:                                                                                                       | The opaque id of the user generated content.                                                                             |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## get

Read a particular shortcut's details given its ID.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.shortcuts.get(get_shortcut_request={
        "alias": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `get_shortcut_request`                                                                                                   | [models.GetShortcutRequest](../../models/getshortcutrequest.md)                                                          | :heavy_check_mark:                                                                                                       | GetShortcut request                                                                                                      |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.GetShortcutResponse](../../models/getshortcutresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## get_similar

Get shortcuts with similar aliases to a given alias.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.shortcuts.get_similar(alias="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `alias`                                                                                                                  | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | Link text following go/ prefix.                                                                                          |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.GetSimilarShortcutsResponse](../../models/getsimilarshortcutsresponse.md)**

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
| `x_scio_actas`                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).                                                              |                                                                                                                                                                                       |
| `x_glean_auth_type`                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                                                                             |                                                                                                                                                                                       |
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

## preview

Preview a shortcut that contains an alias and destination URL.

### Example Usage

```python
from datetime import date
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.shortcuts.preview(added_roles=[
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
            role=models.UserRole.VIEWER,
        ),
    ], removed_roles=[
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
                    management_chain=[],
                    phone="6505551234",
                    photo_url="https://example.com/george.jpg",
                    reports=[],
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
            role=models.UserRole.ANSWER_MODERATOR,
        ),
        models.UserRoleSpecification(
            role=models.UserRole.VERIFIER,
        ),
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `input_alias`                                                                                                            | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Link text following go/ prefix as entered by the user.                                                                   |
| `destination_url`                                                                                                        | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Destination URL for the shortcut.                                                                                        |
| `destination_document_id`                                                                                                | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Glean Document ID for the URL, if known.                                                                                 |
| `description`                                                                                                            | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | A short, plain text blurb to help people understand the intent of the shortcut.                                          |
| `unlisted`                                                                                                               | *Optional[bool]*                                                                                                         | :heavy_minus_sign:                                                                                                       | Whether this shortcut is unlisted or not. Unlisted shortcuts are visible to author + admins only.                        |
| `url_template`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | For variable shortcuts, contains the URL template; note, `destinationUrl` contains default URL.                          |
| `added_roles`                                                                                                            | List[[models.UserRoleSpecification](../../models/userrolespecification.md)]                                              | :heavy_minus_sign:                                                                                                       | A list of user roles added for the Shortcut.                                                                             |
| `removed_roles`                                                                                                          | List[[models.UserRoleSpecification](../../models/userrolespecification.md)]                                              | :heavy_minus_sign:                                                                                                       | A list of user roles removed for the Shortcut.                                                                           |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.PreviewShortcutResponse](../../models/previewshortcutresponse.md)**

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
                related_documents=[],
                metadata=models.PersonMetadata(
                    type=models.PersonMetadataType.FULL_TIME,
                    title="Actor",
                    department="Movies",
                    email="george@example.com",
                    location="Hollywood, CA",
                    management_chain=[],
                    phone="6505551234",
                    photo_url="https://example.com/george.jpg",
                    reports=[],
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
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                     | *int*                                                                                                                    | :heavy_check_mark:                                                                                                       | The opaque id of the user generated content.                                                                             |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `input_alias`                                                                                                            | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Link text following go/ prefix as entered by the user.                                                                   |
| `destination_url`                                                                                                        | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Destination URL for the shortcut.                                                                                        |
| `destination_document_id`                                                                                                | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Glean Document ID for the URL, if known.                                                                                 |
| `description`                                                                                                            | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | A short, plain text blurb to help people understand the intent of the shortcut.                                          |
| `unlisted`                                                                                                               | *Optional[bool]*                                                                                                         | :heavy_minus_sign:                                                                                                       | Whether this shortcut is unlisted or not. Unlisted shortcuts are visible to author + admins only.                        |
| `url_template`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | For variable shortcuts, contains the URL template; note, `destinationUrl` contains default URL.                          |
| `added_roles`                                                                                                            | List[[models.UserRoleSpecification](../../models/userrolespecification.md)]                                              | :heavy_minus_sign:                                                                                                       | A list of user roles added for the Shortcut.                                                                             |
| `removed_roles`                                                                                                          | List[[models.UserRoleSpecification](../../models/userrolespecification.md)]                                              | :heavy_minus_sign:                                                                                                       | A list of user roles removed for the Shortcut.                                                                           |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.UpdateShortcutResponse](../../models/updateshortcutresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## upload

Creates glean shortcuts for uploaded shortcuts info. Glean would host the shortcuts, and they can be managed in the knowledge tab once uploaded.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.client.shortcuts.upload(upload_id="<id>", shortcuts=[
        {
            "input_alias": "<value>",
            "destination_url": "https://needy-harp.name",
            "created_by": "<value>",
        },
    ])

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `upload_id`                                                                                              | *str*                                                                                                    | :heavy_check_mark:                                                                                       | Unique id that must be used for this bulk upload instance                                                |
| `shortcuts`                                                                                              | List[[models.Shortcut](../../models/shortcut.md)]                                                        | :heavy_check_mark:                                                                                       | Batch of shortcuts information                                                                           |
| `is_first_page`                                                                                          | *Optional[bool]*                                                                                         | :heavy_minus_sign:                                                                                       | true if this is the first page of the upload. Defaults to false                                          |
| `is_last_page`                                                                                           | *Optional[bool]*                                                                                         | :heavy_minus_sign:                                                                                       | true if this is the last page of the upload. Defaults to false                                           |
| `force_restart_upload`                                                                                   | *Optional[bool]*                                                                                         | :heavy_minus_sign:                                                                                       | Flag to discard previous upload attempts and start from scratch. Must be specified with isFirstPage=true |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |