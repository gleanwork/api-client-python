# Tools
(*client.tools*)

## Overview

### Available Operations

* [execute_action](#execute_action) - Execute Action Tool

## execute_action

Executes an Action tool with the specified parameters.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.tools.execute_action(name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                     | *str*                                                                                                      | :heavy_check_mark:                                                                                         | The name of the tool.                                                                                      |
| `timezone_offset`                                                                                          | *Optional[int]*                                                                                            | :heavy_minus_sign:                                                                                         | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC. |
| `action_run_id`                                                                                            | *Optional[str]*                                                                                            | :heavy_minus_sign:                                                                                         | Unique identifier for this actionRun execution event.                                                      |
| `action_instance_id`                                                                                       | *Optional[str]*                                                                                            | :heavy_minus_sign:                                                                                         | Unique identifier of an action instance.                                                                   |
| `parameters`                                                                                               | Dict[str, [models.WriteActionParameter](../../models/writeactionparameter.md)]                             | :heavy_minus_sign:                                                                                         | The parameters to be passed to the tool for action.                                                        |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[models.ExecuteActionToolResponse](../../models/executeactiontoolresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |