# Agents

## Overview

### Available Operations

* [search](#search) - Search agents
* [get](#get) - Get agent
* [get_schemas](#get_schemas) - Get agent schemas
* [create_run](#create_run) - Create agent run
* [get_run](#get_run) - Get agent run
* [cancel_run](#cancel_run) - Cancel an agent run
* [respond_to_run](#respond_to_run) - Respond to agent run approvals

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

Execute an agent run. By default, set `stream` to true to receive server-sent events; otherwise the response contains the final agent messages. Set `execution_mode` to `DURABLE` to persist a new run and return its initial snapshot with HTTP 201 without waiting for execution. Poll the agent-scoped GET run endpoint for progress. Durable execution continues after an HTTP disconnect, but is not automatically resumed after a QE restart or crash. An active turn becomes overdue more than 40 minutes after acceptance (a 30-minute execution timeout plus 10 minutes of grace). The next GET of the run marks the overdue turn FAILED without replay; there is no periodic sweep. Without a GET, the stored run can remain RUNNING. Failure does not prove that external tool work has stopped. Paused runs are not expired; an accepted approval continuation starts a fresh deadline. Each POST creates a new run; retrying a POST can create another execution. Submit pending approval decisions through the run responses endpoint, and cancellation can be requested through the run cancellations endpoint. A run tracks one workflow execution; automatic background-subagent wake turns are separate executions, not continuations tracked by this run ID.


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
    ], stream=False, execution_mode=models.ExecutionMode.REQUEST_BOUND)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | ID of the agent to run.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | {agent_id}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `input`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Dict[str, *Any*]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Input fields for an input-form triggered agent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `messages`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | List[[models.PlatformMessageInput](../../models/platformmessageinput.md)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Messages to pass to the agent. When provided, the array MUST contain at least one message and each message MUST specify a valid `role` and non-empty `content`.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `metadata`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Dict[str, *Any*]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Metadata to pass to the agent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `stream`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Whether to stream the run response as server-sent events. Not supported in DURABLE mode.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `execution_mode`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | [Optional[models.ExecutionMode]](../../models/executionmode.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | REQUEST_BOUND preserves the existing wait/stream behavior. DURABLE starts a fresh, persisted execution with a 30-minute execution timeout and returns immediately. DURABLE requires stream to be false or omitted and does not accept metadata.chat_session_id. It does not bypass tool approval requirements or provide automatic QE-crash resumption. Expiry is read-triggered: the next GET of the run marks an active turn FAILED if more than 40 minutes have passed since the turn was accepted. There is no periodic sweep, so the stored run can remain RUNNING until it is read. Expiry never replays execution or expires approval-paused runs, and failure does not prove that external tool work has stopped.<br/> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

### Response

**[models.PlatformAgentsCreateRunResponse](../../models/platformagentscreaterunresponse.md)**

### Errors

| Error Type                                        | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| errors.PlatformUnauthorizedAgentToolsProblemError | 422                                               | application/problem+json                          |
| errors.PlatformProblemDetailError                 | 400, 401, 403, 404, 408, 409, 413, 429            | application/problem+json                          |
| errors.PlatformProblemDetailError                 | 500, 503                                          | application/problem+json                          |
| errors.GleanError                                 | 4XX, 5XX                                          | \*/\*                                             |

## get_run

Retrieve a persisted workflow execution owned by the authenticated user. The run must belong to the specified agent, and the user must still have access to that agent. Unknown runs, runs owned by another user, and mismatched agent/run identifiers return 404. Requires the agents.run scope. Executions without a persisted workflow record are not available through this endpoint.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-agents-get-run" method="get" path="/api/agents/{agent_id}/runs/{run_id}" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.agents.get_run(agent_id="{agent_id}", run_id="{run_id}")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | ID of the agent that owns the run.                                  | {agent_id}                                                          |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | ID of the durable run to retrieve.                                  | {run_id}                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PlatformAgentRunResponse](../../models/platformagentrunresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 429      | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## cancel_run

Request cooperative cancellation of the durable agent run identified by `run_id` in the JSON body. Requires ownership, current agent access, and the agents.run scope. Sending a cancellation signal does not itself change an active run from RUNNING; poll GET run for the final state. Paused runs become CANCELLED without resuming execution. Repeated requests and requests for terminal runs return the current snapshot. Completion may win a race with cancellation. Completed tool side effects cannot be undone, and external work may continue if a tool does not support cancellation. Cancellation targets this run, not separate background-subagent executions. An active run without a cancellation registration returns 409. Cancellation signaling requires Redis. An interrupted active run can instead become FAILED through deadline cleanup; this does not verify that external tool work has stopped.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-agents-cancel-run" method="post" path="/api/agents/{agent_id}/cancellations" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.agents.cancel_run(agent_id="{agent_id}", run_id="{run_id}")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               | Example                                                                   |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `agent_id`                                                                | *str*                                                                     | :heavy_check_mark:                                                        | ID of the agent that owns the run.                                        | {agent_id}                                                                |
| `run_id`                                                                  | *str*                                                                     | :heavy_check_mark:                                                        | ID of the run to cancel. Must belong to the agent identified in the path. |                                                                           |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |                                                                           |

### Response

**[models.PlatformAgentRunResponse](../../models/platformagentrunresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.PlatformProblemDetailError      | 400, 401, 403, 404, 408, 409, 413, 429 | application/problem+json               |
| errors.PlatformProblemDetailError      | 500, 503                               | application/problem+json               |
| errors.GleanError                      | 4XX, 5XX                               | \*/\*                                  |

## respond_to_run

Submit decisions for every pending tool approval in the paused run's current batch. The run is identified by `run_id` in the JSON body. Decisions apply only to the stored invocations and arguments; argument edits, authentication responses, and session-wide grants are not supported. The caller must own the run, still have agent access, and have the agents.run scope. Acceptance persists the decisions before resuming the same run and chat session. Identical accepted decisions return the current snapshot without another continuation. Conflicting, stale, incomplete, or non-pending decisions return 409. Cancellation registration failure returns 503 without accepting the decisions; retry the same approval batch. This retry guarantee does not cover an indeterminate database commit outcome. Go workflow approval resumes currently support one tool invocation and one approval response. Unsupported multi-tool or multi-decision Go resumes fail without executing tools. The resumed action must resolve to the tool identified by the stored approval request and paused checkpoint. Missing or inconsistent identity fails without executing tools. Execution continues after HTTP disconnects, but is not automatically resumed after a QE crash. Each accepted continuation starts a fresh 30-minute execution timeout and 40-minute cleanup deadline. Identical retries do not extend that deadline. Waiting for approval does not expire a run. The next GET marks an overdue active turn FAILED without replaying execution.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-agents-create-run-responses" method="post" path="/api/agents/{agent_id}/responses" -->
```python
from glean.api_client import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.agents.respond_to_run(agent_id="{agent_id}", run_id="{run_id}", responses=[
        {
            "interaction_id": "{interaction_id}",
            "decision": models.Decision.APPROVE,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                | Example                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `agent_id`                                                                                                 | *str*                                                                                                      | :heavy_check_mark:                                                                                         | ID of the agent that owns the run.                                                                         | {agent_id}                                                                                                 |
| `run_id`                                                                                                   | *str*                                                                                                      | :heavy_check_mark:                                                                                         | ID of the run whose pending approvals are being answered. Must belong to the agent identified in the path. |                                                                                                            |
| `responses`                                                                                                | List[[models.PlatformAgentRunApprovalDecision](../../models/platformagentrunapprovaldecision.md)]          | :heavy_check_mark:                                                                                         | One decision per pending interaction. Interaction IDs must be unique.                                      |                                                                                                            |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |                                                                                                            |

### Response

**[models.PlatformAgentRunResponse](../../models/platformagentrunresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.PlatformProblemDetailError      | 400, 401, 403, 404, 408, 409, 413, 429 | application/problem+json               |
| errors.PlatformProblemDetailError      | 500, 503                               | application/problem+json               |
| errors.GleanError                      | 4XX, 5XX                               | \*/\*                                  |