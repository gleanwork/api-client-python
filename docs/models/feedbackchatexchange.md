# FeedbackChatExchange


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `timestamp`                                                  | *Optional[int]*                                              | :heavy_minus_sign:                                           | Unix timestamp in millis for the chat request.               |
| `agent`                                                      | *Optional[str]*                                              | :heavy_minus_sign:                                           | Either DEFAULT (company knowledge) or GPT (world knowledge). |
| `user_query`                                                 | *Optional[str]*                                              | :heavy_minus_sign:                                           | Initial query entered by the user.                           |
| `search_query`                                               | *Optional[str]*                                              | :heavy_minus_sign:                                           | Search query performed by the agent.                         |
| `result_documents`                                           | List[[models.ResultDocument](../models/resultdocument.md)]   | :heavy_minus_sign:                                           | List of documents read by the agent.                         |
| `response`                                                   | *Optional[str]*                                              | :heavy_minus_sign:                                           | N/A                                                          |