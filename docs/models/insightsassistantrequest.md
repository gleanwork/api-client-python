# InsightsAssistantRequest


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `departments`                                                                      | List[*str*]                                                                        | :heavy_minus_sign:                                                                 | Departments for which Insights are requested.                                      |
| `manager_emails`                                                                   | List[*str*]                                                                        | :heavy_minus_sign:                                                                 | Manager emails whose teams should be filtered for. Empty array means no filtering. |
| `day_range`                                                                        | [Optional[models.Period]](../models/period.md)                                     | :heavy_minus_sign:                                                                 | N/A                                                                                |