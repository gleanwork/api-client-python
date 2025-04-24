# AnswerLike


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `user`                                                               | [Optional[models.Person]](../models/person.md)                       | :heavy_minus_sign:                                                   | N/A                                                                  | {<br/>"name": "George Clooney",<br/>"obfuscatedId": "abc123"<br/>}   |
| `create_time`                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The time the user liked the answer in ISO format (ISO 8601).         |                                                                      |