# PreviewStructuredTextResponse


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `structured_text`                                    | [models.StructuredText](../models/structuredtext.md) | :heavy_check_mark:                                   | N/A                                                  |
| `docs_inaccessible_to_user`                          | List[*str*]                                          | :heavy_minus_sign:                                   | A list of links the user doesn't have access to.     |
| `combined_answer_text`                               | [models.StructuredText](../models/structuredtext.md) | :heavy_check_mark:                                   | N/A                                                  |