# People
(*indexing.people*)

## Overview

### Available Operations

* [debug](#debug) - Beta: Get user information

* [~~count~~](#count) - Get user count :warning: **Deprecated**
* [index](#index) - Index employee
* [bulk_index](#bulk_index) - Bulk index employees
* [process_all_employees_and_teams](#process_all_employees_and_teams) - Schedules the processing of uploaded employees and teams
* [delete](#delete) - Delete employee
* [index_team](#index_team) - Index team
* [delete_team](#delete_team) - Delete team
* [bulk_index_teams](#bulk_index_teams) - Bulk index teams

## debug

Gives various information that would help in debugging related to a particular user. Currently in beta, might undergo breaking changes without prior notice.

Tip: Refer to the [Troubleshooting tutorial](https://developers.glean.com/docs/indexing_api/indexing_api_troubleshooting/) for more information.


### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.indexing.people.debug(datasource="<value>", email="u1@foo.com")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The datasource to which the user belongs                            |                                                                     |
| `email`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Email ID of the user to get the status for                          | u1@foo.com                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DebugUserResponse](../../models/debuguserresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## ~~count~~

Fetches user count for the specified custom datasource.

Tip: Use [/debug/{datasource}/status](https://developers.glean.com/docs/indexing_api/indexing_api_troubleshooting/#debug-datasource-status) for richer information.


> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.indexing.people.count(datasource="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Datasource name for which user count is needed.                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetUserCountResponse](../../models/getusercountresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## index

Adds an employee or updates information about an employee

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.indexing.people.index(employee={
        "email": "Santos.Turcotte@yahoo.com",
        "department": "<value>",
        "datasource_profiles": [
            {
                "datasource": "github",
                "handle": "<value>",
            },
            {
                "datasource": "github",
                "handle": "<value>",
            },
        ],
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `employee`                                                                             | [models.EmployeeInfoDefinition](../../models/employeeinfodefinition.md)                | :heavy_check_mark:                                                                     | Describes employee info                                                                |
| `version`                                                                              | *Optional[int]*                                                                        | :heavy_minus_sign:                                                                     | Version number for the employee object. If absent or 0 then no version checks are done |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## bulk_index

Replaces all the currently indexed employees using paginated batch API calls. Please refer to the [bulk indexing](https://developers.glean.com/docs/indexing_api_bulk_indexing/#bulk-upload-model) documentation for an explanation of how to use bulk endpoints.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.indexing.people.bulk_index(upload_id="<id>", employees=[])

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `upload_id`                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                   | Unique id that must be used for this bulk upload instance                                                                                                                                                                            |
| `employees`                                                                                                                                                                                                                          | List[[models.EmployeeInfoDefinition](../../models/employeeinfodefinition.md)]                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                   | Batch of employee information                                                                                                                                                                                                        |
| `is_first_page`                                                                                                                                                                                                                      | *Optional[bool]*                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                   | true if this is the first page of the upload. Defaults to false                                                                                                                                                                      |
| `is_last_page`                                                                                                                                                                                                                       | *Optional[bool]*                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                   | true if this is the last page of the upload. Defaults to false                                                                                                                                                                       |
| `force_restart_upload`                                                                                                                                                                                                               | *Optional[bool]*                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                   | Flag to discard previous upload attempts and start from scratch. Must be specified with isFirstPage=true                                                                                                                             |
| `disable_stale_data_deletion_check`                                                                                                                                                                                                  | *Optional[bool]*                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                   | True if older employee data needs to be force deleted after the upload completes. Defaults to older data being deleted only if the percentage of data being deleted is less than 20%. This must only be set when `isLastPage = true` |
| `retries`                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                  |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## process_all_employees_and_teams

Schedules the immediate processing of employees and teams uploaded through the indexing API. By default all uploaded people data will be processed asynchronously but this API can be used to schedule its processing on demand.


### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.indexing.people.process_all_employees_and_teams()

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## delete

Delete an employee. Silently succeeds if employee is not present.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.indexing.people.delete(employee_email="<value>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `employee_email`                                                                                                | *str*                                                                                                           | :heavy_check_mark:                                                                                              | The deleted employee's email                                                                                    |
| `version`                                                                                                       | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | Version number for document for optimistic concurrency control. If absent or 0 then no version checks are done. |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## index_team

Adds a team or updates information about a team

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.indexing.people.index_team(team={
        "id": "<id>",
        "name": "<value>",
        "datasource_profiles": [
            {
                "datasource": "github",
                "handle": "<value>",
            },
            {
                "datasource": "github",
                "handle": "<value>",
            },
            {
                "datasource": "github",
                "handle": "<value>",
            },
        ],
        "members": [
            {
                "email": "Rachelle20@yahoo.com",
            },
            {
                "email": "Rebeka.Gerhold@hotmail.com",
            },
            {
                "email": "Jace86@yahoo.com",
            },
        ],
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `team`                                                                             | [models.TeamInfoDefinition](../../models/teaminfodefinition.md)                    | :heavy_check_mark:                                                                 | Information about an employee's team                                               |
| `version`                                                                          | *Optional[int]*                                                                    | :heavy_minus_sign:                                                                 | Version number for the team object. If absent or 0 then no version checks are done |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## delete_team

Delete a team based on provided id.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.indexing.people.delete_team(id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The deleted team's id                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## bulk_index_teams

Replaces all the currently indexed teams using paginated batch API calls. Please refer to the [bulk indexing](https://developers.glean.com/docs/indexing_api_bulk_indexing/#bulk-upload-model) documentation for an explanation of how to use bulk endpoints.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.indexing.people.bulk_index_teams(upload_id="<id>", teams=[])

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `upload_id`                                                                                              | *str*                                                                                                    | :heavy_check_mark:                                                                                       | Unique id that must be used for this bulk upload instance                                                |
| `teams`                                                                                                  | List[[models.TeamInfoDefinition](../../models/teaminfodefinition.md)]                                    | :heavy_check_mark:                                                                                       | Batch of team information                                                                                |
| `is_first_page`                                                                                          | *Optional[bool]*                                                                                         | :heavy_minus_sign:                                                                                       | true if this is the first page of the upload. Defaults to false                                          |
| `is_last_page`                                                                                           | *Optional[bool]*                                                                                         | :heavy_minus_sign:                                                                                       | true if this is the last page of the upload. Defaults to false                                           |
| `force_restart_upload`                                                                                   | *Optional[bool]*                                                                                         | :heavy_minus_sign:                                                                                       | Flag to discard previous upload attempts and start from scratch. Must be specified with isFirstPage=true |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |