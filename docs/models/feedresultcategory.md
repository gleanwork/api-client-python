# FeedResultCategory

Category of the result, one of the requested categories in incoming request.

## Example Usage

```python
from glean.api_client.models import FeedResultCategory

value = FeedResultCategory.DOCUMENT_SUGGESTION

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                                | Value                               |
| ----------------------------------- | ----------------------------------- |
| `DOCUMENT_SUGGESTION`               | DOCUMENT_SUGGESTION                 |
| `DOCUMENT_SUGGESTION_SCENARIO`      | DOCUMENT_SUGGESTION_SCENARIO        |
| `TRENDING_DOCUMENT`                 | TRENDING_DOCUMENT                   |
| `USE_CASE`                          | USE_CASE                            |
| `VERIFICATION_REMINDER`             | VERIFICATION_REMINDER               |
| `EVENT`                             | EVENT                               |
| `ANNOUNCEMENT`                      | ANNOUNCEMENT                        |
| `MENTION`                           | MENTION                             |
| `DATASOURCE_AFFINITY`               | DATASOURCE_AFFINITY                 |
| `RECENT`                            | RECENT                              |
| `COMPANY_RESOURCE`                  | COMPANY_RESOURCE                    |
| `EXPERIMENTAL`                      | EXPERIMENTAL                        |
| `PEOPLE_CELEBRATIONS`               | PEOPLE_CELEBRATIONS                 |
| `SOCIAL_LINK`                       | SOCIAL_LINK                         |
| `EXTERNAL_TASKS`                    | EXTERNAL_TASKS                      |
| `DISPLAYABLE_LIST`                  | DISPLAYABLE_LIST                    |
| `ZERO_STATE_CHAT_SUGGESTION`        | ZERO_STATE_CHAT_SUGGESTION          |
| `ZERO_STATE_CHAT_TOOL_SUGGESTION`   | ZERO_STATE_CHAT_TOOL_SUGGESTION     |
| `ZERO_STATE_WORKFLOW_CREATED_BY_ME` | ZERO_STATE_WORKFLOW_CREATED_BY_ME   |
| `ZERO_STATE_WORKFLOW_FAVORITES`     | ZERO_STATE_WORKFLOW_FAVORITES       |
| `ZERO_STATE_WORKFLOW_POPULAR`       | ZERO_STATE_WORKFLOW_POPULAR         |
| `ZERO_STATE_WORKFLOW_RECENT`        | ZERO_STATE_WORKFLOW_RECENT          |
| `ZERO_STATE_WORKFLOW_SUGGESTION`    | ZERO_STATE_WORKFLOW_SUGGESTION      |
| `PERSONALIZED_CHAT_SUGGESTION`      | PERSONALIZED_CHAT_SUGGESTION        |
| `DAILY_DIGEST`                      | DAILY_DIGEST                        |
| `TASK`                              | TASK                                |
| `PLAN_MY_DAY`                       | PLAN_MY_DAY                         |
| `END_MY_DAY`                        | END_MY_DAY                          |
| `STARTER_KIT`                       | STARTER_KIT                         |
| `MID_DAY_CATCH_UP`                  | MID_DAY_CATCH_UP                    |
| `QUERY_SUGGESTION`                  | QUERY_SUGGESTION                    |
| `COWORK_CUJ_PROMO`                  | COWORK_CUJ_PROMO                    |
| `WEEKLY_MEETINGS`                   | WEEKLY_MEETINGS                     |
| `FOLLOW_UP`                         | FOLLOW_UP                           |
| `MILESTONE_TIMELINE_CHECK`          | MILESTONE_TIMELINE_CHECK            |
| `PROJECT_DISCUSSION_DIGEST`         | PROJECT_DISCUSSION_DIGEST           |
| `PROJECT_FOCUS_BLOCK`               | PROJECT_FOCUS_BLOCK                 |
| `PROJECT_NEXT_STEP`                 | PROJECT_NEXT_STEP                   |
| `DEMO_CARD`                         | DEMO_CARD                           |
| `OOO_PLANNER`                       | OOO_PLANNER                         |