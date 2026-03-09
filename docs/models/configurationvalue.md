# ConfigurationValue

A single configuration value, either a scalar or a list


## Fields

| Field                                                                                             | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `value`                                                                                           | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | The configuration value as a string. Only one of value or valueList should be populated.          |
| `value_list`                                                                                      | List[*str*]                                                                                       | :heavy_minus_sign:                                                                                | The configuration value as a list of strings. Only one of value or valueList should be populated. |