# PlatformAgentPrompt

A conversation starter whose template is sent as the first chat message.


## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `display_name`                                                                            | *str*                                                                                     | :heavy_check_mark:                                                                        | Short title of the conversation starter.                                                  |
| `template`                                                                                | *str*                                                                                     | :heavy_check_mark:                                                                        | Chat message that starts the conversation. May contain `[[variable_name]]` placeholders.<br/> |