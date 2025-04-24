# ClientUser
(*client.user*)

## Overview

### Available Operations

* [add_credential](#add_credential) - Create credentials
* [delete_query_history](#delete_query_history) - Delete query history
* [invite](#invite) - Send invitation
* [get_public_config](#get_public_config) - Read public client configuration
* [remove_credential](#remove_credential) - Delete credentials
* [send_support_email](#send_support_email) - Send support email

## add_credential

API to save a user's credentials. Used for Confluence restricted pages and Tableau per-user auth, for example

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.client.user.add_credential()

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `datasource`                                                                                                             | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | the datasource the credential applies to                                                                                 |
| `datasource_instance`                                                                                                    | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | the datasource instance the credential applies to                                                                        |
| `user`                                                                                                                   | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | the user info (email or username for example) for the credential                                                         |
| `token`                                                                                                                  | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | the token part of the credential (password, apiToken etc)                                                                |
| `metadata`                                                                                                               | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | any metadata associated with the user credential                                                                         |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## delete_query_history

Remove one or more queries from a user's query history.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.user.delete_query_history()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `queries`                                                                                                                | List[*str*]                                                                                                              | :heavy_minus_sign:                                                                                                       | Queries to delete.                                                                                                       |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.DeleteQueryHistoryResponse](../../models/deletequeryhistoryresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## invite

Invites people to Glean via email or Slack

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.client.user.invite(recipients=[
        models.Person(
            name="George Clooney",
            obfuscated_id="abc123",
        ),
    ], recipient_filters={
        "filter_": [
            {
                "field_name": "type",
                "values": [
                    {
                        "value": "Spreadsheet",
                        "relation_type": models.RelationType.EQUALS,
                    },
                    {
                        "value": "Presentation",
                        "relation_type": models.RelationType.EQUALS,
                    },
                ],
            },
        ],
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `channel`                                                                                                                | [Optional[models.CommunicationChannel]](../../models/communicationchannel.md)                                            | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |
| `template`                                                                                                               | [Optional[models.CommunicationTemplate]](../../models/communicationtemplate.md)                                          | :heavy_minus_sign:                                                                                                       | The type of email to send                                                                                                |
| `recipients`                                                                                                             | List[[models.Person](../../models/person.md)]                                                                            | :heavy_minus_sign:                                                                                                       | The people who should receive this invite                                                                                |
| `recipient_filters`                                                                                                      | [Optional[models.PeopleFilters]](../../models/peoplefilters.md)                                                          | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## get_public_config

Read configuration information such as the company name, logo and etc that is public and is not considered as PII.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.user.get_public_config()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `public_config_request`                                                                                                  | [Optional[models.PublicConfigRequest]](../../models/publicconfigrequest.md)                                              | :heavy_minus_sign:                                                                                                       | Public Config request                                                                                                    |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.ClientConfig](../../models/clientconfig.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## remove_credential

Delete a user's credentials. Used for Confluence restricted pages and Tableau per-user auth, for example

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.client.user.remove_credential()

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `datasource`                                                                                                             | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | the datasource the credential applies to                                                                                 |
| `datasource_instance`                                                                                                    | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | the datasource instance the credential applies to                                                                        |
| `user`                                                                                                                   | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | the user info (email or username for example) for the credential                                                         |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## send_support_email

Sends a support email based on a template to the Glean support team.

### Example Usage

```python
from datetime import date
from glean import Glean, models
from glean.utils import parse_datetime
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.client.user.send_support_email(email_template=models.CommunicationTemplate.ONBOARDING_TIPS, recipients=[
        models.Person(
            name="George Clooney",
            obfuscated_id="abc123",
        ),
    ], cc_recipients=[
        models.Person(
            name="George Clooney",
            obfuscated_id="abc123",
        ),
    ], recipient_filters={
        "filter_": [
            {
                "field_name": "type",
                "values": [
                    {
                        "value": "Spreadsheet",
                        "relation_type": models.RelationType.EQUALS,
                    },
                    {
                        "value": "Presentation",
                        "relation_type": models.RelationType.EQUALS,
                    },
                ],
            },
        ],
    }, senders=[
        models.Person(
            name="George Clooney",
            obfuscated_id="abc123",
        ),
    ], documents=[
        models.Document(
            metadata=models.DocumentMetadata(
                datasource="datasource",
                object_type="Feature Request",
                container="container",
                parent_id="JIRA_EN-1337",
                mime_type="mimeType",
                document_id="documentId",
                create_time=parse_datetime("2000-01-23T04:56:07.000Z"),
                update_time=parse_datetime("2000-01-23T04:56:07.000Z"),
                author=models.Person(
                    name="George Clooney",
                    obfuscated_id="abc123",
                    related_documents=[],
                    metadata=models.PersonMetadata(
                        type=models.PersonMetadataType.FULL_TIME,
                        title="Actor",
                        department="Movies",
                        email="george@example.com",
                        location="Hollywood, CA",
                        phone="6505551234",
                        photo_url="https://example.com/george.jpg",
                        start_date=date.fromisoformat("2000-01-23"),
                        datasource_profile=[
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                        ],
                        query_suggestions=models.QuerySuggestionList(
                            suggestions=[],
                        ),
                        invite_info=models.InviteInfo(
                            invites=[],
                        ),
                        custom_fields=[],
                        badges=[
                            models.Badge(
                                key="deployment_name_new_hire",
                                display_name="New hire",
                                icon_config=models.IconConfig(
                                    color="#343CED",
                                    key="person_icon",
                                    icon_type=models.IconType.GLYPH,
                                    name="user",
                                ),
                            ),
                        ],
                    ),
                ),
                owner=models.Person(
                    name="George Clooney",
                    obfuscated_id="abc123",
                ),
                mentioned_people=[],
                components=[
                    "Backend",
                    "Networking",
                ],
                status="[\"Done\"]",
                pins=[],
                assigned_to=models.Person(
                    name="George Clooney",
                    obfuscated_id="abc123",
                ),
                updated_by=models.Person(
                    name="George Clooney",
                    obfuscated_id="abc123",
                ),
                collections=[],
                interactions=models.DocumentInteractions(
                    reacts=[],
                    shares=[],
                ),
                verification=models.Verification(
                    state=models.State.DEPRECATED,
                    metadata=models.VerificationMetadata(
                        last_verifier=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                        ),
                        reminders=[],
                        last_reminder=models.Reminder(
                            assignee=models.Person(
                                name="George Clooney",
                                obfuscated_id="abc123",
                            ),
                            requestor=models.Person(
                                name="George Clooney",
                                obfuscated_id="abc123",
                            ),
                            remind_at=631645,
                        ),
                        candidate_verifiers=[],
                    ),
                ),
                custom_data={
                    "someCustomField": models.CustomDataValue(),
                },
                contact_person=models.Person(
                    name="George Clooney",
                    obfuscated_id="abc123",
                ),
            ),
        ),
        models.Document(),
    ], feedback_payload={
        "custom_json": "{\"comment\": \"glean is awesome!\", \"sender\": \"happycustomer@customer.com\"}",
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `email_template`                                                                                                                                 | [models.CommunicationTemplate](../../models/communicationtemplate.md)                                                                            | :heavy_check_mark:                                                                                                                               | The type of email to send                                                                                                                        |
| `x_scio_actas`                                                                                                                                   | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).                         |
| `x_glean_auth_type`                                                                                                                              | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                                        |
| `alert_data`                                                                                                                                     | [Optional[models.AlertData]](../../models/alertdata.md)                                                                                          | :heavy_minus_sign:                                                                                                                               | Admin alert related information that is used to construct the admin alert email                                                                  |
| `recipients`                                                                                                                                     | List[[models.Person](../../models/person.md)]                                                                                                    | :heavy_minus_sign:                                                                                                                               | The people to send emails to                                                                                                                     |
| `cc_recipients`                                                                                                                                  | List[[models.Person](../../models/person.md)]                                                                                                    | :heavy_minus_sign:                                                                                                                               | The people to CC for each email                                                                                                                  |
| `recipient_filters`                                                                                                                              | [Optional[models.PeopleFilters]](../../models/peoplefilters.md)                                                                                  | :heavy_minus_sign:                                                                                                                               | N/A                                                                                                                                              |
| `company_name`                                                                                                                                   | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | Name of the company.                                                                                                                             |
| `datasource_instance`                                                                                                                            | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | The instance ID of the datasource (if any)                                                                                                       |
| `senders`                                                                                                                                        | List[[models.Person](../../models/person.md)]                                                                                                    | :heavy_minus_sign:                                                                                                                               | The people who triggered this email                                                                                                              |
| `web_app_url`                                                                                                                                    | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | The URL of the client triggering the request, as received in the ClientConfig                                                                    |
| `server_url`                                                                                                                                     | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | The URL of the QE instance the email request is processed by.                                                                                    |
| `unsubscribe_url`                                                                                                                                | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | The URL to unsubscribe from emails.                                                                                                              |
| `documents`                                                                                                                                      | List[[models.Document](../../models/document.md)]                                                                                                | :heavy_minus_sign:                                                                                                                               | The documents this email request refers to                                                                                                       |
| `reasons`                                                                                                                                        | List[*str*]                                                                                                                                      | :heavy_minus_sign:                                                                                                                               | Reasons this email request was sent. Will be shown directly to end user.                                                                         |
| `blocks`                                                                                                                                         | Dict[str, List[[models.Block](../../models/block.md)]]                                                                                           | :heavy_minus_sign:                                                                                                                               | For building complex email UIs, we use a block structure that dictates what we create in the UI                                                  |
| `subjects`                                                                                                                                       | Dict[str, *str*]                                                                                                                                 | :heavy_minus_sign:                                                                                                                               | Mapping of recipientIds to the email subject they are to receive. Optional and only meant for templates with Sendgrid subject set to {{subject}} |
| `feedback_payload`                                                                                                                               | [Optional[models.FeedbackPayload]](../../models/feedbackpayload.md)                                                                              | :heavy_minus_sign:                                                                                                                               | Optional payload for feedback reporting.                                                                                                         |
| `chat_feedback_payload`                                                                                                                          | [Optional[models.ChatFeedbackPayload]](../../models/chatfeedbackpayload.md)                                                                      | :heavy_minus_sign:                                                                                                                               | Payload for chat feedback reporting. Required when template is `CHAT_FEEDBACK`.                                                                  |
| `dlp_report_data`                                                                                                                                | [Optional[models.DlpReportData]](../../models/dlpreportdata.md)                                                                                  | :heavy_minus_sign:                                                                                                                               | Dlp report metadata which is used to construct report email                                                                                      |
| `onboarding_admin_invite_data`                                                                                                                   | [Optional[models.OnboardingAdminInviteData]](../../models/onboardingadmininvitedata.md)                                                          | :heavy_minus_sign:                                                                                                                               | N/A                                                                                                                                              |
| `retries`                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                 | :heavy_minus_sign:                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                              |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |