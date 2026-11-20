# PlatformDocumentsBatchWarningContext


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `index`                                                                          | *int*                                                                            | :heavy_check_mark:                                                               | Zero-based index into document_specs.                                            |
| `document_id`                                                                    | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Submitted document_id when the spec was an ID.                                   |
| `url`                                                                            | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Submitted URL when the spec was a URL. Empty when the caller sent an empty url.<br/> |