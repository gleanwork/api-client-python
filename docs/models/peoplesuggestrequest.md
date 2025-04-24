# PeopleSuggestRequest

Includes request params for type of suggestions.


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `categories`                                                                        | List[[models.PeopleSuggestionCategory](../models/peoplesuggestioncategory.md)]      | :heavy_check_mark:                                                                  | Categories of data requested. Request can include single or multiple categories.    |
| `departments`                                                                       | List[*str*]                                                                         | :heavy_minus_sign:                                                                  | Departments that the data is requested for. If empty, corresponds to whole company. |