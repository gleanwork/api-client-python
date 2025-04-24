# AskExperimentalMetadata


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `query_has_mentions`                                                     | *Optional[bool]*                                                         | :heavy_minus_sign:                                                       | Whether or not the query (i.e. the slack message) has a mention.         |
| `query_is_length_appropriate`                                            | *Optional[bool]*                                                         | :heavy_minus_sign:                                                       | Whether or not the query (i.e. the slack message) is length appropriate. |
| `query_is_answerable`                                                    | *Optional[bool]*                                                         | :heavy_minus_sign:                                                       | Whether or not the query (i.e. the slack message) has a question term.   |