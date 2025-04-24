# DocumentStatusResponse

Describes the document status response body


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `upload_status`                                                       | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Upload status, enum of NOT_UPLOADED, UPLOADED, STATUS_UNKNOWN         | UPLOADED                                                              |
| `last_uploaded_at`                                                    | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Time of last successful upload for the document, in ISO 8601 format   | 2021-08-06T17:58:01.000Z                                              |
| `indexing_status`                                                     | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Indexing status, enum of NOT_INDEXED, INDEXED, STATUS_UNKNOWN         | INDEXED                                                               |
| `last_indexed_at`                                                     | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Time of last successful indexing for the document, in ISO 8601 format | 2021-08-06T17:58:01.000Z                                              |