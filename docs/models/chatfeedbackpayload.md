# ChatFeedbackPayload

Payload for chat feedback reporting. Required when template is `CHAT_FEEDBACK`.


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `rating`                                                                      | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | Rating given to the conversation (currently either "upvoted" or "downvoted"). |
| `issues`                                                                      | List[*str*]                                                                   | :heavy_minus_sign:                                                            | The type(s) of issue being reported.                                          |
| `comments`                                                                    | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | Additional freeform comments provided by the reporter.                        |
| `previous_messages`                                                           | List[*str*]                                                                   | :heavy_minus_sign:                                                            | Previous messages in this conversation.                                       |
| `chat_transcript`                                                             | List[[models.FeedbackChatExchange](../models/feedbackchatexchange.md)]        | :heavy_minus_sign:                                                            | N/A                                                                           |