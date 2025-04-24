# Answers
(*client.answers*)

## Overview

### Available Operations

* [create](#create) - Create Answer
* [delete](#delete) - Delete Answer
* [edit](#edit) - Update Answer
* [get](#get) - Read Answer
* [list](#list) - List Answers
* [preview](#preview) - Preview Answer
* [preview_draft](#preview_draft) - Preview draft Answer
* [update_likes](#update_likes) - Update Answer likes
* [~~create_board~~](#create_board) - Create Answer Board :warning: **Deprecated**
* [~~delete_board~~](#delete_board) - Delete Answer Board :warning: **Deprecated**
* [~~update_board~~](#update_board) - Update Answer Board :warning: **Deprecated**
* [~~get_board~~](#get_board) - Read Answer Board :warning: **Deprecated**
* [~~list_boards~~](#list_boards) - List Answer Boards :warning: **Deprecated**

## create

Create a user-generated Answer that contains a question and answer.

### Example Usage

```python
from datetime import date
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.answers.create(data={
        "question": "Why is the sky blue?",
        "body_text": "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.",
        "audience_filters": [
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
        "added_roles": [
            models.UserRoleSpecification(
                person=models.Person(
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
                role=models.UserRole.OWNER,
            ),
            models.UserRoleSpecification(
                role=models.UserRole.VERIFIER,
            ),
        ],
        "removed_roles": [
            models.UserRoleSpecification(
                role=models.UserRole.VERIFIER,
            ),
            models.UserRoleSpecification(
                role=models.UserRole.ANSWER_MODERATOR,
            ),
            models.UserRoleSpecification(
                role=models.UserRole.OWNER,
            ),
        ],
        "roles": [
            models.UserRoleSpecification(
                role=models.UserRole.ANSWER_MODERATOR,
            ),
            models.UserRoleSpecification(
                role=models.UserRole.OWNER,
            ),
            models.UserRoleSpecification(
                role=models.UserRole.VERIFIER,
            ),
        ],
        "combined_answer_text": {
            "text": "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `data`                                                                                                                   | [models.AnswerCreationData](../../models/answercreationdata.md)                                                          | :heavy_check_mark:                                                                                                       | N/A                                                                                                                      |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.Answer](../../models/answer.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## delete

Delete an existing user-generated Answer.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.client.answers.delete(id=3, doc_id="ANSWERS_answer_3")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                   | Type                                                                                                                                                                        | Required                                                                                                                                                                    | Description                                                                                                                                                                 | Example                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                        | *int*                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                          | The opaque ID of the Answer.                                                                                                                                                | 3                                                                                                                                                                           |
| `x_scio_actas`                                                                                                                                                              | *Optional[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).                                                    |                                                                                                                                                                             |
| `x_glean_auth_type`                                                                                                                                                         | *Optional[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                                                                   |                                                                                                                                                                             |
| `doc_id`                                                                                                                                                                    | *Optional[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | Glean Document ID of the Answer. The Glean Document ID is supported for cases where the Answer ID isn't available. If both are available, using the Answer ID is preferred. | ANSWERS_answer_3                                                                                                                                                            |
| `retries`                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                            | :heavy_minus_sign:                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                         |                                                                                                                                                                             |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## edit

Update an existing user-generated Answer.

### Example Usage

```python
from datetime import date
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.answers.edit(id=3, doc_id="ANSWERS_answer_3", question="Why is the sky blue?", body_text="From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.", audience_filters=[
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
    ], added_roles=[
        models.UserRoleSpecification(
            person=models.Person(
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
            role=models.UserRole.EDITOR,
        ),
    ], removed_roles=[
        models.UserRoleSpecification(
            person=models.Person(
                name="George Clooney",
                obfuscated_id="abc123",
                related_documents=[],
                metadata=models.PersonMetadata(
                    type=models.PersonMetadataType.FULL_TIME,
                    title="Actor",
                    department="Movies",
                    email="george@example.com",
                    location="Hollywood, CA",
                    management_chain=[],
                    phone="6505551234",
                    photo_url="https://example.com/george.jpg",
                    reports=[],
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
            role=models.UserRole.EDITOR,
        ),
    ], roles=[
        models.UserRoleSpecification(
            person=models.Person(
                name="George Clooney",
                obfuscated_id="abc123",
                related_documents=[],
                metadata=models.PersonMetadata(
                    type=models.PersonMetadataType.FULL_TIME,
                    title="Actor",
                    department="Movies",
                    email="george@example.com",
                    location="Hollywood, CA",
                    management_chain=[],
                    phone="6505551234",
                    photo_url="https://example.com/george.jpg",
                    reports=[],
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
            role=models.UserRole.ANSWER_MODERATOR,
        ),
        models.UserRoleSpecification(
            role=models.UserRole.OWNER,
        ),
    ], combined_answer_text={
        "text": "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                   | Type                                                                                                                                                                        | Required                                                                                                                                                                    | Description                                                                                                                                                                 | Example                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                        | *int*                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                          | The opaque ID of the Answer.                                                                                                                                                | 3                                                                                                                                                                           |
| `x_scio_actas`                                                                                                                                                              | *Optional[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).                                                    |                                                                                                                                                                             |
| `x_glean_auth_type`                                                                                                                                                         | *Optional[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                                                                   |                                                                                                                                                                             |
| `doc_id`                                                                                                                                                                    | *Optional[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | Glean Document ID of the Answer. The Glean Document ID is supported for cases where the Answer ID isn't available. If both are available, using the Answer ID is preferred. | ANSWERS_answer_3                                                                                                                                                            |
| `question`                                                                                                                                                                  | *Optional[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | N/A                                                                                                                                                                         | Why is the sky blue?                                                                                                                                                        |
| `question_variations`                                                                                                                                                       | List[*str*]                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                          | Additional ways of phrasing this question.                                                                                                                                  |                                                                                                                                                                             |
| `body_text`                                                                                                                                                                 | *Optional[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | The plain text answer to the question.                                                                                                                                      | From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.                       |
| `board_id`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | The parent board ID of this Answer, or 0 if it's a floating Answer.                                                                                                         |                                                                                                                                                                             |
| `audience_filters`                                                                                                                                                          | List[[models.FacetFilter](../../models/facetfilter.md)]                                                                                                                     | :heavy_minus_sign:                                                                                                                                                          | Filters which restrict who should see the answer. Values are taken from the corresponding filters in people search.                                                         |                                                                                                                                                                             |
| `added_roles`                                                                                                                                                               | List[[models.UserRoleSpecification](../../models/userrolespecification.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                                          | A list of user roles for the answer added by the owner.                                                                                                                     |                                                                                                                                                                             |
| `removed_roles`                                                                                                                                                             | List[[models.UserRoleSpecification](../../models/userrolespecification.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                                          | A list of user roles for the answer removed by the owner.                                                                                                                   |                                                                                                                                                                             |
| `roles`                                                                                                                                                                     | List[[models.UserRoleSpecification](../../models/userrolespecification.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                                          | A list of roles for this answer explicitly granted by an owner, editor, or admin.                                                                                           |                                                                                                                                                                             |
| `source_document_spec`                                                                                                                                                      | [Optional[models.DocumentSpecUnion]](../../models/documentspecunion.md)                                                                                                     | :heavy_minus_sign:                                                                                                                                                          | N/A                                                                                                                                                                         |                                                                                                                                                                             |
| `source_type`                                                                                                                                                               | [Optional[models.EditAnswerRequestSourceType]](../../models/editanswerrequestsourcetype.md)                                                                                 | :heavy_minus_sign:                                                                                                                                                          | N/A                                                                                                                                                                         |                                                                                                                                                                             |
| `added_collections`                                                                                                                                                         | List[*int*]                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                          | IDs of Collections to which a document is added.                                                                                                                            |                                                                                                                                                                             |
| `removed_collections`                                                                                                                                                       | List[*int*]                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                          | IDs of Collections from which a document is removed.                                                                                                                        |                                                                                                                                                                             |
| `combined_answer_text`                                                                                                                                                      | [Optional[models.StructuredTextMutableProperties]](../../models/structuredtextmutableproperties.md)                                                                         | :heavy_minus_sign:                                                                                                                                                          | N/A                                                                                                                                                                         |                                                                                                                                                                             |
| `retries`                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                            | :heavy_minus_sign:                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                         |                                                                                                                                                                             |

### Response

**[models.Answer](../../models/answer.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## get

Read the details of a particular Answer given its ID.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.answers.get(id=3, doc_id="ANSWERS_answer_3")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                   | Type                                                                                                                                                                        | Required                                                                                                                                                                    | Description                                                                                                                                                                 | Example                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `x_scio_actas`                                                                                                                                                              | *Optional[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).                                                    |                                                                                                                                                                             |
| `x_glean_auth_type`                                                                                                                                                         | *Optional[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                                                                   |                                                                                                                                                                             |
| `id`                                                                                                                                                                        | *Optional[int]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | The opaque ID of the Answer.                                                                                                                                                | 3                                                                                                                                                                           |
| `doc_id`                                                                                                                                                                    | *Optional[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | Glean Document ID of the Answer. The Glean Document ID is supported for cases where the Answer ID isn't available. If both are available, using the Answer ID is preferred. | ANSWERS_answer_3                                                                                                                                                            |
| `retries`                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                            | :heavy_minus_sign:                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                         |                                                                                                                                                                             |

### Response

**[models.GetAnswerResponse](../../models/getanswerresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## list

List Answers created by the current user.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.answers.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `board_id`                                                                                                               | *Optional[int]*                                                                                                          | :heavy_minus_sign:                                                                                                       | The Answer Board Id to list answers on.                                                                                  |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.ListAnswersResponse](../../models/listanswersresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## preview

Generate a preview for a user-generated Answer that contains a question and answer.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.answers.preview(text="From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                             | Type                                                                                                                                                  | Required                                                                                                                                              | Description                                                                                                                                           | Example                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `text`                                                                                                                                                | *str*                                                                                                                                                 | :heavy_check_mark:                                                                                                                                    | N/A                                                                                                                                                   | From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light. |
| `x_scio_actas`                                                                                                                                        | *Optional[str]*                                                                                                                                       | :heavy_minus_sign:                                                                                                                                    | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).                              |                                                                                                                                                       |
| `x_glean_auth_type`                                                                                                                                   | *Optional[str]*                                                                                                                                       | :heavy_minus_sign:                                                                                                                                    | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                                             |                                                                                                                                                       |
| `retries`                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                      | :heavy_minus_sign:                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                   |                                                                                                                                                       |

### Response

**[models.PreviewStructuredTextResponse](../../models/previewstructuredtextresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## preview_draft

Generate a preview for a user-generated answer from a draft.

### Example Usage

```python
from datetime import date
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.answers.preview_draft(draft=models.UgcDraft(
        announcement=models.AnnouncementMutableProperties(
            body=models.StructuredText(
                text="From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.",
                structured_list=[],
            ),
            audience_filters=[
                models.FacetFilter(
                    field_name="type",
                    values=[
                        models.FacetFilterValue(
                            value="Spreadsheet",
                            relation_type=models.RelationType.EQUALS,
                        ),
                        models.FacetFilterValue(
                            value="Presentation",
                            relation_type=models.RelationType.EQUALS,
                        ),
                    ],
                ),
            ],
        ),
        answer=models.AnswerMutableProperties(
            question="Why is the sky blue?",
            body_text="From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.",
            audience_filters=[
                models.FacetFilter(
                    field_name="type",
                    values=[
                        models.FacetFilterValue(
                            value="Spreadsheet",
                            relation_type=models.RelationType.EQUALS,
                        ),
                        models.FacetFilterValue(
                            value="Presentation",
                            relation_type=models.RelationType.EQUALS,
                        ),
                    ],
                ),
            ],
            added_roles=[
                models.UserRoleSpecification(
                    person=models.Person(
                        name="George Clooney",
                        obfuscated_id="abc123",
                        related_documents=[],
                        metadata=models.PersonMetadata(
                            type=models.PersonMetadataType.FULL_TIME,
                            title="Actor",
                            department="Movies",
                            email="george@example.com",
                            location="Hollywood, CA",
                            management_chain=[],
                            phone="6505551234",
                            photo_url="https://example.com/george.jpg",
                            reports=[],
                            start_date=date.fromisoformat("2000-01-23"),
                            datasource_profile=[
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
                    role=models.UserRole.ANSWER_MODERATOR,
                ),
            ],
            removed_roles=[
                models.UserRoleSpecification(
                    role=models.UserRole.OWNER,
                ),
                models.UserRoleSpecification(
                    role=models.UserRole.VIEWER,
                ),
                models.UserRoleSpecification(
                    role=models.UserRole.OWNER,
                ),
            ],
            roles=[
                models.UserRoleSpecification(
                    role=models.UserRole.VIEWER,
                ),
                models.UserRoleSpecification(
                    role=models.UserRole.VIEWER,
                ),
                models.UserRoleSpecification(
                    role=models.UserRole.OWNER,
                ),
            ],
        ),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `draft`                                                                                                                  | [Optional[models.UgcDraft]](../../models/ugcdraft.md)                                                                    | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |
| `draft_spec`                                                                                                             | [Optional[models.DocumentSpecUnion]](../../models/documentspecunion.md)                                                  | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |
| `type`                                                                                                                   | [Optional[models.UgcType]](../../models/ugctype.md)                                                                      | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.PreviewUgcResponse](../../models/previewugcresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## update_likes

Update the likes for an existing user-generated Answer. Examples are liking or unliking the Answer.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.answers.update_likes(answer_id=3, action=models.UpdateAnswerLikesRequestAction.LIKE, answer_doc_id="ANSWERS_answer_3")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                  | Type                                                                                                                                                                       | Required                                                                                                                                                                   | Description                                                                                                                                                                | Example                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `answer_id`                                                                                                                                                                | *int*                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                         | The opaque id of the answer to like.                                                                                                                                       | 3                                                                                                                                                                          |
| `action`                                                                                                                                                                   | [models.UpdateAnswerLikesRequestAction](../../models/updateanswerlikesrequestaction.md)                                                                                    | :heavy_check_mark:                                                                                                                                                         | N/A                                                                                                                                                                        |                                                                                                                                                                            |
| `x_scio_actas`                                                                                                                                                             | *Optional[str]*                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                         | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).                                                   |                                                                                                                                                                            |
| `x_glean_auth_type`                                                                                                                                                        | *Optional[str]*                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                         | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                                                                  |                                                                                                                                                                            |
| `answer_doc_id`                                                                                                                                                            | *Optional[str]*                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                         | Glean Document ID of the Answer. The Glean Document ID is supported for cases where the Answer ID is unavailable. If both are available, using the Answer ID is preferred. | ANSWERS_answer_3                                                                                                                                                           |
| `retries`                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                           | :heavy_minus_sign:                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                        |                                                                                                                                                                            |

### Response

**[models.UpdateAnswerLikesResponse](../../models/updateanswerlikesresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## ~~create_board~~

Create a board of Answers.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from datetime import date
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.answers.create_board(name="<value>", added_roles=[
        models.UserRoleSpecification(
            person=models.Person(
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
            role=models.UserRole.ANSWER_MODERATOR,
        ),
        models.UserRoleSpecification(
            role=models.UserRole.OWNER,
        ),
    ], removed_roles=[
        models.UserRoleSpecification(
            person=models.Person(
                name="George Clooney",
                obfuscated_id="abc123",
                related_documents=[],
                metadata=models.PersonMetadata(
                    type=models.PersonMetadataType.FULL_TIME,
                    title="Actor",
                    department="Movies",
                    email="george@example.com",
                    location="Hollywood, CA",
                    management_chain=[],
                    phone="6505551234",
                    photo_url="https://example.com/george.jpg",
                    reports=[],
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
            role=models.UserRole.ANSWER_MODERATOR,
        ),
    ], audience_filters=[
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
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `name`                                                                                                                   | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | The unique name of the Collection.                                                                                       |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `description`                                                                                                            | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | A brief summary of the Collection's contents.                                                                            |
| `added_roles`                                                                                                            | List[[models.UserRoleSpecification](../../models/userrolespecification.md)]                                              | :heavy_minus_sign:                                                                                                       | A list of added user roles for the Collection.                                                                           |
| `removed_roles`                                                                                                          | List[[models.UserRoleSpecification](../../models/userrolespecification.md)]                                              | :heavy_minus_sign:                                                                                                       | A list of removed user roles for the Collection.                                                                         |
| `audience_filters`                                                                                                       | List[[models.FacetFilter](../../models/facetfilter.md)]                                                                  | :heavy_minus_sign:                                                                                                       | Filters which restrict who should see this Collection. Values are taken from the corresponding filters in people search. |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.CreateAnswerBoardResponse](../../models/createanswerboardresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## ~~delete_board~~

Delete an Answer Board given the Answer Board's ID. Multi-delete is not currently supported.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.answers.delete_board(ids=[
        983393,
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `ids`                                                                                                                    | List[*int*]                                                                                                              | :heavy_check_mark:                                                                                                       | The IDs of the Answer Boards to delete.                                                                                  |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.DeleteAnswerBoardsResponse](../../models/deleteanswerboardsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## ~~update_board~~

Modifies the properties of an existing Answer Board.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from datetime import date
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.answers.update_board(name="<value>", id=892222, added_roles=[
        models.UserRoleSpecification(
            person=models.Person(
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
            role=models.UserRole.EDITOR,
        ),
    ], removed_roles=[
        models.UserRoleSpecification(
            person=models.Person(
                name="George Clooney",
                obfuscated_id="abc123",
                related_documents=[],
                metadata=models.PersonMetadata(
                    type=models.PersonMetadataType.FULL_TIME,
                    title="Actor",
                    department="Movies",
                    email="george@example.com",
                    location="Hollywood, CA",
                    management_chain=[],
                    phone="6505551234",
                    photo_url="https://example.com/george.jpg",
                    reports=[],
                    start_date=date.fromisoformat("2000-01-23"),
                    datasource_profile=[
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
            role=models.UserRole.VIEWER,
        ),
    ], audience_filters=[
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
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `name`                                                                                                                   | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | The unique name of the Collection.                                                                                       |
| `id`                                                                                                                     | *int*                                                                                                                    | :heavy_check_mark:                                                                                                       | The ID of the Answer Board to modify.                                                                                    |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `description`                                                                                                            | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | A brief summary of the Collection's contents.                                                                            |
| `added_roles`                                                                                                            | List[[models.UserRoleSpecification](../../models/userrolespecification.md)]                                              | :heavy_minus_sign:                                                                                                       | A list of added user roles for the Collection.                                                                           |
| `removed_roles`                                                                                                          | List[[models.UserRoleSpecification](../../models/userrolespecification.md)]                                              | :heavy_minus_sign:                                                                                                       | A list of removed user roles for the Collection.                                                                         |
| `audience_filters`                                                                                                       | List[[models.FacetFilter](../../models/facetfilter.md)]                                                                  | :heavy_minus_sign:                                                                                                       | Filters which restrict who should see this Collection. Values are taken from the corresponding filters in people search. |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.EditAnswerBoardResponse](../../models/editanswerboardresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## ~~get_board~~

Read the details of an Answer Board given its ID. Does not fetch items in this Answer Board, use /listanswers instead.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.answers.get_board(id=643179)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                     | *int*                                                                                                                    | :heavy_check_mark:                                                                                                       | The id of the Answer Board to be retrieved.                                                                              |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.GetAnswerBoardResponse](../../models/getanswerboardresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## ~~list_boards~~

List all existing Answer Boards

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.answers.list_boards()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `with_audience`                                                                                                          | *Optional[bool]*                                                                                                         | :heavy_minus_sign:                                                                                                       | Whether to include the audience filters with the listed Answer Boards.                                                   |
| `with_roles`                                                                                                             | *Optional[bool]*                                                                                                         | :heavy_minus_sign:                                                                                                       | Whether to include the editor roles with the listed Answer Boards.                                                       |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.ListAnswerBoardsResponse](../../models/listanswerboardsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |