# WorkflowInputField

Input field argument of a workflow.


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `name`                                                         | *Optional[str]*                                                | :heavy_minus_sign:                                             | The name of the input.                                         |
| `display_name`                                                 | *Optional[str]*                                                | :heavy_minus_sign:                                             | Name of the field as displayed to the user.                    |
| `description`                                                  | *Optional[str]*                                                | :heavy_minus_sign:                                             | Description of the field.                                      |
| `default_value`                                                | *Optional[str]*                                                | :heavy_minus_sign:                                             | Default value for the field.                                   |
| `optional`                                                     | *Optional[bool]*                                               | :heavy_minus_sign:                                             | Whether this field is optional.                                |
| `type`                                                         | [Optional[models.InputFieldType]](../models/inputfieldtype.md) | :heavy_minus_sign:                                             | N/A                                                            |
| `options`                                                      | List[[models.InputFieldOption](../models/inputfieldoption.md)] | :heavy_minus_sign:                                             | Options for SELECT field type.                                 |