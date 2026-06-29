# AllowlistOptions

Terms and regexes that are allow-listed during the scans. If any finding picked up by a rule exactly matches a term, or matches a regex, in the allow-list, it will not be counted as a violation.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `terms`                                                                      | List[*str*]                                                                  | :heavy_minus_sign:                                                           | list of words and phrases to consider as whitelisted content                 |
| `regexes`                                                                    | List[*str*]                                                                  | :heavy_minus_sign:                                                           | list of regular expressions whose matches are considered whitelisted content |