# Messages
(*client.messages*)

## Overview

### Available Operations

* [retrieve](#retrieve) - Read messages

## retrieve

Retrieves list of messages from messaging/chat datasources (e.g. Slack, Teams).

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.client.messages.retrieve(id_type=models.IDType.CONVERSATION_ID, id="<id>", timestamp_millis=558834)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                           | Type                                                                                                                                                                                | Required                                                                                                                                                                            | Description                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id_type`                                                                                                                                                                           | [models.IDType](../../models/idtype.md)                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                  | Type of the id in the incoming request.                                                                                                                                             |
| `id`                                                                                                                                                                                | *str*                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                  | ID corresponding to the requested idType. Note that channel and threads are represented by the underlying datasource's ID and conversations are represented by their document's ID. |
| `workspace_id`                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                  | Id for the for the workspace in case of multiple workspaces.                                                                                                                        |
| `direction`                                                                                                                                                                         | [Optional[models.Direction]](../../models/direction.md)                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                  | The direction of the results asked with respect to the reference timestamp. Missing field defaults to OLDER. Only applicable when using a message_id.                               |
| `timestamp_millis`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                  | Timestamp in millis of the reference message. Only applicable when using a message_id.                                                                                              |
| `include_root_message`                                                                                                                                                              | *Optional[bool]*                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                  | Whether to include root message in response.                                                                                                                                        |
| `datasource`                                                                                                                                                                        | [Optional[models.Datasource]](../../models/datasource.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                  | The type of the data source. Missing field defaults to SLACK.                                                                                                                       |
| `datasource_instance_display_name`                                                                                                                                                  | *Optional[str]*                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                  | The datasource instance display name from which the document was extracted. This is used for appinstance facet filter for datasources that support multiple instances.              |
| `retries`                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                 |

### Response

**[models.MessagesResponse](../../models/messagesresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |