# Announcements
(*client.announcements*)

## Overview

### Available Operations

* [create](#create) - Create Announcement
* [create_draft](#create_draft) - Create draft Announcement
* [delete](#delete) - Delete Announcement
* [delete_draft](#delete_draft) - Delete draft Announcement
* [get](#get) - Read Announcement
* [get_draft](#get_draft) - Read draft Announcement
* [list](#list) - List Announcements
* [preview](#preview) - Preview Announcement
* [preview_draft](#preview_draft) - Preview draft Announcement
* [publish](#publish) - Publish draft Announcement
* [unpublish](#unpublish) - Unpublish Announcement
* [update](#update) - Update Announcement
* [update_draft](#update_draft) - Update draft Announcement

## create

Create a textual announcement visible to some set of users based on department and location.

### Example Usage

```python
from glean import Glean, models
from glean.utils import parse_datetime
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.announcements.create(start_time=parse_datetime("2024-06-17T07:14:55.338Z"), end_time=parse_datetime("2024-11-30T17:06:07.804Z"), title="<value>", body={
        "text": "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.",
        "structured_list": [],
    }, audience_filters=[
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

| Parameter                                                                                                                                                                                             | Type                                                                                                                                                                                                  | Required                                                                                                                                                                                              | Description                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                                                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                    | The date and time at which the announcement becomes active.                                                                                                                                           |
| `end_time`                                                                                                                                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                    | The date and time at which the announcement expires.                                                                                                                                                  |
| `title`                                                                                                                                                                                               | *str*                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                    | The headline of the announcement.                                                                                                                                                                     |
| `x_scio_actas`                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).                                                                              |
| `x_glean_auth_type`                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                                                                                             |
| `body`                                                                                                                                                                                                | [Optional[models.StructuredText]](../../models/structuredtext.md)                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                    | N/A                                                                                                                                                                                                   |
| `emoji`                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | An emoji used to indicate the nature of the announcement.                                                                                                                                             |
| `thumbnail`                                                                                                                                                                                           | [Optional[models.Thumbnail]](../../models/thumbnail.md)                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                    | N/A                                                                                                                                                                                                   |
| `banner`                                                                                                                                                                                              | [Optional[models.Thumbnail]](../../models/thumbnail.md)                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                    | N/A                                                                                                                                                                                                   |
| `audience_filters`                                                                                                                                                                                    | List[[models.FacetFilter](../../models/facetfilter.md)]                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                    | Filters which restrict who should see the announcement. Values are taken from the corresponding filters in people search.                                                                             |
| `source_document_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | The Glean Document ID of the source document this Announcement was created from (e.g. Slack thread).                                                                                                  |
| `hide_attribution`                                                                                                                                                                                    | *Optional[bool]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                    | Whether or not to hide an author attribution.                                                                                                                                                         |
| `channel`                                                                                                                                                                                             | [Optional[models.CreateAnnouncementRequestChannel]](../../models/createannouncementrequestchannel.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                    | This determines whether this is a Social Feed post or a regular announcement.                                                                                                                         |
| `post_type`                                                                                                                                                                                           | [Optional[models.CreateAnnouncementRequestPostType]](../../models/createannouncementrequestposttype.md)                                                                                               | :heavy_minus_sign:                                                                                                                                                                                    | This determines whether this is an external-link post or a regular announcement post. TEXT - Regular announcement that can contain rich text. LINK - Announcement that is linked to an external site. |
| `is_prioritized`                                                                                                                                                                                      | *Optional[bool]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                    | Used by the Social Feed to pin posts to the front of the feed.                                                                                                                                        |
| `view_url`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | URL for viewing the announcement. It will be set to document URL for announcements from other datasources e.g. simpplr. Can only be written when channel="SOCIAL_FEED".                               |
| `retries`                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                   |

### Response

**[models.Announcement](../../models/announcement.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## create_draft

Create a draft of a textual announcement visible to some set of users based on department and location.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.announcements.create_draft(body={
        "text": "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.",
        "structured_list": [],
    }, audience_filters=[
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

| Parameter                                                                                                                                                                                             | Type                                                                                                                                                                                                  | Required                                                                                                                                                                                              | Description                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `x_scio_actas`                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).                                                                              |
| `x_glean_auth_type`                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                                                                                             |
| `start_time`                                                                                                                                                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                    | The date and time at which the announcement becomes active.                                                                                                                                           |
| `end_time`                                                                                                                                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                    | The date and time at which the announcement expires.                                                                                                                                                  |
| `title`                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | The headline of the announcement.                                                                                                                                                                     |
| `body`                                                                                                                                                                                                | [Optional[models.StructuredText]](../../models/structuredtext.md)                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                    | N/A                                                                                                                                                                                                   |
| `emoji`                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | An emoji used to indicate the nature of the announcement.                                                                                                                                             |
| `thumbnail`                                                                                                                                                                                           | [Optional[models.Thumbnail]](../../models/thumbnail.md)                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                    | N/A                                                                                                                                                                                                   |
| `banner`                                                                                                                                                                                              | [Optional[models.Thumbnail]](../../models/thumbnail.md)                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                    | N/A                                                                                                                                                                                                   |
| `audience_filters`                                                                                                                                                                                    | List[[models.FacetFilter](../../models/facetfilter.md)]                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                    | Filters which restrict who should see the announcement. Values are taken from the corresponding filters in people search.                                                                             |
| `source_document_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | The Glean Document ID of the source document this Announcement was created from (e.g. Slack thread).                                                                                                  |
| `hide_attribution`                                                                                                                                                                                    | *Optional[bool]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                    | Whether or not to hide an author attribution.                                                                                                                                                         |
| `channel`                                                                                                                                                                                             | [Optional[models.CreateDraftAnnouncementRequestChannel]](../../models/createdraftannouncementrequestchannel.md)                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | This determines whether this is a Social Feed post or a regular announcement.                                                                                                                         |
| `post_type`                                                                                                                                                                                           | [Optional[models.CreateDraftAnnouncementRequestPostType]](../../models/createdraftannouncementrequestposttype.md)                                                                                     | :heavy_minus_sign:                                                                                                                                                                                    | This determines whether this is an external-link post or a regular announcement post. TEXT - Regular announcement that can contain rich text. LINK - Announcement that is linked to an external site. |
| `is_prioritized`                                                                                                                                                                                      | *Optional[bool]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                    | Used by the Social Feed to pin posts to the front of the feed.                                                                                                                                        |
| `view_url`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | URL for viewing the announcement. It will be set to document URL for announcements from other datasources e.g. simpplr. Can only be written when channel="SOCIAL_FEED".                               |
| `id`                                                                                                                                                                                                  | *Optional[int]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | The opaque id of the parent announcement.                                                                                                                                                             |
| `retries`                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                   |

### Response

**[models.Announcement](../../models/announcement.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## delete

Delete an existing user-generated announcement.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.client.announcements.delete(id=545907)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                     | *int*                                                                                                                    | :heavy_check_mark:                                                                                                       | The opaque id of the announcement to be deleted.                                                                         |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## delete_draft

Delete an existing user-generated draft Announcement.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.client.announcements.delete_draft(id=171443)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                     | *int*                                                                                                                    | :heavy_check_mark:                                                                                                       | The opaque id of the announcement to be deleted.                                                                         |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## get

Read the details of an Announcement given its ID.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.announcements.get(id=700347)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                     | *int*                                                                                                                    | :heavy_check_mark:                                                                                                       | The id of the announcement to be retrieved.                                                                              |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.GetAnnouncementResponse](../../models/getannouncementresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## get_draft

Read the details of an existing user-generated draft Announcement.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.announcements.get_draft(id=476509)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                     | *int*                                                                                                                    | :heavy_check_mark:                                                                                                       | The id of the announcement to be retrieved.                                                                              |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.GetDraftAnnouncementResponse](../../models/getdraftannouncementresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## list

List Announcement details for all Announcements matching the given criteria.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.announcements.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `channel`                                                                                                                | [Optional[models.AnnouncementChannel]](../../models/announcementchannel.md)                                              | :heavy_minus_sign:                                                                                                       | This determines whether this is a Social Feed post or a regular announcement.                                            |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.ListAnnouncementsResponse](../../models/listannouncementsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## preview

Generate a preview for a user-generated Announcement from structured text.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.announcements.preview(text="From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.")

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

Generates a preview for a user-generated Announcement from a draft.

### Example Usage

```python
from datetime import date
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.announcements.preview_draft(draft=models.UgcDraft(
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

## publish

Promote a draft Announcement to be visible to others.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.client.announcements.publish(id=876134)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                     | *int*                                                                                                                    | :heavy_check_mark:                                                                                                       | The opaque id of the draft announcement to be published.                                                                 |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## unpublish

Unpublish an Announcement to hide it from users.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.announcements.unpublish(id=195182)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                     | *int*                                                                                                                    | :heavy_check_mark:                                                                                                       | The opaque id of the announcement to be unpublished.                                                                     |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.Announcement](../../models/announcement.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## update

Update a textual announcement visible to some set of users based on department and location.

### Example Usage

```python
from glean import Glean, models
from glean.utils import parse_datetime
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.announcements.update(start_time=parse_datetime("2025-07-28T19:04:48.565Z"), end_time=parse_datetime("2024-10-16T10:52:42.015Z"), title="<value>", id=761625, body={
        "text": "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.",
        "structured_list": [],
    }, audience_filters=[
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

| Parameter                                                                                                                                                                                             | Type                                                                                                                                                                                                  | Required                                                                                                                                                                                              | Description                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                                                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                    | The date and time at which the announcement becomes active.                                                                                                                                           |
| `end_time`                                                                                                                                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                    | The date and time at which the announcement expires.                                                                                                                                                  |
| `title`                                                                                                                                                                                               | *str*                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                    | The headline of the announcement.                                                                                                                                                                     |
| `id`                                                                                                                                                                                                  | *int*                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                    | The opaque id of the announcement.                                                                                                                                                                    |
| `x_scio_actas`                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).                                                                              |
| `x_glean_auth_type`                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                                                                                             |
| `body`                                                                                                                                                                                                | [Optional[models.StructuredText]](../../models/structuredtext.md)                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                    | N/A                                                                                                                                                                                                   |
| `emoji`                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | An emoji used to indicate the nature of the announcement.                                                                                                                                             |
| `thumbnail`                                                                                                                                                                                           | [Optional[models.Thumbnail]](../../models/thumbnail.md)                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                    | N/A                                                                                                                                                                                                   |
| `banner`                                                                                                                                                                                              | [Optional[models.Thumbnail]](../../models/thumbnail.md)                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                    | N/A                                                                                                                                                                                                   |
| `audience_filters`                                                                                                                                                                                    | List[[models.FacetFilter](../../models/facetfilter.md)]                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                    | Filters which restrict who should see the announcement. Values are taken from the corresponding filters in people search.                                                                             |
| `source_document_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | The Glean Document ID of the source document this Announcement was created from (e.g. Slack thread).                                                                                                  |
| `hide_attribution`                                                                                                                                                                                    | *Optional[bool]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                    | Whether or not to hide an author attribution.                                                                                                                                                         |
| `channel`                                                                                                                                                                                             | [Optional[models.UpdateAnnouncementRequestChannel]](../../models/updateannouncementrequestchannel.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                    | This determines whether this is a Social Feed post or a regular announcement.                                                                                                                         |
| `post_type`                                                                                                                                                                                           | [Optional[models.UpdateAnnouncementRequestPostType]](../../models/updateannouncementrequestposttype.md)                                                                                               | :heavy_minus_sign:                                                                                                                                                                                    | This determines whether this is an external-link post or a regular announcement post. TEXT - Regular announcement that can contain rich text. LINK - Announcement that is linked to an external site. |
| `is_prioritized`                                                                                                                                                                                      | *Optional[bool]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                    | Used by the Social Feed to pin posts to the front of the feed.                                                                                                                                        |
| `view_url`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | URL for viewing the announcement. It will be set to document URL for announcements from other datasources e.g. simpplr. Can only be written when channel="SOCIAL_FEED".                               |
| `retries`                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                   |

### Response

**[models.Announcement](../../models/announcement.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## update_draft

Update a textual Announcement visible to some set of users based on department and location.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.announcements.update_draft(draft_id=758103, body={
        "text": "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.",
        "structured_list": [],
    }, audience_filters=[
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

| Parameter                                                                                                                                                                                             | Type                                                                                                                                                                                                  | Required                                                                                                                                                                                              | Description                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `draft_id`                                                                                                                                                                                            | *int*                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                    | The opaque id of the draft.                                                                                                                                                                           |
| `x_scio_actas`                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens).                                                                              |
| `x_glean_auth_type`                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                                                                                             |
| `start_time`                                                                                                                                                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                    | The date and time at which the announcement becomes active.                                                                                                                                           |
| `end_time`                                                                                                                                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                    | The date and time at which the announcement expires.                                                                                                                                                  |
| `title`                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | The headline of the announcement.                                                                                                                                                                     |
| `body`                                                                                                                                                                                                | [Optional[models.StructuredText]](../../models/structuredtext.md)                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                    | N/A                                                                                                                                                                                                   |
| `emoji`                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | An emoji used to indicate the nature of the announcement.                                                                                                                                             |
| `thumbnail`                                                                                                                                                                                           | [Optional[models.Thumbnail]](../../models/thumbnail.md)                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                    | N/A                                                                                                                                                                                                   |
| `banner`                                                                                                                                                                                              | [Optional[models.Thumbnail]](../../models/thumbnail.md)                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                    | N/A                                                                                                                                                                                                   |
| `audience_filters`                                                                                                                                                                                    | List[[models.FacetFilter](../../models/facetfilter.md)]                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                    | Filters which restrict who should see the announcement. Values are taken from the corresponding filters in people search.                                                                             |
| `source_document_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | The Glean Document ID of the source document this Announcement was created from (e.g. Slack thread).                                                                                                  |
| `hide_attribution`                                                                                                                                                                                    | *Optional[bool]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                    | Whether or not to hide an author attribution.                                                                                                                                                         |
| `channel`                                                                                                                                                                                             | [Optional[models.UpdateDraftAnnouncementRequestChannel]](../../models/updatedraftannouncementrequestchannel.md)                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | This determines whether this is a Social Feed post or a regular announcement.                                                                                                                         |
| `post_type`                                                                                                                                                                                           | [Optional[models.UpdateDraftAnnouncementRequestPostType]](../../models/updatedraftannouncementrequestposttype.md)                                                                                     | :heavy_minus_sign:                                                                                                                                                                                    | This determines whether this is an external-link post or a regular announcement post. TEXT - Regular announcement that can contain rich text. LINK - Announcement that is linked to an external site. |
| `is_prioritized`                                                                                                                                                                                      | *Optional[bool]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                    | Used by the Social Feed to pin posts to the front of the feed.                                                                                                                                        |
| `view_url`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | URL for viewing the announcement. It will be set to document URL for announcements from other datasources e.g. simpplr. Can only be written when channel="SOCIAL_FEED".                               |
| `id`                                                                                                                                                                                                  | *Optional[int]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | The opaque id of the announcement.                                                                                                                                                                    |
| `retries`                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                   |

### Response

**[models.Announcement](../../models/announcement.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |