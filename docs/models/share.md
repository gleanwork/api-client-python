# Share

Search endpoint will only fill out numDays ago since that's all we need to display shared badge; docmetadata endpoint will fill out all the fields so that we can display shared badge tooltip


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 | Example                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `num_days_ago`                                              | *int*                                                       | :heavy_check_mark:                                          | The number of days that has passed since the share happened |                                                             |
| `sharer`                                                    | [Optional[models.Person]](../models/person.md)              | :heavy_minus_sign:                                          | N/A                                                         | {<br/>"name": "George Clooney",<br/>"obfuscatedId": "abc123"<br/>} |
| `sharing_document`                                          | [Optional[models.Document]](../models/document.md)          | :heavy_minus_sign:                                          | N/A                                                         |                                                             |