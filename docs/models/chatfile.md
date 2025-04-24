# ChatFile

Structure for file uploaded by a user for Chat.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Unique identifier of the file.                                     | FILE_1234                                                          |
| `url`                                                              | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Url of the file.                                                   | www.google.com                                                     |
| `name`                                                             | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Name of the uploaded file.                                         | sample.pdf                                                         |
| `metadata`                                                         | [Optional[models.ChatFileMetadata]](../models/chatfilemetadata.md) | :heavy_minus_sign:                                                 | Metadata of a file uploaded by a user for Chat.                    |                                                                    |