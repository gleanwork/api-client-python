# QueryInsight


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `query`                                                | *str*                                                  | :heavy_check_mark:                                     | The query string the information is about.             |
| `search_count`                                         | [Optional[models.CountInfo]](../models/countinfo.md)   | :heavy_minus_sign:                                     | N/A                                                    |
| `searchor_count`                                       | [Optional[models.CountInfo]](../models/countinfo.md)   | :heavy_minus_sign:                                     | N/A                                                    |
| `search_with_click_count`                              | [Optional[models.CountInfo]](../models/countinfo.md)   | :heavy_minus_sign:                                     | N/A                                                    |
| `click_count`                                          | [Optional[models.CountInfo]](../models/countinfo.md)   | :heavy_minus_sign:                                     | N/A                                                    |
| `similar_queries`                                      | List[[models.QueryInsight](../models/queryinsight.md)] | :heavy_minus_sign:                                     | list of similar queries to current one.                |