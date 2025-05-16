# Search
(*client.search*)

## Overview

### Available Operations

* [query_as_admin](#query_as_admin) - Search the index (admin)
* [autocomplete](#autocomplete) - Autocomplete
* [retrieve_feed](#retrieve_feed) - Feed of documents and events
* [recommendations](#recommendations) - Recommend documents
* [query](#query) - Search

## query_as_admin

Retrieves results for search query without respect for permissions. This is available only to privileged users.

### Example Usage

```python
from datetime import date
from glean import Glean, models
from glean.utils import parse_datetime
import os


with Glean(
    security=models.Security(
        act_as_bearer_token=os.getenv("GLEAN_ACT_AS_BEARER_TOKEN", ""),
    ),
) as g_client:

    res = g_client.client.search.query_as_admin(request=models.SearchRequest(
        tracking_token="trackingToken",
        source_document=models.Document(
            metadata=models.DocumentMetadata(
                datasource="datasource",
                object_type="Feature Request",
                container="container",
                parent_id="JIRA_EN-1337",
                mime_type="mimeType",
                document_id="documentId",
                create_time=parse_datetime("2000-01-23T04:56:07.000Z"),
                update_time=parse_datetime("2000-01-23T04:56:07.000Z"),
                author=models.Person(
                    name="George Clooney",
                    obfuscated_id="abc123",
                    related_documents=[
                        models.RelatedDocuments(
                            query_suggestion=models.QuerySuggestion(
                                query="app:github type:pull author:mortimer",
                                search_provider_info=models.SearchProviderInfo(
                                    name="Google",
                                    search_link_url_template="https://www.google.com/search?q={query}&hl=en",
                                ),
                                label="Mortimer's PRs",
                                datasource="github",
                                request_options=models.SearchRequestOptions(
                                    datasource_filter="JIRA",
                                    datasources_filter=[
                                        "JIRA",
                                    ],
                                    query_overrides_facet_filters=True,
                                    facet_filters=[
                                        models.FacetFilter(
                                            field_name="type",
                                            values=[
                                                models.FacetFilterValue(
                                                    value="Spreadsheet",
                                                    relation_type=models.RelationType.EQUALS,
                                                ),
                                                models.FacetFilterValue(
                                                    value="Presentation",
                                                    relation_type=models.RelationType.EQUALS,
                                                ),
                                            ],
                                        ),
                                    ],
                                    facet_filter_sets=[
                                        models.FacetFilterSet(
                                            filters=[
                                                models.FacetFilter(
                                                    field_name="type",
                                                    values=[
                                                        models.FacetFilterValue(
                                                            value="Spreadsheet",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                        models.FacetFilterValue(
                                                            value="Presentation",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        models.FacetFilterSet(
                                            filters=[
                                                models.FacetFilter(
                                                    field_name="type",
                                                    values=[
                                                        models.FacetFilterValue(
                                                            value="Spreadsheet",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                        models.FacetFilterValue(
                                                            value="Presentation",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        models.FacetFilterSet(
                                            filters=[
                                                models.FacetFilter(
                                                    field_name="type",
                                                    values=[
                                                        models.FacetFilterValue(
                                                            value="Spreadsheet",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                        models.FacetFilterValue(
                                                            value="Presentation",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                    facet_bucket_size=629241,
                                    auth_tokens=[
                                        models.AuthToken(
                                            access_token="123abc",
                                            datasource="gmail",
                                            scope="email profile https://www.googleapis.com/auth/gmail.readonly",
                                            token_type="Bearer",
                                            auth_user="1",
                                        ),
                                    ],
                                ),
                                ranges=[
                                    models.TextRange(
                                        start_index=927545,
                                    ),
                                ],
                                input_details=models.SearchRequestInputDetails(
                                    has_copy_paste=True,
                                ),
                            ),
                            results=[
                                models.SearchResult(
                                    title="title",
                                    url="https://example.com/foo/bar",
                                    native_app_url="slack://foo/bar",
                                    snippets=[
                                        models.SearchResultSnippet(
                                            snippet="snippet",
                                            mime_type="mimeType",
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        models.RelatedDocuments(
                            query_suggestion=models.QuerySuggestion(
                                query="app:github type:pull author:mortimer",
                                search_provider_info=models.SearchProviderInfo(
                                    name="Google",
                                    search_link_url_template="https://www.google.com/search?q={query}&hl=en",
                                ),
                                label="Mortimer's PRs",
                                datasource="github",
                                request_options=models.SearchRequestOptions(
                                    datasource_filter="JIRA",
                                    datasources_filter=[
                                        "JIRA",
                                    ],
                                    query_overrides_facet_filters=True,
                                    facet_filters=[
                                        models.FacetFilter(
                                            field_name="type",
                                            values=[
                                                models.FacetFilterValue(
                                                    value="Spreadsheet",
                                                    relation_type=models.RelationType.EQUALS,
                                                ),
                                                models.FacetFilterValue(
                                                    value="Presentation",
                                                    relation_type=models.RelationType.EQUALS,
                                                ),
                                            ],
                                        ),
                                    ],
                                    facet_filter_sets=[
                                        models.FacetFilterSet(
                                            filters=[
                                                models.FacetFilter(
                                                    field_name="type",
                                                    values=[
                                                        models.FacetFilterValue(
                                                            value="Spreadsheet",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                        models.FacetFilterValue(
                                                            value="Presentation",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        models.FacetFilterSet(
                                            filters=[
                                                models.FacetFilter(
                                                    field_name="type",
                                                    values=[
                                                        models.FacetFilterValue(
                                                            value="Spreadsheet",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                        models.FacetFilterValue(
                                                            value="Presentation",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        models.FacetFilterSet(
                                            filters=[
                                                models.FacetFilter(
                                                    field_name="type",
                                                    values=[
                                                        models.FacetFilterValue(
                                                            value="Spreadsheet",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                        models.FacetFilterValue(
                                                            value="Presentation",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                    facet_bucket_size=629241,
                                    auth_tokens=[
                                        models.AuthToken(
                                            access_token="123abc",
                                            datasource="gmail",
                                            scope="email profile https://www.googleapis.com/auth/gmail.readonly",
                                            token_type="Bearer",
                                            auth_user="1",
                                        ),
                                    ],
                                ),
                                ranges=[
                                    models.TextRange(
                                        start_index=927545,
                                    ),
                                ],
                                input_details=models.SearchRequestInputDetails(
                                    has_copy_paste=True,
                                ),
                            ),
                            results=[
                                models.SearchResult(
                                    title="title",
                                    url="https://example.com/foo/bar",
                                    native_app_url="slack://foo/bar",
                                    snippets=[
                                        models.SearchResultSnippet(
                                            snippet="snippet",
                                            mime_type="mimeType",
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        models.RelatedDocuments(
                            query_suggestion=models.QuerySuggestion(
                                query="app:github type:pull author:mortimer",
                                search_provider_info=models.SearchProviderInfo(
                                    name="Google",
                                    search_link_url_template="https://www.google.com/search?q={query}&hl=en",
                                ),
                                label="Mortimer's PRs",
                                datasource="github",
                                request_options=models.SearchRequestOptions(
                                    datasource_filter="JIRA",
                                    datasources_filter=[
                                        "JIRA",
                                    ],
                                    query_overrides_facet_filters=True,
                                    facet_filters=[
                                        models.FacetFilter(
                                            field_name="type",
                                            values=[
                                                models.FacetFilterValue(
                                                    value="Spreadsheet",
                                                    relation_type=models.RelationType.EQUALS,
                                                ),
                                                models.FacetFilterValue(
                                                    value="Presentation",
                                                    relation_type=models.RelationType.EQUALS,
                                                ),
                                            ],
                                        ),
                                    ],
                                    facet_filter_sets=[
                                        models.FacetFilterSet(
                                            filters=[
                                                models.FacetFilter(
                                                    field_name="type",
                                                    values=[
                                                        models.FacetFilterValue(
                                                            value="Spreadsheet",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                        models.FacetFilterValue(
                                                            value="Presentation",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        models.FacetFilterSet(
                                            filters=[
                                                models.FacetFilter(
                                                    field_name="type",
                                                    values=[
                                                        models.FacetFilterValue(
                                                            value="Spreadsheet",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                        models.FacetFilterValue(
                                                            value="Presentation",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        models.FacetFilterSet(
                                            filters=[
                                                models.FacetFilter(
                                                    field_name="type",
                                                    values=[
                                                        models.FacetFilterValue(
                                                            value="Spreadsheet",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                        models.FacetFilterValue(
                                                            value="Presentation",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                    facet_bucket_size=629241,
                                    auth_tokens=[
                                        models.AuthToken(
                                            access_token="123abc",
                                            datasource="gmail",
                                            scope="email profile https://www.googleapis.com/auth/gmail.readonly",
                                            token_type="Bearer",
                                            auth_user="1",
                                        ),
                                    ],
                                ),
                                ranges=[
                                    models.TextRange(
                                        start_index=927545,
                                    ),
                                ],
                                input_details=models.SearchRequestInputDetails(
                                    has_copy_paste=True,
                                ),
                            ),
                            results=[
                                models.SearchResult(
                                    title="title",
                                    url="https://example.com/foo/bar",
                                    native_app_url="slack://foo/bar",
                                    snippets=[
                                        models.SearchResultSnippet(
                                            snippet="snippet",
                                            mime_type="mimeType",
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                    metadata=models.PersonMetadata(
                        type=models.PersonMetadataType.FULL_TIME,
                        title="Actor",
                        department="Movies",
                        email="george@example.com",
                        location="Hollywood, CA",
                        phone="6505551234",
                        photo_url="https://example.com/george.jpg",
                        start_date=date.fromisoformat("2000-01-23"),
                        datasource_profile=[
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                        ],
                        query_suggestions=models.QuerySuggestionList(
                            suggestions=[
                                models.QuerySuggestion(
                                    query="app:github type:pull author:mortimer",
                                    label="Mortimer's PRs",
                                    datasource="github",
                                ),
                            ],
                        ),
                        invite_info=models.InviteInfo(
                            invites=[
                                models.ChannelInviteInfo(),
                            ],
                        ),
                        custom_fields=[
                            models.CustomFieldData(
                                label="<value>",
                                values=[],
                            ),
                            models.CustomFieldData(
                                label="<value>",
                                values=[],
                            ),
                            models.CustomFieldData(
                                label="<value>",
                                values=[],
                            ),
                        ],
                        badges=[
                            models.Badge(
                                key="deployment_name_new_hire",
                                display_name="New hire",
                                icon_config=models.IconConfig(
                                    color="#343CED",
                                    key="person_icon",
                                    icon_type=models.IconType.GLYPH,
                                    name="user",
                                ),
                            ),
                        ],
                    ),
                ),
                owner=models.Person(
                    name="George Clooney",
                    obfuscated_id="abc123",
                    metadata=models.PersonMetadata(
                        type=models.PersonMetadataType.FULL_TIME,
                        title="Actor",
                        department="Movies",
                        email="george@example.com",
                        location="Hollywood, CA",
                        phone="6505551234",
                        photo_url="https://example.com/george.jpg",
                        start_date=date.fromisoformat("2000-01-23"),
                        datasource_profile=[
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                        ],
                        query_suggestions=models.QuerySuggestionList(
                            suggestions=[
                                models.QuerySuggestion(
                                    query="app:github type:pull author:mortimer",
                                    label="Mortimer's PRs",
                                    datasource="github",
                                ),
                            ],
                        ),
                        invite_info=models.InviteInfo(
                            invites=[
                                models.ChannelInviteInfo(),
                            ],
                        ),
                        badges=[
                            models.Badge(
                                key="deployment_name_new_hire",
                                display_name="New hire",
                                icon_config=models.IconConfig(
                                    color="#343CED",
                                    key="person_icon",
                                    icon_type=models.IconType.GLYPH,
                                    name="user",
                                ),
                            ),
                        ],
                    ),
                ),
                mentioned_people=[
                    models.Person(
                        name="George Clooney",
                        obfuscated_id="abc123",
                    ),
                ],
                components=[
                    "Backend",
                    "Networking",
                ],
                status="[\"Done\"]",
                pins=[
                    models.PinDocument(
                        audience_filters=[
                            models.FacetFilter(
                                field_name="type",
                                values=[
                                    models.FacetFilterValue(
                                        value="Spreadsheet",
                                        relation_type=models.RelationType.EQUALS,
                                    ),
                                    models.FacetFilterValue(
                                        value="Presentation",
                                        relation_type=models.RelationType.EQUALS,
                                    ),
                                ],
                            ),
                        ],
                        document_id="<id>",
                        attribution=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ),
                ],
                assigned_to=models.Person(
                    name="George Clooney",
                    obfuscated_id="abc123",
                    metadata=models.PersonMetadata(
                        type=models.PersonMetadataType.FULL_TIME,
                        title="Actor",
                        department="Movies",
                        email="george@example.com",
                        location="Hollywood, CA",
                        phone="6505551234",
                        photo_url="https://example.com/george.jpg",
                        start_date=date.fromisoformat("2000-01-23"),
                        datasource_profile=[
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                        ],
                        query_suggestions=models.QuerySuggestionList(
                            suggestions=[
                                models.QuerySuggestion(
                                    query="app:github type:pull author:mortimer",
                                    label="Mortimer's PRs",
                                    datasource="github",
                                ),
                            ],
                        ),
                        invite_info=models.InviteInfo(
                            invites=[
                                models.ChannelInviteInfo(),
                            ],
                        ),
                        badges=[
                            models.Badge(
                                key="deployment_name_new_hire",
                                display_name="New hire",
                                icon_config=models.IconConfig(
                                    color="#343CED",
                                    key="person_icon",
                                    icon_type=models.IconType.GLYPH,
                                    name="user",
                                ),
                            ),
                        ],
                    ),
                ),
                updated_by=models.Person(
                    name="George Clooney",
                    obfuscated_id="abc123",
                    metadata=models.PersonMetadata(
                        type=models.PersonMetadataType.FULL_TIME,
                        title="Actor",
                        department="Movies",
                        email="george@example.com",
                        location="Hollywood, CA",
                        phone="6505551234",
                        photo_url="https://example.com/george.jpg",
                        start_date=date.fromisoformat("2000-01-23"),
                        datasource_profile=[
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                        ],
                        query_suggestions=models.QuerySuggestionList(
                            suggestions=[
                                models.QuerySuggestion(
                                    query="app:github type:pull author:mortimer",
                                    label="Mortimer's PRs",
                                    datasource="github",
                                ),
                            ],
                        ),
                        invite_info=models.InviteInfo(
                            invites=[
                                models.ChannelInviteInfo(),
                            ],
                        ),
                        badges=[
                            models.Badge(
                                key="deployment_name_new_hire",
                                display_name="New hire",
                                icon_config=models.IconConfig(
                                    color="#343CED",
                                    key="person_icon",
                                    icon_type=models.IconType.GLYPH,
                                    name="user",
                                ),
                            ),
                        ],
                    ),
                ),
                collections=[
                    models.Collection(
                        name="<value>",
                        description="gadzooks aside turret although as before exalted hospitalization option whether",
                        added_roles=[
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                role=models.UserRole.VERIFIER,
                            ),
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                role=models.UserRole.VERIFIER,
                            ),
                        ],
                        removed_roles=[
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                role=models.UserRole.VIEWER,
                            ),
                        ],
                        audience_filters=[
                            models.FacetFilter(
                                field_name="type",
                                values=[
                                    models.FacetFilterValue(
                                        value="Spreadsheet",
                                        relation_type=models.RelationType.EQUALS,
                                    ),
                                    models.FacetFilterValue(
                                        value="Presentation",
                                        relation_type=models.RelationType.EQUALS,
                                    ),
                                ],
                            ),
                        ],
                        id=740835,
                        creator=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        items=[
                            models.CollectionItem(
                                collection_id=177661,
                                created_by=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                shortcut=models.Shortcut(
                                    input_alias="<value>",
                                    created_by=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    updated_by=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    roles=[
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.VERIFIER,
                                        ),
                                    ],
                                ),
                                item_type=models.CollectionItemItemType.TEXT,
                            ),
                            models.CollectionItem(
                                collection_id=177661,
                                created_by=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                shortcut=models.Shortcut(
                                    input_alias="<value>",
                                    created_by=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    updated_by=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    roles=[
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.VERIFIER,
                                        ),
                                    ],
                                ),
                                item_type=models.CollectionItemItemType.TEXT,
                            ),
                            models.CollectionItem(
                                collection_id=177661,
                                created_by=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                shortcut=models.Shortcut(
                                    input_alias="<value>",
                                    created_by=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    updated_by=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    roles=[
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.VERIFIER,
                                        ),
                                    ],
                                ),
                                item_type=models.CollectionItemItemType.TEXT,
                            ),
                        ],
                    ),
                ],
                interactions=models.DocumentInteractions(
                    reacts=[
                        models.Reaction(
                            reactors=[
                                models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                            ],
                        ),
                        models.Reaction(
                            reactors=[
                                models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                            ],
                        ),
                    ],
                    shares=[
                        models.Share(
                            num_days_ago=867476,
                            sharer=models.Person(
                                name="George Clooney",
                                obfuscated_id="abc123",
                                metadata=models.PersonMetadata(
                                    type=models.PersonMetadataType.FULL_TIME,
                                    title="Actor",
                                    department="Movies",
                                    email="george@example.com",
                                    location="Hollywood, CA",
                                    phone="6505551234",
                                    photo_url="https://example.com/george.jpg",
                                    start_date=date.fromisoformat("2000-01-23"),
                                    datasource_profile=[
                                        models.DatasourceProfile(
                                            datasource="github",
                                            handle="<value>",
                                        ),
                                        models.DatasourceProfile(
                                            datasource="github",
                                            handle="<value>",
                                        ),
                                        models.DatasourceProfile(
                                            datasource="github",
                                            handle="<value>",
                                        ),
                                    ],
                                    query_suggestions=models.QuerySuggestionList(
                                        suggestions=[
                                            models.QuerySuggestion(
                                                query="app:github type:pull author:mortimer",
                                                label="Mortimer's PRs",
                                                datasource="github",
                                            ),
                                        ],
                                    ),
                                    invite_info=models.InviteInfo(
                                        invites=[
                                            models.ChannelInviteInfo(),
                                        ],
                                    ),
                                    badges=[
                                        models.Badge(
                                            key="deployment_name_new_hire",
                                            display_name="New hire",
                                            icon_config=models.IconConfig(
                                                color="#343CED",
                                                key="person_icon",
                                                icon_type=models.IconType.GLYPH,
                                                name="user",
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                        ),
                        models.Share(
                            num_days_ago=867476,
                            sharer=models.Person(
                                name="George Clooney",
                                obfuscated_id="abc123",
                                metadata=models.PersonMetadata(
                                    type=models.PersonMetadataType.FULL_TIME,
                                    title="Actor",
                                    department="Movies",
                                    email="george@example.com",
                                    location="Hollywood, CA",
                                    phone="6505551234",
                                    photo_url="https://example.com/george.jpg",
                                    start_date=date.fromisoformat("2000-01-23"),
                                    datasource_profile=[
                                        models.DatasourceProfile(
                                            datasource="github",
                                            handle="<value>",
                                        ),
                                        models.DatasourceProfile(
                                            datasource="github",
                                            handle="<value>",
                                        ),
                                        models.DatasourceProfile(
                                            datasource="github",
                                            handle="<value>",
                                        ),
                                    ],
                                    query_suggestions=models.QuerySuggestionList(
                                        suggestions=[
                                            models.QuerySuggestion(
                                                query="app:github type:pull author:mortimer",
                                                label="Mortimer's PRs",
                                                datasource="github",
                                            ),
                                        ],
                                    ),
                                    invite_info=models.InviteInfo(
                                        invites=[
                                            models.ChannelInviteInfo(),
                                        ],
                                    ),
                                    badges=[
                                        models.Badge(
                                            key="deployment_name_new_hire",
                                            display_name="New hire",
                                            icon_config=models.IconConfig(
                                                color="#343CED",
                                                key="person_icon",
                                                icon_type=models.IconType.GLYPH,
                                                name="user",
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                        ),
                    ],
                ),
                verification=models.Verification(
                    state=models.State.DEPRECATED,
                    metadata=models.VerificationMetadata(
                        last_verifier=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        reminders=[
                            models.Reminder(
                                assignee=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                requestor=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                remind_at=935874,
                            ),
                            models.Reminder(
                                assignee=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                requestor=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                remind_at=935874,
                            ),
                            models.Reminder(
                                assignee=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                requestor=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                remind_at=935874,
                            ),
                        ],
                        last_reminder=models.Reminder(
                            assignee=models.Person(
                                name="George Clooney",
                                obfuscated_id="abc123",
                                metadata=models.PersonMetadata(
                                    type=models.PersonMetadataType.FULL_TIME,
                                    title="Actor",
                                    department="Movies",
                                    email="george@example.com",
                                    location="Hollywood, CA",
                                    phone="6505551234",
                                    photo_url="https://example.com/george.jpg",
                                    start_date=date.fromisoformat("2000-01-23"),
                                    datasource_profile=[
                                        models.DatasourceProfile(
                                            datasource="github",
                                            handle="<value>",
                                        ),
                                        models.DatasourceProfile(
                                            datasource="github",
                                            handle="<value>",
                                        ),
                                    ],
                                    query_suggestions=models.QuerySuggestionList(
                                        suggestions=[
                                            models.QuerySuggestion(
                                                query="app:github type:pull author:mortimer",
                                                label="Mortimer's PRs",
                                                datasource="github",
                                            ),
                                        ],
                                    ),
                                    invite_info=models.InviteInfo(
                                        invites=[
                                            models.ChannelInviteInfo(),
                                        ],
                                    ),
                                    badges=[
                                        models.Badge(
                                            key="deployment_name_new_hire",
                                            display_name="New hire",
                                            icon_config=models.IconConfig(
                                                color="#343CED",
                                                key="person_icon",
                                                icon_type=models.IconType.GLYPH,
                                                name="user",
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            requestor=models.Person(
                                name="George Clooney",
                                obfuscated_id="abc123",
                                metadata=models.PersonMetadata(
                                    type=models.PersonMetadataType.FULL_TIME,
                                    title="Actor",
                                    department="Movies",
                                    email="george@example.com",
                                    location="Hollywood, CA",
                                    phone="6505551234",
                                    photo_url="https://example.com/george.jpg",
                                    start_date=date.fromisoformat("2000-01-23"),
                                    datasource_profile=[
                                        models.DatasourceProfile(
                                            datasource="github",
                                            handle="<value>",
                                        ),
                                        models.DatasourceProfile(
                                            datasource="github",
                                            handle="<value>",
                                        ),
                                    ],
                                    query_suggestions=models.QuerySuggestionList(
                                        suggestions=[
                                            models.QuerySuggestion(
                                                query="app:github type:pull author:mortimer",
                                                label="Mortimer's PRs",
                                                datasource="github",
                                            ),
                                        ],
                                    ),
                                    invite_info=models.InviteInfo(
                                        invites=[
                                            models.ChannelInviteInfo(),
                                        ],
                                    ),
                                    badges=[
                                        models.Badge(
                                            key="deployment_name_new_hire",
                                            display_name="New hire",
                                            icon_config=models.IconConfig(
                                                color="#343CED",
                                                key="person_icon",
                                                icon_type=models.IconType.GLYPH,
                                                name="user",
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            remind_at=346805,
                        ),
                        candidate_verifiers=[
                            models.Person(
                                name="George Clooney",
                                obfuscated_id="abc123",
                            ),
                        ],
                    ),
                ),
                shortcuts=[
                    models.Shortcut(
                        input_alias="<value>",
                        created_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ),
                    models.Shortcut(
                        input_alias="<value>",
                        created_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ),
                    models.Shortcut(
                        input_alias="<value>",
                        created_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ),
                ],
                custom_data={
                    "someCustomField": models.CustomDataValue(),
                },
                contact_person=models.Person(
                    name="George Clooney",
                    obfuscated_id="abc123",
                    metadata=models.PersonMetadata(
                        type=models.PersonMetadataType.FULL_TIME,
                        title="Actor",
                        department="Movies",
                        email="george@example.com",
                        location="Hollywood, CA",
                        phone="6505551234",
                        photo_url="https://example.com/george.jpg",
                        start_date=date.fromisoformat("2000-01-23"),
                        datasource_profile=[
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                        ],
                        query_suggestions=models.QuerySuggestionList(
                            suggestions=[
                                models.QuerySuggestion(
                                    query="app:github type:pull author:mortimer",
                                    label="Mortimer's PRs",
                                    datasource="github",
                                ),
                            ],
                        ),
                        invite_info=models.InviteInfo(
                            invites=[
                                models.ChannelInviteInfo(),
                            ],
                        ),
                        badges=[
                            models.Badge(
                                key="deployment_name_new_hire",
                                display_name="New hire",
                                icon_config=models.IconConfig(
                                    color="#343CED",
                                    key="person_icon",
                                    icon_type=models.IconType.GLYPH,
                                    name="user",
                                ),
                            ),
                        ],
                    ),
                ),
            ),
        ),
        page_size=100,
        max_snippet_size=400,
        query="vacation policy",
        input_details=models.SearchRequestInputDetails(
            has_copy_paste=True,
        ),
        request_options=models.SearchRequestOptions(
            datasource_filter="JIRA",
            datasources_filter=[
                "JIRA",
            ],
            query_overrides_facet_filters=True,
            facet_filters=[
                models.FacetFilter(
                    field_name="type",
                    values=[
                        models.FacetFilterValue(
                            value="Spreadsheet",
                            relation_type=models.RelationType.EQUALS,
                        ),
                        models.FacetFilterValue(
                            value="Presentation",
                            relation_type=models.RelationType.EQUALS,
                        ),
                    ],
                ),
            ],
            facet_filter_sets=[
                models.FacetFilterSet(
                    filters=[
                        models.FacetFilter(
                            field_name="type",
                            values=[
                                models.FacetFilterValue(
                                    value="Spreadsheet",
                                    relation_type=models.RelationType.EQUALS,
                                ),
                                models.FacetFilterValue(
                                    value="Presentation",
                                    relation_type=models.RelationType.EQUALS,
                                ),
                            ],
                        ),
                    ],
                ),
                models.FacetFilterSet(
                    filters=[
                        models.FacetFilter(
                            field_name="type",
                            values=[
                                models.FacetFilterValue(
                                    value="Spreadsheet",
                                    relation_type=models.RelationType.EQUALS,
                                ),
                                models.FacetFilterValue(
                                    value="Presentation",
                                    relation_type=models.RelationType.EQUALS,
                                ),
                            ],
                        ),
                    ],
                ),
            ],
            facet_bucket_size=421489,
            auth_tokens=[
                models.AuthToken(
                    access_token="123abc",
                    datasource="gmail",
                    scope="email profile https://www.googleapis.com/auth/gmail.readonly",
                    token_type="Bearer",
                    auth_user="1",
                ),
            ],
        ),
        timeout_millis=5000,
        people=[
            models.Person(
                name="George Clooney",
                obfuscated_id="abc123",
            ),
        ],
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SearchRequest](../../models/searchrequest.md)               | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SearchResponse](../../models/searchresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GleanDataError | 403, 422              | application/json      |
| errors.GleanError     | 4XX, 5XX              | \*/\*                 |

## autocomplete

Retrieve query suggestions, operators and documents for the given partially typed query.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    security=models.Security(
        act_as_bearer_token=os.getenv("GLEAN_ACT_AS_BEARER_TOKEN", ""),
    ),
) as g_client:

    res = g_client.client.search.autocomplete(request={
        "tracking_token": "trackingToken",
        "query": "San Fra",
        "datasource": "GDRIVE",
        "result_size": 10,
        "auth_tokens": [
            {
                "access_token": "123abc",
                "datasource": "gmail",
                "scope": "email profile https://www.googleapis.com/auth/gmail.readonly",
                "token_type": "Bearer",
                "auth_user": "1",
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.AutocompleteRequest](../../models/autocompleterequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AutocompleteResponse](../../models/autocompleteresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## retrieve_feed

The personalized feed/home includes different types of contents including suggestions, recents, calendar events and many more.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    security=models.Security(
        act_as_bearer_token=os.getenv("GLEAN_ACT_AS_BEARER_TOKEN", ""),
    ),
) as g_client:

    res = g_client.client.search.retrieve_feed(request={
        "timeout_millis": 5000,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.FeedRequest](../../models/feedrequest.md)                   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FeedResponse](../../models/feedresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## recommendations

Retrieve recommended documents for the given URL or Glean Document ID.

### Example Usage

```python
from datetime import date
from glean import Glean, models
from glean.utils import parse_datetime
import os


with Glean(
    security=models.Security(
        act_as_bearer_token=os.getenv("GLEAN_ACT_AS_BEARER_TOKEN", ""),
    ),
) as g_client:

    res = g_client.client.search.recommendations(request=models.RecommendationsRequest(
        source_document=models.Document(
            metadata=models.DocumentMetadata(
                datasource="datasource",
                object_type="Feature Request",
                container="container",
                parent_id="JIRA_EN-1337",
                mime_type="mimeType",
                document_id="documentId",
                create_time=parse_datetime("2000-01-23T04:56:07.000Z"),
                update_time=parse_datetime("2000-01-23T04:56:07.000Z"),
                author=models.Person(
                    name="George Clooney",
                    obfuscated_id="abc123",
                    related_documents=[
                        models.RelatedDocuments(
                            query_suggestion=models.QuerySuggestion(
                                query="app:github type:pull author:mortimer",
                                search_provider_info=models.SearchProviderInfo(
                                    name="Google",
                                    search_link_url_template="https://www.google.com/search?q={query}&hl=en",
                                ),
                                label="Mortimer's PRs",
                                datasource="github",
                                request_options=models.SearchRequestOptions(
                                    datasource_filter="JIRA",
                                    datasources_filter=[
                                        "JIRA",
                                    ],
                                    query_overrides_facet_filters=True,
                                    facet_filters=[
                                        models.FacetFilter(
                                            field_name="type",
                                            values=[
                                                models.FacetFilterValue(
                                                    value="Spreadsheet",
                                                    relation_type=models.RelationType.EQUALS,
                                                ),
                                                models.FacetFilterValue(
                                                    value="Presentation",
                                                    relation_type=models.RelationType.EQUALS,
                                                ),
                                            ],
                                        ),
                                    ],
                                    facet_filter_sets=[
                                        models.FacetFilterSet(
                                            filters=[
                                                models.FacetFilter(
                                                    field_name="type",
                                                    values=[
                                                        models.FacetFilterValue(
                                                            value="Spreadsheet",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                        models.FacetFilterValue(
                                                            value="Presentation",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        models.FacetFilterSet(
                                            filters=[
                                                models.FacetFilter(
                                                    field_name="type",
                                                    values=[
                                                        models.FacetFilterValue(
                                                            value="Spreadsheet",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                        models.FacetFilterValue(
                                                            value="Presentation",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        models.FacetFilterSet(
                                            filters=[
                                                models.FacetFilter(
                                                    field_name="type",
                                                    values=[
                                                        models.FacetFilterValue(
                                                            value="Spreadsheet",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                        models.FacetFilterValue(
                                                            value="Presentation",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                    facet_bucket_size=711201,
                                    auth_tokens=[
                                        models.AuthToken(
                                            access_token="123abc",
                                            datasource="gmail",
                                            scope="email profile https://www.googleapis.com/auth/gmail.readonly",
                                            token_type="Bearer",
                                            auth_user="1",
                                        ),
                                    ],
                                ),
                                ranges=[
                                    models.TextRange(
                                        start_index=707124,
                                    ),
                                    models.TextRange(
                                        start_index=707124,
                                    ),
                                ],
                                input_details=models.SearchRequestInputDetails(
                                    has_copy_paste=True,
                                ),
                            ),
                            results=[
                                models.SearchResult(
                                    title="title",
                                    url="https://example.com/foo/bar",
                                    native_app_url="slack://foo/bar",
                                    snippets=[
                                        models.SearchResultSnippet(
                                            snippet="snippet",
                                            mime_type="mimeType",
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                    metadata=models.PersonMetadata(
                        type=models.PersonMetadataType.FULL_TIME,
                        title="Actor",
                        department="Movies",
                        email="george@example.com",
                        location="Hollywood, CA",
                        phone="6505551234",
                        photo_url="https://example.com/george.jpg",
                        start_date=date.fromisoformat("2000-01-23"),
                        datasource_profile=[
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                        ],
                        query_suggestions=models.QuerySuggestionList(
                            suggestions=[
                                models.QuerySuggestion(
                                    query="app:github type:pull author:mortimer",
                                    label="Mortimer's PRs",
                                    datasource="github",
                                ),
                            ],
                        ),
                        invite_info=models.InviteInfo(
                            invites=[
                                models.ChannelInviteInfo(),
                            ],
                        ),
                        custom_fields=[
                            models.CustomFieldData(
                                label="<value>",
                                values=[
                                    models.CustomFieldValueStr(),
                                ],
                            ),
                            models.CustomFieldData(
                                label="<value>",
                                values=[
                                    models.CustomFieldValueStr(),
                                ],
                            ),
                        ],
                        badges=[
                            models.Badge(
                                key="deployment_name_new_hire",
                                display_name="New hire",
                                icon_config=models.IconConfig(
                                    color="#343CED",
                                    key="person_icon",
                                    icon_type=models.IconType.GLYPH,
                                    name="user",
                                ),
                            ),
                        ],
                    ),
                ),
                owner=models.Person(
                    name="George Clooney",
                    obfuscated_id="abc123",
                    metadata=models.PersonMetadata(
                        type=models.PersonMetadataType.FULL_TIME,
                        title="Actor",
                        department="Movies",
                        email="george@example.com",
                        location="Hollywood, CA",
                        phone="6505551234",
                        photo_url="https://example.com/george.jpg",
                        start_date=date.fromisoformat("2000-01-23"),
                        datasource_profile=[
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                        ],
                        query_suggestions=models.QuerySuggestionList(
                            suggestions=[
                                models.QuerySuggestion(
                                    query="app:github type:pull author:mortimer",
                                    label="Mortimer's PRs",
                                    datasource="github",
                                ),
                            ],
                        ),
                        invite_info=models.InviteInfo(
                            invites=[
                                models.ChannelInviteInfo(),
                            ],
                        ),
                        badges=[
                            models.Badge(
                                key="deployment_name_new_hire",
                                display_name="New hire",
                                icon_config=models.IconConfig(
                                    color="#343CED",
                                    key="person_icon",
                                    icon_type=models.IconType.GLYPH,
                                    name="user",
                                ),
                            ),
                        ],
                    ),
                ),
                mentioned_people=[
                    models.Person(
                        name="George Clooney",
                        obfuscated_id="abc123",
                    ),
                ],
                components=[
                    "Backend",
                    "Networking",
                ],
                status="[\"Done\"]",
                pins=[
                    models.PinDocument(
                        audience_filters=[
                            models.FacetFilter(
                                field_name="type",
                                values=[
                                    models.FacetFilterValue(
                                        value="Spreadsheet",
                                        relation_type=models.RelationType.EQUALS,
                                    ),
                                    models.FacetFilterValue(
                                        value="Presentation",
                                        relation_type=models.RelationType.EQUALS,
                                    ),
                                ],
                            ),
                        ],
                        document_id="<id>",
                        attribution=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ),
                    models.PinDocument(
                        audience_filters=[
                            models.FacetFilter(
                                field_name="type",
                                values=[
                                    models.FacetFilterValue(
                                        value="Spreadsheet",
                                        relation_type=models.RelationType.EQUALS,
                                    ),
                                    models.FacetFilterValue(
                                        value="Presentation",
                                        relation_type=models.RelationType.EQUALS,
                                    ),
                                ],
                            ),
                        ],
                        document_id="<id>",
                        attribution=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ),
                    models.PinDocument(
                        audience_filters=[
                            models.FacetFilter(
                                field_name="type",
                                values=[
                                    models.FacetFilterValue(
                                        value="Spreadsheet",
                                        relation_type=models.RelationType.EQUALS,
                                    ),
                                    models.FacetFilterValue(
                                        value="Presentation",
                                        relation_type=models.RelationType.EQUALS,
                                    ),
                                ],
                            ),
                        ],
                        document_id="<id>",
                        attribution=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ),
                ],
                assigned_to=models.Person(
                    name="George Clooney",
                    obfuscated_id="abc123",
                    metadata=models.PersonMetadata(
                        type=models.PersonMetadataType.FULL_TIME,
                        title="Actor",
                        department="Movies",
                        email="george@example.com",
                        location="Hollywood, CA",
                        phone="6505551234",
                        photo_url="https://example.com/george.jpg",
                        start_date=date.fromisoformat("2000-01-23"),
                        datasource_profile=[
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                        ],
                        query_suggestions=models.QuerySuggestionList(
                            suggestions=[
                                models.QuerySuggestion(
                                    query="app:github type:pull author:mortimer",
                                    label="Mortimer's PRs",
                                    datasource="github",
                                ),
                            ],
                        ),
                        invite_info=models.InviteInfo(
                            invites=[
                                models.ChannelInviteInfo(),
                            ],
                        ),
                        badges=[
                            models.Badge(
                                key="deployment_name_new_hire",
                                display_name="New hire",
                                icon_config=models.IconConfig(
                                    color="#343CED",
                                    key="person_icon",
                                    icon_type=models.IconType.GLYPH,
                                    name="user",
                                ),
                            ),
                        ],
                    ),
                ),
                updated_by=models.Person(
                    name="George Clooney",
                    obfuscated_id="abc123",
                    metadata=models.PersonMetadata(
                        type=models.PersonMetadataType.FULL_TIME,
                        title="Actor",
                        department="Movies",
                        email="george@example.com",
                        location="Hollywood, CA",
                        phone="6505551234",
                        photo_url="https://example.com/george.jpg",
                        start_date=date.fromisoformat("2000-01-23"),
                        datasource_profile=[
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                        ],
                        query_suggestions=models.QuerySuggestionList(
                            suggestions=[
                                models.QuerySuggestion(
                                    query="app:github type:pull author:mortimer",
                                    label="Mortimer's PRs",
                                    datasource="github",
                                ),
                            ],
                        ),
                        invite_info=models.InviteInfo(
                            invites=[
                                models.ChannelInviteInfo(),
                            ],
                        ),
                        badges=[
                            models.Badge(
                                key="deployment_name_new_hire",
                                display_name="New hire",
                                icon_config=models.IconConfig(
                                    color="#343CED",
                                    key="person_icon",
                                    icon_type=models.IconType.GLYPH,
                                    name="user",
                                ),
                            ),
                        ],
                    ),
                ),
                collections=[
                    models.Collection(
                        name="<value>",
                        description="hence why at epic only supposing",
                        added_roles=[
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                role=models.UserRole.VERIFIER,
                            ),
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                role=models.UserRole.VERIFIER,
                            ),
                        ],
                        removed_roles=[
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                role=models.UserRole.VERIFIER,
                            ),
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                role=models.UserRole.VERIFIER,
                            ),
                        ],
                        audience_filters=[
                            models.FacetFilter(
                                field_name="type",
                                values=[
                                    models.FacetFilterValue(
                                        value="Spreadsheet",
                                        relation_type=models.RelationType.EQUALS,
                                    ),
                                    models.FacetFilterValue(
                                        value="Presentation",
                                        relation_type=models.RelationType.EQUALS,
                                    ),
                                ],
                            ),
                        ],
                        id=253796,
                        creator=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        items=[
                            models.CollectionItem(
                                collection_id=94361,
                                created_by=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                shortcut=models.Shortcut(
                                    input_alias="<value>",
                                    created_by=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    updated_by=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    roles=[
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.VERIFIER,
                                        ),
                                    ],
                                ),
                                item_type=models.CollectionItemItemType.URL,
                            ),
                        ],
                    ),
                ],
                interactions=models.DocumentInteractions(
                    reacts=[
                        models.Reaction(
                            reactors=[
                                models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                            ],
                        ),
                        models.Reaction(
                            reactors=[
                                models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                            ],
                        ),
                        models.Reaction(
                            reactors=[
                                models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                            ],
                        ),
                    ],
                    shares=[
                        models.Share(
                            num_days_ago=652391,
                            sharer=models.Person(
                                name="George Clooney",
                                obfuscated_id="abc123",
                                metadata=models.PersonMetadata(
                                    type=models.PersonMetadataType.FULL_TIME,
                                    title="Actor",
                                    department="Movies",
                                    email="george@example.com",
                                    location="Hollywood, CA",
                                    phone="6505551234",
                                    photo_url="https://example.com/george.jpg",
                                    start_date=date.fromisoformat("2000-01-23"),
                                    datasource_profile=[
                                        models.DatasourceProfile(
                                            datasource="github",
                                            handle="<value>",
                                        ),
                                    ],
                                    query_suggestions=models.QuerySuggestionList(
                                        suggestions=[
                                            models.QuerySuggestion(
                                                query="app:github type:pull author:mortimer",
                                                label="Mortimer's PRs",
                                                datasource="github",
                                            ),
                                        ],
                                    ),
                                    invite_info=models.InviteInfo(
                                        invites=[
                                            models.ChannelInviteInfo(),
                                        ],
                                    ),
                                    badges=[
                                        models.Badge(
                                            key="deployment_name_new_hire",
                                            display_name="New hire",
                                            icon_config=models.IconConfig(
                                                color="#343CED",
                                                key="person_icon",
                                                icon_type=models.IconType.GLYPH,
                                                name="user",
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                        ),
                    ],
                ),
                verification=models.Verification(
                    state=models.State.DEPRECATED,
                    metadata=models.VerificationMetadata(
                        last_verifier=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        reminders=[
                            models.Reminder(
                                assignee=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                requestor=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                remind_at=611121,
                            ),
                            models.Reminder(
                                assignee=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                requestor=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                remind_at=611121,
                            ),
                            models.Reminder(
                                assignee=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                requestor=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                remind_at=611121,
                            ),
                        ],
                        last_reminder=models.Reminder(
                            assignee=models.Person(
                                name="George Clooney",
                                obfuscated_id="abc123",
                                metadata=models.PersonMetadata(
                                    type=models.PersonMetadataType.FULL_TIME,
                                    title="Actor",
                                    department="Movies",
                                    email="george@example.com",
                                    location="Hollywood, CA",
                                    phone="6505551234",
                                    photo_url="https://example.com/george.jpg",
                                    start_date=date.fromisoformat("2000-01-23"),
                                    datasource_profile=[
                                        models.DatasourceProfile(
                                            datasource="github",
                                            handle="<value>",
                                        ),
                                        models.DatasourceProfile(
                                            datasource="github",
                                            handle="<value>",
                                        ),
                                        models.DatasourceProfile(
                                            datasource="github",
                                            handle="<value>",
                                        ),
                                    ],
                                    query_suggestions=models.QuerySuggestionList(
                                        suggestions=[
                                            models.QuerySuggestion(
                                                query="app:github type:pull author:mortimer",
                                                label="Mortimer's PRs",
                                                datasource="github",
                                            ),
                                        ],
                                    ),
                                    invite_info=models.InviteInfo(
                                        invites=[
                                            models.ChannelInviteInfo(),
                                        ],
                                    ),
                                    badges=[
                                        models.Badge(
                                            key="deployment_name_new_hire",
                                            display_name="New hire",
                                            icon_config=models.IconConfig(
                                                color="#343CED",
                                                key="person_icon",
                                                icon_type=models.IconType.GLYPH,
                                                name="user",
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            requestor=models.Person(
                                name="George Clooney",
                                obfuscated_id="abc123",
                                metadata=models.PersonMetadata(
                                    type=models.PersonMetadataType.FULL_TIME,
                                    title="Actor",
                                    department="Movies",
                                    email="george@example.com",
                                    location="Hollywood, CA",
                                    phone="6505551234",
                                    photo_url="https://example.com/george.jpg",
                                    start_date=date.fromisoformat("2000-01-23"),
                                    datasource_profile=[
                                        models.DatasourceProfile(
                                            datasource="github",
                                            handle="<value>",
                                        ),
                                    ],
                                    query_suggestions=models.QuerySuggestionList(
                                        suggestions=[
                                            models.QuerySuggestion(
                                                query="app:github type:pull author:mortimer",
                                                label="Mortimer's PRs",
                                                datasource="github",
                                            ),
                                        ],
                                    ),
                                    invite_info=models.InviteInfo(
                                        invites=[
                                            models.ChannelInviteInfo(),
                                        ],
                                    ),
                                    badges=[
                                        models.Badge(
                                            key="deployment_name_new_hire",
                                            display_name="New hire",
                                            icon_config=models.IconConfig(
                                                color="#343CED",
                                                key="person_icon",
                                                icon_type=models.IconType.GLYPH,
                                                name="user",
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            remind_at=148513,
                        ),
                        candidate_verifiers=[
                            models.Person(
                                name="George Clooney",
                                obfuscated_id="abc123",
                            ),
                        ],
                    ),
                ),
                shortcuts=[
                    models.Shortcut(
                        input_alias="<value>",
                        created_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ),
                    models.Shortcut(
                        input_alias="<value>",
                        created_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ),
                ],
                custom_data={
                    "someCustomField": models.CustomDataValue(),
                },
                contact_person=models.Person(
                    name="George Clooney",
                    obfuscated_id="abc123",
                    metadata=models.PersonMetadata(
                        type=models.PersonMetadataType.FULL_TIME,
                        title="Actor",
                        department="Movies",
                        email="george@example.com",
                        location="Hollywood, CA",
                        phone="6505551234",
                        photo_url="https://example.com/george.jpg",
                        start_date=date.fromisoformat("2000-01-23"),
                        datasource_profile=[
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                        ],
                        query_suggestions=models.QuerySuggestionList(
                            suggestions=[
                                models.QuerySuggestion(
                                    query="app:github type:pull author:mortimer",
                                    label="Mortimer's PRs",
                                    datasource="github",
                                ),
                            ],
                        ),
                        invite_info=models.InviteInfo(
                            invites=[
                                models.ChannelInviteInfo(),
                            ],
                        ),
                        badges=[
                            models.Badge(
                                key="deployment_name_new_hire",
                                display_name="New hire",
                                icon_config=models.IconConfig(
                                    color="#343CED",
                                    key="person_icon",
                                    icon_type=models.IconType.GLYPH,
                                    name="user",
                                ),
                            ),
                        ],
                    ),
                ),
            ),
        ),
        page_size=100,
        max_snippet_size=400,
        request_options=models.RecommendationsRequestOptions(
            facet_filter_sets=[
                models.FacetFilterSet(
                    filters=[
                        models.FacetFilter(
                            field_name="type",
                            values=[
                                models.FacetFilterValue(
                                    value="Spreadsheet",
                                    relation_type=models.RelationType.EQUALS,
                                ),
                                models.FacetFilterValue(
                                    value="Presentation",
                                    relation_type=models.RelationType.EQUALS,
                                ),
                            ],
                        ),
                    ],
                ),
                models.FacetFilterSet(
                    filters=[
                        models.FacetFilter(
                            field_name="type",
                            values=[
                                models.FacetFilterValue(
                                    value="Spreadsheet",
                                    relation_type=models.RelationType.EQUALS,
                                ),
                                models.FacetFilterValue(
                                    value="Presentation",
                                    relation_type=models.RelationType.EQUALS,
                                ),
                            ],
                        ),
                    ],
                ),
                models.FacetFilterSet(
                    filters=[
                        models.FacetFilter(
                            field_name="type",
                            values=[
                                models.FacetFilterValue(
                                    value="Spreadsheet",
                                    relation_type=models.RelationType.EQUALS,
                                ),
                                models.FacetFilterValue(
                                    value="Presentation",
                                    relation_type=models.RelationType.EQUALS,
                                ),
                            ],
                        ),
                    ],
                ),
            ],
            context=models.Document(
                metadata=models.DocumentMetadata(
                    datasource="datasource",
                    object_type="Feature Request",
                    container="container",
                    parent_id="JIRA_EN-1337",
                    mime_type="mimeType",
                    document_id="documentId",
                    create_time=parse_datetime("2000-01-23T04:56:07.000Z"),
                    update_time=parse_datetime("2000-01-23T04:56:07.000Z"),
                    author=models.Person(
                        name="George Clooney",
                        obfuscated_id="abc123",
                        metadata=models.PersonMetadata(
                            type=models.PersonMetadataType.FULL_TIME,
                            title="Actor",
                            department="Movies",
                            email="george@example.com",
                            location="Hollywood, CA",
                            phone="6505551234",
                            photo_url="https://example.com/george.jpg",
                            start_date=date.fromisoformat("2000-01-23"),
                            datasource_profile=[
                                models.DatasourceProfile(
                                    datasource="github",
                                    handle="<value>",
                                ),
                                models.DatasourceProfile(
                                    datasource="github",
                                    handle="<value>",
                                ),
                            ],
                            query_suggestions=models.QuerySuggestionList(
                                suggestions=[
                                    models.QuerySuggestion(
                                        query="app:github type:pull author:mortimer",
                                        label="Mortimer's PRs",
                                        datasource="github",
                                    ),
                                ],
                            ),
                            invite_info=models.InviteInfo(
                                invites=[
                                    models.ChannelInviteInfo(),
                                ],
                            ),
                            badges=[
                                models.Badge(
                                    key="deployment_name_new_hire",
                                    display_name="New hire",
                                    icon_config=models.IconConfig(
                                        color="#343CED",
                                        key="person_icon",
                                        icon_type=models.IconType.GLYPH,
                                        name="user",
                                    ),
                                ),
                            ],
                        ),
                    ),
                    owner=models.Person(
                        name="George Clooney",
                        obfuscated_id="abc123",
                        metadata=models.PersonMetadata(
                            type=models.PersonMetadataType.FULL_TIME,
                            title="Actor",
                            department="Movies",
                            email="george@example.com",
                            location="Hollywood, CA",
                            phone="6505551234",
                            photo_url="https://example.com/george.jpg",
                            start_date=date.fromisoformat("2000-01-23"),
                            datasource_profile=[
                                models.DatasourceProfile(
                                    datasource="github",
                                    handle="<value>",
                                ),
                                models.DatasourceProfile(
                                    datasource="github",
                                    handle="<value>",
                                ),
                                models.DatasourceProfile(
                                    datasource="github",
                                    handle="<value>",
                                ),
                            ],
                            query_suggestions=models.QuerySuggestionList(
                                suggestions=[
                                    models.QuerySuggestion(
                                        query="app:github type:pull author:mortimer",
                                        label="Mortimer's PRs",
                                        datasource="github",
                                    ),
                                ],
                            ),
                            invite_info=models.InviteInfo(
                                invites=[
                                    models.ChannelInviteInfo(),
                                ],
                            ),
                            badges=[
                                models.Badge(
                                    key="deployment_name_new_hire",
                                    display_name="New hire",
                                    icon_config=models.IconConfig(
                                        color="#343CED",
                                        key="person_icon",
                                        icon_type=models.IconType.GLYPH,
                                        name="user",
                                    ),
                                ),
                            ],
                        ),
                    ),
                    components=[
                        "Backend",
                        "Networking",
                    ],
                    status="[\"Done\"]",
                    assigned_to=models.Person(
                        name="George Clooney",
                        obfuscated_id="abc123",
                        metadata=models.PersonMetadata(
                            type=models.PersonMetadataType.FULL_TIME,
                            title="Actor",
                            department="Movies",
                            email="george@example.com",
                            location="Hollywood, CA",
                            phone="6505551234",
                            photo_url="https://example.com/george.jpg",
                            start_date=date.fromisoformat("2000-01-23"),
                            datasource_profile=[
                                models.DatasourceProfile(
                                    datasource="github",
                                    handle="<value>",
                                ),
                                models.DatasourceProfile(
                                    datasource="github",
                                    handle="<value>",
                                ),
                            ],
                            query_suggestions=models.QuerySuggestionList(
                                suggestions=[
                                    models.QuerySuggestion(
                                        query="app:github type:pull author:mortimer",
                                        label="Mortimer's PRs",
                                        datasource="github",
                                    ),
                                ],
                            ),
                            invite_info=models.InviteInfo(
                                invites=[
                                    models.ChannelInviteInfo(),
                                ],
                            ),
                            badges=[
                                models.Badge(
                                    key="deployment_name_new_hire",
                                    display_name="New hire",
                                    icon_config=models.IconConfig(
                                        color="#343CED",
                                        key="person_icon",
                                        icon_type=models.IconType.GLYPH,
                                        name="user",
                                    ),
                                ),
                            ],
                        ),
                    ),
                    updated_by=models.Person(
                        name="George Clooney",
                        obfuscated_id="abc123",
                        metadata=models.PersonMetadata(
                            type=models.PersonMetadataType.FULL_TIME,
                            title="Actor",
                            department="Movies",
                            email="george@example.com",
                            location="Hollywood, CA",
                            phone="6505551234",
                            photo_url="https://example.com/george.jpg",
                            start_date=date.fromisoformat("2000-01-23"),
                            datasource_profile=[
                                models.DatasourceProfile(
                                    datasource="github",
                                    handle="<value>",
                                ),
                            ],
                            query_suggestions=models.QuerySuggestionList(
                                suggestions=[
                                    models.QuerySuggestion(
                                        query="app:github type:pull author:mortimer",
                                        label="Mortimer's PRs",
                                        datasource="github",
                                    ),
                                ],
                            ),
                            invite_info=models.InviteInfo(
                                invites=[
                                    models.ChannelInviteInfo(),
                                ],
                            ),
                            badges=[
                                models.Badge(
                                    key="deployment_name_new_hire",
                                    display_name="New hire",
                                    icon_config=models.IconConfig(
                                        color="#343CED",
                                        key="person_icon",
                                        icon_type=models.IconType.GLYPH,
                                        name="user",
                                    ),
                                ),
                            ],
                        ),
                    ),
                    interactions=models.DocumentInteractions(
                        reacts=[
                            models.Reaction(
                                reactors=[
                                    models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                    ),
                                ],
                            ),
                            models.Reaction(
                                reactors=[
                                    models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                    ),
                                ],
                            ),
                            models.Reaction(
                                reactors=[
                                    models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                    ),
                                ],
                            ),
                        ],
                        shares=[
                            models.Share(
                                num_days_ago=652391,
                                sharer=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ),
                        ],
                    ),
                    verification=models.Verification(
                        state=models.State.DEPRECATED,
                        metadata=models.VerificationMetadata(
                            last_verifier=models.Person(
                                name="George Clooney",
                                obfuscated_id="abc123",
                                metadata=models.PersonMetadata(
                                    type=models.PersonMetadataType.FULL_TIME,
                                    title="Actor",
                                    department="Movies",
                                    email="george@example.com",
                                    location="Hollywood, CA",
                                    phone="6505551234",
                                    photo_url="https://example.com/george.jpg",
                                    start_date=date.fromisoformat("2000-01-23"),
                                    datasource_profile=[
                                        models.DatasourceProfile(
                                            datasource="github",
                                            handle="<value>",
                                        ),
                                        models.DatasourceProfile(
                                            datasource="github",
                                            handle="<value>",
                                        ),
                                        models.DatasourceProfile(
                                            datasource="github",
                                            handle="<value>",
                                        ),
                                    ],
                                    query_suggestions=models.QuerySuggestionList(
                                        suggestions=[
                                            models.QuerySuggestion(
                                                query="app:github type:pull author:mortimer",
                                                label="Mortimer's PRs",
                                                datasource="github",
                                            ),
                                        ],
                                    ),
                                    invite_info=models.InviteInfo(
                                        invites=[
                                            models.ChannelInviteInfo(),
                                        ],
                                    ),
                                    badges=[
                                        models.Badge(
                                            key="deployment_name_new_hire",
                                            display_name="New hire",
                                            icon_config=models.IconConfig(
                                                color="#343CED",
                                                key="person_icon",
                                                icon_type=models.IconType.GLYPH,
                                                name="user",
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            reminders=[
                                models.Reminder(
                                    assignee=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    requestor=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    remind_at=611121,
                                ),
                                models.Reminder(
                                    assignee=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    requestor=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    remind_at=611121,
                                ),
                                models.Reminder(
                                    assignee=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    requestor=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    remind_at=611121,
                                ),
                            ],
                            last_reminder=models.Reminder(
                                assignee=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                requestor=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                remind_at=148513,
                            ),
                            candidate_verifiers=[
                                models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                            ],
                        ),
                    ),
                    custom_data={
                        "someCustomField": models.CustomDataValue(),
                    },
                    contact_person=models.Person(
                        name="George Clooney",
                        obfuscated_id="abc123",
                        metadata=models.PersonMetadata(
                            type=models.PersonMetadataType.FULL_TIME,
                            title="Actor",
                            department="Movies",
                            email="george@example.com",
                            location="Hollywood, CA",
                            phone="6505551234",
                            photo_url="https://example.com/george.jpg",
                            start_date=date.fromisoformat("2000-01-23"),
                            datasource_profile=[
                                models.DatasourceProfile(
                                    datasource="github",
                                    handle="<value>",
                                ),
                                models.DatasourceProfile(
                                    datasource="github",
                                    handle="<value>",
                                ),
                                models.DatasourceProfile(
                                    datasource="github",
                                    handle="<value>",
                                ),
                            ],
                            query_suggestions=models.QuerySuggestionList(
                                suggestions=[
                                    models.QuerySuggestion(
                                        query="app:github type:pull author:mortimer",
                                        label="Mortimer's PRs",
                                        datasource="github",
                                    ),
                                ],
                            ),
                            invite_info=models.InviteInfo(
                                invites=[
                                    models.ChannelInviteInfo(),
                                ],
                            ),
                            badges=[
                                models.Badge(
                                    key="deployment_name_new_hire",
                                    display_name="New hire",
                                    icon_config=models.IconConfig(
                                        color="#343CED",
                                        key="person_icon",
                                        icon_type=models.IconType.GLYPH,
                                        name="user",
                                    ),
                                ),
                            ],
                        ),
                    ),
                ),
            ),
        ),
    ))

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.RecommendationsRequest](../../models/recommendationsrequest.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.ResultsResponse](../../models/resultsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## query

Retrieve results from the index for the given query and filters.

### Example Usage

```python
from datetime import date
from glean import Glean, models
from glean.utils import parse_datetime
import os


with Glean(
    security=models.Security(
        act_as_bearer_token=os.getenv("GLEAN_ACT_AS_BEARER_TOKEN", ""),
    ),
) as g_client:

    res = g_client.client.search.query(request=models.SearchRequest(
        tracking_token="trackingToken",
        source_document=models.Document(
            metadata=models.DocumentMetadata(
                datasource="datasource",
                object_type="Feature Request",
                container="container",
                parent_id="JIRA_EN-1337",
                mime_type="mimeType",
                document_id="documentId",
                create_time=parse_datetime("2000-01-23T04:56:07.000Z"),
                update_time=parse_datetime("2000-01-23T04:56:07.000Z"),
                author=models.Person(
                    name="George Clooney",
                    obfuscated_id="abc123",
                    related_documents=[
                        models.RelatedDocuments(
                            query_suggestion=models.QuerySuggestion(
                                query="app:github type:pull author:mortimer",
                                search_provider_info=models.SearchProviderInfo(
                                    name="Google",
                                    search_link_url_template="https://www.google.com/search?q={query}&hl=en",
                                ),
                                label="Mortimer's PRs",
                                datasource="github",
                                request_options=models.SearchRequestOptions(
                                    datasource_filter="JIRA",
                                    datasources_filter=[
                                        "JIRA",
                                    ],
                                    query_overrides_facet_filters=True,
                                    facet_filters=[
                                        models.FacetFilter(
                                            field_name="type",
                                            values=[
                                                models.FacetFilterValue(
                                                    value="Spreadsheet",
                                                    relation_type=models.RelationType.EQUALS,
                                                ),
                                                models.FacetFilterValue(
                                                    value="Presentation",
                                                    relation_type=models.RelationType.EQUALS,
                                                ),
                                            ],
                                        ),
                                    ],
                                    facet_filter_sets=[
                                        models.FacetFilterSet(
                                            filters=[
                                                models.FacetFilter(
                                                    field_name="type",
                                                    values=[
                                                        models.FacetFilterValue(
                                                            value="Spreadsheet",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                        models.FacetFilterValue(
                                                            value="Presentation",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                    facet_bucket_size=718804,
                                    auth_tokens=[
                                        models.AuthToken(
                                            access_token="123abc",
                                            datasource="gmail",
                                            scope="email profile https://www.googleapis.com/auth/gmail.readonly",
                                            token_type="Bearer",
                                            auth_user="1",
                                        ),
                                    ],
                                ),
                                ranges=[
                                    models.TextRange(
                                        start_index=337360,
                                    ),
                                    models.TextRange(
                                        start_index=337360,
                                    ),
                                ],
                                input_details=models.SearchRequestInputDetails(
                                    has_copy_paste=True,
                                ),
                            ),
                            results=[
                                models.SearchResult(
                                    title="title",
                                    url="https://example.com/foo/bar",
                                    native_app_url="slack://foo/bar",
                                    snippets=[
                                        models.SearchResultSnippet(
                                            snippet="snippet",
                                            mime_type="mimeType",
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        models.RelatedDocuments(
                            query_suggestion=models.QuerySuggestion(
                                query="app:github type:pull author:mortimer",
                                search_provider_info=models.SearchProviderInfo(
                                    name="Google",
                                    search_link_url_template="https://www.google.com/search?q={query}&hl=en",
                                ),
                                label="Mortimer's PRs",
                                datasource="github",
                                request_options=models.SearchRequestOptions(
                                    datasource_filter="JIRA",
                                    datasources_filter=[
                                        "JIRA",
                                    ],
                                    query_overrides_facet_filters=True,
                                    facet_filters=[
                                        models.FacetFilter(
                                            field_name="type",
                                            values=[
                                                models.FacetFilterValue(
                                                    value="Spreadsheet",
                                                    relation_type=models.RelationType.EQUALS,
                                                ),
                                                models.FacetFilterValue(
                                                    value="Presentation",
                                                    relation_type=models.RelationType.EQUALS,
                                                ),
                                            ],
                                        ),
                                    ],
                                    facet_filter_sets=[
                                        models.FacetFilterSet(
                                            filters=[
                                                models.FacetFilter(
                                                    field_name="type",
                                                    values=[
                                                        models.FacetFilterValue(
                                                            value="Spreadsheet",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                        models.FacetFilterValue(
                                                            value="Presentation",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                    facet_bucket_size=718804,
                                    auth_tokens=[
                                        models.AuthToken(
                                            access_token="123abc",
                                            datasource="gmail",
                                            scope="email profile https://www.googleapis.com/auth/gmail.readonly",
                                            token_type="Bearer",
                                            auth_user="1",
                                        ),
                                    ],
                                ),
                                ranges=[
                                    models.TextRange(
                                        start_index=337360,
                                    ),
                                    models.TextRange(
                                        start_index=337360,
                                    ),
                                ],
                                input_details=models.SearchRequestInputDetails(
                                    has_copy_paste=True,
                                ),
                            ),
                            results=[
                                models.SearchResult(
                                    title="title",
                                    url="https://example.com/foo/bar",
                                    native_app_url="slack://foo/bar",
                                    snippets=[
                                        models.SearchResultSnippet(
                                            snippet="snippet",
                                            mime_type="mimeType",
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        models.RelatedDocuments(
                            query_suggestion=models.QuerySuggestion(
                                query="app:github type:pull author:mortimer",
                                search_provider_info=models.SearchProviderInfo(
                                    name="Google",
                                    search_link_url_template="https://www.google.com/search?q={query}&hl=en",
                                ),
                                label="Mortimer's PRs",
                                datasource="github",
                                request_options=models.SearchRequestOptions(
                                    datasource_filter="JIRA",
                                    datasources_filter=[
                                        "JIRA",
                                    ],
                                    query_overrides_facet_filters=True,
                                    facet_filters=[
                                        models.FacetFilter(
                                            field_name="type",
                                            values=[
                                                models.FacetFilterValue(
                                                    value="Spreadsheet",
                                                    relation_type=models.RelationType.EQUALS,
                                                ),
                                                models.FacetFilterValue(
                                                    value="Presentation",
                                                    relation_type=models.RelationType.EQUALS,
                                                ),
                                            ],
                                        ),
                                    ],
                                    facet_filter_sets=[
                                        models.FacetFilterSet(
                                            filters=[
                                                models.FacetFilter(
                                                    field_name="type",
                                                    values=[
                                                        models.FacetFilterValue(
                                                            value="Spreadsheet",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                        models.FacetFilterValue(
                                                            value="Presentation",
                                                            relation_type=models.RelationType.EQUALS,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                    facet_bucket_size=718804,
                                    auth_tokens=[
                                        models.AuthToken(
                                            access_token="123abc",
                                            datasource="gmail",
                                            scope="email profile https://www.googleapis.com/auth/gmail.readonly",
                                            token_type="Bearer",
                                            auth_user="1",
                                        ),
                                    ],
                                ),
                                ranges=[
                                    models.TextRange(
                                        start_index=337360,
                                    ),
                                    models.TextRange(
                                        start_index=337360,
                                    ),
                                ],
                                input_details=models.SearchRequestInputDetails(
                                    has_copy_paste=True,
                                ),
                            ),
                            results=[
                                models.SearchResult(
                                    title="title",
                                    url="https://example.com/foo/bar",
                                    native_app_url="slack://foo/bar",
                                    snippets=[
                                        models.SearchResultSnippet(
                                            snippet="snippet",
                                            mime_type="mimeType",
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                    metadata=models.PersonMetadata(
                        type=models.PersonMetadataType.FULL_TIME,
                        title="Actor",
                        department="Movies",
                        email="george@example.com",
                        location="Hollywood, CA",
                        phone="6505551234",
                        photo_url="https://example.com/george.jpg",
                        start_date=date.fromisoformat("2000-01-23"),
                        datasource_profile=[
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                        ],
                        query_suggestions=models.QuerySuggestionList(
                            suggestions=[
                                models.QuerySuggestion(
                                    query="app:github type:pull author:mortimer",
                                    label="Mortimer's PRs",
                                    datasource="github",
                                ),
                            ],
                        ),
                        invite_info=models.InviteInfo(
                            invites=[
                                models.ChannelInviteInfo(),
                                models.ChannelInviteInfo(),
                            ],
                        ),
                        custom_fields=[
                            models.CustomFieldData(
                                label="<value>",
                                values=[
                                    models.CustomFieldValueStr(),
                                    models.CustomFieldValueStr(),
                                ],
                            ),
                        ],
                        badges=[
                            models.Badge(
                                key="deployment_name_new_hire",
                                display_name="New hire",
                                icon_config=models.IconConfig(
                                    color="#343CED",
                                    key="person_icon",
                                    icon_type=models.IconType.GLYPH,
                                    name="user",
                                ),
                            ),
                        ],
                    ),
                ),
                owner=models.Person(
                    name="George Clooney",
                    obfuscated_id="abc123",
                    metadata=models.PersonMetadata(
                        type=models.PersonMetadataType.FULL_TIME,
                        title="Actor",
                        department="Movies",
                        email="george@example.com",
                        location="Hollywood, CA",
                        phone="6505551234",
                        photo_url="https://example.com/george.jpg",
                        start_date=date.fromisoformat("2000-01-23"),
                        datasource_profile=[
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                        ],
                        query_suggestions=models.QuerySuggestionList(
                            suggestions=[
                                models.QuerySuggestion(
                                    query="app:github type:pull author:mortimer",
                                    label="Mortimer's PRs",
                                    datasource="github",
                                ),
                            ],
                        ),
                        invite_info=models.InviteInfo(
                            invites=[
                                models.ChannelInviteInfo(),
                                models.ChannelInviteInfo(),
                            ],
                        ),
                        badges=[
                            models.Badge(
                                key="deployment_name_new_hire",
                                display_name="New hire",
                                icon_config=models.IconConfig(
                                    color="#343CED",
                                    key="person_icon",
                                    icon_type=models.IconType.GLYPH,
                                    name="user",
                                ),
                            ),
                        ],
                    ),
                ),
                mentioned_people=[
                    models.Person(
                        name="George Clooney",
                        obfuscated_id="abc123",
                    ),
                ],
                components=[
                    "Backend",
                    "Networking",
                ],
                status="[\"Done\"]",
                pins=[
                    models.PinDocument(
                        audience_filters=[
                            models.FacetFilter(
                                field_name="type",
                                values=[
                                    models.FacetFilterValue(
                                        value="Spreadsheet",
                                        relation_type=models.RelationType.EQUALS,
                                    ),
                                    models.FacetFilterValue(
                                        value="Presentation",
                                        relation_type=models.RelationType.EQUALS,
                                    ),
                                ],
                            ),
                        ],
                        document_id="<id>",
                        attribution=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ),
                    models.PinDocument(
                        audience_filters=[
                            models.FacetFilter(
                                field_name="type",
                                values=[
                                    models.FacetFilterValue(
                                        value="Spreadsheet",
                                        relation_type=models.RelationType.EQUALS,
                                    ),
                                    models.FacetFilterValue(
                                        value="Presentation",
                                        relation_type=models.RelationType.EQUALS,
                                    ),
                                ],
                            ),
                        ],
                        document_id="<id>",
                        attribution=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ),
                    models.PinDocument(
                        audience_filters=[
                            models.FacetFilter(
                                field_name="type",
                                values=[
                                    models.FacetFilterValue(
                                        value="Spreadsheet",
                                        relation_type=models.RelationType.EQUALS,
                                    ),
                                    models.FacetFilterValue(
                                        value="Presentation",
                                        relation_type=models.RelationType.EQUALS,
                                    ),
                                ],
                            ),
                        ],
                        document_id="<id>",
                        attribution=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ),
                ],
                assigned_to=models.Person(
                    name="George Clooney",
                    obfuscated_id="abc123",
                    metadata=models.PersonMetadata(
                        type=models.PersonMetadataType.FULL_TIME,
                        title="Actor",
                        department="Movies",
                        email="george@example.com",
                        location="Hollywood, CA",
                        phone="6505551234",
                        photo_url="https://example.com/george.jpg",
                        start_date=date.fromisoformat("2000-01-23"),
                        datasource_profile=[
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                        ],
                        query_suggestions=models.QuerySuggestionList(
                            suggestions=[
                                models.QuerySuggestion(
                                    query="app:github type:pull author:mortimer",
                                    label="Mortimer's PRs",
                                    datasource="github",
                                ),
                            ],
                        ),
                        invite_info=models.InviteInfo(
                            invites=[
                                models.ChannelInviteInfo(),
                                models.ChannelInviteInfo(),
                            ],
                        ),
                        badges=[
                            models.Badge(
                                key="deployment_name_new_hire",
                                display_name="New hire",
                                icon_config=models.IconConfig(
                                    color="#343CED",
                                    key="person_icon",
                                    icon_type=models.IconType.GLYPH,
                                    name="user",
                                ),
                            ),
                        ],
                    ),
                ),
                updated_by=models.Person(
                    name="George Clooney",
                    obfuscated_id="abc123",
                    metadata=models.PersonMetadata(
                        type=models.PersonMetadataType.FULL_TIME,
                        title="Actor",
                        department="Movies",
                        email="george@example.com",
                        location="Hollywood, CA",
                        phone="6505551234",
                        photo_url="https://example.com/george.jpg",
                        start_date=date.fromisoformat("2000-01-23"),
                        datasource_profile=[
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                        ],
                        query_suggestions=models.QuerySuggestionList(
                            suggestions=[
                                models.QuerySuggestion(
                                    query="app:github type:pull author:mortimer",
                                    label="Mortimer's PRs",
                                    datasource="github",
                                ),
                            ],
                        ),
                        invite_info=models.InviteInfo(
                            invites=[
                                models.ChannelInviteInfo(),
                                models.ChannelInviteInfo(),
                            ],
                        ),
                        badges=[
                            models.Badge(
                                key="deployment_name_new_hire",
                                display_name="New hire",
                                icon_config=models.IconConfig(
                                    color="#343CED",
                                    key="person_icon",
                                    icon_type=models.IconType.GLYPH,
                                    name="user",
                                ),
                            ),
                        ],
                    ),
                ),
                collections=[
                    models.Collection(
                        name="<value>",
                        description="incidentally provided bonfire furiously besides whose aw smoggy until following",
                        added_roles=[
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                role=models.UserRole.EDITOR,
                            ),
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                role=models.UserRole.EDITOR,
                            ),
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                role=models.UserRole.EDITOR,
                            ),
                        ],
                        removed_roles=[
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                role=models.UserRole.VIEWER,
                            ),
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                role=models.UserRole.VIEWER,
                            ),
                        ],
                        audience_filters=[
                            models.FacetFilter(
                                field_name="type",
                                values=[
                                    models.FacetFilterValue(
                                        value="Spreadsheet",
                                        relation_type=models.RelationType.EQUALS,
                                    ),
                                    models.FacetFilterValue(
                                        value="Presentation",
                                        relation_type=models.RelationType.EQUALS,
                                    ),
                                ],
                            ),
                        ],
                        id=709012,
                        creator=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        items=[
                            models.CollectionItem(
                                collection_id=94240,
                                created_by=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                shortcut=models.Shortcut(
                                    input_alias="<value>",
                                    created_by=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    updated_by=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    roles=[
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                    ],
                                ),
                                item_type=models.CollectionItemItemType.TEXT,
                            ),
                            models.CollectionItem(
                                collection_id=94240,
                                created_by=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                shortcut=models.Shortcut(
                                    input_alias="<value>",
                                    created_by=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    updated_by=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    roles=[
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                    ],
                                ),
                                item_type=models.CollectionItemItemType.TEXT,
                            ),
                            models.CollectionItem(
                                collection_id=94240,
                                created_by=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                shortcut=models.Shortcut(
                                    input_alias="<value>",
                                    created_by=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    updated_by=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    roles=[
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                    ],
                                ),
                                item_type=models.CollectionItemItemType.TEXT,
                            ),
                        ],
                    ),
                    models.Collection(
                        name="<value>",
                        description="incidentally provided bonfire furiously besides whose aw smoggy until following",
                        added_roles=[
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                role=models.UserRole.EDITOR,
                            ),
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                role=models.UserRole.EDITOR,
                            ),
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                role=models.UserRole.EDITOR,
                            ),
                        ],
                        removed_roles=[
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                role=models.UserRole.VIEWER,
                            ),
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                role=models.UserRole.VIEWER,
                            ),
                        ],
                        audience_filters=[
                            models.FacetFilter(
                                field_name="type",
                                values=[
                                    models.FacetFilterValue(
                                        value="Spreadsheet",
                                        relation_type=models.RelationType.EQUALS,
                                    ),
                                    models.FacetFilterValue(
                                        value="Presentation",
                                        relation_type=models.RelationType.EQUALS,
                                    ),
                                ],
                            ),
                        ],
                        id=709012,
                        creator=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        items=[
                            models.CollectionItem(
                                collection_id=94240,
                                created_by=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                shortcut=models.Shortcut(
                                    input_alias="<value>",
                                    created_by=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    updated_by=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    roles=[
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                    ],
                                ),
                                item_type=models.CollectionItemItemType.TEXT,
                            ),
                            models.CollectionItem(
                                collection_id=94240,
                                created_by=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                shortcut=models.Shortcut(
                                    input_alias="<value>",
                                    created_by=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    updated_by=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    roles=[
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                    ],
                                ),
                                item_type=models.CollectionItemItemType.TEXT,
                            ),
                            models.CollectionItem(
                                collection_id=94240,
                                created_by=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                shortcut=models.Shortcut(
                                    input_alias="<value>",
                                    created_by=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    updated_by=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    roles=[
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                    ],
                                ),
                                item_type=models.CollectionItemItemType.TEXT,
                            ),
                        ],
                    ),
                    models.Collection(
                        name="<value>",
                        description="incidentally provided bonfire furiously besides whose aw smoggy until following",
                        added_roles=[
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                role=models.UserRole.EDITOR,
                            ),
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                role=models.UserRole.EDITOR,
                            ),
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                role=models.UserRole.EDITOR,
                            ),
                        ],
                        removed_roles=[
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                role=models.UserRole.VIEWER,
                            ),
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                role=models.UserRole.VIEWER,
                            ),
                        ],
                        audience_filters=[
                            models.FacetFilter(
                                field_name="type",
                                values=[
                                    models.FacetFilterValue(
                                        value="Spreadsheet",
                                        relation_type=models.RelationType.EQUALS,
                                    ),
                                    models.FacetFilterValue(
                                        value="Presentation",
                                        relation_type=models.RelationType.EQUALS,
                                    ),
                                ],
                            ),
                        ],
                        id=709012,
                        creator=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        items=[
                            models.CollectionItem(
                                collection_id=94240,
                                created_by=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                shortcut=models.Shortcut(
                                    input_alias="<value>",
                                    created_by=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    updated_by=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    roles=[
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                    ],
                                ),
                                item_type=models.CollectionItemItemType.TEXT,
                            ),
                            models.CollectionItem(
                                collection_id=94240,
                                created_by=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                shortcut=models.Shortcut(
                                    input_alias="<value>",
                                    created_by=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    updated_by=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    roles=[
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                    ],
                                ),
                                item_type=models.CollectionItemItemType.TEXT,
                            ),
                            models.CollectionItem(
                                collection_id=94240,
                                created_by=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                shortcut=models.Shortcut(
                                    input_alias="<value>",
                                    created_by=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    updated_by=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                        metadata=models.PersonMetadata(
                                            type=models.PersonMetadataType.FULL_TIME,
                                            title="Actor",
                                            department="Movies",
                                            email="george@example.com",
                                            location="Hollywood, CA",
                                            phone="6505551234",
                                            photo_url="https://example.com/george.jpg",
                                            start_date=date.fromisoformat("2000-01-23"),
                                            datasource_profile=[
                                                models.DatasourceProfile(
                                                    datasource="github",
                                                    handle="<value>",
                                                ),
                                            ],
                                            query_suggestions=models.QuerySuggestionList(
                                                suggestions=[
                                                    models.QuerySuggestion(
                                                        query="app:github type:pull author:mortimer",
                                                        label="Mortimer's PRs",
                                                        datasource="github",
                                                    ),
                                                ],
                                            ),
                                            invite_info=models.InviteInfo(
                                                invites=[
                                                    models.ChannelInviteInfo(),
                                                    models.ChannelInviteInfo(),
                                                ],
                                            ),
                                            badges=[
                                                models.Badge(
                                                    key="deployment_name_new_hire",
                                                    display_name="New hire",
                                                    icon_config=models.IconConfig(
                                                        color="#343CED",
                                                        key="person_icon",
                                                        icon_type=models.IconType.GLYPH,
                                                        name="user",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    roles=[
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                        models.UserRoleSpecification(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                                metadata=models.PersonMetadata(
                                                    type=models.PersonMetadataType.FULL_TIME,
                                                    title="Actor",
                                                    department="Movies",
                                                    email="george@example.com",
                                                    location="Hollywood, CA",
                                                    phone="6505551234",
                                                    photo_url="https://example.com/george.jpg",
                                                    start_date=date.fromisoformat("2000-01-23"),
                                                    datasource_profile=[
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                        models.DatasourceProfile(
                                                            datasource="github",
                                                            handle="<value>",
                                                        ),
                                                    ],
                                                    query_suggestions=models.QuerySuggestionList(
                                                        suggestions=[
                                                            models.QuerySuggestion(
                                                                query="app:github type:pull author:mortimer",
                                                                label="Mortimer's PRs",
                                                                datasource="github",
                                                            ),
                                                        ],
                                                    ),
                                                    invite_info=models.InviteInfo(
                                                        invites=[
                                                            models.ChannelInviteInfo(),
                                                            models.ChannelInviteInfo(),
                                                        ],
                                                    ),
                                                    badges=[
                                                        models.Badge(
                                                            key="deployment_name_new_hire",
                                                            display_name="New hire",
                                                            icon_config=models.IconConfig(
                                                                color="#343CED",
                                                                key="person_icon",
                                                                icon_type=models.IconType.GLYPH,
                                                                name="user",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            role=models.UserRole.ANSWER_MODERATOR,
                                        ),
                                    ],
                                ),
                                item_type=models.CollectionItemItemType.TEXT,
                            ),
                        ],
                    ),
                ],
                interactions=models.DocumentInteractions(
                    reacts=[
                        models.Reaction(
                            reactors=[
                                models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                            ],
                        ),
                        models.Reaction(
                            reactors=[
                                models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                            ],
                        ),
                    ],
                    shares=[
                        models.Share(
                            num_days_ago=211330,
                            sharer=models.Person(
                                name="George Clooney",
                                obfuscated_id="abc123",
                                metadata=models.PersonMetadata(
                                    type=models.PersonMetadataType.FULL_TIME,
                                    title="Actor",
                                    department="Movies",
                                    email="george@example.com",
                                    location="Hollywood, CA",
                                    phone="6505551234",
                                    photo_url="https://example.com/george.jpg",
                                    start_date=date.fromisoformat("2000-01-23"),
                                    datasource_profile=[
                                        models.DatasourceProfile(
                                            datasource="github",
                                            handle="<value>",
                                        ),
                                        models.DatasourceProfile(
                                            datasource="github",
                                            handle="<value>",
                                        ),
                                        models.DatasourceProfile(
                                            datasource="github",
                                            handle="<value>",
                                        ),
                                    ],
                                    query_suggestions=models.QuerySuggestionList(
                                        suggestions=[
                                            models.QuerySuggestion(
                                                query="app:github type:pull author:mortimer",
                                                label="Mortimer's PRs",
                                                datasource="github",
                                            ),
                                        ],
                                    ),
                                    invite_info=models.InviteInfo(
                                        invites=[
                                            models.ChannelInviteInfo(),
                                            models.ChannelInviteInfo(),
                                        ],
                                    ),
                                    badges=[
                                        models.Badge(
                                            key="deployment_name_new_hire",
                                            display_name="New hire",
                                            icon_config=models.IconConfig(
                                                color="#343CED",
                                                key="person_icon",
                                                icon_type=models.IconType.GLYPH,
                                                name="user",
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                        ),
                    ],
                ),
                verification=models.Verification(
                    state=models.State.VERIFIED,
                    metadata=models.VerificationMetadata(
                        last_verifier=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        reminders=[
                            models.Reminder(
                                assignee=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                requestor=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                remind_at=43921,
                            ),
                            models.Reminder(
                                assignee=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                requestor=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                    metadata=models.PersonMetadata(
                                        type=models.PersonMetadataType.FULL_TIME,
                                        title="Actor",
                                        department="Movies",
                                        email="george@example.com",
                                        location="Hollywood, CA",
                                        phone="6505551234",
                                        photo_url="https://example.com/george.jpg",
                                        start_date=date.fromisoformat("2000-01-23"),
                                        datasource_profile=[
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                            models.DatasourceProfile(
                                                datasource="github",
                                                handle="<value>",
                                            ),
                                        ],
                                        query_suggestions=models.QuerySuggestionList(
                                            suggestions=[
                                                models.QuerySuggestion(
                                                    query="app:github type:pull author:mortimer",
                                                    label="Mortimer's PRs",
                                                    datasource="github",
                                                ),
                                            ],
                                        ),
                                        invite_info=models.InviteInfo(
                                            invites=[
                                                models.ChannelInviteInfo(),
                                                models.ChannelInviteInfo(),
                                            ],
                                        ),
                                        badges=[
                                            models.Badge(
                                                key="deployment_name_new_hire",
                                                display_name="New hire",
                                                icon_config=models.IconConfig(
                                                    color="#343CED",
                                                    key="person_icon",
                                                    icon_type=models.IconType.GLYPH,
                                                    name="user",
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                remind_at=43921,
                            ),
                        ],
                        last_reminder=models.Reminder(
                            assignee=models.Person(
                                name="George Clooney",
                                obfuscated_id="abc123",
                                metadata=models.PersonMetadata(
                                    type=models.PersonMetadataType.FULL_TIME,
                                    title="Actor",
                                    department="Movies",
                                    email="george@example.com",
                                    location="Hollywood, CA",
                                    phone="6505551234",
                                    photo_url="https://example.com/george.jpg",
                                    start_date=date.fromisoformat("2000-01-23"),
                                    datasource_profile=[
                                        models.DatasourceProfile(
                                            datasource="github",
                                            handle="<value>",
                                        ),
                                    ],
                                    query_suggestions=models.QuerySuggestionList(
                                        suggestions=[
                                            models.QuerySuggestion(
                                                query="app:github type:pull author:mortimer",
                                                label="Mortimer's PRs",
                                                datasource="github",
                                            ),
                                        ],
                                    ),
                                    invite_info=models.InviteInfo(
                                        invites=[
                                            models.ChannelInviteInfo(),
                                            models.ChannelInviteInfo(),
                                        ],
                                    ),
                                    badges=[
                                        models.Badge(
                                            key="deployment_name_new_hire",
                                            display_name="New hire",
                                            icon_config=models.IconConfig(
                                                color="#343CED",
                                                key="person_icon",
                                                icon_type=models.IconType.GLYPH,
                                                name="user",
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            requestor=models.Person(
                                name="George Clooney",
                                obfuscated_id="abc123",
                                metadata=models.PersonMetadata(
                                    type=models.PersonMetadataType.FULL_TIME,
                                    title="Actor",
                                    department="Movies",
                                    email="george@example.com",
                                    location="Hollywood, CA",
                                    phone="6505551234",
                                    photo_url="https://example.com/george.jpg",
                                    start_date=date.fromisoformat("2000-01-23"),
                                    datasource_profile=[
                                        models.DatasourceProfile(
                                            datasource="github",
                                            handle="<value>",
                                        ),
                                    ],
                                    query_suggestions=models.QuerySuggestionList(
                                        suggestions=[
                                            models.QuerySuggestion(
                                                query="app:github type:pull author:mortimer",
                                                label="Mortimer's PRs",
                                                datasource="github",
                                            ),
                                        ],
                                    ),
                                    invite_info=models.InviteInfo(
                                        invites=[
                                            models.ChannelInviteInfo(),
                                            models.ChannelInviteInfo(),
                                        ],
                                    ),
                                    badges=[
                                        models.Badge(
                                            key="deployment_name_new_hire",
                                            display_name="New hire",
                                            icon_config=models.IconConfig(
                                                color="#343CED",
                                                key="person_icon",
                                                icon_type=models.IconType.GLYPH,
                                                name="user",
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            remind_at=973534,
                        ),
                        candidate_verifiers=[
                            models.Person(
                                name="George Clooney",
                                obfuscated_id="abc123",
                            ),
                        ],
                    ),
                ),
                shortcuts=[
                    models.Shortcut(
                        input_alias="<value>",
                        created_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ),
                    models.Shortcut(
                        input_alias="<value>",
                        created_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ),
                    models.Shortcut(
                        input_alias="<value>",
                        created_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                            metadata=models.PersonMetadata(
                                type=models.PersonMetadataType.FULL_TIME,
                                title="Actor",
                                department="Movies",
                                email="george@example.com",
                                location="Hollywood, CA",
                                phone="6505551234",
                                photo_url="https://example.com/george.jpg",
                                start_date=date.fromisoformat("2000-01-23"),
                                datasource_profile=[
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(
                                    suggestions=[
                                        models.QuerySuggestion(
                                            query="app:github type:pull author:mortimer",
                                            label="Mortimer's PRs",
                                            datasource="github",
                                        ),
                                    ],
                                ),
                                invite_info=models.InviteInfo(
                                    invites=[
                                        models.ChannelInviteInfo(),
                                        models.ChannelInviteInfo(),
                                    ],
                                ),
                                badges=[
                                    models.Badge(
                                        key="deployment_name_new_hire",
                                        display_name="New hire",
                                        icon_config=models.IconConfig(
                                            color="#343CED",
                                            key="person_icon",
                                            icon_type=models.IconType.GLYPH,
                                            name="user",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ),
                ],
                custom_data={
                    "someCustomField": models.CustomDataValue(),
                },
                contact_person=models.Person(
                    name="George Clooney",
                    obfuscated_id="abc123",
                    metadata=models.PersonMetadata(
                        type=models.PersonMetadataType.FULL_TIME,
                        title="Actor",
                        department="Movies",
                        email="george@example.com",
                        location="Hollywood, CA",
                        phone="6505551234",
                        photo_url="https://example.com/george.jpg",
                        start_date=date.fromisoformat("2000-01-23"),
                        datasource_profile=[
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                        ],
                        query_suggestions=models.QuerySuggestionList(
                            suggestions=[
                                models.QuerySuggestion(
                                    query="app:github type:pull author:mortimer",
                                    label="Mortimer's PRs",
                                    datasource="github",
                                ),
                            ],
                        ),
                        invite_info=models.InviteInfo(
                            invites=[
                                models.ChannelInviteInfo(),
                                models.ChannelInviteInfo(),
                            ],
                        ),
                        badges=[
                            models.Badge(
                                key="deployment_name_new_hire",
                                display_name="New hire",
                                icon_config=models.IconConfig(
                                    color="#343CED",
                                    key="person_icon",
                                    icon_type=models.IconType.GLYPH,
                                    name="user",
                                ),
                            ),
                        ],
                    ),
                ),
            ),
        ),
        page_size=100,
        max_snippet_size=400,
        query="vacation policy",
        input_details=models.SearchRequestInputDetails(
            has_copy_paste=True,
        ),
        request_options=models.SearchRequestOptions(
            datasource_filter="JIRA",
            datasources_filter=[
                "JIRA",
            ],
            query_overrides_facet_filters=True,
            facet_filters=[
                models.FacetFilter(
                    field_name="type",
                    values=[
                        models.FacetFilterValue(
                            value="Spreadsheet",
                            relation_type=models.RelationType.EQUALS,
                        ),
                        models.FacetFilterValue(
                            value="Presentation",
                            relation_type=models.RelationType.EQUALS,
                        ),
                    ],
                ),
            ],
            facet_filter_sets=[
                models.FacetFilterSet(
                    filters=[
                        models.FacetFilter(
                            field_name="type",
                            values=[
                                models.FacetFilterValue(
                                    value="Spreadsheet",
                                    relation_type=models.RelationType.EQUALS,
                                ),
                                models.FacetFilterValue(
                                    value="Presentation",
                                    relation_type=models.RelationType.EQUALS,
                                ),
                            ],
                        ),
                    ],
                ),
                models.FacetFilterSet(
                    filters=[
                        models.FacetFilter(
                            field_name="type",
                            values=[
                                models.FacetFilterValue(
                                    value="Spreadsheet",
                                    relation_type=models.RelationType.EQUALS,
                                ),
                                models.FacetFilterValue(
                                    value="Presentation",
                                    relation_type=models.RelationType.EQUALS,
                                ),
                            ],
                        ),
                    ],
                ),
            ],
            facet_bucket_size=400611,
            auth_tokens=[
                models.AuthToken(
                    access_token="123abc",
                    datasource="gmail",
                    scope="email profile https://www.googleapis.com/auth/gmail.readonly",
                    token_type="Bearer",
                    auth_user="1",
                ),
            ],
        ),
        timeout_millis=5000,
        people=[
            models.Person(
                name="George Clooney",
                obfuscated_id="abc123",
            ),
        ],
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SearchRequest](../../models/searchrequest.md)               | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SearchResponse](../../models/searchresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GleanDataError | 403, 422              | application/json      |
| errors.GleanError     | 4XX, 5XX              | \*/\*                 |