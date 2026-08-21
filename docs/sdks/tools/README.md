# Client.Tools

## Overview

### Available Operations

* [list](#list) - List available tools
* [run](#run) - Execute the specified tool
* [retrieve_action_pack_auth_status](#retrieve_action_pack_auth_status) - Get end-user authentication status for an action pack.
* [authorize_action_pack](#authorize_action_pack) - Start the OAuth authorization flow for an action pack.
* [retrieve_tool_server_auth_status](#retrieve_tool_server_auth_status) - Get end-user authentication status for a tool server.
* [authorize_tool_server](#authorize_tool_server) - Start the OAuth authorization flow for a tool server.
* [get_tool_server_tools](#get_tool_server_tools) - Get tool definitions from a tool server.

## list

Returns a filtered set of available tools based on optional tool name parameters. If no filters are provided, all available tools are returned.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_/rest/api/v1/tools/list" method="get" path="/rest/api/v1/tools/list" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.tools.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `tool_names`                                                        | List[*str*]                                                         | :heavy_minus_sign:                                                  | Optional array of tool names to filter by                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ToolsListResponse](../../models/toolslistresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## run

Execute the specified tool with provided parameters

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/rest/api/v1/tools/call" method="post" path="/rest/api/v1/tools/call" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.tools.run(name="<value>", parameters={

    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                    | *str*                                                                                                     | :heavy_check_mark:                                                                                        | Required name of the tool to execute                                                                      |
| `parameters`                                                                                              | Dict[str, [models.ToolsCallParameter](../../models/toolscallparameter.md)]                                | :heavy_check_mark:                                                                                        | The parameters for the tool. Each key is the name of the parameter and the value is the parameter object. |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.ToolsCallResponse](../../models/toolscallresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## retrieve_action_pack_auth_status

Reports whether the calling user is already authenticated against the third-party
tool backing the specified action pack. Intended for headless / server-driven clients
that render an "Authorize" prompt when the user has not yet consented to the tool.


### Example Usage

<!-- UsageSnippet language="python" operationID="getActionPackAuthStatus" method="get" path="/rest/api/v1/actions/actionpack/{actionPackId}/auth" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.tools.retrieve_action_pack_auth_status(action_pack_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `action_pack_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | ID of the action pack to query or authorize.                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ActionPackAuthStatusResponse](../../models/actionpackauthstatusresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## authorize_action_pack

Starts the third-party OAuth flow for the specified action pack and returns the
redirect URL that the client should navigate the end user to. After the OAuth
callback completes, the user's browser is redirected back to `returnUrl` with a
status query parameter (`?glean_action_auth=success|error&actionPackId=...`).

`returnUrl` must match the tenant's configured return URL allowlist; otherwise the
request is rejected with 400.


### Example Usage

<!-- UsageSnippet language="python" operationID="authorizeActionPack" method="post" path="/rest/api/v1/actions/actionpack/{actionPackId}/auth" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.tools.authorize_action_pack(action_pack_id="<id>", return_url="https://merry-allocation.org/")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `action_pack_id`                                                                                                                                                               | *str*                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                             | ID of the action pack to query or authorize.                                                                                                                                   |
| `return_url`                                                                                                                                                                   | *str*                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                             | URL on the customer's domain to redirect the end user's browser back to after the third-party OAuth<br/>callback completes. Must be present in the tenant's return URL allowlist.<br/> |
| `retries`                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                               | :heavy_minus_sign:                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                            |

### Response

**[models.AuthorizeActionPackResponse](../../models/authorizeactionpackresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## retrieve_tool_server_auth_status

Returns display information and the calling user's current authentication status
for the specified tool server.


### Example Usage

<!-- UsageSnippet language="python" operationID="getToolServerAuthStatus" method="get" path="/rest/api/v1/tool-servers/{serverId}/auth" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.tools.retrieve_tool_server_auth_status(server_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `server_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the tool server.                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ToolServerAuthStatusResponse](../../models/toolserverauthstatusresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## authorize_tool_server

Initiates the third-party OAuth flow for the specified tool server and returns the
authorization URL that the client should navigate the end user to. After the OAuth
callback completes, the user's browser is redirected back to `returnUrl` with query
parameters indicating the result.

`returnUrl` must match the tenant's configured return URL allowlist; otherwise the
request is rejected with 400.


### Example Usage

<!-- UsageSnippet language="python" operationID="authorizeToolServer" method="post" path="/rest/api/v1/tool-servers/{serverId}/auth" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.tools.authorize_tool_server(server_id="<id>", return_url="https://lucky-disadvantage.com")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `server_id`                                                                                                                                      | *str*                                                                                                                                            | :heavy_check_mark:                                                                                                                               | Unique identifier of the tool server.                                                                                                            |
| `return_url`                                                                                                                                     | *str*                                                                                                                                            | :heavy_check_mark:                                                                                                                               | URL to redirect the end user's browser back to after the OAuth flow completes.<br/>Must be present in the tenant's configured return URL allowlist.<br/> |
| `retries`                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                 | :heavy_minus_sign:                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                              |

### Response

**[models.AuthorizeToolServerResponse](../../models/authorizetoolserverresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## get_tool_server_tools

Returns the name, description and JSON input schema for the named tools on the
specified tool server. Works for Glean's built-in tools, tool packs and MCP
servers.

`toolNames` is required. Names that do not exist on the server are returned in
`notFound` rather than failing the request, so a single bad name does not force
callers into one-at-a-time retries. Matching is case-insensitive and treats `-`
and `_` as equivalent.

Use `serverId=native` for Glean's built-in tools.


### Example Usage

<!-- UsageSnippet language="python" operationID="getToolServerTools" method="get" path="/rest/api/v1/tool-servers/{serverId}/tools" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.tools.get_tool_server_tools(server_id="<id>", tool_names=[
        "<value 1>",
        "<value 2>",
        "<value 3>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `server_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the tool server.                               |
| `tool_names`                                                        | List[*str*]                                                         | :heavy_check_mark:                                                  | Tool names to look up on this server. Maximum 100.                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ToolDefinitionsResponse](../../models/tooldefinitionsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |