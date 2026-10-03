# Skills

## Overview

### Available Operations

* [create](#create) - Create skill
* [list](#list) - List skills
* [import_](#import_) - Import skills from GitHub
* [validate](#validate) - Validate skill bundle
* [preview_source](#preview_source) - Preview a GitHub skill source
* [update](#update) - Update skill
* [delete](#delete) - Delete skill
* [retrieve](#retrieve) - Retrieve skill
* [retrieve_content](#retrieve_content) - Download skill content
* [sync](#sync) - Sync a GitHub-imported skill
* [create_version](#create_version) - Create skill version
* [list_versions](#list_versions) - List skill versions
* [retrieve_version](#retrieve_version) - Retrieve skill version
* [retrieve_version_content](#retrieve_version_content) - Download skill version content
* [preview_source_stream](#preview_source_stream) - Preview a GitHub skill source as events

## create

Create a skill from an uploaded SKILL.md, .zip, or .skill bundle. If the authenticated user already has a skill with the same name, the existing skill is superseded with a new version, unless it is source-managed: a same-name create over a GitHub-imported skill returns 409, and the caller syncs the existing skill instead. Two concurrent same-name creates can still produce two skills.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-skills-create" method="post" path="/api/skills" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.skills.create(file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `file`                                                                                  | [models.PlatformSkillCreateRequestFile](../../models/platformskillcreaterequestfile.md) | :heavy_check_mark:                                                                      | SKILL.md, .zip, or .skill bundle to create.                                             |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.PlatformSkillCreateResponse](../../models/platformskillcreateresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.PlatformProblemDetailError      | 400, 401, 403, 404, 408, 409, 413, 429 | application/problem+json               |
| errors.PlatformProblemDetailError      | 500, 503                               | application/problem+json               |
| errors.GleanError                      | 4XX, 5XX                               | \*/\*                                  |

## list

List every custom skill the authenticated caller can access. Built-in skills are excluded: they have no versions, content download, update, or delete, so their identifiers would fail most skill operations. Chat-authored skills shared with the caller without a listed grant are omitted: they stay retrievable by identifier when it is known, but this list does not discover them.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-skills-list" method="get" path="/api/skills" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.skills.list(page_size=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum number of skills to return. Defaults to 20. Maximum is 100. |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Opaque pagination cursor from a previous response.                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlatformSkillsListResponse](../../models/platformskillslistresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 429      | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## import_

Import one or more skills selected from a GitHub source preview. Each source URL is fetched and persisted as an independent skill with source provenance. This operation does not create a durable source resource. The import is atomic: if any source cannot be fetched, validated, or persisted, no skills are created.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-skills-import" method="post" path="/api/skills/import" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.skills.import_(source_urls=[
        "https://github.com/anthropics/skills/tree/main/skills/skill-creator",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `source_urls`                                                       | List[*str*]                                                         | :heavy_check_mark:                                                  | Resolved GitHub skill URLs selected from a source preview.          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlatformSkillImportResponse](../../models/platformskillimportresponse.md)**

### Errors

| Error Type                                        | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| errors.PlatformUnauthorizedAgentToolsProblemError | 422                                               | application/problem+json                          |
| errors.PlatformProblemDetailError                 | 400, 401, 403, 408, 409, 413, 429                 | application/problem+json                          |
| errors.PlatformProblemDetailError                 | 500, 503                                          | application/problem+json                          |
| errors.GleanError                                 | 4XX, 5XX                                          | \*/\*                                             |

## validate

Validate a skill bundle without persisting it. Accepts a SKILL.md, .zip, or .skill upload and returns parsed metadata plus the normalized file layout.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-skills-validate" method="post" path="/api/skills/validation" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.skills.validate(file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `file`                                                                                          | [models.PlatformSkillValidationRequestFile](../../models/platformskillvalidationrequestfile.md) | :heavy_check_mark:                                                                              | SKILL.md, .zip, or .skill bundle to validate.                                                   |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.PlatformSkillValidationResponse](../../models/platformskillvalidationresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 413, 429 | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## preview_source

Inspect a GitHub URL without persisting a source or any discovered skills. Set stream to true to receive repository scan progress as server-sent events; otherwise the response contains the completed preview.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-skills-preview-source" method="post" path="/api/skills/sources/preview" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.skills.preview_source(source_url="https://github.com/anthropics/skills")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `source_url`                                                               | *str*                                                                      | :heavy_check_mark:                                                         | GitHub URL for a skill directory, SKILL.md file, or repository to inspect. |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[models.PlatformSkillSourcePreviewResponse](../../models/platformskillsourcepreviewresponse.md)**

### Errors

| Error Type                                        | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| errors.PlatformUnauthorizedAgentToolsProblemError | 422                                               | application/problem+json                          |
| errors.PlatformProblemDetailError                 | 400, 401, 403, 408, 413, 429                      | application/problem+json                          |
| errors.PlatformProblemDetailError                 | 500, 503                                          | application/problem+json                          |
| errors.GleanError                                 | 4XX, 5XX                                          | \*/\*                                             |

## update

Enable or disable the skill for the authenticated caller without changing its content. The owner's update sets the skill's stored status. Any other caller's update applies only to that caller.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-skills-update" method="patch" path="/api/skills/{skill_id}" -->
```python
from glean.api_client import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.skills.update(skill_id="{skill_id}", status=models.PlatformSkillUpdateStatus.ENABLED)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                              | Type                                                                                                                                                                   | Required                                                                                                                                                               | Description                                                                                                                                                            | Example                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `skill_id`                                                                                                                                                             | *str*                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                     | Glean skill ID.                                                                                                                                                        | {skill_id}                                                                                                                                                             |
| `status`                                                                                                                                                               | [models.PlatformSkillUpdateStatus](../../models/platformskillupdatestatus.md)                                                                                          | :heavy_check_mark:                                                                                                                                                     | Activation to apply for the authenticated caller. For the owner, this updates the skill's stored status. For any other caller, it updates only that caller's setting.<br/> |                                                                                                                                                                        |
| `retries`                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                       | :heavy_minus_sign:                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                    |                                                                                                                                                                        |

### Response

**[models.PlatformSkillUpdateResponse](../../models/platformskillupdateresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.PlatformProblemDetailError      | 400, 401, 403, 404, 408, 409, 413, 429 | application/problem+json               |
| errors.PlatformProblemDetailError      | 500, 503                               | application/problem+json               |
| errors.GleanError                      | 4XX, 5XX                               | \*/\*                                  |

## delete

Delete a skill the authenticated caller is allowed to manage. This operation permanently removes all versions of the skill.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-skills-delete" method="delete" path="/api/skills/{skill_id}" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    glean.skills.delete(skill_id="{skill_id}")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `skill_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Glean skill ID.                                                     | {skill_id}                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 429      | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## retrieve

Retrieve metadata for a skill available to the authenticated user.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-skills-get" method="get" path="/api/skills/{skill_id}" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.skills.retrieve(skill_id="{skill_id}")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `skill_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Glean skill ID.                                                     | {skill_id}                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PlatformSkillGetResponse](../../models/platformskillgetresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 429      | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## retrieve_content

Download the latest installable bundle for a skill available to the authenticated user.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-skills-get-content" method="get" path="/api/skills/{skill_id}/content" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.skills.retrieve_content(skill_id="{skill_id}")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `skill_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Glean skill ID.                                                     | {skill_id}                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PlatformSkillsGetContentResponse](../../models/platformskillsgetcontentresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 429      | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## sync

Refresh one GitHub-imported skill from its stored source URL. If the skill content has changed, this operation creates a new skill version. If the skill is no longer present upstream, the stored skill is left unchanged and must be deleted explicitly.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-skills-sync" method="post" path="/api/skills/{skill_id}/sync" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.skills.sync(skill_id="{skill_id}")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `skill_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | ID of the GitHub-imported skill to sync.                            | {skill_id}                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PlatformSkillSyncResponse](../../models/platformskillsyncresponse.md)**

### Errors

| Error Type                                        | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| errors.PlatformUnauthorizedAgentToolsProblemError | 422                                               | application/problem+json                          |
| errors.PlatformProblemDetailError                 | 400, 401, 403, 404, 408, 409, 429                 | application/problem+json                          |
| errors.PlatformProblemDetailError                 | 500, 503                                          | application/problem+json                          |
| errors.GleanError                                 | 4XX, 5XX                                          | \*/\*                                             |

## create_version

Create a new immutable version for an existing caller-managed skill from an uploaded SKILL.md, .zip, or .skill bundle. A create-version over a GitHub-imported skill returns 409, and the caller syncs the existing skill instead.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-skills-create-version" method="post" path="/api/skills/{skill_id}/versions" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.skills.create_version(skill_id="{skill_id}", file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           | Example                                                                                               |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `skill_id`                                                                                            | *str*                                                                                                 | :heavy_check_mark:                                                                                    | Glean skill ID.                                                                                       | {skill_id}                                                                                            |
| `file`                                                                                                | [models.PlatformSkillVersionCreateRequestFile](../../models/platformskillversioncreaterequestfile.md) | :heavy_check_mark:                                                                                    | SKILL.md, .zip, or .skill bundle to store as a new version.                                           |                                                                                                       |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |                                                                                                       |

### Response

**[models.PlatformSkillVersionCreateResponse](../../models/platformskillversioncreateresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.PlatformProblemDetailError      | 400, 401, 403, 404, 408, 409, 413, 429 | application/problem+json               |
| errors.PlatformProblemDetailError      | 500, 503                               | application/problem+json               |
| errors.GleanError                      | 4XX, 5XX                               | \*/\*                                  |

## list_versions

List versions for a skill available to the authenticated user.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-skills-list-versions" method="get" path="/api/skills/{skill_id}/versions" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.skills.list_versions(skill_id="{skill_id}", page_size=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `skill_id`                                                            | *str*                                                                 | :heavy_check_mark:                                                    | Glean skill ID.                                                       | {skill_id}                                                            |
| `page_size`                                                           | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | Maximum number of versions to return. Defaults to 20. Maximum is 100. |                                                                       |
| `cursor`                                                              | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Opaque pagination cursor from a previous response.                    |                                                                       |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |                                                                       |

### Response

**[models.PlatformSkillVersionsListResponse](../../models/platformskillversionslistresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 429      | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## retrieve_version

Retrieve metadata for a skill version available to the authenticated user.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-skills-get-version" method="get" path="/api/skills/{skill_id}/versions/{version}" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.skills.retrieve_version(skill_id="{skill_id}", version=1)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `skill_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Glean skill ID.                                                     | {skill_id}                                                          |
| `version`                                                           | *int*                                                               | :heavy_check_mark:                                                  | Major version number.                                               | 1                                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PlatformSkillVersionGetResponse](../../models/platformskillversiongetresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 429      | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## retrieve_version_content

Download the installable bundle for a skill version available to the authenticated user.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-skills-get-version-content" method="get" path="/api/skills/{skill_id}/versions/{version}/content" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.skills.retrieve_version_content(skill_id="{skill_id}", version=1)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `skill_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Glean skill ID.                                                     | {skill_id}                                                          |
| `version`                                                           | *int*                                                               | :heavy_check_mark:                                                  | Major version number.                                               | 1                                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PlatformSkillsGetVersionContentResponse](../../models/platformskillsgetversioncontentresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 429      | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## preview_source_stream

SDK-only logical operation. HTTP clients must call the base path; the URL fragment is not sent. Inspect a GitHub URL as server-sent events. HTTP clients request this mode by setting `stream` to true in the JSON body.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-skills-preview-source-stream" method="post" path="/api/skills/sources/preview#stream" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.skills.preview_source_stream(source_url="https://github.com/anthropics/skills")

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `source_url`                                                               | *str*                                                                      | :heavy_check_mark:                                                         | GitHub URL for a skill directory, SKILL.md file, or repository to inspect. |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[Union[eventstreaming.EventStream[models.PlatformSkillSourcePreviewStreamEventServerSentEvent], eventstreaming.EventStreamAsync[models.PlatformSkillSourcePreviewStreamEventServerSentEvent]]](../../models/.md)**

### Errors

| Error Type                                        | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| errors.PlatformUnauthorizedAgentToolsProblemError | 422                                               | application/problem+json                          |
| errors.PlatformProblemDetailError                 | 400, 401, 403, 408, 413, 429                      | application/problem+json                          |
| errors.PlatformProblemDetailError                 | 500, 503                                          | application/problem+json                          |
| errors.GleanError                                 | 4XX, 5XX                                          | \*/\*                                             |