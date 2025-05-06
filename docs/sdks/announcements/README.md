# Announcements
(*client.announcements*)

## Overview

### Available Operations

* [create](#create) - Create Announcement
* [delete](#delete) - Delete Announcement
* [update](#update) - Update Announcement

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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | The opaque id of the announcement to be deleted.                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

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