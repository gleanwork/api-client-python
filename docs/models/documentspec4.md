# DocumentSpec4


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `ugc_type`                                                       | [models.DocumentSpecUgcType2](../models/documentspecugctype2.md) | :heavy_check_mark:                                               | The type of the user generated content (UGC datasource).         |
| `ugc_id`                                                         | *str*                                                            | :heavy_check_mark:                                               | The string id for user generated content. Used for CHATS.        |
| `doc_type`                                                       | *Optional[str]*                                                  | :heavy_minus_sign:                                               | The specific type of the user generated content type.            |