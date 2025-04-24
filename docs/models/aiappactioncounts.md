# AiAppActionCounts

Map from action to frequency.


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `total_slackbot_responses`                                              | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | Total number of Slackbot responses, both proactive and reactive.        |
| `total_slackbot_responses_shared`                                       | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | Total number of Slackbot responses shared publicly (upvoted).           |
| `total_slackbot_responses_not_helpful`                                  | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | Total number of Slackbot responses rejected as not helpful (downvoted). |
| `total_chat_messages`                                                   | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | Total number of Chat messages sent in requested period.                 |
| `total_upvotes`                                                         | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | Total number of Chat messages which received upvotes by the user.       |
| `total_downvotes`                                                       | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | Total number of Chat messages which received downvotes by the user.     |
| `__pydantic_extra__`                                                    | Dict[str, *int*]                                                        | :heavy_minus_sign:                                                      | N/A                                                                     |