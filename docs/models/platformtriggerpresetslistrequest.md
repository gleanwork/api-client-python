# PlatformTriggerPresetsListRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `datasource`                                                       | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Restrict results to presets for a single datasource (e.g. github). |
| `page_size`                                                        | *Optional[int]*                                                    | :heavy_minus_sign:                                                 | Maximum number of presets to return.                               |
| `cursor`                                                           | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Opaque pagination cursor from a previous response.                 |