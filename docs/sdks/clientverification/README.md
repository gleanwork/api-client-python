# ClientVerification
(*client.verification*)

## Overview

### Available Operations

* [add_reminder](#add_reminder) - Create verification
* [list](#list) - List verifications
* [verify](#verify) - Update verification

## add_reminder

Creates a verification reminder for the document. Users can create verification reminders from different product surfaces.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.verification.add_reminder(document_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `document_id`                                                                                                                                                                                       | *str*                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                  | The document which the verification is for new reminders and/or update.                                                                                                                             |
| `assignee`                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The obfuscated id of the person this verification is assigned to.                                                                                                                                   |
| `remind_in_days`                                                                                                                                                                                    | *Optional[int]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | Reminder for the next verifications in terms of days. For deletion, this will be omitted.                                                                                                           |
| `reason`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | An optional free-text reason for the reminder. This is particularly useful when a reminder is used to ask for verification from another user (for example, "Duplicate", "Incomplete", "Incorrect"). |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Response

**[models.Verification](../../models/verification.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## list

Returns the information to be rendered in verification dashboard. Includes information for each document owned by user regarding their verifications.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.verification.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `count`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum number of documents to return                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.VerificationFeed](../../models/verificationfeed.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## verify

Verify documents to keep the knowledge up to date within customer corpus.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.verification.verify(document_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `document_id`                                                               | *str*                                                                       | :heavy_check_mark:                                                          | The document which is verified.                                             |
| `action`                                                                    | [Optional[models.VerifyRequestAction]](../../models/verifyrequestaction.md) | :heavy_minus_sign:                                                          | The verification action requested.                                          |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.Verification](../../models/verification.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |