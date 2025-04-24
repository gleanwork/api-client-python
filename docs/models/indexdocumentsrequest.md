# IndexDocumentsRequest

Describes the request body of the /indexdocuments API call


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `upload_id`                                                        | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Optional id parameter to identify and track a batch of documents.  |
| `datasource`                                                       | *str*                                                              | :heavy_check_mark:                                                 | Datasource of the documents                                        |
| `documents`                                                        | List[[models.DocumentDefinition](../models/documentdefinition.md)] | :heavy_check_mark:                                                 | Batch of documents being added/updated                             |