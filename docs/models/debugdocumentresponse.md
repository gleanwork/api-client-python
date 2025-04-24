# DebugDocumentResponse

Describes the response body of the /debug/{datasource}/document API call


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `status`                                                                                     | [Optional[models.DocumentStatusResponse]](../models/documentstatusresponse.md)               | :heavy_minus_sign:                                                                           | Describes the document status response body                                                  |
| `uploaded_permissions`                                                                       | [Optional[models.DocumentPermissionsDefinition]](../models/documentpermissionsdefinition.md) | :heavy_minus_sign:                                                                           | describes the access control details of the document                                         |