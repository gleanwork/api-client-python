# InviteRequest

A request to send an invite to the specified user[s]


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `channel`                                                                    | [Optional[models.CommunicationChannel]](../models/communicationchannel.md)   | :heavy_minus_sign:                                                           | N/A                                                                          |
| `template`                                                                   | [Optional[models.CommunicationTemplate]](../models/communicationtemplate.md) | :heavy_minus_sign:                                                           | The type of email to send                                                    |
| `recipients`                                                                 | List[[models.Person](../models/person.md)]                                   | :heavy_minus_sign:                                                           | The people who should receive this invite                                    |
| `recipient_filters`                                                          | [Optional[models.PeopleFilters]](../models/peoplefilters.md)                 | :heavy_minus_sign:                                                           | N/A                                                                          |