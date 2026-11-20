# CreateWorkflowRequest


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `name`                                            | *Optional[str]*                                   | :heavy_minus_sign:                                | The name of the workflow.                         |
| `transient`                                       | *Optional[bool]*                                  | :heavy_minus_sign:                                | Used to create a transient workflow.              |
| `parent_workflow_id`                              | *Optional[str]*                                   | :heavy_minus_sign:                                | id of the parent workflow for transient workflows |