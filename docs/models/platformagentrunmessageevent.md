# PlatformAgentRunMessageEvent

A `message` event that carries agent output.


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `id`                                                                                     | *Optional[str]*                                                                          | :heavy_minus_sign:                                                                       | Event ID. IDs increase by one across the stream.                                         |
| `event`                                                                                  | *Literal["message"]*                                                                     | :heavy_check_mark:                                                                       | SSE event name. Always `message` for this event.                                         |
| `data`                                                                                   | [models.PlatformAgentRunMessageEventData](../models/platformagentrunmessageeventdata.md) | :heavy_check_mark:                                                                       | Payload for the Agents SSE event `message`.                                              |