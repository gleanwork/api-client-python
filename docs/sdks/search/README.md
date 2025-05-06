# Search
(*client.search*)

## Overview

### Available Operations

* [query_as_admin](#query_as_admin) - Search the index (admin)
* [autocomplete](#autocomplete) - Autocomplete
* [retrieve_feed](#retrieve_feed) - Feed of documents and events
* [recommendations](#recommendations) - Recommend documents
* [query](#query) - Search

## query_as_admin

Retrieves results for search query without respect for permissions. This is available only to privileged users.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.client.search.query_as_admin(request=models.SearchRequest(
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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SearchRequest](../../models/searchrequest.md)               | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SearchResponse](../../models/searchresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GleanDataError | 403, 422              | application/json      |
| errors.GleanError     | 4XX, 5XX              | \*/\*                 |

## autocomplete

Retrieve query suggestions, operators and documents for the given partially typed query.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.client.search.autocomplete(request={
        "tracking_token": "trackingToken",
        "query": "San Fra",
        "datasource": "GDRIVE",
        "result_size": 10,
        "auth_tokens": [
            {
                "access_token": "123abc",
                "datasource": "gmail",
                "scope": "email profile https://www.googleapis.com/auth/gmail.readonly",
                "token_type": "Bearer",
                "auth_user": "1",
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.AutocompleteRequest](../../models/autocompleterequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AutocompleteResponse](../../models/autocompleteresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## retrieve_feed

The personalized feed/home includes different types of contents including suggestions, recents, calendar events and many more.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.client.search.retrieve_feed(request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.FeedRequest](../../models/feedrequest.md)                   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FeedResponse](../../models/feedresponse.md)**

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
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.client.search.recommendations(request=models.RecommendationsRequest(
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
                shortcuts=[],
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

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.RecommendationsRequest](../../models/recommendationsrequest.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.ResultsResponse](../../models/resultsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## query

Retrieve results from the index for the given query and filters.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.client.search.query(request=models.SearchRequest(
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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SearchRequest](../../models/searchrequest.md)               | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SearchResponse](../../models/searchresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GleanDataError | 403, 422              | application/json      |
| errors.GleanError     | 4XX, 5XX              | \*/\*                 |