# PlatformTriggerPresetEventSearchRequest


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 | Example                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `inputs`                                                    | Dict[str, *str*]                                            | :heavy_minus_sign:                                          | Values for the preset's input fields, keyed by field name.<br/> | {<br/>"repository": "acme/payments-api"<br/>}               |
| `page_size`                                                 | *Optional[int]*                                             | :heavy_minus_sign:                                          | Maximum number of events to return.                         |                                                             |