# Users

## Overview

### Available Operations

* [list](#list) - List users
* [get](#get) - Get user

## list

List the users in the Glean directory, ordered by display_name and then by user_id. The list includes the same people as the Glean People directory. Filter by name, email, manager_id, or department_id to find specific users. Use the returned user_id values with other Platform APIs, for example as usage limit targets.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-users-list" method="get" path="/api/users" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.users.list(page_size=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page_size`                                                                                                                                                                                                                                                                                                                                                                                  | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                           | Maximum number of users to return. Defaults to 50. Maximum is 100.                                                                                                                                                                                                                                                                                                                           |
| `cursor`                                                                                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                           | Opaque pagination cursor from a previous response. Send the same filters that the previous request used.<br/>                                                                                                                                                                                                                                                                                |
| `filters`                                                                                                                                                                                                                                                                                                                                                                                    | List[[models.PlatformUserFilter](../../models/platformuserfilter.md)]                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                           | JSON-encoded filters that choose which users are returned. The supported fields are name, email, manager_id, and department_id, each with the operator EQUALS. Multiple values OR within a filter. Multiple filters AND together. Each field may appear in only one filter. A value that matches no user, such as an unknown email or department_id, returns no users rather than an error.<br/> |
| `include`                                                                                                                                                                                                                                                                                                                                                                                    | List[[models.PlatformUserInclude](../../models/platformuserinclude.md)]                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                           | Optional fields to add to each user. Each value only adds fields; it does not change which users are returned.<br/>                                                                                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                          |

### Response

**[models.PlatformListUsersResponse](../../models/platformlistusersresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 429      | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## get

Get one user in the Glean directory by user_id. The user can be any person that the list returns. A user_id that is not in the directory returns 404 resource_not_found. This includes a deleted user and a person that the People directory does not show. An alias ID of a merged person returns the person's canonical user_id.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-users-get" method="get" path="/api/users/{user_id}" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.users.get(user_id="{user_id}")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             | Example                                                                 |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `user_id`                                                               | *str*                                                                   | :heavy_check_mark:                                                      | Canonical Glean user ID, as the list returns it.                        | {user_id}                                                               |
| `include`                                                               | List[[models.PlatformUserInclude](../../models/platformuserinclude.md)] | :heavy_minus_sign:                                                      | Optional fields to add to the user. Each value only adds fields.<br/>   |                                                                         |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |                                                                         |

### Response

**[models.PlatformGetUserResponse](../../models/platformgetuserresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 429      | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |