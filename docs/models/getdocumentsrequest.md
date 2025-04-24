# GetDocumentsRequest


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `document_specs`                                                                             | List[[models.DocumentSpecUnion](../models/documentspecunion.md)]                             | :heavy_check_mark:                                                                           | The specification for the documents to be retrieved.                                         |
| `include_fields`                                                                             | List[[models.GetDocumentsRequestIncludeField](../models/getdocumentsrequestincludefield.md)] | :heavy_minus_sign:                                                                           | List of Document fields to return (that aren't returned by default)                          |