# Disambiguation

A disambiguation between multiple entities with the same name


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `name`                                                 | *Optional[str]*                                        | :heavy_minus_sign:                                     | Name of the ambiguous entity                           |
| `id`                                                   | *Optional[str]*                                        | :heavy_minus_sign:                                     | The unique id of the entity in the knowledge graph     |
| `type`                                                 | [Optional[models.EntityType]](../models/entitytype.md) | :heavy_minus_sign:                                     | The type of entity.                                    |