# Client.Shortcuts

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

<!-- UsageSnippet language="python" operationID="createshortcut" method="post" path="/rest/api/v1/createshortcut" -->
```python
from glean.api_client import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.shortcuts.create(data={
        "added_roles": [
            models.UserRoleSpecification(
                person=models.Person(
                    name="George Clooney",
                    obfuscated_id="abc123",
                ),
                role=models.UserRole.VERIFIER,
            ),
        ],
        "removed_roles": [
            models.UserRoleSpecification(
                person=models.Person(
                    name="George Clooney",
                    obfuscated_id="abc123",
                ),
                role=models.UserRole.VIEWER,
            ),
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `data`                                                                                                                                                                                              | [models.ShortcutMutableProperties](../../models/shortcutmutableproperties.md)                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                  | N/A                                                                                                                                                                                                 |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Response

**[models.CreateShortcutResponse](../../models/createshortcutresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## delete

Delete an existing user-generated shortcut.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteshortcut" method="post" path="/rest/api/v1/deleteshortcut" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    glean.client.shortcuts.delete(id=975862)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                | *int*                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                  | The opaque id of the user generated content.                                                                                                                                                        |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## retrieve

Read a particular shortcut's details given its ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="getshortcut" method="post" path="/rest/api/v1/getshortcut" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.shortcuts.retrieve(get_shortcut_request={
        "alias": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `get_shortcut_request`                                                                                                                                                                              | [models.GetShortcutRequest](../../models/getshortcutrequest.md)                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                  | GetShortcut request                                                                                                                                                                                 |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Response

**[models.GetShortcutResponse](../../models/getshortcutresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## list

List shortcuts editable/owned by the currently authenticated user.

### Example Usage

<!-- UsageSnippet language="python" operationID="listshortcuts" method="post" path="/rest/api/v1/listshortcuts" -->
```python
from glean.api_client import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.shortcuts.list(page_size=10, filters=[
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

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         | Example                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page_size`                                                                                                                                                                                         | *int*                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                  | N/A                                                                                                                                                                                                 | 10                                                                                                                                                                                                  |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |                                                                                                                                                                                                     |
| `include_fields`                                                                                                                                                                                    | List[[models.ListShortcutsPaginatedRequestIncludeField](../../models/listshortcutspaginatedrequestincludefield.md)]                                                                                 | :heavy_minus_sign:                                                                                                                                                                                  | Array of fields/data to be included in response that are not included by default                                                                                                                    |                                                                                                                                                                                                     |
| `cursor`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | A token specifying the position in the overall results to start at. Received from the endpoint and iterated back. Currently being used as page no (as we implement offset pagination)               |                                                                                                                                                                                                     |
| `filters`                                                                                                                                                                                           | List[[models.FacetFilter](../../models/facetfilter.md)]                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                  | A list of filters for the query. An AND is assumed between different filters. We support filters on Go Link name, author, department and type.                                                      |                                                                                                                                                                                                     |
| `sort`                                                                                                                                                                                              | [Optional[models.SortOptions]](../../models/sortoptions.md)                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                  | N/A                                                                                                                                                                                                 |                                                                                                                                                                                                     |
| `query`                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | Search query that should be a substring in atleast one of the fields (alias , inputAlias, destinationUrl, description). Empty query does not filter shortcuts.                                      |                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |                                                                                                                                                                                                     |

### Response

**[models.ListShortcutsPaginatedResponse](../../models/listshortcutspaginatedresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## update

Updates the shortcut with the given ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateshortcut" method="post" path="/rest/api/v1/updateshortcut" -->
```python
from glean.api_client import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.shortcuts.update(id=268238, added_roles=[
        models.UserRoleSpecification(
            person=models.Person(
                name="George Clooney",
                obfuscated_id="abc123",
            ),
            role=models.UserRole.ANSWER_MODERATOR,
        ),
    ], removed_roles=[
        models.UserRoleSpecification(
            person=models.Person(
                name="George Clooney",
                obfuscated_id="abc123",
            ),
            role=models.UserRole.ANSWER_MODERATOR,
        ),
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                | *int*                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                  | The opaque id of the user generated content.                                                                                                                                                        |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |
| `input_alias`                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | Link text following go/ prefix as entered by the user.                                                                                                                                              |
| `destination_url`                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | Destination URL for the shortcut.                                                                                                                                                                   |
| `destination_document_id`                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | Glean Document ID for the URL, if known.                                                                                                                                                            |
| `description`                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | A short, plain text blurb to help people understand the intent of the shortcut.                                                                                                                     |
| `unlisted`                                                                                                                                                                                          | *Optional[bool]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Whether this shortcut is unlisted or not. Unlisted shortcuts are visible to author + admins only.                                                                                                   |
| `url_template`                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | For variable shortcuts, contains the URL template; note, `destinationUrl` contains default URL.                                                                                                     |
| `added_roles`                                                                                                                                                                                       | List[[models.UserRoleSpecification](../../models/userrolespecification.md)]                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                  | A list of user roles added for the Shortcut.                                                                                                                                                        |
| `removed_roles`                                                                                                                                                                                     | List[[models.UserRoleSpecification](../../models/userrolespecification.md)]                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                  | A list of user roles removed for the Shortcut.                                                                                                                                                      |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Response

**[models.UpdateShortcutResponse](../../models/updateshortcutresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |