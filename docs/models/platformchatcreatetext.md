# PlatformChatCreateText

Optional configuration for the assistant's text response. When `format.type` is `JSON_SCHEMA`, the response is constrained to the supplied JSON schema and returned in `output[*].content[*].structured_output`. Structured output is not supported when `stream` is true.



## Fields

| Field                                                                                                                     | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `format_`                                                                                                                 | [Optional[models.PlatformChatCreateFormat]](../models/platformchatcreateformat.md)                                        | :heavy_minus_sign:                                                                                                        | Output format for the assistant text. TEXT is unconstrained. JSON_SCHEMA constrains the response to the supplied schema.<br/> |