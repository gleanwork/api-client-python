# FileUploadConfig

Configuration settings for the chat file upload feature


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `enabled`                                                     | *Optional[bool]*                                              | :heavy_minus_sign:                                            | Whether file upload for Chat is enabled for the deployment    |
| `max_file_count`                                              | *Optional[int]*                                               | :heavy_minus_sign:                                            | Maximum number of files that can be uploaded in a single turn |
| `max_file_size`                                               | *Optional[int]*                                               | :heavy_minus_sign:                                            | Maximum file size, in bytes, that is allowed for upload       |
| `upload_timeout_seconds`                                      | *Optional[int]*                                               | :heavy_minus_sign:                                            | Timeout in seconds for polling the file upload status         |