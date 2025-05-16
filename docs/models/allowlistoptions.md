# AllowlistOptions

Terms that are allow-listed during the scans. If any finding picked up by a rule exactly matches a term in the allow-list, it will not be counted as a violation.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `terms`                                                      | List[*str*]                                                  | :heavy_minus_sign:                                           | list of words and phrases to consider as whitelisted content |