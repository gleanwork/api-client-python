# Agents

## Overview

### Available Operations

* [search](#search) - Search agents
* [get](#get) - Get agent
* [get_schemas](#get_schemas) - Get agent schemas
* [create_run](#create_run) - Create agent run

## search

Search agents available to the authenticated user by agent name.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-agents-search" method="post" path="/api/agents/search" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.agents.search(name="HR Policy Agent")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              | Example                                                                                                  |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                   | *Optional[str]*                                                                                          | :heavy_minus_sign:                                                                                       | Case-insensitive substring to match against agent names. If omitted or empty, no name filter is applied. | HR Policy Agent                                                                                          |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |                                                                                                          |

### Response

**[models.PlatformAgentsSearchResponse](../../models/platformagentssearchresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 413, 429 | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## get

Retrieve details for an agent available to the authenticated user.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-agents-get" method="get" path="/api/agents/{agent_id}" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.agents.get(agent_id="{agent_id}")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | ID of the agent to retrieve.                                        | {agent_id}                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PlatformAgentGetResponse](../../models/platformagentgetresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 429      | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## get_schemas

Retrieve an agent's input and output JSON schemas.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-agents-get-schemas" method="get" path="/api/agents/{agent_id}/schemas" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.agents.get_schemas(agent_id="{agent_id}", include_tools=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | ID of the agent whose schemas should be retrieved.                  | {agent_id}                                                          |
| `include_tools`                                                     | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Whether to include tool metadata in the response.                   |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PlatformAgentSchemasResponse](../../models/platformagentschemasresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 429      | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## create_run

Execute an agent run. Set `stream` to true to receive server-sent events; otherwise the response contains the final agent messages.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-agents-create-run" method="post" path="/api/agents/{agent_id}/runs" -->
```python
from glean.api_client import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.agents.create_run(agent_id="{agent_id}", messages=[
        {
            "role": models.PlatformMessageRole.USER,
            "content": [
                {
                    "text": "What is our parental leave policy?",
                    "type": models.PlatformContentType.TEXT,
                },
            ],
        },
    ], stream=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      | Example                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent_id`                                                                                                                                                       | *str*                                                                                                                                                            | :heavy_check_mark:                                                                                                                                               | ID of the agent to run.                                                                                                                                          | {agent_id}                                                                                                                                                       |
| `input`                                                                                                                                                          | Dict[str, *Any*]                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Input fields for an input-form triggered agent.                                                                                                                  |                                                                                                                                                                  |
| `messages`                                                                                                                                                       | List[[models.PlatformMessage](../../models/platformmessage.md)]                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Messages to pass to the agent. When provided, the array MUST contain at least one message and each message MUST specify a valid `role` and non-empty `content`.<br/> |                                                                                                                                                                  |
| `metadata`                                                                                                                                                       | Dict[str, *Any*]                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Metadata to pass to the agent.                                                                                                                                   |                                                                                                                                                                  |
| `stream`                                                                                                                                                         | *Optional[bool]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Whether to stream the run response as server-sent events.                                                                                                        |                                                                                                                                                                  |
| `retries`                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                              |                                                                                                                                                                  |

### Response

**[models.PlatformAgentsCreateRunResponse](../../models/platformagentscreaterunresponse.md)**

### Errors

| Error Type                                        | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| errors.PlatformUnauthorizedAgentToolsProblemError | 422                                               | application/problem+json                          |
| errors.PlatformProblemDetailError                 | 400, 401, 403, 404, 408, 409, 413, 429            | application/problem+json                          |
| errors.PlatformProblemDetailError                 | 500, 503                                          | application/problem+json                          |
| errors.GleanError                                 | 4XX, 5XX                                          | \*/\*                                             |