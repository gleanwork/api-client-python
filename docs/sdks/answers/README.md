# Client.Answers

## Overview

### Available Operations

* [create](#create) - Create Answer
* [delete](#delete) - Delete Answer
* [update](#update) - Update Answer
* [retrieve](#retrieve) - Read Answer
* [~~list~~](#list) - List Answers :warning: **Deprecated**

## create

Create a user-generated Answer that contains a question and answer.

### Example Usage

<!-- UsageSnippet language="python" operationID="createanswer" method="post" path="/rest/api/v1/createanswer" -->
```python
from glean.api_client import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.answers.create(data={
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
                ),
                role=models.UserRole.VIEWER,
            ),
        ],
        "removed_roles": [
            models.UserRoleSpecification(
                person=models.Person(
                    name="George Clooney",
                    obfuscated_id="abc123",
                ),
                role=models.UserRole.ANSWER_MODERATOR,
            ),
        ],
        "roles": [
            models.UserRoleSpecification(
                person=models.Person(
                    name="George Clooney",
                    obfuscated_id="abc123",
                ),
                role=models.UserRole.OWNER,
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

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `data`                                                                                                                                                                                              | [models.AnswerCreationData](../../models/answercreationdata.md)                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                  | N/A                                                                                                                                                                                                 |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Response

**[models.Answer](../../models/answer.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## delete

Delete an existing user-generated Answer.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteanswer" method="post" path="/rest/api/v1/deleteanswer" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    glean.client.answers.delete(id=3, doc_id="ANSWERS_answer_3")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         | Example                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                | *int*                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                  | The opaque ID of the Answer.                                                                                                                                                                        | 3                                                                                                                                                                                                   |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |                                                                                                                                                                                                     |
| `doc_id`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | Glean Document ID of the Answer. The Glean Document ID is supported for cases where the Answer ID isn't available. If both are available, using the Answer ID is preferred.                         | ANSWERS_answer_3                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |                                                                                                                                                                                                     |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## update

Update an existing user-generated Answer.

### Example Usage

<!-- UsageSnippet language="python" operationID="editanswer" method="post" path="/rest/api/v1/editanswer" -->
```python
from glean.api_client import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.answers.update(id=3, doc_id="ANSWERS_answer_3", question="Why is the sky blue?", body_text="From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.", audience_filters=[
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
            ),
            role=models.UserRole.EDITOR,
        ),
    ], removed_roles=[
        models.UserRoleSpecification(
            person=models.Person(
                name="George Clooney",
                obfuscated_id="abc123",
            ),
            role=models.UserRole.OWNER,
        ),
    ], roles=[
        models.UserRoleSpecification(
            person=models.Person(
                name="George Clooney",
                obfuscated_id="abc123",
            ),
            role=models.UserRole.EDITOR,
        ),
    ], combined_answer_text={
        "text": "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                 | *int*                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                   | The opaque ID of the Answer.                                                                                                                                                                                                                         | 3                                                                                                                                                                                                                                                    |
| `locale`                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                   | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`.                                                  |                                                                                                                                                                                                                                                      |
| `doc_id`                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                   | Glean Document ID of the Answer. The Glean Document ID is supported for cases where the Answer ID isn't available. If both are available, using the Answer ID is preferred.                                                                          | ANSWERS_answer_3                                                                                                                                                                                                                                     |
| `question`                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                                                  | Why is the sky blue?                                                                                                                                                                                                                                 |
| `question_variations`                                                                                                                                                                                                                                | List[*str*]                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                   | Additional ways of phrasing this question.                                                                                                                                                                                                           |                                                                                                                                                                                                                                                      |
| `body_text`                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                   | The plain text answer to the question.                                                                                                                                                                                                               | From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.                                                                                                |
| `board_id`                                                                                                                                                                                                                                           | *Optional[int]*                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                   | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>The parent board ID of this Answer, or 0 if it's a floating Answer. Adding Answers to Answer Boards is no longer permitted. |                                                                                                                                                                                                                                                      |
| `audience_filters`                                                                                                                                                                                                                                   | List[[models.FacetFilter](../../models/facetfilter.md)]                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                   | Filters which restrict who should see the answer. Values are taken from the corresponding filters in people search.                                                                                                                                  |                                                                                                                                                                                                                                                      |
| `added_roles`                                                                                                                                                                                                                                        | List[[models.UserRoleSpecification](../../models/userrolespecification.md)]                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                   | A list of user roles for the answer added by the owner.                                                                                                                                                                                              |                                                                                                                                                                                                                                                      |
| `removed_roles`                                                                                                                                                                                                                                      | List[[models.UserRoleSpecification](../../models/userrolespecification.md)]                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                   | A list of user roles for the answer removed by the owner.                                                                                                                                                                                            |                                                                                                                                                                                                                                                      |
| `roles`                                                                                                                                                                                                                                              | List[[models.UserRoleSpecification](../../models/userrolespecification.md)]                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                   | A list of roles for this answer explicitly granted by an owner, editor, or admin.                                                                                                                                                                    |                                                                                                                                                                                                                                                      |
| `source_document_spec`                                                                                                                                                                                                                               | [Optional[models.DocumentSpecUnion]](../../models/documentspecunion.md)                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                      |
| `source_type`                                                                                                                                                                                                                                        | [Optional[models.EditAnswerRequestSourceType]](../../models/editanswerrequestsourcetype.md)                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                      |
| `added_collections`                                                                                                                                                                                                                                  | List[*int*]                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                   | IDs of Collections to which a document is added.                                                                                                                                                                                                     |                                                                                                                                                                                                                                                      |
| `removed_collections`                                                                                                                                                                                                                                | List[*int*]                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                   | IDs of Collections from which a document is removed.                                                                                                                                                                                                 |                                                                                                                                                                                                                                                      |
| `combined_answer_text`                                                                                                                                                                                                                               | [Optional[models.StructuredTextMutableProperties]](../../models/structuredtextmutableproperties.md)                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                  |                                                                                                                                                                                                                                                      |

### Response

**[models.Answer](../../models/answer.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## retrieve

Read the details of a particular Answer given its ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="getanswer" method="post" path="/rest/api/v1/getanswer" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.answers.retrieve(id=3, doc_id="ANSWERS_answer_3")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         | Example                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |                                                                                                                                                                                                     |
| `id`                                                                                                                                                                                                | *Optional[int]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The opaque ID of the Answer.                                                                                                                                                                        | 3                                                                                                                                                                                                   |
| `doc_id`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | Glean Document ID of the Answer. The Glean Document ID is supported for cases where the Answer ID isn't available. If both are available, using the Answer ID is preferred.                         | ANSWERS_answer_3                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |                                                                                                                                                                                                     |

### Response

**[models.GetAnswerResponse](../../models/getanswerresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## ~~list~~

List Answers created by the current user.

> :warning: **DEPRECATED**: Deprecated on 2026-01-21, removal scheduled for 2026-10-15: Answer boards have been removed and this endpoint no longer serves a purpose.

### Example Usage

<!-- UsageSnippet language="python" operationID="listanswers" method="post" path="/rest/api/v1/listanswers" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.answers.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |
| `board_id`                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The Answer Board Id to list answers on.                                                                                                                                                             |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Response

**[models.ListAnswersResponse](../../models/listanswersresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |