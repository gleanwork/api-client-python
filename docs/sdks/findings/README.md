# Client.Governance.Data.Findings

## Overview

### Available Operations

* [create](#create) - Creates findings export
* [list](#list) - Lists findings exports
* [download](#download) - Downloads findings export
* [delete](#delete) - Deletes findings export

## create

Creates a new DLP findings export job.

### Example Usage

<!-- UsageSnippet language="python" operationID="createfindingsexport" method="post" path="/rest/api/v1/governance/data/findings/exports" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.governance.data.findings.create()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `export_type`                                                                                             | [Optional[models.DlpExportFindingsRequestExportType]](../../models/dlpexportfindingsrequestexporttype.md) | :heavy_minus_sign:                                                                                        | The type of export to perform                                                                             |
| `filter_`                                                                                                 | [Optional[models.DlpFindingFilter]](../../models/dlpfindingfilter.md)                                     | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `issue_filter`                                                                                            | [Optional[models.DlpIssueFilter]](../../models/dlpissuefilter.md)                                         | :heavy_minus_sign:                                                                                        | Filter for DLP issues. Includes document-level filters and issue-specific filters.                        |
| `file_name`                                                                                               | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | The name of the file to export the findings to                                                            |
| `field_scope`                                                                                             | [Optional[models.FieldScope]](../../models/fieldscope.md)                                                 | :heavy_minus_sign:                                                                                        | Controls which fields to include in the export                                                            |
| `fields_to_exclude`                                                                                       | List[*str*]                                                                                               | :heavy_minus_sign:                                                                                        | List of field names to exclude from the export                                                            |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.ExportInfo](../../models/exportinfo.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## list

Lists all DLP findings exports.

### Example Usage

<!-- UsageSnippet language="python" operationID="listfindingsexports" method="get" path="/rest/api/v1/governance/data/findings/exports" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.governance.data.findings.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListDlpFindingsExportsResponse](../../models/listdlpfindingsexportsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## download

Downloads a DLP findings export as a CSV file.

### Example Usage

<!-- UsageSnippet language="python" operationID="downloadfindingsexport" method="get" path="/rest/api/v1/governance/data/findings/exports/{id}" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.governance.data.findings.download(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the export to download.                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[str](../../models/.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## delete

Deletes a DLP findings export.

### Example Usage

<!-- UsageSnippet language="python" operationID="deletefindingsexport" method="delete" path="/rest/api/v1/governance/data/findings/exports/{id}" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    glean.client.governance.data.findings.delete(id=741945)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | The ID of the export to delete.                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |