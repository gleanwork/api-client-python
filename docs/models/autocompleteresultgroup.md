# AutocompleteResultGroup

A subsection of the results list from which distinct sections should be created.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `start_index`                                                        | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | The inclusive start index of the range.                              |
| `end_index`                                                          | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | The exclusive end index of the range.                                |
| `title`                                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The title of the result group to be displayed. Empty means no title. |