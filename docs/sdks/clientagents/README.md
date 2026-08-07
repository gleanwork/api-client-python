# Client.Agents

## Overview

### Available Operations

* [create](#create) - Create an agent
* [retrieve](#retrieve) - Retrieve an agent
* [update](#update) - Edit an agent
* [retrieve_schemas](#retrieve_schemas) - List an agent's schemas
* [import_](#import_) - Import an agent
* [list](#list) - Search agents
* [run_stream](#run_stream) - Create an agent run and stream the response
* [run](#run) - Create an agent run and wait for the response

## create

Create an agent.

### Example Usage

<!-- UsageSnippet language="python" operationID="createAgent" method="post" path="/rest/api/v1/agents" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.agents.create()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |
| `timezone_offset`                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.                                                                                          |
| `name`                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The name of the workflow.                                                                                                                                                                           |
| `transient`                                                                                                                                                                                         | *Optional[bool]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Used to create a transient workflow.                                                                                                                                                                |
| `parent_workflow_id`                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | id of the parent workflow for transient workflows                                                                                                                                                   |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Response

**[models.WorkflowResult](../../models/workflowresult.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

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

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 404                  | application/json     |
| errors.GleanError    | 4XX, 5XX             | \*/\*                |

## update

Creates a draft or publishes an [agent](https://developers.glean.com/agents/agents-api). Use `isDraft=true` to save a draft, or `isDraft=false` (or omit) to publish immediately. Only draft and publish modes are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="editAgent" method="post" path="/rest/api/v1/agents/{agent_id}" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    glean.client.agents.update(agent_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent_id`                                                                                                                                                                                          | *str*                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                  | The ID of the agent.                                                                                                                                                                                |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |
| `timezone_offset`                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.                                                                                          |
| `name`                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The name of the workflow.                                                                                                                                                                           |
| `id`                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The workflow ID we want to update.                                                                                                                                                                  |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 404                  | application/json     |
| errors.GleanError    | 4XX, 5XX             | \*/\*                |

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

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 404, 422             | application/json     |
| errors.GleanError    | 4XX, 5XX             | \*/\*                |

## import_

Imports an [agent](https://developers.glean.com/agents/agents-api) from its on-disk folder representation (spec.yaml, instructions.md, skills/, subagents/) packaged as a zip, and creates or updates the agent. Inverse of the export flow: the folder-to-schema conversion runs server-side. The bundle must contain only regular files; symlinks are resolved by the caller at packaging time.

### Example Usage

<!-- UsageSnippet language="python" operationID="importAgent" method="post" path="/rest/api/v1/agents/{agent_id}/import" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.agents.import_(agent_id="<id>", bundle={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent_id`                                                                                                                                                                                          | *str*                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                  | The ID of the agent to create or update.                                                                                                                                                            |
| `bundle`                                                                                                                                                                                            | [models.Bundle](../../models/bundle.md)                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                  | Zip of the agent folder (spec.yaml, instructions.md, skills/, subagents/) with symlinks dereferenced.<br/>                                                                                          |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |
| `timezone_offset`                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.                                                                                          |
| `git_commit_sha`                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | Optional Git commit SHA to associate with this import.                                                                                                                                              |
| `git_author_id`                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | Optional VCS commit author ID to associate with this import.                                                                                                                                        |
| `commit_message`                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | Optional commit message for the imported version.                                                                                                                                                   |
| `sync_mode`                                                                                                                                                                                         | [Optional[models.ImportAgentSyncMode]](../../models/importagentsyncmode.md)                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                  | Whether the imported version is staged (saved without updating the live version) or published directly to the live version.<br/>                                                                    |
| `is_draft`                                                                                                                                                                                          | *Optional[bool]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | When true, validates and stores a draft preview without publishing (used for PR preview links). Takes precedence over `syncMode`: when `isDraft` is true, `syncMode` is ignored.<br/>               |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Response

**[models.ImportAgentResponse](../../models/importagentresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 404                  | application/json     |
| errors.GleanError    | 4XX, 5XX             | \*/\*                |

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

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 404, 422             | application/json     |
| errors.GleanError    | 4XX, 5XX             | \*/\*                |

## run_stream

Executes an [agent](https://developers.glean.com/agents/agents-api) run and returns the result as a stream of server-sent events (SSE). **Note**: If the agent uses an input form trigger, all form fields (including optional fields) must be included in the `input` object.

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

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `agent_id`                                                                  | *str*                                                                       | :heavy_check_mark:                                                          | The ID of the agent to run.                                                 |
| `input`                                                                     | Dict[str, *Any*]                                                            | :heavy_minus_sign:                                                          | The input to the agent. Required when the agent uses an input form trigger. |
| `messages`                                                                  | List[[models.Message](../../models/message.md)]                             | :heavy_minus_sign:                                                          | The messages to pass an input to the agent.                                 |
| `metadata`                                                                  | Dict[str, *Any*]                                                            | :heavy_minus_sign:                                                          | The metadata to pass to the agent.                                          |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[str](../../models/.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.ErrorResponse               | 404, 409                           | application/json                   |
| errors.UnauthorizedAgentToolsError | 422                                | application/json                   |
| errors.GleanError                  | 4XX, 5XX                           | \*/\*                              |

## run

Executes an [agent](https://developers.glean.com/agents/agents-api) run and returns the final response. **Note**: If the agent uses an input form trigger, all form fields (including optional fields) must be included in the `input` object.

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

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `agent_id`                                                                  | *str*                                                                       | :heavy_check_mark:                                                          | The ID of the agent to run.                                                 |
| `input`                                                                     | Dict[str, *Any*]                                                            | :heavy_minus_sign:                                                          | The input to the agent. Required when the agent uses an input form trigger. |
| `messages`                                                                  | List[[models.Message](../../models/message.md)]                             | :heavy_minus_sign:                                                          | The messages to pass an input to the agent.                                 |
| `metadata`                                                                  | Dict[str, *Any*]                                                            | :heavy_minus_sign:                                                          | The metadata to pass to the agent.                                          |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.AgentRunWaitResponse](../../models/agentrunwaitresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.UnauthorizedAgentToolsError | 422                                | application/json                   |
| errors.GleanError                  | 4XX, 5XX                           | \*/\*                              |