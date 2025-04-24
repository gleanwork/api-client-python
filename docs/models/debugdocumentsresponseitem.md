# DebugDocumentsResponseItem

Describes the response body of a single document in the /debug/{datasource}/documents API call


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `doc_id`                                                                     | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Id of the document                                                           |
| `object_type`                                                                | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | objectType of the document                                                   |
| `debug_info`                                                                 | [Optional[models.DebugDocumentResponse]](../models/debugdocumentresponse.md) | :heavy_minus_sign:                                                           | Describes the response body of the /debug/{datasource}/document API call     |