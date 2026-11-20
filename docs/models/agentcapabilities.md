# AgentCapabilities

Describes features that the agent supports. example: {
  "ap.io.messages": true,
  "ap.io.streaming": true
}


## Fields

| Field                                                                                                                         | Type                                                                                                                          | Required                                                                                                                      | Description                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `ap_io_messages`                                                                                                              | *Optional[bool]*                                                                                                              | :heavy_minus_sign:                                                                                                            | Whether the agent supports messages as an input. If true, you'll pass `messages` as an input when running the agent.          |
| `ap_io_streaming`                                                                                                             | *Optional[bool]*                                                                                                              | :heavy_minus_sign:                                                                                                            | Whether the agent supports streaming output. If true, you you can stream agent ouput. All agents currently support streaming. |
| `__pydantic_extra__`                                                                                                          | Dict[str, *Any*]                                                                                                              | :heavy_minus_sign:                                                                                                            | N/A                                                                                                                           |