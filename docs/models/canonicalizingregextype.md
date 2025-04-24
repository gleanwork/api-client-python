# CanonicalizingRegexType

Regular expression to apply to an arbitrary string to transform it into a canonical string.


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `match_regex`                                            | *Optional[str]*                                          | :heavy_minus_sign:                                       | Regular expression to match to an arbitrary string.      |
| `rewrite_regex`                                          | *Optional[str]*                                          | :heavy_minus_sign:                                       | Regular expression to transform into a canonical string. |