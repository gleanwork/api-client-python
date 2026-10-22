# Departments

## Overview

### Available Operations

* [list](#list) - List departments
* [get](#get) - Get a department

## list

List the departments in the Glean directory, ordered by display_name and then by department_id. The list includes every department that at least one user belongs to or that a usage limit names, so a caller can show the name of a department that a usage limit still names after its users leave it. Department names are exact, so names that differ only by case are different departments.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-departments-list" method="get" path="/api/departments" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.departments.list(page_size=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `page_size`                                                              | *Optional[int]*                                                          | :heavy_minus_sign:                                                       | Maximum number of departments to return. Defaults to 50. Maximum is 100. |
| `cursor`                                                                 | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | Opaque pagination cursor from a previous response.                       |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |

### Response

**[models.PlatformListDepartmentsResponse](../../models/platformlistdepartmentsresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 429      | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## get

Get one department by its department_id. The department can be any department that the list returns, including one that only a usage limit names. A department_id that is not valid, or that no user and no usage limit uses, returns 404 resource_not_found. A department_id comes from the exact department name, so a renamed department gets a new ID, and a name that is used again gets its old ID back.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-departments-get" method="get" path="/api/departments/{department_id}" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.departments.get(department_id="{department_id}")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  | Example                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `department_id`                                                                                                              | *str*                                                                                                                        | :heavy_check_mark:                                                                                                           | The department_id from a list departments response or from a user's department. IDs are opaque. Do not parse or build them.<br/> | {department_id}                                                                                                              |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |                                                                                                                              |

### Response

**[models.PlatformGetDepartmentResponse](../../models/platformgetdepartmentresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 429      | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |