# Glean Python API Client

<!-- no [summary] -->

The Glean Python SDK provides convenient access to the Glean REST API from any Python 3.8+ application. It includes type hints for all request parameters and response fields, and supports both synchronous and asynchronous usage via [httpx](https://www.python-httpx.org/).

<!-- Start Summary [summary] -->
## Summary

Glean API: # Introduction
In addition to the data sources that Glean has built-in support for, Glean also provides a REST API that enables customers to put arbitrary content in the search index. This is useful, for example, for doing permissions-aware search over content in internal tools that reside on-prem as well as for searching over applications that Glean does not currently support first class. In addition these APIs allow the customer to push organization data (people info, organization structure etc) into Glean.

# Usage guidelines
This API is evolving fast. Glean will provide advance notice of any planned backwards incompatible changes along
with a 6-month sunset period for anything that requires developers to adopt the new versions.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [Glean Python API Client](#glean-python-api-client)
* [Usage guidelines](#usage-guidelines)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
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
pip install api-client-glean
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add api-client-glean
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from api-client-glean python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "api-client-glean",
# ]
# ///

from glean import Glean

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

### Example

```python
# Synchronous Example
from glean import Glean, models
from glean.utils import parse_datetime
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.client.activity.report(events=[
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

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from glean import Glean, models
from glean.utils import parse_datetime
import os

async def main():

    async with Glean(
        bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
    ) as g_client:

        await g_client.client.activity.report_async(events=[
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

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type | Scheme      | Environment Variable |
| ------------- | ---- | ----------- | -------------------- |
| `bearer_auth` | http | HTTP Bearer | `GLEAN_BEARER_AUTH`  |

To authenticate with the API the `bearer_auth` parameter must be set when initializing the SDK client instance. For example:
```python
from glean import Glean, models
from glean.utils import parse_datetime
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.client.activity.report(events=[
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

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [agents](docs/sdks/agents/README.md)

* [runagent](docs/sdks/agents/README.md#runagent) - Runs an Agent.
* [listagents](docs/sdks/agents/README.md#listagents) - Lists all agents.
* [getagentinputs](docs/sdks/agents/README.md#getagentinputs) - Gets the inputs to an agent.

### [client](docs/sdks/client/README.md)


#### [client.activities](docs/sdks/activities/README.md)

* [report_activity](docs/sdks/activities/README.md#report_activity) - Report client activity

#### [client.activity](docs/sdks/clientactivity/README.md)

* [report](docs/sdks/clientactivity/README.md#report) - Report document activity

#### [client.announcements](docs/sdks/announcements/README.md)

* [create](docs/sdks/announcements/README.md#create) - Create Announcement
* [delete](docs/sdks/announcements/README.md#delete) - Delete Announcement
* [update](docs/sdks/announcements/README.md#update) - Update Announcement

#### [client.answers](docs/sdks/answers/README.md)

* [create](docs/sdks/answers/README.md#create) - Create Answer
* [delete](docs/sdks/answers/README.md#delete) - Delete Answer
* [edit](docs/sdks/answers/README.md#edit) - Update Answer
* [get](docs/sdks/answers/README.md#get) - Read Answer
* [list](docs/sdks/answers/README.md#list) - List Answers

#### [client.authentication](docs/sdks/clientauthentication/README.md)

* [create_token](docs/sdks/clientauthentication/README.md#create_token) - Create authentication token

#### [client.chat](docs/sdks/clientchat/README.md)

* [start](docs/sdks/clientchat/README.md#start) - Chat
* [delete_all](docs/sdks/clientchat/README.md#delete_all) - Deletes all saved Chats owned by a user
* [delete](docs/sdks/clientchat/README.md#delete) - Deletes saved Chats
* [get](docs/sdks/clientchat/README.md#get) - Retrieves a Chat
* [list](docs/sdks/clientchat/README.md#list) - Retrieves all saved Chats
* [get_application](docs/sdks/clientchat/README.md#get_application) - Gets the metadata for a custom Chat application
* [upload_files](docs/sdks/clientchat/README.md#upload_files) - Upload files for Chat.
* [get_files](docs/sdks/clientchat/README.md#get_files) - Get files uploaded by a user for Chat.
* [delete_files](docs/sdks/clientchat/README.md#delete_files) - Delete files uploaded by a user for chat.

#### [client.collections](docs/sdks/collections/README.md)

* [add_items](docs/sdks/collections/README.md#add_items) - Add Collection item
* [create](docs/sdks/collections/README.md#create) - Create Collection
* [delete](docs/sdks/collections/README.md#delete) - Delete Collection
* [delete_item](docs/sdks/collections/README.md#delete_item) - Delete Collection item
* [update](docs/sdks/collections/README.md#update) - Update Collection
* [edit_item](docs/sdks/collections/README.md#edit_item) - Update Collection item
* [get](docs/sdks/collections/README.md#get) - Read Collection
* [list](docs/sdks/collections/README.md#list) - List Collections

#### [client.documents](docs/sdks/clientdocuments/README.md)

* [get_permissions](docs/sdks/clientdocuments/README.md#get_permissions) - Read document permissions
* [get](docs/sdks/clientdocuments/README.md#get) - Read documents
* [get_by_facets](docs/sdks/clientdocuments/README.md#get_by_facets) - Read documents by facets

#### [client.entities](docs/sdks/entities/README.md)

* [list](docs/sdks/entities/README.md#list) - List entities
* [read_people](docs/sdks/entities/README.md#read_people) - Read people

#### [client.insights](docs/sdks/insights/README.md)

* [get](docs/sdks/insights/README.md#get) - Read insights

#### [client.messages](docs/sdks/messages/README.md)

* [get](docs/sdks/messages/README.md#get) - Read messages

#### [client.pins](docs/sdks/pins/README.md)

* [edit](docs/sdks/pins/README.md#edit) - Update pin
* [get](docs/sdks/pins/README.md#get) - Read pin
* [list](docs/sdks/pins/README.md#list) - List pins
* [create](docs/sdks/pins/README.md#create) - Create pin
* [remove](docs/sdks/pins/README.md#remove) - Delete pin

#### [client.search](docs/sdks/search/README.md)

* [admin](docs/sdks/search/README.md#admin) - Search the index (admin)
* [autocomplete](docs/sdks/search/README.md#autocomplete) - Autocomplete
* [get_feed](docs/sdks/search/README.md#get_feed) - Feed of documents and events
* [recommendations](docs/sdks/search/README.md#recommendations) - Recommend documents
* [execute](docs/sdks/search/README.md#execute) - Search

#### [client.shortcuts](docs/sdks/clientshortcuts/README.md)

* [create](docs/sdks/clientshortcuts/README.md#create) - Create shortcut
* [delete](docs/sdks/clientshortcuts/README.md#delete) - Delete shortcut
* [get](docs/sdks/clientshortcuts/README.md#get) - Read shortcut
* [list](docs/sdks/clientshortcuts/README.md#list) - List shortcuts
* [update](docs/sdks/clientshortcuts/README.md#update) - Update shortcut
* [upload](docs/sdks/clientshortcuts/README.md#upload) - Upload shortcuts

#### [client.summarize](docs/sdks/summarize/README.md)

* [generate](docs/sdks/summarize/README.md#generate) - Summarize documents

#### [client.verification](docs/sdks/clientverification/README.md)

* [add_reminder](docs/sdks/clientverification/README.md#add_reminder) - Create verification
* [list](docs/sdks/clientverification/README.md#list) - List verifications
* [verify](docs/sdks/clientverification/README.md#verify) - Update verification


### [indexing](docs/sdks/indexing/README.md)


#### [indexing.authentication](docs/sdks/indexingauthentication/README.md)

* [rotate_token](docs/sdks/indexingauthentication/README.md#rotate_token) - Rotate token

#### [indexing.datasources](docs/sdks/datasources/README.md)

* [add](docs/sdks/datasources/README.md#add) - Add or update datasource
* [get_config](docs/sdks/datasources/README.md#get_config) - Get datasource config

#### [indexing.documents](docs/sdks/indexingdocuments/README.md)

* [add_or_update](docs/sdks/indexingdocuments/README.md#add_or_update) - Index document
* [index](docs/sdks/indexingdocuments/README.md#index) - Index documents
* [bulk_index](docs/sdks/indexingdocuments/README.md#bulk_index) - Bulk index documents
* [process_all](docs/sdks/indexingdocuments/README.md#process_all) - Schedules the processing of uploaded documents
* [delete](docs/sdks/indexingdocuments/README.md#delete) - Delete document

#### [indexing.people](docs/sdks/people/README.md)

* [index](docs/sdks/people/README.md#index) - Index employee
* [bulk_index_employees](docs/sdks/people/README.md#bulk_index_employees) - Bulk index employees
* [~~bulk_index~~](docs/sdks/people/README.md#bulk_index) - Bulk index employees :warning: **Deprecated**
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

#### [indexing.troubleshooting](docs/sdks/troubleshooting/README.md)

* [get_datasource_status](docs/sdks/troubleshooting/README.md#get_datasource_status) - Beta: Get datasource status

* [post_document_debug](docs/sdks/troubleshooting/README.md#post_document_debug) - Beta: Get document information

* [post_documents_debug](docs/sdks/troubleshooting/README.md#post_documents_debug) - Beta: Get information of a batch of documents

* [debug_user](docs/sdks/troubleshooting/README.md#debug_user) - Beta: Get user information

* [check_access](docs/sdks/troubleshooting/README.md#check_access) - Check document access
* [~~get_status~~](docs/sdks/troubleshooting/README.md#get_status) - Get document upload and indexing status :warning: **Deprecated**
* [~~get_document_count~~](docs/sdks/troubleshooting/README.md#get_document_count) - Get document count :warning: **Deprecated**
* [~~get_user_count~~](docs/sdks/troubleshooting/README.md#get_user_count) - Get user count :warning: **Deprecated**

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from glean import Glean, models
from glean.utils import BackoffStrategy, RetryConfig, parse_datetime
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.client.activity.report(events=[
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
from glean import Glean, models
from glean.utils import BackoffStrategy, RetryConfig, parse_datetime
import os


with Glean(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.client.activity.report(events=[
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
from glean import Glean, errors
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
    server_url=os.getenv("GLEAN_SERVER_URL", "https://customer-be.glean.com")
) as glean:
    try:
        res = glean.chat.ask()
        print(res)
    # If the server returned structured data
    except errors.GleanDataError as e:
        print(e.data)
        print(e.data.errorMessage)
    except errors.GleanError as e:
        print(e.message)
        print(e.status_code)
        print(e.raw_response)
        print(e.body)
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

The default server `https://{domain}-be.glean.com` contains variables and is set to `https://domain-be.glean.com` by default. To override default values, the following parameters are available when initializing the SDK client instance:

| Variable | Parameter     | Default    | Description                                                              |
| -------- | ------------- | ---------- | ------------------------------------------------------------------------ |
| `domain` | `domain: str` | `"domain"` | Email domain (without extension) that determines the deployment backend. |

#### Example

```python
from glean import Glean, models
from glean.utils import parse_datetime
import os


with Glean(
    domain="scared-pearl.biz"
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.client.activity.report(events=[
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
from glean import Glean, models
from glean.utils import parse_datetime
import os


with Glean(
    server_url="https://domain-be.glean.com",
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.client.activity.report(events=[
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
from glean import Glean
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Glean(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from glean import Glean
from glean.httpclient import AsyncHttpClient
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
from glean import Glean
import os
def main():

    with Glean(
        bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
    ) as g_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Glean(
        bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
    ) as g_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from glean import Glean
import logging

logging.basicConfig(level=logging.DEBUG)
s = Glean(debug_logger=logging.getLogger("glean"))
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
