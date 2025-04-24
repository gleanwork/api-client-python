# PreviewShortcutResponse


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `shortcut`                                                   | [Optional[models.Shortcut]](../models/shortcut.md)           | :heavy_minus_sign:                                           | N/A                                                          |
| `existing_url_shortcuts`                                     | List[[models.Shortcut](../models/shortcut.md)]               | :heavy_minus_sign:                                           | Exising shortcuts that have a similar destination URL.       |
| `error`                                                      | [Optional[models.ShortcutError]](../models/shortcuterror.md) | :heavy_minus_sign:                                           | N/A                                                          |