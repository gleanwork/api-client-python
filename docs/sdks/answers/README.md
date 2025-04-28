# Answers
(*client.answers*)

## Overview

### Available Operations

* [create](#create) - Create Answer
* [delete](#delete) - Delete Answer
* [edit](#edit) - Update Answer
* [get](#get) - Read Answer
* [list](#list) - List Answers

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
| `x_glean_act_as`                                                                                                         | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
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
| `x_glean_act_as`                                                                                                                                                            | *Optional[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).                                                    |                                                                                                                                                                             |
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
                    query_suggestions=models.QuerySuggestionList(),
                    invite_info=models.InviteInfo(),
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
                    query_suggestions=models.QuerySuggestionList(),
                    invite_info=models.InviteInfo(),
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
| `x_glean_act_as`                                                                                                                                                            | *Optional[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).                                                    |                                                                                                                                                                             |
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
| `x_glean_act_as`                                                                                                                                                            | *Optional[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).                                                    |                                                                                                                                                                             |
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
| `x_glean_act_as`                                                                                                         | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `board_id`                                                                                                               | *Optional[int]*                                                                                                          | :heavy_minus_sign:                                                                                                       | The Answer Board Id to list answers on.                                                                                  |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.ListAnswersResponse](../../models/listanswersresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |