# Skills

## Overview

### Available Operations

* [create](#create) - Create skill
* [list](#list) - List skills
* [validate](#validate) - Validate skill bundle
* [retrieve](#retrieve) - Retrieve skill
* [retrieve_content](#retrieve_content) - Download skill content
* [create_version](#create_version) - Create skill version
* [list_versions](#list_versions) - List skill versions
* [retrieve_version](#retrieve_version) - Retrieve skill version
* [retrieve_version_content](#retrieve_version_content) - Download skill version content

## create

Create a skill from an uploaded SKILL.md, .zip, or .skill bundle. If the authenticated user already has a skill with the same name, the existing skill is superseded with a new version.


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

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 413, 429 | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## list

List skills available to the authenticated user.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-skills-list" method="get" path="/api/skills" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.skills.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum number of skills to return.                                 |
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

    res = glean.skills.retrieve(skill_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `skill_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Glean skill ID.                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

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

    res = glean.skills.retrieve_content(skill_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `skill_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Glean skill ID.                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlatformSkillsGetContentResponse](../../models/platformskillsgetcontentresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 429      | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |

## create_version

Create a new immutable version for an existing caller-managed skill from an uploaded SKILL.md, .zip, or .skill bundle.


### Example Usage

<!-- UsageSnippet language="python" operationID="platform-skills-create-version" method="post" path="/api/skills/{skill_id}/versions" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.skills.create_version(skill_id="<id>", file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `skill_id`                                                                                            | *str*                                                                                                 | :heavy_check_mark:                                                                                    | Glean skill ID.                                                                                       |
| `file`                                                                                                | [models.PlatformSkillVersionCreateRequestFile](../../models/platformskillversioncreaterequestfile.md) | :heavy_check_mark:                                                                                    | SKILL.md, .zip, or .skill bundle to store as a new version.                                           |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

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

    res = glean.skills.list_versions(skill_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `skill_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Glean skill ID.                                                     |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum number of versions to return.                               |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Opaque pagination cursor from a previous response.                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

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

    res = glean.skills.retrieve_version(skill_id="<id>", version=495658)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `skill_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Glean skill ID.                                                     |
| `version`                                                           | *int*                                                               | :heavy_check_mark:                                                  | Major version number.                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

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

    res = glean.skills.retrieve_version_content(skill_id="<id>", version=117760)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `skill_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Glean skill ID.                                                     |
| `version`                                                           | *int*                                                               | :heavy_check_mark:                                                  | Major version number.                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlatformSkillsGetVersionContentResponse](../../models/platformskillsgetversioncontentresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PlatformProblemDetailError | 400, 401, 403, 404, 408, 429      | application/problem+json          |
| errors.PlatformProblemDetailError | 500, 503                          | application/problem+json          |
| errors.GleanError                 | 4XX, 5XX                          | \*/\*                             |