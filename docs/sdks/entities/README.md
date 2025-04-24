# Entities
(*client.entities*)

## Overview

### Available Operations

* [list](#list) - List entities
* [read_people](#read_people) - Read people
* [get_teams](#get_teams) - Read teams

## list

List some set of details for all entities that fit the given criteria and return in the requested order. Does not support negation in filters, assumes relation type EQUALS. There is a limit of 10000 entities that can be retrieved via this endpoint.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.entities.list(filter_=[
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
    ], page_size=100)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          | Example                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `x_scio_actas`                                                                                                                       | *Optional[str]*                                                                                                                      | :heavy_minus_sign:                                                                                                                   | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).             |                                                                                                                                      |
| `x_glean_auth_type`                                                                                                                  | *Optional[str]*                                                                                                                      | :heavy_minus_sign:                                                                                                                   | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                            |                                                                                                                                      |
| `filter_`                                                                                                                            | List[[models.FacetFilter](../../models/facetfilter.md)]                                                                              | :heavy_minus_sign:                                                                                                                   | N/A                                                                                                                                  |                                                                                                                                      |
| `sort`                                                                                                                               | List[[models.SortOptions](../../models/sortoptions.md)]                                                                              | :heavy_minus_sign:                                                                                                                   | Use EntitiesSortOrder enum for SortOptions.sortBy                                                                                    |                                                                                                                                      |
| `entity_type`                                                                                                                        | [Optional[models.ListEntitiesRequestEntityType]](../../models/listentitiesrequestentitytype.md)                                      | :heavy_minus_sign:                                                                                                                   | N/A                                                                                                                                  |                                                                                                                                      |
| `datasource`                                                                                                                         | *Optional[str]*                                                                                                                      | :heavy_minus_sign:                                                                                                                   | The datasource associated with the entity type, most commonly used with CUSTOM_ENTITIES                                              |                                                                                                                                      |
| `query`                                                                                                                              | *Optional[str]*                                                                                                                      | :heavy_minus_sign:                                                                                                                   | A query string to search for entities that each entity in the response must conform to. An empty query does not filter any entities. |                                                                                                                                      |
| `include_fields`                                                                                                                     | List[[models.ListEntitiesRequestIncludeField](../../models/listentitiesrequestincludefield.md)]                                      | :heavy_minus_sign:                                                                                                                   | List of entity fields to return (that aren't returned by default)                                                                    |                                                                                                                                      |
| `page_size`                                                                                                                          | *Optional[int]*                                                                                                                      | :heavy_minus_sign:                                                                                                                   | Hint to the server about how many results to send back. Server may return less.                                                      | 100                                                                                                                                  |
| `cursor`                                                                                                                             | *Optional[str]*                                                                                                                      | :heavy_minus_sign:                                                                                                                   | Pagination cursor. A previously received opaque token representing the position in the overall results at which to start.            |                                                                                                                                      |
| `source`                                                                                                                             | *Optional[str]*                                                                                                                      | :heavy_minus_sign:                                                                                                                   | A string denoting the search surface from which the endpoint is called.                                                              |                                                                                                                                      |
| `retries`                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                     | :heavy_minus_sign:                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                  |                                                                                                                                      |

### Response

**[models.ListEntitiesResponse](../../models/listentitiesresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## read_people

Read people details for the given IDs.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.entities.read_people(obfuscated_ids=[
        "abc123",
        "abc456",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `timezone_offset`                                                                                                        | *Optional[int]*                                                                                                          | :heavy_minus_sign:                                                                                                       | The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.               |
| `obfuscated_ids`                                                                                                         | List[*str*]                                                                                                              | :heavy_minus_sign:                                                                                                       | The Person IDs to retrieve. If no IDs are requested, the current user's details are returned.                            |
| `email_ids`                                                                                                              | List[*str*]                                                                                                              | :heavy_minus_sign:                                                                                                       | The email IDs to retrieve. The result is the deduplicated union of emailIds and obfuscatedIds.                           |
| `include_fields`                                                                                                         | List[[models.PeopleRequestIncludeField](../../models/peoplerequestincludefield.md)]                                      | :heavy_minus_sign:                                                                                                       | List of PersonMetadata fields to return (that aren't returned by default)                                                |
| `include_types`                                                                                                          | List[[models.IncludeType](../../models/includetype.md)]                                                                  | :heavy_minus_sign:                                                                                                       | The types of people entities to include in the response in addition to those returned by default.                        |
| `source`                                                                                                                 | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | A string denoting the search surface from which the endpoint is called.                                                  |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.PeopleResponse](../../models/peopleresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## get_teams

Read the details of the teams with the given IDs.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.entities.get_teams(ids=[
        "abc123",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `ids`                                                                                                                    | List[*str*]                                                                                                              | :heavy_minus_sign:                                                                                                       | The IDs of the teams to retrieve.                                                                                        |
| `include_fields`                                                                                                         | List[[models.TeamsRequestIncludeField](../../models/teamsrequestincludefield.md)]                                        | :heavy_minus_sign:                                                                                                       | List of teams fields to return that aren't returned by default                                                           |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.TeamsResponse](../../models/teamsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |