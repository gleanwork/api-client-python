# IndexDocumentRequest

Describes the request body of the /indexdocument API call


## Fields

| Field                                                                                                           | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `version`                                                                                                       | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | Version number for document for optimistic concurrency control. If absent or 0 then no version checks are done. |
| `document`                                                                                                      | [models.DocumentDefinition](../models/documentdefinition.md)                                                    | :heavy_check_mark:                                                                                              | Indexable document structure                                                                                    |