# ChatResult


## Fields

| Field                                                                                       | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `chat`                                                                                      | [Optional[models.Chat]](../models/chat.md)                                                  | :heavy_minus_sign:                                                                          | A historical representation of a series of chat messages a user had with Glean Assistant.   |
| `tracking_token`                                                                            | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | An opaque token that represents this particular Chat. To be used for `/feedback` reporting. |