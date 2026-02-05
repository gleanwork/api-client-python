# Client.Agents

## Overview

### Available Operations

* [retrieve](#retrieve) - Retrieve an agent
* [retrieve_schemas](#retrieve_schemas) - List an agent's schemas
* [list](#list) - Search agents
* [run_stream](#run_stream) - Create an agent run and stream the response
* [run](#run) - Create an agent run and wait for the response

## retrieve

Returns details of an [agent](https://developers.glean.com/agents/agents-api) created in the Agent Builder.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAgent" method="get" path="/rest/api/v1/agents/{agent_id}" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.agents.retrieve(agent_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent_id`                                                                                                                                                                                          | *str*                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                  | The ID of the agent.                                                                                                                                                                                |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |
| `timezone_offset`                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.                                                                                          |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Response

**[models.Agent](../../models/agent.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## retrieve_schemas

Return [agent](https://developers.glean.com/agents/agents-api)'s input and output schemas. You can use these schemas to detect changes to an agent's input or output structure.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAgentSchemas" method="get" path="/rest/api/v1/agents/{agent_id}/schemas" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.agents.retrieve_schemas(agent_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent_id`                                                                                                                                                                                          | *str*                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                  | The ID of the agent.                                                                                                                                                                                |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |
| `timezone_offset`                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.                                                                                          |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Response

**[models.AgentSchemas](../../models/agentschemas.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## list

Search for [agents](https://developers.glean.com/agents/agents-api) by agent name.

### Example Usage

<!-- UsageSnippet language="python" operationID="searchAgents" method="post" path="/rest/api/v1/agents/search" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.agents.list(name="HR Policy Agent")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        | Example                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                             | *Optional[str]*                                                                                                                    | :heavy_minus_sign:                                                                                                                 | Filters on the name of the agent. The keyword search is case-insensitive. If search string is ommited or empty, acts as no filter. | HR Policy Agent                                                                                                                    |
| `retries`                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                   | :heavy_minus_sign:                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                |                                                                                                                                    |

### Response

**[models.SearchAgentsResponse](../../models/searchagentsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## run_stream

Executes an [agent](https://developers.glean.com/agents/agents-api) run and returns the result as a stream of server-sent events (SSE).

### Example Usage

<!-- UsageSnippet language="python" operationID="createAndStreamRun" method="post" path="/rest/api/v1/agents/runs/stream" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.agents.run_stream(agent_id="<id>", messages=[
        {
            "role": "USER",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The ID of the agent to run.                                         |
| `input`                                                             | Dict[str, *Any*]                                                    | :heavy_minus_sign:                                                  | The input to the agent.                                             |
| `messages`                                                          | List[[models.Message](../../models/message.md)]                     | :heavy_minus_sign:                                                  | The messages to pass an input to the agent.                         |
| `metadata`                                                          | Dict[str, *Any*]                                                    | :heavy_minus_sign:                                                  | The metadata to pass to the agent.                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[str](../../models/.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## run

Executes an [agent](https://developers.glean.com/agents/agents-api) run and returns the final response.

### Example Usage

<!-- UsageSnippet language="python" operationID="createAndWaitRun" method="post" path="/rest/api/v1/agents/runs/wait" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.agents.run(agent_id="<id>", messages=[
        {
            "role": "USER",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The ID of the agent to run.                                         |
| `input`                                                             | Dict[str, *Any*]                                                    | :heavy_minus_sign:                                                  | The input to the agent.                                             |
| `messages`                                                          | List[[models.Message](../../models/message.md)]                     | :heavy_minus_sign:                                                  | The messages to pass an input to the agent.                         |
| `metadata`                                                          | Dict[str, *Any*]                                                    | :heavy_minus_sign:                                                  | The metadata to pass to the agent.                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AgentRunWaitResponse](../../models/agentrunwaitresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |