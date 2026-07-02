# PlatformSearchResponse


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `results`                                                    | List[[models.PlatformResult](../models/platformresult.md)]   | :heavy_check_mark:                                           | Ordered list of search results.                              |
| `has_more`                                                   | *bool*                                                       | :heavy_check_mark:                                           | Indicates whether additional pages of results are available. |
| `next_cursor`                                                | *Nullable[str]*                                              | :heavy_check_mark:                                           | Opaque token to pass as `cursor` in the next request.        |
| `request_id`                                                 | *str*                                                        | :heavy_check_mark:                                           | Platform-generated request ID for support correlation.       |