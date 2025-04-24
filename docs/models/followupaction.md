# FollowupAction

A follow-up action that can be invoked by the user after a response. The action parameters are not included and need to be predicted/filled separately.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `action_run_id`                                                                | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | Unique identifier for this actionRun recommendation event.                     |
| `action_instance_id`                                                           | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | The ID of the action instance that will be invoked.                            |
| `action_id`                                                                    | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | The ID of the associated action.                                               |
| `recommendation_text`                                                          | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | Text to be displayed to the user when recommending the action instance.        |
| `action_label`                                                                 | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | The label to be used when displaying a button to execute this action instance. |
| `user_confirmation_required`                                                   | *Optional[bool]*                                                               | :heavy_minus_sign:                                                             | Whether user confirmation is needed before executing this action instance.     |