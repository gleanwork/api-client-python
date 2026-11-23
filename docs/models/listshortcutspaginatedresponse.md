# ListShortcutsPaginatedResponse


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `shortcuts`                                                                    | List[[models.Shortcut](../models/shortcut.md)]                                 | :heavy_check_mark:                                                             | List of all shortcuts accessible to the user                                   |
| `facet_results`                                                                | List[[models.FacetResult](../models/facetresult.md)]                           | :heavy_minus_sign:                                                             | N/A                                                                            |
| `meta`                                                                         | [models.ShortcutsPaginationMetadata](../models/shortcutspaginationmetadata.md) | :heavy_check_mark:                                                             | N/A                                                                            |