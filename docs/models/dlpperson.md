# DlpPerson

Details about the person who created this report/policy.


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `name`                                                                  | *str*                                                                   | :heavy_check_mark:                                                      | The display name.                                                       |
| `obfuscated_id`                                                         | *str*                                                                   | :heavy_check_mark:                                                      | An opaque identifier that can be used to request metadata for a Person. |
| `metadata`                                                              | [Optional[models.DlpPersonMetadata]](../models/dlppersonmetadata.md)    | :heavy_minus_sign:                                                      | N/A                                                                     |