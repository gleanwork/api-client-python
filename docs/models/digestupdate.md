# DigestUpdate


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `url`                                                                  | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | URL link to the content or document.                                   |
| `title`                                                                | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Title or headline of the update.                                       |
| `datasource`                                                           | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Name or identifier of the data source (e.g., slack, confluence, etc.). |
| `summary`                                                              | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Brief summary or description of the update content.                    |
| `type`                                                                 | [Optional[models.UpdateType]](../models/updatetype.md)                 | :heavy_minus_sign:                                                     | Optional type classification for the update.                           |