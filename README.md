# Glean Python API Client

The Glean Python SDK provides convenient access to the Glean REST API from any Python 3.8+ application. It includes type hints for all request parameters and response fields, and supports both synchronous and asynchronous usage via [httpx](https://www.python-httpx.org/).
<!-- No Summary [summary] -->

## Unified SDK Architecture

This SDK combines both the Client and Indexing API namespaces into a single unified package:

- **Client API**: Used for search, retrieval, and end-user interactions with Glean content
- **Indexing API**: Used for indexing content, permissions, and other administrative operations

Each namespace has its own authentication requirements and access patterns. While they serve different purposes, having them in a single SDK provides a consistent developer experience across all Glean API interactions.

```python
# Example of accessing Client namespace
from glean.api_client import Glean
import os

with Glean(api_token="client-token", instance="instance-name") as glean:
    search_response = glean.client.search.query(query="search term")

    print(search_response)

# Example of accessing Indexing namespace 
from glean.api_client import Glean, models
import os

with Glean(api_token="indexing-token", instance="instance-name") as glean:
    document_response = glean.indexing.documents.index(
        document=models.Document(
            id="doc-123",
            title="Sample Document",
            container_id="container-456",
            datasource="confluence"
        )
    )
```

Remember that each namespace requires its own authentication token type as described in the [Authentication Methods](#authentication-methods) section.

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [Glean Python API Client](#glean-python-api-client)
  * [Unified SDK Architecture](#unified-sdk-architecture)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [File uploads](#file-uploads)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install glean-api-client
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add glean-api-client
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from glean-api-client python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "glean-api-client",
# ]
# ///

from glean.api_client import Glean

sdk = Glean(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- No SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example 1

```python
# Synchronous Example
from glean.api_client import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.chat.create(messages=[
        {
            "fragments": [
                models.ChatMessageFragment(
                    text="What are the company holidays this year?",
                ),
            ],
        },
    ], timeout_millis=30000)

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from glean.api_client import Glean, models
import os

async def main():

    async with Glean(
        api_token=os.getenv("GLEAN_API_TOKEN", ""),
    ) as glean:

        res = await glean.client.chat.create_async(messages=[
            {
                "fragments": [
                    models.ChatMessageFragment(
                        text="What are the company holidays this year?",
                    ),
                ],
            },
        ], timeout_millis=30000)

        # Handle response
        print(res)

asyncio.run(main())
```

### Example 2

```python
# Synchronous Example
from glean.api_client import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.chat.create_stream(messages=[
        {
            "fragments": [
                models.ChatMessageFragment(
                    text="What are the company holidays this year?",
                ),
            ],
        },
    ], timeout_millis=30000)

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from glean.api_client import Glean, models
import os

async def main():

    async with Glean(
        api_token=os.getenv("GLEAN_API_TOKEN", ""),
    ) as glean:

        res = await glean.client.chat.create_stream_async(messages=[
            {
                "fragments": [
                    models.ChatMessageFragment(
                        text="What are the company holidays this year?",
                    ),
                ],
            },
        ], timeout_millis=30000)

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name        | Type | Scheme      | Environment Variable |
| ----------- | ---- | ----------- | -------------------- |
| `api_token` | http | HTTP Bearer | `GLEAN_API_TOKEN`    |

To authenticate with the API the `api_token` parameter must be set when initializing the SDK client instance. For example:
```python
from glean.api_client import Glean, models
from glean.api_client.utils import parse_datetime
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    glean.client.activity.report(events=[
        {
            "action": models.ActivityEventAction.HISTORICAL_VIEW,
            "timestamp": parse_datetime("2000-01-23T04:56:07.000Z"),
            "url": "https://example.com/",
        },
        {
            "action": models.ActivityEventAction.SEARCH,
            "params": {
                "query": "query",
            },
            "timestamp": parse_datetime("2000-01-23T04:56:07.000Z"),
            "url": "https://example.com/search?q=query",
        },
        {
            "action": models.ActivityEventAction.VIEW,
            "params": {
                "duration": 20,
                "referrer": "https://example.com/document",
            },
            "timestamp": parse_datetime("2000-01-23T04:56:07.000Z"),
            "url": "https://example.com/",
        },
    ])

    # Use the SDK ...

```
<!-- End Authentication [security] -->

### Authentication Methods

Glean supports different authentication methods depending on which API namespace you're using:

#### Client Namespace

The Client namespace supports two authentication methods:

1. **Manually Provisioned API Tokens**
   - Can be created by an Admin or a user with the API Token Creator role
   - Used for server-to-server integrations

2. **OAuth**
   - Requires OAuth setup to be completed by an Admin
   - Used for user-based authentication flows

#### Indexing Namespace

The Indexing namespace supports only one authentication method:

1. **Manually Provisioned API Tokens**
   - Can be created by an Admin or a user with the API Token Creator role
   - Used for secure document indexing operations

> [!IMPORTANT]
> Client tokens **will not work** for Indexing operations, and Indexing tokens **will not work** for Client operations. You must use the appropriate token type for the namespace you're accessing.

For more information on obtaining the appropriate token type, please contact your Glean administrator.

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [client](docs/sdks/client/README.md)


#### [client.activity](docs/sdks/clientactivity/README.md)

* [report](docs/sdks/clientactivity/README.md#report) - Report document activity
* [feedback](docs/sdks/clientactivity/README.md#feedback) - Report client activity

#### [client.agents](docs/sdks/agents/README.md)

* [retrieve](docs/sdks/agents/README.md#retrieve) - Retrieve an agent
* [retrieve_schemas](docs/sdks/agents/README.md#retrieve_schemas) - List an agent's schemas
* [list](docs/sdks/agents/README.md#list) - Search agents
* [run_stream](docs/sdks/agents/README.md#run_stream) - Create an agent run and stream the response
* [run](docs/sdks/agents/README.md#run) - Create an agent run and wait for the response

#### [client.announcements](docs/sdks/announcements/README.md)

* [create](docs/sdks/announcements/README.md#create) - Create Announcement
* [delete](docs/sdks/announcements/README.md#delete) - Delete Announcement
* [update](docs/sdks/announcements/README.md#update) - Update Announcement

#### [client.answers](docs/sdks/answers/README.md)

* [create](docs/sdks/answers/README.md#create) - Create Answer
* [delete](docs/sdks/answers/README.md#delete) - Delete Answer
* [update](docs/sdks/answers/README.md#update) - Update Answer
* [retrieve](docs/sdks/answers/README.md#retrieve) - Read Answer
* [list](docs/sdks/answers/README.md#list) - List Answers

#### [client.authentication](docs/sdks/clientauthentication/README.md)

* [create_token](docs/sdks/clientauthentication/README.md#create_token) - Create authentication token

#### [client.chat](docs/sdks/clientchat/README.md)

* [create](docs/sdks/clientchat/README.md#create) - Chat
* [delete_all](docs/sdks/clientchat/README.md#delete_all) - Deletes all saved Chats owned by a user
* [delete](docs/sdks/clientchat/README.md#delete) - Deletes saved Chats
* [retrieve](docs/sdks/clientchat/README.md#retrieve) - Retrieves a Chat
* [list](docs/sdks/clientchat/README.md#list) - Retrieves all saved Chats
* [retrieve_application](docs/sdks/clientchat/README.md#retrieve_application) - Gets the metadata for a custom Chat application
* [upload_files](docs/sdks/clientchat/README.md#upload_files) - Upload files for Chat.
* [retrieve_files](docs/sdks/clientchat/README.md#retrieve_files) - Get files uploaded by a user for Chat.
* [delete_files](docs/sdks/clientchat/README.md#delete_files) - Delete files uploaded by a user for chat.
* [create_stream](docs/sdks/clientchat/README.md#create_stream) - Chat

#### [client.collections](docs/sdks/collections/README.md)

* [add_items](docs/sdks/collections/README.md#add_items) - Add Collection item
* [create](docs/sdks/collections/README.md#create) - Create Collection
* [delete](docs/sdks/collections/README.md#delete) - Delete Collection
* [delete_item](docs/sdks/collections/README.md#delete_item) - Delete Collection item
* [update](docs/sdks/collections/README.md#update) - Update Collection
* [update_item](docs/sdks/collections/README.md#update_item) - Update Collection item
* [retrieve](docs/sdks/collections/README.md#retrieve) - Read Collection
* [list](docs/sdks/collections/README.md#list) - List Collections

#### [client.documents](docs/sdks/clientdocuments/README.md)

* [retrieve_permissions](docs/sdks/clientdocuments/README.md#retrieve_permissions) - Read document permissions
* [retrieve](docs/sdks/clientdocuments/README.md#retrieve) - Read documents
* [retrieve_by_facets](docs/sdks/clientdocuments/README.md#retrieve_by_facets) - Read documents by facets
* [summarize](docs/sdks/clientdocuments/README.md#summarize) - Summarize documents

#### [client.entities](docs/sdks/entities/README.md)

* [list](docs/sdks/entities/README.md#list) - List entities
* [read_people](docs/sdks/entities/README.md#read_people) - Read people

#### [client.governance.data.policies](docs/sdks/policies/README.md)

* [retrieve](docs/sdks/policies/README.md#retrieve) - Gets specified policy
* [update](docs/sdks/policies/README.md#update) - Updates an existing policy
* [list](docs/sdks/policies/README.md#list) - Lists policies
* [create](docs/sdks/policies/README.md#create) - Creates new policy
* [download](docs/sdks/policies/README.md#download) - Downloads violations CSV for policy

#### [client.governance.data.reports](docs/sdks/reports/README.md)

* [create](docs/sdks/reports/README.md#create) - Creates new one-time report
* [download](docs/sdks/reports/README.md#download) - Downloads violations CSV for report
* [status](docs/sdks/reports/README.md#status) - Fetches report run status

#### [client.governance.documents.visibilityoverrides](docs/sdks/visibilityoverrides/README.md)

* [list](docs/sdks/visibilityoverrides/README.md#list) - Fetches documents visibility
* [create](docs/sdks/visibilityoverrides/README.md#create) - Hide or unhide docs

#### [client.insights](docs/sdks/insights/README.md)

* [retrieve](docs/sdks/insights/README.md#retrieve) - Read insights

#### [client.messages](docs/sdks/messages/README.md)

* [retrieve](docs/sdks/messages/README.md#retrieve) - Read messages

#### [client.pins](docs/sdks/pins/README.md)

* [update](docs/sdks/pins/README.md#update) - Update pin
* [retrieve](docs/sdks/pins/README.md#retrieve) - Read pin
* [list](docs/sdks/pins/README.md#list) - List pins
* [create](docs/sdks/pins/README.md#create) - Create pin
* [remove](docs/sdks/pins/README.md#remove) - Delete pin

#### [client.search](docs/sdks/search/README.md)

* [query_as_admin](docs/sdks/search/README.md#query_as_admin) - Search the index (admin)
* [autocomplete](docs/sdks/search/README.md#autocomplete) - Autocomplete
* [retrieve_feed](docs/sdks/search/README.md#retrieve_feed) - Feed of documents and events
* [recommendations](docs/sdks/search/README.md#recommendations) - Recommend documents
* [query](docs/sdks/search/README.md#query) - Search

#### [client.shortcuts](docs/sdks/clientshortcuts/README.md)

* [create](docs/sdks/clientshortcuts/README.md#create) - Create shortcut
* [delete](docs/sdks/clientshortcuts/README.md#delete) - Delete shortcut
* [retrieve](docs/sdks/clientshortcuts/README.md#retrieve) - Read shortcut
* [list](docs/sdks/clientshortcuts/README.md#list) - List shortcuts
* [update](docs/sdks/clientshortcuts/README.md#update) - Update shortcut

#### [client.tools](docs/sdks/tools/README.md)

* [list](docs/sdks/tools/README.md#list) - List available tools
* [run](docs/sdks/tools/README.md#run) - Execute the specified tool

#### [client.verification](docs/sdks/clientverification/README.md)

* [add_reminder](docs/sdks/clientverification/README.md#add_reminder) - Create verification
* [list](docs/sdks/clientverification/README.md#list) - List verifications
* [verify](docs/sdks/clientverification/README.md#verify) - Update verification


### [indexing](docs/sdks/indexing/README.md)


#### [indexing.authentication](docs/sdks/indexingauthentication/README.md)

* [rotate_token](docs/sdks/indexingauthentication/README.md#rotate_token) - Rotate token

#### [indexing.datasource](docs/sdks/indexingdatasource/README.md)

* [status](docs/sdks/indexingdatasource/README.md#status) - Beta: Get datasource status


#### [indexing.datasources](docs/sdks/datasources/README.md)

* [add](docs/sdks/datasources/README.md#add) - Add or update datasource
* [retrieve_config](docs/sdks/datasources/README.md#retrieve_config) - Get datasource config

#### [indexing.documents](docs/sdks/indexingdocuments/README.md)

* [add_or_update](docs/sdks/indexingdocuments/README.md#add_or_update) - Index document
* [index](docs/sdks/indexingdocuments/README.md#index) - Index documents
* [bulk_index](docs/sdks/indexingdocuments/README.md#bulk_index) - Bulk index documents
* [process_all](docs/sdks/indexingdocuments/README.md#process_all) - Schedules the processing of uploaded documents
* [delete](docs/sdks/indexingdocuments/README.md#delete) - Delete document
* [debug](docs/sdks/indexingdocuments/README.md#debug) - Beta: Get document information

* [debug_many](docs/sdks/indexingdocuments/README.md#debug_many) - Beta: Get information of a batch of documents

* [check_access](docs/sdks/indexingdocuments/README.md#check_access) - Check document access
* [~~status~~](docs/sdks/indexingdocuments/README.md#status) - Get document upload and indexing status :warning: **Deprecated**
* [~~count~~](docs/sdks/indexingdocuments/README.md#count) - Get document count :warning: **Deprecated**

#### [indexing.people](docs/sdks/people/README.md)

* [debug](docs/sdks/people/README.md#debug) - Beta: Get user information

* [~~count~~](docs/sdks/people/README.md#count) - Get user count :warning: **Deprecated**
* [index](docs/sdks/people/README.md#index) - Index employee
* [bulk_index](docs/sdks/people/README.md#bulk_index) - Bulk index employees
* [process_all_employees_and_teams](docs/sdks/people/README.md#process_all_employees_and_teams) - Schedules the processing of uploaded employees and teams
* [delete](docs/sdks/people/README.md#delete) - Delete employee
* [index_team](docs/sdks/people/README.md#index_team) - Index team
* [delete_team](docs/sdks/people/README.md#delete_team) - Delete team
* [bulk_index_teams](docs/sdks/people/README.md#bulk_index_teams) - Bulk index teams

#### [indexing.permissions](docs/sdks/indexingpermissions/README.md)

* [update_permissions](docs/sdks/indexingpermissions/README.md#update_permissions) - Update document permissions
* [index_user](docs/sdks/indexingpermissions/README.md#index_user) - Index user
* [bulk_index_users](docs/sdks/indexingpermissions/README.md#bulk_index_users) - Bulk index users
* [index_group](docs/sdks/indexingpermissions/README.md#index_group) - Index group
* [bulk_index_groups](docs/sdks/indexingpermissions/README.md#bulk_index_groups) - Bulk index groups
* [index_membership](docs/sdks/indexingpermissions/README.md#index_membership) - Index membership
* [bulk_index_memberships](docs/sdks/indexingpermissions/README.md#bulk_index_memberships) - Bulk index memberships for a group
* [process_memberships](docs/sdks/indexingpermissions/README.md#process_memberships) - Schedules the processing of group memberships
* [delete_user](docs/sdks/indexingpermissions/README.md#delete_user) - Delete user
* [delete_group](docs/sdks/indexingpermissions/README.md#delete_group) - Delete group
* [delete_membership](docs/sdks/indexingpermissions/README.md#delete_membership) - Delete membership
* [authorize_beta_users](docs/sdks/indexingpermissions/README.md#authorize_beta_users) - Beta users

#### [indexing.shortcuts](docs/sdks/indexingshortcuts/README.md)

* [bulk_index](docs/sdks/indexingshortcuts/README.md#bulk_index) - Bulk index external shortcuts
* [upload](docs/sdks/indexingshortcuts/README.md#upload) - Upload shortcuts

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.chat.upload_files(files=[])

    # Handle response
    print(res)

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from glean.api_client import Glean, models
from glean.api_client.utils import BackoffStrategy, RetryConfig, parse_datetime
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    glean.client.activity.report(events=[
        {
            "action": models.ActivityEventAction.HISTORICAL_VIEW,
            "timestamp": parse_datetime("2000-01-23T04:56:07.000Z"),
            "url": "https://example.com/",
        },
        {
            "action": models.ActivityEventAction.SEARCH,
            "params": {
                "query": "query",
            },
            "timestamp": parse_datetime("2000-01-23T04:56:07.000Z"),
            "url": "https://example.com/search?q=query",
        },
        {
            "action": models.ActivityEventAction.VIEW,
            "params": {
                "duration": 20,
                "referrer": "https://example.com/document",
            },
            "timestamp": parse_datetime("2000-01-23T04:56:07.000Z"),
            "url": "https://example.com/",
        },
    ],
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Use the SDK ...

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from glean.api_client import Glean, models
from glean.api_client.utils import BackoffStrategy, RetryConfig, parse_datetime
import os


with Glean(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    glean.client.activity.report(events=[
        {
            "action": models.ActivityEventAction.HISTORICAL_VIEW,
            "timestamp": parse_datetime("2000-01-23T04:56:07.000Z"),
            "url": "https://example.com/",
        },
        {
            "action": models.ActivityEventAction.SEARCH,
            "params": {
                "query": "query",
            },
            "timestamp": parse_datetime("2000-01-23T04:56:07.000Z"),
            "url": "https://example.com/search?q=query",
        },
        {
            "action": models.ActivityEventAction.VIEW,
            "params": {
                "duration": 20,
                "referrer": "https://example.com/document",
            },
            "timestamp": parse_datetime("2000-01-23T04:56:07.000Z"),
            "url": "https://example.com/",
        },
    ])

    # Use the SDK ...

```
<!-- End Retries [retries] -->

## Error Handling

All operations return a response object or raise an exception:

| Status Code | Description             | Error Type             | Content Type     |
| ----------- | ----------------------- | ---------------------- | ---------------- |
| 400         | Invalid Request         | errors.GleanError      | \*/\*            |
| 401         | Not Authorized          | errors.GleanError      | \*/\*            |
| 403         | Permission Denied       | errors.GleanDataError  | application/json |
| 408         | Request Timeout         | errors.GleanError      | \*/\*            |
| 422         | Invalid Query           | errors.GleanDataError  | application/json |
| 429         | Too Many Requests       | errors.GleanError      | \*/\*            |
| 4XX         | Other Client Errors     | errors.GleanError      | \*/\*            |
| 5XX         | Internal Server Errors  | errors.GleanError      | \*/\*            |


### Example

```python
from glean.api_client import Glean, errors, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:
    try:
        res = g_client.client.search.execute(search_request=models.SearchRequest(
            tracking_token="trackingToken",
            page_size=10,
            query="vacation policy",
            request_options=models.SearchRequestOptions(
                facet_filters=[
                    models.FacetFilter(
                        field_name="type",
                        values=[
                            models.FacetFilterValue(
                                value="article",
                                relation_type=models.RelationType.EQUALS,
                            ),
                            models.FacetFilterValue(
                                value="document",
                                relation_type=models.RelationType.EQUALS,
                            ),
                        ],
                    ),
                    models.FacetFilter(
                        field_name="department",
                        values=[
                            models.FacetFilterValue(
                                value="engineering",
                                relation_type=models.RelationType.EQUALS,
                            ),
                        ],
                    ),
                ],
                facet_bucket_size=246815,
            ),
        ))
        
        # Handle response
        print(res)
    except errors.GleanError as e:
        print(e.message)
        print(e.status_code)
        print(e.raw_response)
        print(e.body)
     # If the server returned structured data
    except errors.GleanDataError as e:
        print(e.data)
        print(e.data.errorMessage)
```

By default, an API error will raise a errors.GleanError exception, which has the following properties:

| Property             | Type             | Description           |
|----------------------|------------------|-----------------------|
| `error.status_code`  | *int*            | The HTTP status code  |
| `error.message`      | *str*            | The error message     |
| `error.raw_response` | *httpx.Response* | The raw HTTP response |
| `error.body`         | *str*            | The response content  |

<!-- No Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Server Variables

The default server `https://{instance}-be.glean.com` contains variables and is set to `https://instance-name-be.glean.com` by default. To override default values, the following parameters are available when initializing the SDK client instance:

| Variable   | Parameter       | Default           | Description                                                                                            |
| ---------- | --------------- | ----------------- | ------------------------------------------------------------------------------------------------------ |
| `instance` | `instance: str` | `"instance-name"` | The instance name (typically the email domain without the TLD) that determines the deployment backend. |

#### Example

```python
from glean.api_client import Glean, models
from glean.api_client.utils import parse_datetime
import os


with Glean(
    instance="<value>"
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    glean.client.activity.report(events=[
        {
            "action": models.ActivityEventAction.HISTORICAL_VIEW,
            "timestamp": parse_datetime("2000-01-23T04:56:07.000Z"),
            "url": "https://example.com/",
        },
        {
            "action": models.ActivityEventAction.SEARCH,
            "params": {
                "query": "query",
            },
            "timestamp": parse_datetime("2000-01-23T04:56:07.000Z"),
            "url": "https://example.com/search?q=query",
        },
        {
            "action": models.ActivityEventAction.VIEW,
            "params": {
                "duration": 20,
                "referrer": "https://example.com/document",
            },
            "timestamp": parse_datetime("2000-01-23T04:56:07.000Z"),
            "url": "https://example.com/",
        },
    ])

    # Use the SDK ...

```

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from glean.api_client import Glean, models
from glean.api_client.utils import parse_datetime
import os


with Glean(
    server_url="https://instance-name-be.glean.com",
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    glean.client.activity.report(events=[
        {
            "action": models.ActivityEventAction.HISTORICAL_VIEW,
            "timestamp": parse_datetime("2000-01-23T04:56:07.000Z"),
            "url": "https://example.com/",
        },
        {
            "action": models.ActivityEventAction.SEARCH,
            "params": {
                "query": "query",
            },
            "timestamp": parse_datetime("2000-01-23T04:56:07.000Z"),
            "url": "https://example.com/search?q=query",
        },
        {
            "action": models.ActivityEventAction.VIEW,
            "params": {
                "duration": 20,
                "referrer": "https://example.com/document",
            },
            "timestamp": parse_datetime("2000-01-23T04:56:07.000Z"),
            "url": "https://example.com/",
        },
    ])

    # Use the SDK ...

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from glean.api_client import Glean
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Glean(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from glean.api_client import Glean
from glean.api_client.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Glean(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Glean` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from glean.api_client import Glean
import os
def main():

    with Glean(
        api_token=os.getenv("GLEAN_API_TOKEN", ""),
    ) as glean:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Glean(
        api_token=os.getenv("GLEAN_API_TOKEN", ""),
    ) as glean:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from glean.api_client import Glean
import logging

logging.basicConfig(level=logging.DEBUG)
s = Glean(debug_logger=logging.getLogger("glean.api_client"))
```

You can also enable a default debug logger by setting an environment variable `GLEAN_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=glean&utm_campaign=python)
