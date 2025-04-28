# IndexingPermissions
(*indexing.permissions*)

## Overview

### Available Operations

* [update_permissions](#update_permissions) - Update document permissions
* [index_user](#index_user) - Index user
* [bulk_index_users](#bulk_index_users) - Bulk index users
* [index_group](#index_group) - Index group
* [bulk_index_groups](#bulk_index_groups) - Bulk index groups
* [index_membership](#index_membership) - Index membership
* [bulk_index_memberships](#bulk_index_memberships) - Bulk index memberships for a group
* [process_memberships](#process_memberships) - Schedules the processing of group memberships
* [delete_user](#delete_user) - Delete user
* [delete_group](#delete_group) - Delete group
* [delete_membership](#delete_membership) - Delete membership
* [authorize_beta_users](#authorize_beta_users) - Beta users

## update_permissions

Updates the permissions for a given document without modifying document content.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.indexing.permissions.update_permissions(datasource="<value>", permissions={})

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                         | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `datasource`                                                                                                                      | *str*                                                                                                                             | :heavy_check_mark:                                                                                                                | N/A                                                                                                                               |
| `permissions`                                                                                                                     | [models.DocumentPermissionsDefinition](../../models/documentpermissionsdefinition.md)                                             | :heavy_check_mark:                                                                                                                | describes the access control details of the document                                                                              |
| `object_type`                                                                                                                     | *Optional[str]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | The type of the document (Case, KnowledgeArticle for Salesforce for example). It cannot have spaces or _                          |
| `id`                                                                                                                              | *Optional[str]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | The datasource specific id for the document. This field is case insensitive and should not be more than 200 characters in length. |
| `view_url`                                                                                                                        | *Optional[str]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | The permalink for viewing the document. **Note: viewURL is a required field if id was not set when uploading the document.**'<br/> |
| `retries`                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                  | :heavy_minus_sign:                                                                                                                | Configuration to override the default retry behavior of the client.                                                               |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## index_user

Adds a datasource user or updates an existing user.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.indexing.permissions.index_user(datasource="<value>", user={
        "email": "Elroy38@gmail.com",
        "name": "<value>",
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `datasource`                                                                                                    | *str*                                                                                                           | :heavy_check_mark:                                                                                              | The datasource for which the user is added                                                                      |
| `user`                                                                                                          | [models.DatasourceUserDefinition](../../models/datasourceuserdefinition.md)                                     | :heavy_check_mark:                                                                                              | describes a user in the datasource                                                                              |
| `version`                                                                                                       | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | Version number for document for optimistic concurrency control. If absent or 0 then no version checks are done. |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## bulk_index_users

Replaces the users in a datasource using paginated batch API calls. Please refer to the [bulk indexing](https://developers.glean.com/docs/indexing_api_bulk_indexing/#bulk-upload-model) documentation for an explanation of how to use bulk endpoints.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.indexing.permissions.bulk_index_users(upload_id="<id>", datasource="<value>", users=[
        {
            "email": "Nola85@hotmail.com",
            "name": "<value>",
        },
        {
            "email": "Francisca44@hotmail.com",
            "name": "<value>",
        },
        {
            "email": "Georgiana_Fadel-Boyle@yahoo.com",
            "name": "<value>",
        },
    ])

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `upload_id`                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                  | Unique id that must be used for this instance of datasource users upload                                                                                                                                                                            |
| `datasource`                                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                  | datasource of the users                                                                                                                                                                                                                             |
| `users`                                                                                                                                                                                                                                             | List[[models.DatasourceUserDefinition](../../models/datasourceuserdefinition.md)]                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                  | batch of users for the datasource                                                                                                                                                                                                                   |
| `is_first_page`                                                                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                  | true if this is the first page of the upload. Defaults to false                                                                                                                                                                                     |
| `is_last_page`                                                                                                                                                                                                                                      | *Optional[bool]*                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                  | true if this is the last page of the upload. Defaults to false                                                                                                                                                                                      |
| `force_restart_upload`                                                                                                                                                                                                                              | *Optional[bool]*                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                  | Flag to discard previous upload attempts and start from scratch. Must be specified with isFirstPage=true                                                                                                                                            |
| `disable_stale_data_deletion_check`                                                                                                                                                                                                                 | *Optional[bool]*                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                  | True if older user data needs to be force deleted after the upload completes. Defaults to older data being deleted only if the percentage of data being deleted is less than a reasonable threshold. This must only be set when `isLastPage = true` |
| `retries`                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                 |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## index_group

Add or update a group in the datasource.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.indexing.permissions.index_group(datasource="<value>", group={
        "name": "<value>",
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `datasource`                                                                                                    | *str*                                                                                                           | :heavy_check_mark:                                                                                              | The datasource for which the group is added                                                                     |
| `group`                                                                                                         | [models.DatasourceGroupDefinition](../../models/datasourcegroupdefinition.md)                                   | :heavy_check_mark:                                                                                              | describes a group in the datasource                                                                             |
| `version`                                                                                                       | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | Version number for document for optimistic concurrency control. If absent or 0 then no version checks are done. |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## bulk_index_groups

Replaces the groups in a datasource using paginated batch API calls. Please refer to the [bulk indexing](https://developers.glean.com/docs/indexing_api_bulk_indexing/#bulk-upload-model) documentation for an explanation of how to use bulk endpoints.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.indexing.permissions.bulk_index_groups(upload_id="<id>", datasource="<value>", groups=[
        {
            "name": "<value>",
        },
        {
            "name": "<value>",
        },
    ])

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `upload_id`                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                   | Unique id that must be used for this instance of datasource groups upload                                                                                                                                                                            |
| `datasource`                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                   | datasource of the groups                                                                                                                                                                                                                             |
| `groups`                                                                                                                                                                                                                                             | List[[models.DatasourceGroupDefinition](../../models/datasourcegroupdefinition.md)]                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                   | batch of groups for the datasource                                                                                                                                                                                                                   |
| `is_first_page`                                                                                                                                                                                                                                      | *Optional[bool]*                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                   | true if this is the first page of the upload. Defaults to false                                                                                                                                                                                      |
| `is_last_page`                                                                                                                                                                                                                                       | *Optional[bool]*                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                   | true if this is the last page of the upload. Defaults to false                                                                                                                                                                                       |
| `force_restart_upload`                                                                                                                                                                                                                               | *Optional[bool]*                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                   | Flag to discard previous upload attempts and start from scratch. Must be specified with isFirstPage=true                                                                                                                                             |
| `disable_stale_data_deletion_check`                                                                                                                                                                                                                  | *Optional[bool]*                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                   | True if older group data needs to be force deleted after the upload completes. Defaults to older data being deleted only if the percentage of data being deleted is less than a reasonable threshold. This must only be set when `isLastPage = true` |
| `retries`                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                  |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## index_membership

Add the memberships of a group in the datasource.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.indexing.permissions.index_membership(datasource="<value>", membership={
        "group_name": "<value>",
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `datasource`                                                                                                    | *str*                                                                                                           | :heavy_check_mark:                                                                                              | The datasource for which the membership is added                                                                |
| `membership`                                                                                                    | [models.DatasourceMembershipDefinition](../../models/datasourcemembershipdefinition.md)                         | :heavy_check_mark:                                                                                              | describes the membership row of a group. Only one of memberUserId and memberGroupName can be specified.         |
| `version`                                                                                                       | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | Version number for document for optimistic concurrency control. If absent or 0 then no version checks are done. |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## bulk_index_memberships

Replaces the memberships for a group in a datasource using paginated batch API calls. Please refer to the [bulk indexing](https://developers.glean.com/docs/indexing_api_bulk_indexing/#bulk-upload-model) documentation for an explanation of how to use bulk endpoints.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.indexing.permissions.bulk_index_memberships(upload_id="<id>", datasource="<value>", memberships=[
        {},
        {},
        {},
    ])

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `upload_id`                                                                                              | *str*                                                                                                    | :heavy_check_mark:                                                                                       | Unique id that must be used for this instance of datasource group memberships upload                     |
| `datasource`                                                                                             | *str*                                                                                                    | :heavy_check_mark:                                                                                       | datasource of the memberships                                                                            |
| `memberships`                                                                                            | List[[models.DatasourceBulkMembershipDefinition](../../models/datasourcebulkmembershipdefinition.md)]    | :heavy_check_mark:                                                                                       | batch of memberships for the group                                                                       |
| `is_first_page`                                                                                          | *Optional[bool]*                                                                                         | :heavy_minus_sign:                                                                                       | true if this is the first page of the upload. Defaults to false                                          |
| `is_last_page`                                                                                           | *Optional[bool]*                                                                                         | :heavy_minus_sign:                                                                                       | true if this is the last page of the upload. Defaults to false                                           |
| `force_restart_upload`                                                                                   | *Optional[bool]*                                                                                         | :heavy_minus_sign:                                                                                       | Flag to discard previous upload attempts and start from scratch. Must be specified with isFirstPage=true |
| `group`                                                                                                  | *Optional[str]*                                                                                          | :heavy_minus_sign:                                                                                       | group who's memberships are specified                                                                    |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## process_memberships

Schedules the immediate processing of all group memberships uploaded through the indexing API. By default the uploaded group memberships will be processed asynchronously but this API can be used to schedule processing of all memberships on demand.


### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.indexing.permissions.process_memberships()

    # Use the SDK ...

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.ProcessAllMembershipsRequest](../../models/processallmembershipsrequest.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## delete_user

Delete the user from the datasource. Silently succeeds if user is not present.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.indexing.permissions.delete_user(datasource="<value>", email="Estrella.Robel56@gmail.com")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `datasource`                                                                                                    | *str*                                                                                                           | :heavy_check_mark:                                                                                              | The datasource for which the user is removed                                                                    |
| `email`                                                                                                         | *str*                                                                                                           | :heavy_check_mark:                                                                                              | The email of the user to be deleted                                                                             |
| `version`                                                                                                       | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | Version number for document for optimistic concurrency control. If absent or 0 then no version checks are done. |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## delete_group

Delete group from the datasource. Silently succeeds if group is not present.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.indexing.permissions.delete_group(datasource="<value>", group_name="<value>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `datasource`                                                                                                    | *str*                                                                                                           | :heavy_check_mark:                                                                                              | The datasource for which the group is removed                                                                   |
| `group_name`                                                                                                    | *str*                                                                                                           | :heavy_check_mark:                                                                                              | the name of the group to be deleted                                                                             |
| `version`                                                                                                       | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | Version number for document for optimistic concurrency control. If absent or 0 then no version checks are done. |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## delete_membership

Delete membership to a group in the specified datasource. Silently succeeds if membership is not present.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.indexing.permissions.delete_membership(datasource="<value>", membership={
        "group_name": "<value>",
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `datasource`                                                                                                    | *str*                                                                                                           | :heavy_check_mark:                                                                                              | The datasource for which the membership is removed                                                              |
| `membership`                                                                                                    | [models.DatasourceMembershipDefinition](../../models/datasourcemembershipdefinition.md)                         | :heavy_check_mark:                                                                                              | describes the membership row of a group. Only one of memberUserId and memberGroupName can be specified.         |
| `version`                                                                                                       | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | Version number for document for optimistic concurrency control. If absent or 0 then no version checks are done. |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## authorize_beta_users

Allow the datasource be visible to the specified beta users. The default behaviour is datasource being visible to all users if it is enabled and not visible to any user if it is not enabled.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.indexing.permissions.authorize_beta_users(datasource="<value>", emails=[
        "Margaret94@gmail.com",
        "Jerel_Wilkinson39@yahoo.com",
    ])

    # Use the SDK ...

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `datasource`                                                                        | *str*                                                                               | :heavy_check_mark:                                                                  | Datasource which needs to be made visible to users specified in the `emails` field. |
| `emails`                                                                            | List[*str*]                                                                         | :heavy_check_mark:                                                                  | The emails of the beta users                                                        |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |