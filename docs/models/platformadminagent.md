# PlatformAdminAgent

An agent in the workspace.


## Fields

| Field                                                                                   | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `agent_id`                                                                              | *str*                                                                                   | :heavy_check_mark:                                                                      | Opaque agent ID. Other Platform APIs, such as usage limits, accept and return this ID.<br/> |
| `display_name`                                                                          | *str*                                                                                   | :heavy_check_mark:                                                                      | The name that Glean shows for the agent.                                                |
| `is_active`                                                                             | *bool*                                                                                  | :heavy_check_mark:                                                                      | Whether the agent is active. A deleted agent is inactive.                               |