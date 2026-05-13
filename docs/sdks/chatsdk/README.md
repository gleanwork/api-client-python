# Chat

## Overview

### Available Operations

* [get_chat_file](#get_chat_file) - Download a chat file

## get_chat_file

Download the raw content of a file generated or uploaded during a chat session (for example, an image produced by the assistant). Returns the file bytes with a Content-Type header matching the file's MIME type.


### Example Usage

<!-- UsageSnippet language="python" operationID="getChatFile" method="get" path="/rest/api/v1/chat-files/{fileId}" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.chat.get_chat_file(file_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `file_id`                                                                                                                  | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | Identifier of the chat file to download.                                                                                   |
| `preview`                                                                                                                  | *Optional[bool]*                                                                                                           | :heavy_minus_sign:                                                                                                         | When true and the file is a PDF, the response is served inline (Content-Disposition: inline) instead of as an attachment.<br/> |
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |

### Response

**[httpx.Response](../../models/.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |