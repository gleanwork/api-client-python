# Search
(*client.search*)

## Overview

### Available Operations

* [admin](#admin) - Search the index (admin)
* [autocomplete](#autocomplete) - Autocomplete
* [get_feed](#get_feed) - Feed of documents and events
* [suggest_people](#suggest_people) - Suggest people
* [suggest_people_admin](#suggest_people_admin) - Suggest people (admin)
* [recommendations](#recommendations) - Recommend documents
* [execute](#execute) - Search

## admin

Retrieves results for search query without respect for permissions. This is available only to privileged users.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.search.admin(search_request=models.SearchRequest(
        tracking_token="trackingToken",
        page_size=10,
        query="vacation policy",
        request_options=models.SearchRequestOptions(
            facet_filters=[
                models.FacetFilter(
                    field_name="type",
                    values=[
                        models.FacetFilterValue(
                            value="article",
                            relation_type=models.RelationType.EQUALS,
                        ),
                        models.FacetFilterValue(
                            value="document",
                            relation_type=models.RelationType.EQUALS,
                        ),
                    ],
                ),
                models.FacetFilter(
                    field_name="department",
                    values=[
                        models.FacetFilterValue(
                            value="engineering",
                            relation_type=models.RelationType.EQUALS,
                        ),
                    ],
                ),
            ],
            facet_bucket_size=254944,
        ),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                 | Type                                                                                                                                                                                                                                                                                                                                                                      | Required                                                                                                                                                                                                                                                                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                               | Example                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `x_scio_actas`                                                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                           |
| `x_glean_auth_type`                                                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                           |
| `search_request`                                                                                                                                                                                                                                                                                                                                                          | [Optional[models.SearchRequest]](../../models/searchrequest.md)                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | Admin search request                                                                                                                                                                                                                                                                                                                                                      | {<br/>"trackingToken": "trackingToken",<br/>"query": "vacation policy",<br/>"pageSize": 10,<br/>"requestOptions": {<br/>"facetFilters": [<br/>{<br/>"fieldName": "type",<br/>"values": [<br/>{<br/>"value": "article",<br/>"relationType": "EQUALS"<br/>},<br/>{<br/>"value": "document",<br/>"relationType": "EQUALS"<br/>}<br/>]<br/>},<br/>{<br/>"fieldName": "department",<br/>"values": [<br/>{<br/>"value": "engineering",<br/>"relationType": "EQUALS"<br/>}<br/>]<br/>}<br/>]<br/>}<br/>} |
| `retries`                                                                                                                                                                                                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                           |

### Response

**[models.SearchResponse](../../models/searchresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.ErrorInfo  | 403, 422          | application/json  |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## autocomplete

Retrieve query suggestions, operators and documents for the given partially typed query.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.search.autocomplete(tracking_token="trackingToken", query="San Fra", datasource="GDRIVE", result_size=10, auth_tokens=[
        {
            "access_token": "123abc",
            "datasource": "gmail",
            "scope": "email profile https://www.googleapis.com/auth/gmail.readonly",
            "token_type": "Bearer",
            "auth_user": "1",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              | Example                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |                                                                                                                          |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |                                                                                                                          |
| `tracking_token`                                                                                                         | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |                                                                                                                          |
| `session_info`                                                                                                           | [Optional[models.SessionInfo]](../../models/sessioninfo.md)                                                              | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |                                                                                                                          |
| `query`                                                                                                                  | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Partially typed query.                                                                                                   | San Fra                                                                                                                  |
| `datasources_filter`                                                                                                     | List[*str*]                                                                                                              | :heavy_minus_sign:                                                                                                       | Filter results to only those relevant to one or more datasources (e.g. jira, gdrive). Results are unfiltered if missing. |                                                                                                                          |
| `datasource`                                                                                                             | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Filter to only return results relevant to the given datasource.                                                          |                                                                                                                          |
| `result_types`                                                                                                           | List[[models.AutocompleteRequestResultType](../../models/autocompleterequestresulttype.md)]                              | :heavy_minus_sign:                                                                                                       | Filter to only return results of the given type(s). All types may be returned if omitted.                                |                                                                                                                          |
| `result_size`                                                                                                            | *Optional[int]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Maximum number of results to be returned. If no value is provided, the backend will cap at 200.<br/>                     | 10                                                                                                                       |
| `auth_tokens`                                                                                                            | List[[models.AuthToken](../../models/authtoken.md)]                                                                      | :heavy_minus_sign:                                                                                                       | Auth tokens which may be used for federated results.                                                                     |                                                                                                                          |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |                                                                                                                          |

### Response

**[models.AutocompleteResponse](../../models/autocompleteresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## get_feed

The personalized feed/home includes different types of contents including suggestions, recents, calendar events and many more.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.search.get_feed(timeout_millis=5000)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              | Example                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |                                                                                                                          |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |                                                                                                                          |
| `categories`                                                                                                             | List[[models.FeedRequestCategory](../../models/feedrequestcategory.md)]                                                  | :heavy_minus_sign:                                                                                                       | Categories of content requested. An allowlist gives flexibility to request content separately or together.               |                                                                                                                          |
| `request_options`                                                                                                        | [Optional[models.FeedRequestOptions]](../../models/feedrequestoptions.md)                                                | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |                                                                                                                          |
| `timeout_millis`                                                                                                         | *Optional[int]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Timeout in milliseconds for the request. A `408` error will be returned if handling the request takes longer.            | 5000                                                                                                                     |
| `session_info`                                                                                                           | [Optional[models.SessionInfo]](../../models/sessioninfo.md)                                                              | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |                                                                                                                          |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |                                                                                                                          |

### Response

**[models.FeedResponse](../../models/feedresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## suggest_people

Retrieves a list of suggested people for given type. Includes information about the persons.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.search.suggest_people(categories=[
        models.PeopleSuggestionCategory.INVITE_NONUSERS,
        models.PeopleSuggestionCategory.INVITE_NONUSERS,
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `categories`                                                                                                             | List[[models.PeopleSuggestionCategory](../../models/peoplesuggestioncategory.md)]                                        | :heavy_check_mark:                                                                                                       | Categories of data requested. Request can include single or multiple categories.                                         |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `departments`                                                                                                            | List[*str*]                                                                                                              | :heavy_minus_sign:                                                                                                       | Departments that the data is requested for. If empty, corresponds to whole company.                                      |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.PeopleSuggestResponse](../../models/peoplesuggestresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## suggest_people_admin

Returns a list of suggested people for given type for admin's view. Includes information about the persons.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.search.suggest_people_admin(categories=[
        models.PeopleSuggestionCategory.INVITE_NONUSERS,
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `categories`                                                                                                             | List[[models.PeopleSuggestionCategory](../../models/peoplesuggestioncategory.md)]                                        | :heavy_check_mark:                                                                                                       | Categories of data requested. Request can include single or multiple categories.                                         |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `departments`                                                                                                            | List[*str*]                                                                                                              | :heavy_minus_sign:                                                                                                       | Departments that the data is requested for. If empty, corresponds to whole company.                                      |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.PeopleSuggestResponse](../../models/peoplesuggestresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## recommendations

Retrieve recommended documents for the given URL or Glean Document ID.

### Example Usage

```python
from datetime import date
from glean import Glean, models
from glean.utils import parse_datetime
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.search.recommendations(recommendations_request=models.RecommendationsRequest(
        source_document=models.Document(
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
                    state=models.State.VERIFIED,
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
                            remind_at=986764,
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
        page_size=100,
        max_snippet_size=400,
        request_options=models.RecommendationsRequestOptions(
            facet_filter_sets=[
                models.FacetFilterSet(
                    filters=[
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
            ],
            context=models.Document(),
        ),
    ))

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `recommendations_request`                                                                                                | [Optional[models.RecommendationsRequest]](../../models/recommendationsrequest.md)                                        | :heavy_minus_sign:                                                                                                       | Recommendations request                                                                                                  |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.ResultsResponse](../../models/resultsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## execute

Retrieve results from the index for the given query and filters.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.search.execute(search_request=models.SearchRequest(
        tracking_token="trackingToken",
        page_size=10,
        query="vacation policy",
        request_options=models.SearchRequestOptions(
            facet_filters=[
                models.FacetFilter(
                    field_name="type",
                    values=[
                        models.FacetFilterValue(
                            value="article",
                            relation_type=models.RelationType.EQUALS,
                        ),
                        models.FacetFilterValue(
                            value="document",
                            relation_type=models.RelationType.EQUALS,
                        ),
                    ],
                ),
                models.FacetFilter(
                    field_name="department",
                    values=[
                        models.FacetFilterValue(
                            value="engineering",
                            relation_type=models.RelationType.EQUALS,
                        ),
                    ],
                ),
            ],
            facet_bucket_size=246815,
        ),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                 | Type                                                                                                                                                                                                                                                                                                                                                                      | Required                                                                                                                                                                                                                                                                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                               | Example                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `x_scio_actas`                                                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                           |
| `x_glean_auth_type`                                                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                           |
| `search_request`                                                                                                                                                                                                                                                                                                                                                          | [Optional[models.SearchRequest]](../../models/searchrequest.md)                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | Search request                                                                                                                                                                                                                                                                                                                                                            | {<br/>"trackingToken": "trackingToken",<br/>"query": "vacation policy",<br/>"pageSize": 10,<br/>"requestOptions": {<br/>"facetFilters": [<br/>{<br/>"fieldName": "type",<br/>"values": [<br/>{<br/>"value": "article",<br/>"relationType": "EQUALS"<br/>},<br/>{<br/>"value": "document",<br/>"relationType": "EQUALS"<br/>}<br/>]<br/>},<br/>{<br/>"fieldName": "department",<br/>"values": [<br/>{<br/>"value": "engineering",<br/>"relationType": "EQUALS"<br/>}<br/>]<br/>}<br/>]<br/>}<br/>} |
| `retries`                                                                                                                                                                                                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                           |

### Response

**[models.SearchResponse](../../models/searchresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.ErrorInfo  | 403, 422          | application/json  |
| errors.GleanError | 4XX, 5XX          | \*/\*             |