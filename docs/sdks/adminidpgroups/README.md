# Admin.Idpgroups

## Overview

### Available Operations

* [list](#list) - List IdP groups
* [get](#get) - Get an IdP group

## list

List the identity provider (IdP) groups that Glean loads from the directory, ordered by display_name and then by idp_group_id. Use idp_group_id to name a group in other Platform APIs, such as the usage limit evaluation and limit increase request APIs. Usage limits apply only to IdP groups from the datasource instance in usage_settings.user_grouping.idp_group_provider_instance of the get usage settings response, and this API always lists that instance's groups. To list only those groups, pass that value in a provider_instance filter of the filters parameter, for example `filters=[{"field":"provider_instance","operator":"EQUALS","values":["okta"]}]`, URL-encoded as `filters=%5B%7B%22field%22%3A%22provider_instance%22%2C%22operator%22%3A%22EQUALS%22%2C%22values%22%3A%5B%22okta%22%5D%7D%5D`. Send a provider filter to list only one provider's groups, and a name filter to list only the groups whose display_name contains a value. Internal O365 ownership groups and SharePoint groups are left out. The caller must be able to read the workspace configuration or the workspace billing.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-admin-idp-groups-list" method="get" path="/api/admin/idp-groups" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.admin.idpgroups.list(page_size=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page_size`                                                                                                                                                                                                                                                                                                                                                            | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                     | Maximum number of IdP groups to return. Defaults to 50. Maximum is 100.                                                                                                                                                                                                                                                                                                |
| `cursor`                                                                                                                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                     | Opaque pagination cursor from a previous response. Send the same filters that the previous request used.<br/>                                                                                                                                                                                                                                                          |
| `filters`                                                                                                                                                                                                                                                                                                                                                              | List[[models.PlatformIdpGroupFilter](../../models/platformidpgroupfilter.md)]                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                     | JSON-encoded filters that choose which IdP groups are returned. The supported fields are provider_instance, provider, and name. The only supported operator is EQUALS. Multiple values OR within a filter. Multiple filters AND together. The name field may appear in only one filter. A value that matches no IdP group returns no IdP groups rather than an error.<br/> |
| `retries`                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                    |

### Response

**[models.PlatformListIdpGroupsResponse](../../models/platformlistidpgroupsresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 429      | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## get

Get one identity provider (IdP) group by its idp_group_id. An idp_group_id that is not valid, or that names no group that the list returns, returns 404 resource_not_found. A group that was removed from the identity provider returns 404 after Glean reloads the directory. The caller must be able to read the workspace configuration or the workspace billing.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-admin-idp-groups-get" method="get" path="/api/admin/idp-groups/{idp_group_id}" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.admin.idpgroups.get(idp_group_id="{idp_group_id}")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            | Example                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `idp_group_id`                                                                                                         | *str*                                                                                                                  | :heavy_check_mark:                                                                                                     | The idp_group_id from a list IdP groups response or a usage API response. IDs are opaque. Do not parse or build them.<br/> | {idp_group_id}                                                                                                         |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |                                                                                                                        |

### Response

**[models.PlatformGetIdpGroupResponse](../../models/platformgetidpgroupresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 429      | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |