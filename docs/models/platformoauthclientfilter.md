# PlatformOAuthClientFilter

A filter on one OAuth client field.


## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `field`                                                                                              | *str*                                                                                                | :heavy_check_mark:                                                                                   | The client field to filter on. The only supported field is is_active.                                |
| `values`                                                                                             | List[*str*]                                                                                          | :heavy_check_mark:                                                                                   | The values to match. A client matches when any value matches.                                        |
| `operator`                                                                                           | [Optional[models.PlatformOAuthClientFilterOperator]](../models/platformoauthclientfilteroperator.md) | :heavy_minus_sign:                                                                                   | The only supported operator is EQUALS. Defaults to EQUALS.                                           |