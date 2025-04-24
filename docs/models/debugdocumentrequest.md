# DebugDocumentRequest

Describes the request body of the /debug/{datasource}/document API call.


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `object_type`                                                  | *str*                                                          | :heavy_check_mark:                                             | Object type of the document to get the status for.             | Article                                                        |
| `doc_id`                                                       | *str*                                                          | :heavy_check_mark:                                             | Glean Document ID within the datasource to get the status for. | art123                                                         |