# PlatformIdpGroupFilter

A filter on one IdP group field.


## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `field`                                                                                        | *str*                                                                                          | :heavy_check_mark:                                                                             | The IdP group field to filter on. The only supported field is provider_instance.<br/>          |
| `values`                                                                                       | List[*str*]                                                                                    | :heavy_check_mark:                                                                             | The values to match. An IdP group matches when any value matches.                              |
| `operator`                                                                                     | [Optional[models.PlatformIdpGroupFilterOperator]](../models/platformidpgroupfilteroperator.md) | :heavy_minus_sign:                                                                             | The only supported operator is EQUALS. Defaults to EQUALS.                                     |