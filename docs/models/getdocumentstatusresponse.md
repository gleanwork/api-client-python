# GetDocumentStatusResponse

Describes the response body of the /getdocumentstatus API call


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `upload_status`                                               | *Optional[str]*                                               | :heavy_minus_sign:                                            | Upload status, enum of NOT_UPLOADED, UPLOADED, STATUS_UNKNOWN |
| `last_uploaded_at`                                            | *Optional[int]*                                               | :heavy_minus_sign:                                            | Time of last successful upload, in epoch seconds              |
| `indexing_status`                                             | *Optional[str]*                                               | :heavy_minus_sign:                                            | Indexing status, enum of NOT_INDEXED, INDEXED, STATUS_UNKNOWN |
| `last_indexed_at`                                             | *Optional[int]*                                               | :heavy_minus_sign:                                            | Time of last successful indexing, in epoch seconds            |