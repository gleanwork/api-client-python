# Summarize
(*client.summarize*)

## Overview

### Available Operations

* [generate](#generate) - Summarize documents

## generate

Generate an AI summary of the requested documents.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.summarize.generate(document_specs=[
        {},
        {},
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `document_specs`                                                                                                         | List[[models.DocumentSpecUnion](../../models/documentspecunion.md)]                                                      | :heavy_check_mark:                                                                                                       | Specifications of documents to summarize                                                                                 |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `timestamp`                                                                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                     | :heavy_minus_sign:                                                                                                       | The ISO 8601 timestamp associated with the client request.                                                               |
| `query`                                                                                                                  | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Optional query that the summary should be about                                                                          |
| `preferred_summary_length`                                                                                               | *Optional[int]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Optional length of summary output. If not given, defaults to 500 chars.                                                  |
| `tracking_token`                                                                                                         | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | An opaque token that represents this particular result. To be used for /feedback reporting.                              |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.SummarizeResponse](../../models/summarizeresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |