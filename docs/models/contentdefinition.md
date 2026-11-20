# ContentDefinition

Describes text content or base64 encoded binary content


## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `mime_type`                                                                               | *str*                                                                                     | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `text_content`                                                                            | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | text content. Only one of textContent or binary content can be specified                  |
| `binary_content`                                                                          | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | base64 encoded binary content. Only one of textContent or binary content can be specified |