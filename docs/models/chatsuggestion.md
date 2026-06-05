# ChatSuggestion


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `query`                                                                 | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | The actionable chat query to run when the user selects this suggestion. |
| `cta`                                                                   | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Button text to show for the suggestion action.                          |
| `feature`                                                               | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Targeted Glean Chat feature for the suggestion.                         |
| `source_document_ids`                                                   | List[*str*]                                                             | :heavy_minus_sign:                                                      | Document IDs that grounded the suggestion.                              |