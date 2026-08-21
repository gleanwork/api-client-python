# Chat

## Overview

### Available Operations

* [create](#create) - Create a chat response

## create

Run an assistant turn. Set `stream` to true to receive server-sent events; otherwise the response is a typed JSON response object.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-chat-create" method="post" path="/api/chat" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.chat.create(input="<value>", stream=False, store=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `input`                                                                                                                                    | [models.Input](../../models/input.md)                                                                                                      | :heavy_check_mark:                                                                                                                         | Either a plain string (single user turn) or a chronological array of `USER`/`ASSISTANT` messages. The final array message must be `USER`.<br/> |
| `stream`                                                                                                                                   | *Optional[bool]*                                                                                                                           | :heavy_minus_sign:                                                                                                                         | When true, respond with `text/event-stream`. When false or omitted, respond with `application/json`.<br/>                                  |
| `store`                                                                                                                                    | *Optional[bool]*                                                                                                                           | :heavy_minus_sign:                                                                                                                         | When true (default), persist the interaction and return a `conversation_id`. When false, run ephemerally with no persistence.<br/>         |
| `conversation_id`                                                                                                                          | *Optional[str]*                                                                                                                            | :heavy_minus_sign:                                                                                                                         | Continue an existing stored conversation. Incompatible with message-array `input` and with `store: false`.<br/>                            |
| `retries`                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                           | :heavy_minus_sign:                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                        |

### Response

**[models.PlatformChatCreateResponse](../../models/platformchatcreateresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.PlatformProblemDetailError      | 400, 401, 403, 404, 408, 413, 422, 429 | application/problem+json               |
| errors.PlatformProblemDetailError      | 500, 503                               | application/problem+json               |
| errors.GleanError                      | 4XX, 5XX                               | \*/\*                                  |