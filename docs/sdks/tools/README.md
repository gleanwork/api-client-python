# Tools
(*client.tools*)

## Overview

### Available Operations

* [list](#list) - List available tools
* [run](#run) - Execute the specified tool

## list

Returns a filtered set of available tools based on optional tool name parameters. If no filters are provided, all available tools are returned.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.client.tools.list()

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

```python
from glean import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.client.tools.run(name="<value>", parameters={
        "key": {
            "name": "<value>",
            "value": "<value>",
        },
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