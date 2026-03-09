# ChatResponse

A single response from the /chat backend.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `messages`                                                           | List[[models.ChatMessage](../models/chatmessage.md)]                 | :heavy_minus_sign:                                                   | N/A                                                                  |                                                                      |
| `chat_id`                                                            | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The id of the associated Chat the messages belong to, if one exists. |                                                                      |
| `follow_up_prompts`                                                  | List[*str*]                                                          | :heavy_minus_sign:                                                   | Follow-up prompts for the user to potentially use                    |                                                                      |
| `backend_time_millis`                                                | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Time in milliseconds the backend took to respond to the request.     | 1100                                                                 |
| `chat_session_tracking_token`                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | A token that is used to track the session.                           |                                                                      |