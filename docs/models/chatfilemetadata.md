# ChatFileMetadata

Metadata of a file uploaded by a user for Chat.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `status`                                                                     | [Optional[models.ChatFileStatus]](../models/chatfilestatus.md)               | :heavy_minus_sign:                                                           | Current status of the file.                                                  |
| `upload_time`                                                                | *Optional[int]*                                                              | :heavy_minus_sign:                                                           | Upload time, in epoch seconds.                                               |
| `processed_size`                                                             | *Optional[int]*                                                              | :heavy_minus_sign:                                                           | Size of the processed file in bytes.                                         |
| `failure_reason`                                                             | [Optional[models.ChatFileFailureReason]](../models/chatfilefailurereason.md) | :heavy_minus_sign:                                                           | Reason for failed status.                                                    |
| `mime_type`                                                                  | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | MIME type of the file.                                                       |