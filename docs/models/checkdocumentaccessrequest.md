# CheckDocumentAccessRequest

Describes the request body of the /checkdocumentaccess API call


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `datasource`                                 | *str*                                        | :heavy_check_mark:                           | Datasource of document to check access for.  |
| `object_type`                                | *str*                                        | :heavy_check_mark:                           | Object type of document to check access for. |
| `doc_id`                                     | *str*                                        | :heavy_check_mark:                           | Glean Document ID to check access for.       |
| `user_email`                                 | *str*                                        | :heavy_check_mark:                           | Email of user to check access for.           |