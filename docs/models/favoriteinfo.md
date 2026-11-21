# FavoriteInfo


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `ugc_type`                                         | [Optional[models.UgcType]](../models/ugctype.md)   | :heavy_minus_sign:                                 | N/A                                                |
| `id`                                               | *Optional[str]*                                    | :heavy_minus_sign:                                 | Opaque id of the UGC.                              |
| `count`                                            | *Optional[int]*                                    | :heavy_minus_sign:                                 | Number of users this object has been favorited by. |
| `favorited_by_user`                                | *Optional[bool]*                                   | :heavy_minus_sign:                                 | If the requesting user has favorited this object.  |