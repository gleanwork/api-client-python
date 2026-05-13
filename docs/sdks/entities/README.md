# Entities

## Overview

### Available Operations

* [get_person_photo](#get_person_photo) - Get person photo

## get_person_photo

Returns the profile photo bytes for a person whose photo is stored in Glean (crawled from an identity source or user-uploaded via admin console). Photos hosted externally (e.g. Slack CDN) are not served by this endpoint; callers should follow the photoUrl from /people or /listentities directly. Responses include a Cache-Control header (max-age=3600) to reduce redundant fetches.


### Example Usage

<!-- UsageSnippet language="python" operationID="getPersonPhoto" method="get" path="/rest/api/v1/people/{person_id}/photo" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.entities.get_person_photo(person_id="<id>")

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