# ClientChat
(*client.chat*)

## Overview

### Available Operations

* [ask](#ask) - Detect and answer questions
* [start](#start) - Chat
* [delete_all](#delete_all) - Deletes all saved Chats owned by a user
* [delete](#delete) - Deletes saved Chats
* [get](#get) - Retrieves a Chat
* [list](#list) - Retrieves all saved Chats
* [get_application](#get_application) - Gets the metadata for a custom Chat application
* [upload_files](#upload_files) - Upload files for Chat.
* [get_files](#get_files) - Get files uploaded by a user for Chat.
* [delete_files](#delete_files) - Delete files uploaded by a user for chat.

## ask

Classify a query as information seeking or not. If so, generate an AI answer and/or provide relevant documents. Useful for integrating into existing chat interfaces.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.chat.ask(ask_request=models.AskRequest(
        detect_only=True,
        ask_experimental_metadata=models.AskExperimentalMetadata(
            query_has_mentions=True,
            query_is_length_appropriate=True,
            query_is_answerable=True,
        ),
        search_request=models.SearchRequest(
            tracking_token="trackingToken",
            page_size=10,
            query="vacation policy",
            request_options=models.SearchRequestOptions(
                facet_filters=[
                    models.FacetFilter(
                        field_name="type",
                        values=[
                            models.FacetFilterValue(
                                value="article",
                                relation_type=models.RelationType.EQUALS,
                            ),
                            models.FacetFilterValue(
                                value="document",
                                relation_type=models.RelationType.EQUALS,
                            ),
                        ],
                    ),
                    models.FacetFilter(
                        field_name="department",
                        values=[
                            models.FacetFilterValue(
                                value="engineering",
                                relation_type=models.RelationType.EQUALS,
                            ),
                        ],
                    ),
                ],
                facet_bucket_size=250170,
            ),
        ),
        excluded_document_specs=[
            models.DocumentSpec1(
                url="string",
            ),
        ],
        operators="string",
        backend=models.Backend.SEARCH,
        chat_application_id="string",
        inclusions=models.ChatRestrictionFilters(
            container_specs=[
                models.DocumentSpec1(
                    url="string",
                ),
            ],
            document_specs=[
                models.DocumentSpec1(
                    url="string",
                ),
            ],
            datasource_instances=[
                "string",
            ],
        ),
        exclusions=models.ChatRestrictionFilters(
            container_specs=[
                models.DocumentSpec1(
                    url="string",
                ),
            ],
            document_specs=[
                models.DocumentSpec1(
                    url="string",
                ),
            ],
            datasource_instances=[
                "string",
            ],
        ),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `ask_request`                                                                                                            | [Optional[models.AskRequest]](../../models/askrequest.md)                                                                | :heavy_minus_sign:                                                                                                       | Ask request                                                                                                              |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.AskResponse](../../models/askresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GleanDataError | 403, 422              | application/json      |
| errors.GleanError     | 4XX, 5XX              | \*/\*                 |

## start

Have a conversation with Glean AI.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.chat.start(messages=[
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

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                    | Example                                                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `messages`                                                                                                                                                                                                                                                                                                                                                                                     | List[[models.ChatMessage](../../models/chatmessage.md)]                                                                                                                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                             | A list of chat messages, from most recent to least recent. It can be assumed that the first chat message in the list is the user's most recent query.                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                |
| `x_scio_actas`                                                                                                                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                |
| `x_glean_auth_type`                                                                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                |
| `timezone_offset`                                                                                                                                                                                                                                                                                                                                                                              | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                |
| `save_chat`                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | Save the current interaction as a Chat for the user to access and potentially continue later.                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                |
| `chat_id`                                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | The id of the Chat that context should be retrieved from and messages added to. An empty id starts a new Chat, and the Chat is saved if saveChat is true.                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                |
| `agent_config`                                                                                                                                                                                                                                                                                                                                                                                 | [Optional[models.AgentConfig]](../../models/agentconfig.md)                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | Describes the agent that executes the request.                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                |
| `inclusions`                                                                                                                                                                                                                                                                                                                                                                                   | [Optional[models.ChatRestrictionFilters]](../../models/chatrestrictionfilters.md)                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                |
| `exclusions`                                                                                                                                                                                                                                                                                                                                                                                   | [Optional[models.ChatRestrictionFilters]](../../models/chatrestrictionfilters.md)                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                |
| `timeout_millis`                                                                                                                                                                                                                                                                                                                                                                               | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | Timeout in milliseconds for the request. A `408` error will be returned if handling the request takes longer.                                                                                                                                                                                                                                                                                  | 30000                                                                                                                                                                                                                                                                                                                                                                                          |
| `application_id`                                                                                                                                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | The ID of the application this request originates from, used to determine the configuration of underlying chat processes. This should correspond to the ID set during admin setup. If not specified, the default chat experience will be used.                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                |
| `stream`                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | If set, response lines will be streamed one-by-one as they become available. Each will be a ChatResponse, formatted as JSON, and separated by a new line. If false, the entire response will be returned at once. Note that if this is set and the model being used does not support streaming, the model's response will not be streamed, but other messages from the endpoint still will be. |                                                                                                                                                                                                                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                |

### Response

**[str](../../models/.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## delete_all

Deletes all saved Chats a user has had and all their contained conversational content.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.client.chat.delete_all()

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `timezone_offset`                                                                                                        | *Optional[int]*                                                                                                          | :heavy_minus_sign:                                                                                                       | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## delete

Deletes saved Chats and all their contained conversational content.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.client.chat.delete(ids=[
        "<value>",
        "<value>",
    ])

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `ids`                                                                                                                    | List[*str*]                                                                                                              | :heavy_check_mark:                                                                                                       | A non-empty list of ids of the Chats to be deleted.                                                                      |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `timezone_offset`                                                                                                        | *Optional[int]*                                                                                                          | :heavy_minus_sign:                                                                                                       | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## get

Retrieves the chat history between Glean Assistant and the user for a given Chat.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.chat.get(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                     | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | The id of the Chat to be retrieved.                                                                                      |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `timezone_offset`                                                                                                        | *Optional[int]*                                                                                                          | :heavy_minus_sign:                                                                                                       | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.GetChatResponse](../../models/getchatresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## list

Retrieves all the saved Chats between Glean Assistant and the user. The returned Chats contain only metadata and no conversational content.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.chat.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `timezone_offset`                                                                                                        | *Optional[int]*                                                                                                          | :heavy_minus_sign:                                                                                                       | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.ListChatsResponse](../../models/listchatsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## get_application

Gets the Chat application details for the specified application ID.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.chat.get_application(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                     | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | The id of the Chat application to be retrieved.                                                                          |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `timezone_offset`                                                                                                        | *Optional[int]*                                                                                                          | :heavy_minus_sign:                                                                                                       | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.GetChatApplicationResponse](../../models/getchatapplicationresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## upload_files

Upload files for Chat.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.chat.upload_files(files=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `files`                                                                                                                  | List[[models.File](../../models/file.md)]                                                                                | :heavy_check_mark:                                                                                                       | Raw files to be uploaded for chat in binary format.                                                                      |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `timezone_offset`                                                                                                        | *Optional[int]*                                                                                                          | :heavy_minus_sign:                                                                                                       | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.UploadChatFilesResponse](../../models/uploadchatfilesresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## get_files

Get files uploaded by a user for Chat.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.chat.get_files(file_ids=[
        "<value>",
        "<value>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `file_ids`                                                                                                               | List[*str*]                                                                                                              | :heavy_check_mark:                                                                                                       | IDs of files to fetch.                                                                                                   |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `timezone_offset`                                                                                                        | *Optional[int]*                                                                                                          | :heavy_minus_sign:                                                                                                       | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.GetChatFilesResponse](../../models/getchatfilesresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## delete_files

Delete files uploaded by a user for Chat.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.client.chat.delete_files(file_ids=[
        "<value>",
    ])

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `file_ids`                                                                                                               | List[*str*]                                                                                                              | :heavy_check_mark:                                                                                                       | IDs of files to delete.                                                                                                  |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `timezone_offset`                                                                                                        | *Optional[int]*                                                                                                          | :heavy_minus_sign:                                                                                                       | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |