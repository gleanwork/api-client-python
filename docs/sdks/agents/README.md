# Agents
(*agents*)

## Overview

### Available Operations

* [get_agent](#get_agent) - Get Agent
* [get_agent_schemas](#get_agent_schemas) - Get Agent Schemas
* [search_agents](#search_agents) - Search Agents
* [create_and_stream_run](#create_and_stream_run) - Create Run, Stream Output
* [create_and_wait_run](#create_and_wait_run) - Create Run, Wait for Output

## get_agent

Get an agent by ID. This endpoint implements the LangChain Agent Protocol, specifically part of the Agents stage (https://langchain-ai.github.io/agent-protocol/api.html#tag/agents/GET/agents/{agent_id}). It adheres to the standard contract defined for agent interoperability and can be used by agent runtimes that support the Agent Protocol.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.agents.get_agent(agent_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `agent_id`                                                                                                 | *str*                                                                                                      | :heavy_check_mark:                                                                                         | The ID of the agent.                                                                                       |
| `timezone_offset`                                                                                          | *Optional[int]*                                                                                            | :heavy_minus_sign:                                                                                         | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC. |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[models.Agent](../../models/agent.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## get_agent_schemas

Get an agent's schemas by ID. This endpoint implements the LangChain Agent Protocol, specifically part of the Agents stage (https://langchain-ai.github.io/agent-protocol/api.html#tag/agents/GET/agents/{agent_id}/schemas). It adheres to the standard contract defined for agent interoperability and can be used by agent runtimes that support the Agent Protocol.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.agents.get_agent_schemas(agent_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `agent_id`                                                                                                 | *str*                                                                                                      | :heavy_check_mark:                                                                                         | The ID of the agent.                                                                                       |
| `timezone_offset`                                                                                          | *Optional[int]*                                                                                            | :heavy_minus_sign:                                                                                         | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC. |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[models.AgentSchemas](../../models/agentschemas.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## search_agents

List Agents available in this service. This endpoint implements the LangChain Agent Protocol, specifically part of the Agents stage (https://langchain-ai.github.io/agent-protocol/api.html#tag/agents/POST/agents/search). It adheres to the standard contract defined for agent interoperability and can be used by agent runtimes that support the Agent Protocol.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.agents.search_agents()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SearchAgentsRequest](../../models/searchagentsrequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SearchAgentsResponse](../../models/searchagentsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## create_and_stream_run

Creates and triggers a run of an agent. Streams the output in SSE format. This endpoint implements the LangChain Agent Protocol, specifically part of the Runs stage (https://langchain-ai.github.io/agent-protocol/api.html#tag/runs/POST/runs/stream). It adheres to the standard contract defined for agent interoperability and can be used by agent runtimes that support the Agent Protocol. Note that running agents that reference third party platform write actions is unsupported as it requires user confirmation.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.agents.create_and_stream_run()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.AgentRunCreate](../../models/agentruncreate.md)             | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[str](../../models/.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## create_and_wait_run

Creates and triggers a run of an agent. Waits for final output and then returns it. This endpoint implements the LangChain Agent Protocol, specifically part of the Runs stage (https://langchain-ai.github.io/agent-protocol/api.html#tag/runs/POST/runs/wait). It adheres to the standard contract defined for agent interoperability and can be used by agent runtimes that support the Agent Protocol. Note that running agents that reference third party platform write actions is unsupported as it requires user confirmation.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.agents.create_and_wait_run()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.AgentRunCreate](../../models/agentruncreate.md)             | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AgentRunWaitResponse](../../models/agentrunwaitresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |