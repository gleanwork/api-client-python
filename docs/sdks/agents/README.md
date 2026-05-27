# Agents

## Overview

### Available Operations

* [edit_agent](#edit_agent) - Edit an agent

## edit_agent

Creates a draft or publishes an [agent](https://developers.glean.com/agents/agents-api). Use `isDraft=true` to save a draft, or `isDraft=false` (or omit) to publish immediately. Only draft and publish modes are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="editAgent" method="post" path="/rest/api/v1/agents/{agent_id}" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    glean.agents.edit_agent(agent_id="<id>")

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