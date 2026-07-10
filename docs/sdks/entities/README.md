# Client.Entities

## Overview

### Available Operations

* [list](#list) - List entities
* [read_people](#read_people) - Read people
* [retrieve_person_photo](#retrieve_person_photo) - Get person photo

## list

List some set of details for all entities that fit the given criteria and return in the requested order. Does not support negation in filters, assumes relation type EQUALS. There is a limit of 10000 entities that can be retrieved via this endpoint, except when using FULL_DIRECTORY request type for people entities.

### Example Usage

<!-- UsageSnippet language="python" operationID="listentities" method="post" path="/rest/api/v1/listentities" -->
```python
from glean.api_client import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.entities.list(filter_=[
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
    ], entity_type=models.ListEntitiesRequestEntityType.PEOPLE, page_size=100, request_type=models.ListEntitiesRequestRequestType.STANDARD)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         | Example                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |                                                                                                                                                                                                     |
| `filter_`                                                                                                                                                                                           | List[[models.FacetFilter](../../models/facetfilter.md)]                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                  | N/A                                                                                                                                                                                                 |                                                                                                                                                                                                     |
| `sort`                                                                                                                                                                                              | List[[models.SortOptions](../../models/sortoptions.md)]                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                  | Use EntitiesSortOrder enum for SortOptions.sortBy                                                                                                                                                   |                                                                                                                                                                                                     |
| `entity_type`                                                                                                                                                                                       | [Optional[models.ListEntitiesRequestEntityType]](../../models/listentitiesrequestentitytype.md)                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | N/A                                                                                                                                                                                                 |                                                                                                                                                                                                     |
| `datasource`                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The datasource associated with the entity type, most commonly used with CUSTOM_ENTITIES                                                                                                             |                                                                                                                                                                                                     |
| `query`                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | A query string to search for entities that each entity in the response must conform to. An empty query does not filter any entities.                                                                |                                                                                                                                                                                                     |
| `include_fields`                                                                                                                                                                                    | List[[models.ListEntitiesRequestIncludeField](../../models/listentitiesrequestincludefield.md)]                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | List of entity fields to return (that aren't returned by default)                                                                                                                                   |                                                                                                                                                                                                     |
| `page_size`                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | Hint to the server about how many results to send back. Server may return less.                                                                                                                     | 100                                                                                                                                                                                                 |
| `cursor`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | Pagination cursor. A previously received opaque token representing the position in the overall results at which to start.                                                                           |                                                                                                                                                                                                     |
| `source`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | A string denoting the search surface from which the endpoint is called.                                                                                                                             |                                                                                                                                                                                                     |
| `request_type`                                                                                                                                                                                      | [Optional[models.ListEntitiesRequestRequestType]](../../models/listentitiesrequestrequesttype.md)                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                  | The type of request being made.                                                                                                                                                                     |                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |                                                                                                                                                                                                     |

### Response

**[models.ListEntitiesResponse](../../models/listentitiesresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## read_people

Read people details for the given IDs.

### Example Usage

<!-- UsageSnippet language="python" operationID="people" method="post" path="/rest/api/v1/people" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.entities.read_people(obfuscated_ids=[
        "abc123",
        "abc456",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |
| `timezone_offset`                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.                                                                                          |
| `obfuscated_ids`                                                                                                                                                                                    | List[*str*]                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                  | The Person IDs to retrieve. If no IDs are requested, the current user's details are returned.                                                                                                       |
| `email_ids`                                                                                                                                                                                         | List[*str*]                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                  | The email IDs to retrieve. The result is the deduplicated union of emailIds and obfuscatedIds.                                                                                                      |
| `include_fields`                                                                                                                                                                                    | List[[models.PeopleRequestIncludeField](../../models/peoplerequestincludefield.md)]                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                  | List of PersonMetadata fields to return (that aren't returned by default)                                                                                                                           |
| `include_types`                                                                                                                                                                                     | List[[models.IncludeType](../../models/includetype.md)]                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                  | The types of people entities to include in the response in addition to those returned by default.                                                                                                   |
| `source`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | A string denoting the search surface from which the endpoint is called.                                                                                                                             |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Response

**[models.PeopleResponse](../../models/peopleresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## retrieve_person_photo

Returns the profile photo bytes for a person whose photo is stored in Glean (crawled from an identity source or user-uploaded via admin console). Photos hosted externally (e.g. Slack CDN) are not served by this endpoint; callers should follow the photoUrl from /people or /listentities directly. Responses include a Cache-Control header (max-age=3600) to reduce redundant fetches.


### Example Usage

<!-- UsageSnippet language="python" operationID="getPersonPhoto" method="get" path="/rest/api/v1/people/{person_id}/photo" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.entities.retrieve_person_photo(person_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                              | Type                                                                                                                                                                                                   | Required                                                                                                                                                                                               | Description                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `person_id`                                                                                                                                                                                            | *str*                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                     | The obfuscated ID of the person whose photo to retrieve.                                                                                                                                               |
| `ds`                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                     | Optional datasource override for crawled photos (e.g. AZURE, GDRIVE, OKTA). When omitted, the datasource is derived from the person's stored photo URL or the deployment's primary person datasource.<br/> |
| `retries`                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                    |

### Response

**[models.GetPersonPhotoResponse](../../models/getpersonphotoresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |