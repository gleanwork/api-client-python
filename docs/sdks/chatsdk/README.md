# Chat

## Overview

### Available Operations

* [create](#create) - Create a chat response
* [create_stream](#create_stream) - SDK-only logical operation. HTTP clients must call the base path; the URL fragment is not sent. Create a chat response

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

    res = glean.chat.create(input="What is our parental leave policy?", store=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `input`                                                                                                                                    | [models.PlatformChatCreateInput](../../models/platformchatcreateinput.md)                                                                  | :heavy_check_mark:                                                                                                                         | Either a plain string (single user turn) or a chronological array of `USER`/`ASSISTANT` messages. The final array message must be `USER`.<br/> |
| `store`                                                                                                                                    | *Optional[bool]*                                                                                                                           | :heavy_minus_sign:                                                                                                                         | When true (default), persist the interaction and return a `conversation_id`. When false, run ephemerally with no persistence.<br/>         |
| `conversation_id`                                                                                                                          | *Optional[str]*                                                                                                                            | :heavy_minus_sign:                                                                                                                         | Continue an existing stored conversation. Incompatible with message-array `input` and with `store: false`.<br/>                            |
| `retries`                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                           | :heavy_minus_sign:                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                        |

### Response

**[models.PlatformChatCompletedResponse](../../models/platformchatcompletedresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.PlatformProblemDetailError      | 400, 401, 403, 404, 408, 413, 422, 429 | application/problem+json               |
| errors.PlatformProblemDetailError      | 500, 503                               | application/problem+json               |
| errors.GleanError                      | 4XX, 5XX                               | \*/\*                                  |

## create_stream

SDK-only logical operation. HTTP clients must call the base path; the URL fragment is not sent. Run an assistant turn. Set `stream` to true to receive server-sent events; otherwise the response is a typed JSON response object.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-chat-create-stream" method="post" path="/api/chat#stream" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.chat.create_stream(input="What is our parental leave policy?", store=True)

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `input`                                                                                                                                    | [models.PlatformChatCreateStreamInput](../../models/platformchatcreatestreaminput.md)                                                      | :heavy_check_mark:                                                                                                                         | Either a plain string (single user turn) or a chronological array of `USER`/`ASSISTANT` messages. The final array message must be `USER`.<br/> |
| `store`                                                                                                                                    | *Optional[bool]*                                                                                                                           | :heavy_minus_sign:                                                                                                                         | When true (default), persist the interaction and return a `conversation_id`. When false, run ephemerally with no persistence.<br/>         |
| `conversation_id`                                                                                                                          | *Optional[str]*                                                                                                                            | :heavy_minus_sign:                                                                                                                         | Continue an existing stored conversation. Incompatible with message-array `input` and with `store: false`.<br/>                            |
| `retries`                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                           | :heavy_minus_sign:                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                        |

### Response

**[Union[eventstreaming.EventStream[models.PlatformChatStreamEventServerSentEvent], eventstreaming.EventStreamAsync[models.PlatformChatStreamEventServerSentEvent]]](../../models/.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.PlatformProblemDetailError      | 400, 401, 403, 404, 408, 413, 422, 429 | application/problem+json               |
| errors.PlatformProblemDetailError      | 500, 503                               | application/problem+json               |
| errors.GleanError                      | 4XX, 5XX                               | \*/\*                                  |