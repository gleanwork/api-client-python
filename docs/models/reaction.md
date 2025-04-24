# Reaction


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `type`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `count`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The count of the reaction type on the document.                     |
| `reactors`                                                          | List[[models.Person](../models/person.md)]                          | :heavy_minus_sign:                                                  | N/A                                                                 |
| `reacted_by_viewer`                                                 | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Whether the user in context reacted with this type to the document. |