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
from glean.utils import parse_datetime
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.client.search.query_as_admin(query="vacation policy", tracking_token="trackingToken", source_document=models.Document(
        container_document=models.Document(
            parent_document=models.Document(
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
                        name="name",
                        obfuscated_id="<id>",
                    ),
                    components=[
                        "Backend",
                        "Networking",
                    ],
                    status="[\"Done\"]",
                    custom_data={
                        "someCustomField": models.CustomDataValue(),
                    },
                ),
            ),
        ),
    ), page_size=10, max_snippet_size=400, input_details={
        "has_copy_paste": True,
    }, request_options=models.SearchRequestOptions(
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
        facet_bucket_size=421489,
    ), timeout_millis=5000, people=[
        models.Person(
            name="George Clooney",
            obfuscated_id="abc123",
        ),
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                 | Example                                                                                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `query`                                                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                                                          | The search terms.                                                                                                                                                                                                                                                           | vacation policy                                                                                                                                                                                                                                                             |
| `timestamp`                                                                                                                                                                                                                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                          | The ISO 8601 timestamp associated with the client request.                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                             |
| `tracking_token`                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                          | A previously received trackingToken for a search associated with the same query. Useful for more requests and requests for other tabs.                                                                                                                                      |                                                                                                                                                                                                                                                                             |
| `session_info`                                                                                                                                                                                                                                                              | [Optional[models.SessionInfo]](../../models/sessioninfo.md)                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                             |
| `source_document`                                                                                                                                                                                                                                                           | [Optional[models.Document]](../../models/document.md)                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                             |
| `page_size`                                                                                                                                                                                                                                                                 | *Optional[int]*                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                          | Hint to the server about how many results to send back. Server may return less or more. Structured results and clustered results don't count towards pageSize.                                                                                                              | 100                                                                                                                                                                                                                                                                         |
| `max_snippet_size`                                                                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                          | Hint to the server about how many characters long a snippet may be. Server may return less or more.                                                                                                                                                                         | 400                                                                                                                                                                                                                                                                         |
| `cursor`                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                          | Pagination cursor. A previously received opaque token representing the position in the overall results at which to start.                                                                                                                                                   |                                                                                                                                                                                                                                                                             |
| `result_tab_ids`                                                                                                                                                                                                                                                            | List[*str*]                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                          | The unique IDs of the result tabs for which to fetch results. This will have precedence over datasource filters if both are specified and in conflict.                                                                                                                      |                                                                                                                                                                                                                                                                             |
| `input_details`                                                                                                                                                                                                                                                             | [Optional[models.SearchRequestInputDetails]](../../models/searchrequestinputdetails.md)                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                         | {<br/>"hasCopyPaste": true<br/>}                                                                                                                                                                                                                                            |
| `request_options`                                                                                                                                                                                                                                                           | [Optional[models.SearchRequestOptions]](../../models/searchrequestoptions.md)                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                         | {<br/>"datasourceFilter": "JIRA",<br/>"datasourcesFilter": [<br/>"JIRA"<br/>],<br/>"queryOverridesFacetFilters": true,<br/>"facetFilters": [<br/>{<br/>"fieldName": "fieldName",<br/>"values": [<br/>"fieldValues",<br/>"fieldValues"<br/>]<br/>},<br/>{<br/>"fieldName": "fieldName",<br/>"values": [<br/>"fieldValues",<br/>"fieldValues"<br/>]<br/>}<br/>]<br/>} |
| `timeout_millis`                                                                                                                                                                                                                                                            | *Optional[int]*                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                          | Timeout in milliseconds for the request. A `408` error will be returned if handling the request takes longer.                                                                                                                                                               | 5000                                                                                                                                                                                                                                                                        |
| `people`                                                                                                                                                                                                                                                                    | List[[models.Person](../../models/person.md)]                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                          | People associated with the search request. Hints to the server to fetch additional information for these people. Note that in this request, an email may be used as a person's obfuscatedId value.                                                                          |                                                                                                                                                                                                                                                                             |
| `disable_spellcheck`                                                                                                                                                                                                                                                        | *Optional[bool]*                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                          | Whether or not to disable spellcheck.                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                             |
| `retries`                                                                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                             |

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
        "query": "what is a que",
        "datasource": "GDRIVE",
        "result_size": 10,
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

    res = g_client.client.search.retrieve_feed(request={
        "timeout_millis": 5000,
    })

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
                    name="name",
                    obfuscated_id="abc123",
                ),
                components=[
                    "Backend",
                    "Networking",
                ],
                status="[\"Done\"]",
                custom_data={
                    "someCustomField": models.CustomDataValue(),
                },
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
            context=models.Document(
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
                        name="name",
                        obfuscated_id="abc123",
                    ),
                    components=[
                        "Backend",
                        "Networking",
                    ],
                    status="[\"Done\"]",
                    custom_data={
                        "someCustomField": models.CustomDataValue(),
                    },
                ),
            ),
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
from glean.utils import parse_datetime
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.client.search.query(query="vacation policy", tracking_token="trackingToken", source_document=models.Document(
        container_document=models.Document(
            parent_document=models.Document(
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
                        name="name",
                        obfuscated_id="<id>",
                    ),
                    components=[
                        "Backend",
                        "Networking",
                    ],
                    status="[\"Done\"]",
                    custom_data={
                        "someCustomField": models.CustomDataValue(),
                    },
                ),
            ),
        ),
    ), page_size=10, max_snippet_size=400, input_details={
        "has_copy_paste": True,
    }, request_options=models.SearchRequestOptions(
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
        facet_bucket_size=400611,
    ), timeout_millis=5000, people=[
        models.Person(
            name="George Clooney",
            obfuscated_id="abc123",
        ),
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                 | Example                                                                                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `query`                                                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                                                          | The search terms.                                                                                                                                                                                                                                                           | vacation policy                                                                                                                                                                                                                                                             |
| `timestamp`                                                                                                                                                                                                                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                          | The ISO 8601 timestamp associated with the client request.                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                             |
| `tracking_token`                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                          | A previously received trackingToken for a search associated with the same query. Useful for more requests and requests for other tabs.                                                                                                                                      |                                                                                                                                                                                                                                                                             |
| `session_info`                                                                                                                                                                                                                                                              | [Optional[models.SessionInfo]](../../models/sessioninfo.md)                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                             |
| `source_document`                                                                                                                                                                                                                                                           | [Optional[models.Document]](../../models/document.md)                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                             |
| `page_size`                                                                                                                                                                                                                                                                 | *Optional[int]*                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                          | Hint to the server about how many results to send back. Server may return less or more. Structured results and clustered results don't count towards pageSize.                                                                                                              | 100                                                                                                                                                                                                                                                                         |
| `max_snippet_size`                                                                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                          | Hint to the server about how many characters long a snippet may be. Server may return less or more.                                                                                                                                                                         | 400                                                                                                                                                                                                                                                                         |
| `cursor`                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                          | Pagination cursor. A previously received opaque token representing the position in the overall results at which to start.                                                                                                                                                   |                                                                                                                                                                                                                                                                             |
| `result_tab_ids`                                                                                                                                                                                                                                                            | List[*str*]                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                          | The unique IDs of the result tabs for which to fetch results. This will have precedence over datasource filters if both are specified and in conflict.                                                                                                                      |                                                                                                                                                                                                                                                                             |
| `input_details`                                                                                                                                                                                                                                                             | [Optional[models.SearchRequestInputDetails]](../../models/searchrequestinputdetails.md)                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                         | {<br/>"hasCopyPaste": true<br/>}                                                                                                                                                                                                                                            |
| `request_options`                                                                                                                                                                                                                                                           | [Optional[models.SearchRequestOptions]](../../models/searchrequestoptions.md)                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                         | {<br/>"datasourceFilter": "JIRA",<br/>"datasourcesFilter": [<br/>"JIRA"<br/>],<br/>"queryOverridesFacetFilters": true,<br/>"facetFilters": [<br/>{<br/>"fieldName": "fieldName",<br/>"values": [<br/>"fieldValues",<br/>"fieldValues"<br/>]<br/>},<br/>{<br/>"fieldName": "fieldName",<br/>"values": [<br/>"fieldValues",<br/>"fieldValues"<br/>]<br/>}<br/>]<br/>} |
| `timeout_millis`                                                                                                                                                                                                                                                            | *Optional[int]*                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                          | Timeout in milliseconds for the request. A `408` error will be returned if handling the request takes longer.                                                                                                                                                               | 5000                                                                                                                                                                                                                                                                        |
| `people`                                                                                                                                                                                                                                                                    | List[[models.Person](../../models/person.md)]                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                          | People associated with the search request. Hints to the server to fetch additional information for these people. Note that in this request, an email may be used as a person's obfuscatedId value.                                                                          |                                                                                                                                                                                                                                                                             |
| `disable_spellcheck`                                                                                                                                                                                                                                                        | *Optional[bool]*                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                          | Whether or not to disable spellcheck.                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                             |
| `retries`                                                                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                             |

### Response

**[models.SearchResponse](../../models/searchresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GleanDataError | 403, 422              | application/json      |
| errors.GleanError     | 4XX, 5XX              | \*/\*                 |