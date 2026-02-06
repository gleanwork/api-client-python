# Client.Chat

## Overview

### Available Operations

* [create](#create) - Chat
* [delete_all](#delete_all) - Deletes all saved Chats owned by a user
* [delete](#delete) - Deletes saved Chats
* [retrieve](#retrieve) - Retrieves a Chat
* [list](#list) - Retrieves all saved Chats
* [retrieve_application](#retrieve_application) - Gets the metadata for a custom Chat application
* [upload_files](#upload_files) - Upload files for Chat.
* [retrieve_files](#retrieve_files) - Get files uploaded by a user for Chat.
* [delete_files](#delete_files) - Delete files uploaded by a user for chat.
* [create_stream](#create_stream) - Chat

## create

Have a conversation with Glean AI.

### Example Usage: citationResponse

<!-- UsageSnippet language="python" operationID="chat" method="post" path="/rest/api/v1/chat" example="citationResponse" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.chat.create(messages=[], timeout_millis=30000)

    # Handle response
    print(res)

```
### Example Usage: defaultExample

<!-- UsageSnippet language="python" operationID="chat" method="post" path="/rest/api/v1/chat" example="defaultExample" -->
```python
from glean.api_client import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.chat.create(messages=[
        {
            "fragments": [
                models.ChatMessageFragment(
                    text="What are the company holidays this year?",
                ),
            ],
        },
    ], timeout_millis=30000)

    # Handle response
    print(res)

```
### Example Usage: gptAgentExample

<!-- UsageSnippet language="python" operationID="chat" method="post" path="/rest/api/v1/chat" example="gptAgentExample" -->
```python
from glean.api_client import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.chat.create(messages=[
        {
            "fragments": [
                models.ChatMessageFragment(
                    text="Who was the first person to land on the moon?",
                ),
            ],
        },
    ], agent_config={
        "agent": models.AgentEnum.GPT,
    }, timeout_millis=30000)

    # Handle response
    print(res)

```
### Example Usage: streamingExample

<!-- UsageSnippet language="python" operationID="chat" method="post" path="/rest/api/v1/chat" example="streamingExample" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.chat.create(messages=[], timeout_millis=30000)

    # Handle response
    print(res)

```
### Example Usage: updateResponse

<!-- UsageSnippet language="python" operationID="chat" method="post" path="/rest/api/v1/chat" example="updateResponse" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.chat.create(messages=[], timeout_millis=30000)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                    | Example                                                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `messages`                                                                                                                                                                                                                                                                                                                                                                                     | List[[models.ChatMessage](../../models/chatmessage.md)]                                                                                                                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                             | A list of chat messages, from most recent to least recent. At least one message must specify a USER author.                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                |
| `locale`                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`.                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                |
| `timezone_offset`                                                                                                                                                                                                                                                                                                                                                                              | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                |
| `session_info`                                                                                                                                                                                                                                                                                                                                                                                 | [Optional[models.SessionInfo]](../../models/sessioninfo.md)                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                |
| `save_chat`                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | Save the current interaction as a Chat for the user to access and potentially continue later.                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                |
| `chat_id`                                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | The id of the Chat that context should be retrieved from and messages added to. An empty id starts a new Chat, and the Chat is saved if saveChat is true.                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                |
| `agent_config`                                                                                                                                                                                                                                                                                                                                                                                 | [Optional[models.AgentConfig]](../../models/agentconfig.md)                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | Describes the agent that executes the request.                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                |
| `inclusions`                                                                                                                                                                                                                                                                                                                                                                                   | [Optional[models.ChatRestrictionFilters]](../../models/chatrestrictionfilters.md)                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                |
| `exclusions`                                                                                                                                                                                                                                                                                                                                                                                   | [Optional[models.ChatRestrictionFilters]](../../models/chatrestrictionfilters.md)                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                |
| `timeout_millis`                                                                                                                                                                                                                                                                                                                                                                               | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | Timeout in milliseconds for the request. A `408` error will be returned if handling the request takes longer.                                                                                                                                                                                                                                                                                  | 30000                                                                                                                                                                                                                                                                                                                                                                                          |
| `application_id`                                                                                                                                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | The ID of the application this request originates from, used to determine the configuration of underlying chat processes. This should correspond to the ID set during admin setup. If not specified, the default chat experience will be used.                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                |
| `agent_id`                                                                                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | The ID of the Agent that should process this chat request. Only Agents with trigger set to 'User chat message' are invokable through this API. If not specified, the default chat experience will be used.                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                |
| `stream`                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | If set, response lines will be streamed one-by-one as they become available. Each will be a ChatResponse, formatted as JSON, and separated by a new line. If false, the entire response will be returned at once. Note that if this is set and the model being used does not support streaming, the model's response will not be streamed, but other messages from the endpoint still will be. |                                                                                                                                                                                                                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                |

### Response

**[models.ChatResponse](../../models/chatresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## delete_all

Deletes all saved Chats a user has had and all their contained conversational content.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteallchats" method="post" path="/rest/api/v1/deleteallchats" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    glean.client.chat.delete_all()

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |
| `timezone_offset`                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.                                                                                          |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## delete

Deletes saved Chats and all their contained conversational content.

### Example Usage

<!-- UsageSnippet language="python" operationID="deletechats" method="post" path="/rest/api/v1/deletechats" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    glean.client.chat.delete(ids=[])

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ids`                                                                                                                                                                                               | List[*str*]                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                  | A non-empty list of ids of the Chats to be deleted.                                                                                                                                                 |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |
| `timezone_offset`                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.                                                                                          |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## retrieve

Retrieves the chat history between Glean Assistant and the user for a given Chat.

### Example Usage

<!-- UsageSnippet language="python" operationID="getchat" method="post" path="/rest/api/v1/getchat" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.chat.retrieve(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                | *str*                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                  | The id of the Chat to be retrieved.                                                                                                                                                                 |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |
| `timezone_offset`                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.                                                                                          |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Response

**[models.GetChatResponse](../../models/getchatresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## list

Retrieves all the saved Chats between Glean Assistant and the user. The returned Chats contain only metadata and no conversational content.

### Example Usage

<!-- UsageSnippet language="python" operationID="listchats" method="post" path="/rest/api/v1/listchats" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.chat.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |
| `timezone_offset`                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.                                                                                          |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Response

**[models.ListChatsResponse](../../models/listchatsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## retrieve_application

Gets the Chat application details for the specified application ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="getchatapplication" method="post" path="/rest/api/v1/getchatapplication" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.chat.retrieve_application(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                | *str*                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                  | The id of the Chat application to be retrieved.                                                                                                                                                     |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |
| `timezone_offset`                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.                                                                                          |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Response

**[models.GetChatApplicationResponse](../../models/getchatapplicationresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## upload_files

Upload files for Chat.

### Example Usage

<!-- UsageSnippet language="python" operationID="uploadchatfiles" method="post" path="/rest/api/v1/uploadchatfiles" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.chat.upload_files(files=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `files`                                                                                                                                                                                             | List[[models.File](../../models/file.md)]                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                  | Raw files to be uploaded for chat in binary format.                                                                                                                                                 |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |
| `timezone_offset`                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.                                                                                          |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Response

**[models.UploadChatFilesResponse](../../models/uploadchatfilesresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## retrieve_files

Get files uploaded by a user for Chat.

### Example Usage

<!-- UsageSnippet language="python" operationID="getchatfiles" method="post" path="/rest/api/v1/getchatfiles" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.chat.retrieve_files(file_ids=[
        "<value 1>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `file_ids`                                                                                                                                                                                          | List[*str*]                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                  | IDs of files to fetch.                                                                                                                                                                              |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |
| `timezone_offset`                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.                                                                                          |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Response

**[models.GetChatFilesResponse](../../models/getchatfilesresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## delete_files

Delete files uploaded by a user for Chat.

### Example Usage

<!-- UsageSnippet language="python" operationID="deletechatfiles" method="post" path="/rest/api/v1/deletechatfiles" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    glean.client.chat.delete_files(file_ids=[
        "<value 1>",
        "<value 2>",
        "<value 3>",
    ])

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `file_ids`                                                                                                                                                                                          | List[*str*]                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                  | IDs of files to delete.                                                                                                                                                                             |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |
| `timezone_offset`                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.                                                                                          |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## create_stream

Have a conversation with Glean AI.

### Example Usage: citationResponse

<!-- UsageSnippet language="python" operationID="chatStream" method="post" path="/rest/api/v1/chat#stream" example="citationResponse" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.chat.create_stream(messages=[], timeout_millis=30000)

    # Handle response
    print(res)

```
### Example Usage: defaultExample

<!-- UsageSnippet language="python" operationID="chatStream" method="post" path="/rest/api/v1/chat#stream" example="defaultExample" -->
```python
from glean.api_client import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.chat.create_stream(messages=[
        {
            "fragments": [
                models.ChatMessageFragment(
                    text="What are the company holidays this year?",
                ),
            ],
        },
    ], timeout_millis=30000)

    # Handle response
    print(res)

```
### Example Usage: gptAgentExample

<!-- UsageSnippet language="python" operationID="chatStream" method="post" path="/rest/api/v1/chat#stream" example="gptAgentExample" -->
```python
from glean.api_client import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.chat.create_stream(messages=[
        {
            "fragments": [
                models.ChatMessageFragment(
                    text="Who was the first person to land on the moon?",
                ),
            ],
        },
    ], agent_config={
        "agent": models.AgentEnum.GPT,
    }, timeout_millis=30000)

    # Handle response
    print(res)

```
### Example Usage: streamingExample

<!-- UsageSnippet language="python" operationID="chatStream" method="post" path="/rest/api/v1/chat#stream" example="streamingExample" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.chat.create_stream(messages=[], timeout_millis=30000)

    # Handle response
    print(res)

```
### Example Usage: updateResponse

<!-- UsageSnippet language="python" operationID="chatStream" method="post" path="/rest/api/v1/chat#stream" example="updateResponse" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.chat.create_stream(messages=[], timeout_millis=30000)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                    | Example                                                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `messages`                                                                                                                                                                                                                                                                                                                                                                                     | List[[models.ChatMessage](../../models/chatmessage.md)]                                                                                                                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                             | A list of chat messages, from most recent to least recent. At least one message must specify a USER author.                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                |
| `timezone_offset`                                                                                                                                                                                                                                                                                                                                                                              | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                |
| `session_info`                                                                                                                                                                                                                                                                                                                                                                                 | [Optional[models.SessionInfo]](../../models/sessioninfo.md)                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                |
| `save_chat`                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | Save the current interaction as a Chat for the user to access and potentially continue later.                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                |
| `chat_id`                                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | The id of the Chat that context should be retrieved from and messages added to. An empty id starts a new Chat, and the Chat is saved if saveChat is true.                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                |
| `agent_config`                                                                                                                                                                                                                                                                                                                                                                                 | [Optional[models.AgentConfig]](../../models/agentconfig.md)                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | Describes the agent that executes the request.                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                |
| `inclusions`                                                                                                                                                                                                                                                                                                                                                                                   | [Optional[models.ChatRestrictionFilters]](../../models/chatrestrictionfilters.md)                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                |
| `exclusions`                                                                                                                                                                                                                                                                                                                                                                                   | [Optional[models.ChatRestrictionFilters]](../../models/chatrestrictionfilters.md)                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                |
| `timeout_millis`                                                                                                                                                                                                                                                                                                                                                                               | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | Timeout in milliseconds for the request. A `408` error will be returned if handling the request takes longer.                                                                                                                                                                                                                                                                                  | 30000                                                                                                                                                                                                                                                                                                                                                                                          |
| `application_id`                                                                                                                                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | The ID of the application this request originates from, used to determine the configuration of underlying chat processes. This should correspond to the ID set during admin setup. If not specified, the default chat experience will be used.                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                |
| `agent_id`                                                                                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | The ID of the Agent that should process this chat request. Only Agents with trigger set to 'User chat message' are invokable through this API. If not specified, the default chat experience will be used.                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                |
| `stream`                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | If set, response lines will be streamed one-by-one as they become available. Each will be a ChatResponse, formatted as JSON, and separated by a new line. If false, the entire response will be returned at once. Note that if this is set and the model being used does not support streaming, the model's response will not be streamed, but other messages from the endpoint still will be. |                                                                                                                                                                                                                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                |

### Response

**[str](../../models/.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |