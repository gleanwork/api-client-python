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

with Glean(api_token="client-token", server_url="https://mycompany-be.glean.com") as glean:
    search_response = glean.client.search.query(query="search term")

    print(search_response)

# Example of accessing Indexing namespace 
from glean.api_client import Glean, models
import os

with Glean(api_token="indexing-token", server_url="https://mycompany-be.glean.com") as glean:
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
  * [Server-sent event streaming](#server-sent-event-streaming)
  * [File uploads](#file-uploads)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
  * [Experimental Features and Deprecation Testing](#experimental-features-and-deprecation-testing)
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

The same SDK client can also be used to make asynchronous requests by importing asyncio.

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

The same SDK client can also be used to make asynchronous requests by importing asyncio.

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
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.agents.search(name="HR Policy Agent")

    # Handle response
    print(res)

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

### [Agents](docs/sdks/agents/README.md)

* [search](docs/sdks/agents/README.md#search) - Search agents
* [get](docs/sdks/agents/README.md#get) - Get agent
* [get_schemas](docs/sdks/agents/README.md#get_schemas) - Get agent schemas
* [create_run](docs/sdks/agents/README.md#create_run) - Create agent run

### [Chat](docs/sdks/chatsdk/README.md)

* [create](docs/sdks/chatsdk/README.md#create) - Create a chat response
* [create_stream](docs/sdks/chatsdk/README.md#create_stream) - SDK-only logical operation. HTTP clients must call the base path; the URL fragment is not sent. Create a chat response

### [Client.Activity](docs/sdks/clientactivity/README.md)

* [report](docs/sdks/clientactivity/README.md#report) - Report document activity
* [feedback](docs/sdks/clientactivity/README.md#feedback) - Report client activity

### [Client.Agents](docs/sdks/clientagents/README.md)

* [create](docs/sdks/clientagents/README.md#create) - Create an agent
* [~~retrieve~~](docs/sdks/clientagents/README.md#retrieve) - Retrieve an agent :warning: **Deprecated**
* [update](docs/sdks/clientagents/README.md#update) - Edit an agent
* [~~retrieve_schemas~~](docs/sdks/clientagents/README.md#retrieve_schemas) - List an agent's schemas :warning: **Deprecated**
* [import_](docs/sdks/clientagents/README.md#import_) - Import an agent
* [~~list~~](docs/sdks/clientagents/README.md#list) - Search agents :warning: **Deprecated**
* [~~run_stream~~](docs/sdks/clientagents/README.md#run_stream) - Create an agent run and stream the response :warning: **Deprecated**
* [~~run~~](docs/sdks/clientagents/README.md#run) - Create an agent run and wait for the response :warning: **Deprecated**

### [Client.Announcements](docs/sdks/announcements/README.md)

* [create](docs/sdks/announcements/README.md#create) - Create Announcement
* [delete](docs/sdks/announcements/README.md#delete) - Delete Announcement
* [update](docs/sdks/announcements/README.md#update) - Update Announcement

### [Client.Answers](docs/sdks/answers/README.md)

* [create](docs/sdks/answers/README.md#create) - Create Answer
* [delete](docs/sdks/answers/README.md#delete) - Delete Answer
* [update](docs/sdks/answers/README.md#update) - Update Answer
* [retrieve](docs/sdks/answers/README.md#retrieve) - Read Answer
* [~~list~~](docs/sdks/answers/README.md#list) - List Answers :warning: **Deprecated**

### [Client.Authentication](docs/sdks/clientauthentication/README.md)

* [check_datasource_auth](docs/sdks/clientauthentication/README.md#check_datasource_auth) - Check datasource authorization
* [create_token](docs/sdks/clientauthentication/README.md#create_token) - Create authentication token

### [Client.Chat](docs/sdks/clientchat/README.md)

* [create](docs/sdks/clientchat/README.md#create) - Chat
* [delete_all](docs/sdks/clientchat/README.md#delete_all) - Deletes all saved Chats owned by a user
* [delete](docs/sdks/clientchat/README.md#delete) - Deletes saved Chats
* [retrieve](docs/sdks/clientchat/README.md#retrieve) - Retrieves a Chat
* [list](docs/sdks/clientchat/README.md#list) - Retrieves all saved Chats
* [retrieve_application](docs/sdks/clientchat/README.md#retrieve_application) - Gets the metadata for a custom Chat application
* [upload_files](docs/sdks/clientchat/README.md#upload_files) - Upload files for Chat
* [retrieve_files](docs/sdks/clientchat/README.md#retrieve_files) - Get files uploaded by a user for Chat
* [delete_files](docs/sdks/clientchat/README.md#delete_files) - Delete files uploaded by a user for chat
* [retrieve_file](docs/sdks/clientchat/README.md#retrieve_file) - Download a chat file
* [create_stream](docs/sdks/clientchat/README.md#create_stream) - Chat

### [Client.Collections](docs/sdks/collections/README.md)

* [add_items](docs/sdks/collections/README.md#add_items) - Add Collection item
* [create](docs/sdks/collections/README.md#create) - Create Collection
* [delete](docs/sdks/collections/README.md#delete) - Delete Collection
* [delete_item](docs/sdks/collections/README.md#delete_item) - Delete Collection item
* [update](docs/sdks/collections/README.md#update) - Update Collection
* [update_item](docs/sdks/collections/README.md#update_item) - Update Collection item
* [retrieve](docs/sdks/collections/README.md#retrieve) - Read Collection
* [list](docs/sdks/collections/README.md#list) - List Collections

### [Client.Datasources](docs/sdks/clientdatasources/README.md)

* [retrieve_configuration](docs/sdks/clientdatasources/README.md#retrieve_configuration) - Get datasource instance configuration
* [update_configuration](docs/sdks/clientdatasources/README.md#update_configuration) - Update datasource instance configuration
* [retrieve_credential_status](docs/sdks/clientdatasources/README.md#retrieve_credential_status) - Get datasource instance credential status
* [rotate_credentials](docs/sdks/clientdatasources/README.md#rotate_credentials) - Rotate datasource instance credentials

### [Client.Documents](docs/sdks/clientdocuments/README.md)

* [retrieve_permissions](docs/sdks/clientdocuments/README.md#retrieve_permissions) - Read document permissions
* [retrieve](docs/sdks/clientdocuments/README.md#retrieve) - Read documents
* [retrieve_by_facets](docs/sdks/clientdocuments/README.md#retrieve_by_facets) - Read documents by facets
* [summarize](docs/sdks/clientdocuments/README.md#summarize) - Summarize documents

### [Client.Entities](docs/sdks/entities/README.md)

* [list](docs/sdks/entities/README.md#list) - List entities
* [read_people](docs/sdks/entities/README.md#read_people) - Read people
* [retrieve_person_photo](docs/sdks/entities/README.md#retrieve_person_photo) - Get person photo

### [Client.Governance.Data.Findings](docs/sdks/findings/README.md)

* [create](docs/sdks/findings/README.md#create) - Creates findings export
* [list](docs/sdks/findings/README.md#list) - Lists findings exports
* [download](docs/sdks/findings/README.md#download) - Downloads findings export
* [delete](docs/sdks/findings/README.md#delete) - Deletes findings export

### [Client.Governance.Data.Policies](docs/sdks/policies/README.md)

* [retrieve](docs/sdks/policies/README.md#retrieve) - Gets specified policy
* [update](docs/sdks/policies/README.md#update) - Updates an existing policy
* [list](docs/sdks/policies/README.md#list) - Lists policies
* [create](docs/sdks/policies/README.md#create) - Creates new policy
* [download](docs/sdks/policies/README.md#download) - Downloads violations CSV for policy

### [Client.Governance.Data.Reports](docs/sdks/reports/README.md)

* [create](docs/sdks/reports/README.md#create) - Creates new one-time report
* [download](docs/sdks/reports/README.md#download) - Downloads violations CSV for report
* [status](docs/sdks/reports/README.md#status) - Fetches report run status

### [Client.Governance.Documents.Visibilityoverrides](docs/sdks/visibilityoverrides/README.md)

* [list](docs/sdks/visibilityoverrides/README.md#list) - Fetches documents visibility
* [create](docs/sdks/visibilityoverrides/README.md#create) - Hide or unhide docs

### [Client.Insights](docs/sdks/insights/README.md)

* [retrieve](docs/sdks/insights/README.md#retrieve) - Get insights

### [Client.Messages](docs/sdks/messages/README.md)

* [retrieve](docs/sdks/messages/README.md#retrieve) - Read messages

### [Client.Pins](docs/sdks/pins/README.md)

* [update](docs/sdks/pins/README.md#update) - Update pin
* [retrieve](docs/sdks/pins/README.md#retrieve) - Read pin
* [list](docs/sdks/pins/README.md#list) - List pins
* [create](docs/sdks/pins/README.md#create) - Create pin
* [remove](docs/sdks/pins/README.md#remove) - Delete pin

### [Client.Search](docs/sdks/clientsearch/README.md)

* [query_as_admin](docs/sdks/clientsearch/README.md#query_as_admin) - Search the index (admin)
* [autocomplete](docs/sdks/clientsearch/README.md#autocomplete) - Autocomplete
* [retrieve_feed](docs/sdks/clientsearch/README.md#retrieve_feed) - Feed of documents and events
* [recommendations](docs/sdks/clientsearch/README.md#recommendations) - Recommend documents
* [query](docs/sdks/clientsearch/README.md#query) - Search

### [Client.Shortcuts](docs/sdks/clientshortcuts/README.md)

* [create](docs/sdks/clientshortcuts/README.md#create) - Create shortcut
* [delete](docs/sdks/clientshortcuts/README.md#delete) - Delete shortcut
* [retrieve](docs/sdks/clientshortcuts/README.md#retrieve) - Read shortcut
* [list](docs/sdks/clientshortcuts/README.md#list) - List shortcuts
* [update](docs/sdks/clientshortcuts/README.md#update) - Update shortcut

### [Client.Tools](docs/sdks/tools/README.md)

* [list](docs/sdks/tools/README.md#list) - List available tools
* [run](docs/sdks/tools/README.md#run) - Execute the specified tool
* [retrieve_action_pack_auth_status](docs/sdks/tools/README.md#retrieve_action_pack_auth_status) - Get end-user authentication status for an action pack.
* [authorize_action_pack](docs/sdks/tools/README.md#authorize_action_pack) - Start the OAuth authorization flow for an action pack.
* [retrieve_tool_server_auth_status](docs/sdks/tools/README.md#retrieve_tool_server_auth_status) - Get end-user authentication status for a tool server.
* [authorize_tool_server](docs/sdks/tools/README.md#authorize_tool_server) - Start the OAuth authorization flow for a tool server.
* [get_tool_server_tools](docs/sdks/tools/README.md#get_tool_server_tools) - Get tool definitions from a tool server.

### [Client.Verification](docs/sdks/clientverification/README.md)

* [add_reminder](docs/sdks/clientverification/README.md#add_reminder) - Create verification
* [list](docs/sdks/clientverification/README.md#list) - List verifications
* [verify](docs/sdks/clientverification/README.md#verify) - Update verification

### [Indexing.Authentication](docs/sdks/indexingauthentication/README.md)

* [rotate_token](docs/sdks/indexingauthentication/README.md#rotate_token) - Rotate token

### [Indexing.CustomMetadata](docs/sdks/custommetadata/README.md)

* [upsert](docs/sdks/custommetadata/README.md#upsert) - Add or update custom metadata
* [delete](docs/sdks/custommetadata/README.md#delete) - Remove custom metadata
* [get_schema](docs/sdks/custommetadata/README.md#get_schema) - Retrieve metadata schema
* [upsert_schema](docs/sdks/custommetadata/README.md#upsert_schema) - Create or update metadata schema
* [delete_schema](docs/sdks/custommetadata/README.md#delete_schema) - Remove metadata schema

### [Indexing.Datasource](docs/sdks/indexingdatasource/README.md)

* [status](docs/sdks/indexingdatasource/README.md#status) - Beta: Get datasource status


### [Indexing.Datasources](docs/sdks/indexingdatasources/README.md)

* [add](docs/sdks/indexingdatasources/README.md#add) - Add or update datasource
* [retrieve_config](docs/sdks/indexingdatasources/README.md#retrieve_config) - Get datasource config
* [submit](docs/sdks/indexingdatasources/README.md#submit) - Submit datasource data

### [Indexing.Documents](docs/sdks/indexingdocuments/README.md)

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
* [debug_events](docs/sdks/indexingdocuments/README.md#debug_events) - Beta: Get document lifecycle events


### [Indexing.People](docs/sdks/people/README.md)

* [debug](docs/sdks/people/README.md#debug) - Beta: Get user information

* [~~count~~](docs/sdks/people/README.md#count) - Get user count :warning: **Deprecated**
* [index](docs/sdks/people/README.md#index) - Index employee
* [~~bulk_index~~](docs/sdks/people/README.md#bulk_index) - Bulk index employees :warning: **Deprecated**
* [process_all_employees_and_teams](docs/sdks/people/README.md#process_all_employees_and_teams) - Schedules the processing of uploaded employees and teams
* [delete](docs/sdks/people/README.md#delete) - Delete employee
* [index_team](docs/sdks/people/README.md#index_team) - Index team
* [delete_team](docs/sdks/people/README.md#delete_team) - Delete team
* [bulk_index_teams](docs/sdks/people/README.md#bulk_index_teams) - Bulk index teams

### [Indexing.Permissions](docs/sdks/indexingpermissions/README.md)

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

### [Indexing.Shortcuts](docs/sdks/indexingshortcuts/README.md)

* [bulk_index](docs/sdks/indexingshortcuts/README.md#bulk_index) - Bulk index external shortcuts
* [upload](docs/sdks/indexingshortcuts/README.md#upload) - Upload shortcuts

### [Search](docs/sdks/search/README.md)

* [query](docs/sdks/search/README.md#query) - Search
* [list_filters](docs/sdks/search/README.md#list_filters) - List search filters

### [Skills](docs/sdks/skills/README.md)

* [create](docs/sdks/skills/README.md#create) - Create skill
* [list](docs/sdks/skills/README.md#list) - List skills
* [import_](docs/sdks/skills/README.md#import_) - Import skills from GitHub
* [validate](docs/sdks/skills/README.md#validate) - Validate skill bundle
* [preview_source](docs/sdks/skills/README.md#preview_source) - Preview a GitHub skill source
* [update](docs/sdks/skills/README.md#update) - Update skill
* [delete](docs/sdks/skills/README.md#delete) - Delete skill
* [retrieve](docs/sdks/skills/README.md#retrieve) - Retrieve skill
* [retrieve_content](docs/sdks/skills/README.md#retrieve_content) - Download skill content
* [sync](docs/sdks/skills/README.md#sync) - Sync a GitHub-imported skill
* [create_version](docs/sdks/skills/README.md#create_version) - Create skill version
* [list_versions](docs/sdks/skills/README.md#list_versions) - List skill versions
* [retrieve_version](docs/sdks/skills/README.md#retrieve_version) - Retrieve skill version
* [retrieve_version_content](docs/sdks/skills/README.md#retrieve_version_content) - Download skill version content

### [Triggers](docs/sdks/triggers/README.md)

* [create](docs/sdks/triggers/README.md#create) - Create trigger
* [list](docs/sdks/triggers/README.md#list) - List triggers
* [get](docs/sdks/triggers/README.md#get) - Get trigger
* [update](docs/sdks/triggers/README.md#update) - Update trigger
* [delete](docs/sdks/triggers/README.md#delete) - Delete trigger
* [search_events](docs/sdks/triggers/README.md#search_events) - Search events for a trigger
* [list_presets](docs/sdks/triggers/README.md#list_presets) - List trigger presets
* [get_preset](docs/sdks/triggers/README.md#get_preset) - Get trigger preset
* [list_preset_input_values](docs/sdks/triggers/README.md#list_preset_input_values) - Search trigger preset input values
* [search_preset_events](docs/sdks/triggers/README.md#search_preset_events) - Search events for a trigger preset

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Server-sent event streaming [eventstream] -->
## Server-sent event streaming

[Server-sent events][mdn-sse] are used to stream content from certain
operations. These operations will expose the stream as [Generator][generator] that
can be consumed using a simple `for` loop. The loop will
terminate when the server no longer has any events to send and closes the
underlying connection.  

The stream is also a [Context Manager][context-manager] and can be used with the `with` statement and will close the
underlying connection when the context is exited.

```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.chat.create_stream(input="What is our parental leave policy?", store=True)

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

[mdn-sse]: https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events
[generator]: https://book.pythontips.com/en/latest/generators.html
[context-manager]: https://book.pythontips.com/en/latest/context_managers.html
<!-- End Server-sent event streaming [eventstream] -->

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

    res = glean.skills.create(file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from glean.api_client import Glean
from glean.api_client.utils import BackoffStrategy, RetryConfig
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.agents.search(name="HR Policy Agent",
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from glean.api_client import Glean
from glean.api_client.utils import BackoffStrategy, RetryConfig
import os


with Glean(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.agents.search(name="HR Policy Agent")

    # Handle response
    print(res)

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
from glean.api_client import Glean
import os


with Glean(
    server_idx=0,
    instance="instance-name",
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.agents.search(name="HR Policy Agent")

    # Handle response
    print(res)

```

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from glean.api_client import Glean
import os


with Glean(
    server_url="https://instance-name-be.glean.com",
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.agents.search(name="HR Policy Agent")

    # Handle response
    print(res)

```

### Override Server URL Per-Operation

The server URL can also be overridden on a per-operation basis, provided a server list was specified for the operation. For example:
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.indexing.datasources.submit(datasource_instance="<value>", type_="<value>", request_body={
        "key": "<value>",
        "key1": "<value>",
        "key2": "<value>",
    }, server_url="https://instance-name-be.glean.com")

    # Handle response
    print(res)

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
### httpx2 (Pydantic's httpx fork)

[httpx2](https://httpx2.pydantic.dev/) is Pydantic's maintained fork of `httpx`. To run this SDK on httpx2, call `alias_httpx()` at your program's entry point, before importing the SDK, so every `import httpx` — including the ones inside the SDK — resolves to `httpx2`:
```python
import httpx2

httpx2.alias_httpx()

from glean.api_client import Glean

s = Glean()
```

An SDK can also be generated against httpx2 directly, so it depends on the fork instead of `httpx`, by setting `python.httpClientLibrary: httpx2` in `gen.yaml`.
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

## Experimental Features and Deprecation Testing

The SDK provides options to test upcoming API changes before they become the default behavior. This is useful for:

- **Testing experimental features** before they are generally available
- **Preparing for deprecations** by excluding deprecated endpoints ahead of their removal

### Configuration Options

You can configure these options either via environment variables or SDK constructor options:

#### Using Environment Variables

```python
import os

# Set environment variables before initializing the SDK
os.environ["X_GLEAN_EXCLUDE_DEPRECATED_AFTER"] = "2026-10-15"
os.environ["X_GLEAN_INCLUDE_EXPERIMENTAL"] = "true"

from glean.api_client import Glean

glean = Glean(
    api_token=os.environ.get("GLEAN_API_TOKEN", ""),
    server_url="https://mycompany-be.glean.com",
)
```

#### Using SDK Constructor Options

```python
import os

from glean.api_client import Glean

glean = Glean(
    api_token=os.environ.get("GLEAN_API_TOKEN", ""),
    server_url="https://mycompany-be.glean.com",
    exclude_deprecated_after="2026-10-15",
    include_experimental=True,
)
```

### Option Reference

| Option | Environment Variable | Type | Description |
| ------ | -------------------- | ---- | ----------- |
| `exclude_deprecated_after` | `X_GLEAN_EXCLUDE_DEPRECATED_AFTER` | `str` (date) | Exclude API endpoints that will be deprecated after this date (format: `YYYY-MM-DD`). Use this to test your integration against upcoming deprecations. |
| `include_experimental` | `X_GLEAN_INCLUDE_EXPERIMENTAL` | `bool` | When `True`, enables experimental API features that are not yet generally available. Use this to preview and test new functionality. |

> [!NOTE]
> Environment variables take precedence over SDK constructor options when both are set.

> [!WARNING]
> Experimental features may change or be removed without notice. Do not rely on experimental features in production environments.

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
