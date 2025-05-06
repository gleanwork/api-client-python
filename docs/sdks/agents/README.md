# Agents
(*client.agents*)

## Overview

### Available Operations

* [run](#run) - Runs an Agent.
* [list](#list) - Lists all agents.
* [retrieve_inputs](#retrieve_inputs) - Gets the inputs to an agent.

## run

Trigger an Agent with a given id.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.agents.run()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `timezone_offset`                                                                                             | *Optional[int]*                                                                                               | :heavy_minus_sign:                                                                                            | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.    |
| `agent_id`                                                                                                    | *Optional[str]*                                                                                               | :heavy_minus_sign:                                                                                            | The ID of the agent to be run.                                                                                |
| `fields`                                                                                                      | Dict[str, *str*]                                                                                              | :heavy_minus_sign:                                                                                            | Key-value mapping of string -> string where the key is the name of the field in the prompt.                   |
| `stream`                                                                                                      | *Optional[bool]*                                                                                              | :heavy_minus_sign:                                                                                            | Whether to stream responses as they become available. If false, the entire response will be returned at once. |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.ChatResponse](../../models/chatresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## list

Lists all agents that are available.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.agents.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `timezone_offset`                                                                                          | *Optional[int]*                                                                                            | :heavy_minus_sign:                                                                                         | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC. |
| `request_body`                                                                                             | *Optional[Any]*                                                                                            | :heavy_minus_sign:                                                                                         | N/A                                                                                                        |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[models.ListAgentsResponse](../../models/listagentsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## retrieve_inputs

Get the inputs to an agent with a given id.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.agents.retrieve_inputs()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `timezone_offset`                                                                                          | *Optional[int]*                                                                                            | :heavy_minus_sign:                                                                                         | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC. |
| `agent_id`                                                                                                 | *Optional[str]*                                                                                            | :heavy_minus_sign:                                                                                         | The id of the agent.                                                                                       |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[models.GetAgentInputsResponse](../../models/getagentinputsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |