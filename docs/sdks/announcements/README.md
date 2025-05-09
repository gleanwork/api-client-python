# Announcements
(*client.announcements*)

## Overview

### Available Operations

* [create](#create) - Create Announcement
* [delete](#delete) - Delete Announcement
* [update](#update) - Update Announcement

## create

Create a textual announcement visible to some set of users based on department and location.

### Example Usage

```python
from datetime import date
from glean import Glean, models
from glean.utils import parse_datetime
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.client.announcements.create(start_time=parse_datetime("2024-06-17T07:14:55.338Z"), end_time=parse_datetime("2024-11-30T17:06:07.804Z"), title="<value>", body={
        "text": "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.",
        "structured_list": [
            models.StructuredTextItem(
                link="https://en.wikipedia.org/wiki/Diffuse_sky_radiation",
                document=models.Document(
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
                                            facet_bucket_size=796474,
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
                                                start_index=86,
                                            ),
                                            models.TextRange(
                                                start_index=169727,
                                            ),
                                            models.TextRange(
                                                start_index=89964,
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
                                            models.CustomFieldValueStr(),
                                        ],
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
                                ],
                                query_suggestions=models.QuerySuggestionList(),
                                invite_info=models.InviteInfo(),
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
                                        query_suggestions=models.QuerySuggestionList(),
                                        invite_info=models.InviteInfo(),
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
                                        query_suggestions=models.QuerySuggestionList(),
                                        invite_info=models.InviteInfo(),
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
                                query_suggestions=models.QuerySuggestionList(),
                                invite_info=models.InviteInfo(),
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
                                query_suggestions=models.QuerySuggestionList(),
                                invite_info=models.InviteInfo(),
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
                                description="yuck mortally round",
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
                                                query_suggestions=models.QuerySuggestionList(),
                                                invite_info=models.InviteInfo(),
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
                                                query_suggestions=models.QuerySuggestionList(),
                                                invite_info=models.InviteInfo(),
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
                                                query_suggestions=models.QuerySuggestionList(),
                                                invite_info=models.InviteInfo(),
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
                                id=924484,
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
                                        query_suggestions=models.QuerySuggestionList(),
                                        invite_info=models.InviteInfo(),
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
                                        query_suggestions=models.QuerySuggestionList(),
                                        invite_info=models.InviteInfo(),
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
                                        collection_id=583353,
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
                                                query_suggestions=models.QuerySuggestionList(),
                                                invite_info=models.InviteInfo(),
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
                                                    query_suggestions=models.QuerySuggestionList(),
                                                    invite_info=models.InviteInfo(),
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
                                                    query_suggestions=models.QuerySuggestionList(),
                                                    invite_info=models.InviteInfo(),
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
                                                            query_suggestions=models.QuerySuggestionList(),
                                                            invite_info=models.InviteInfo(),
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
                                                    role=models.UserRole.OWNER,
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
                                                            query_suggestions=models.QuerySuggestionList(),
                                                            invite_info=models.InviteInfo(),
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
                                models.Reaction(),
                                models.Reaction(),
                            ],
                            shares=[
                                models.Share(
                                    num_days_ago=911742,
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
                                            query_suggestions=models.QuerySuggestionList(),
                                            invite_info=models.InviteInfo(),
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
                                        query_suggestions=models.QuerySuggestionList(),
                                        invite_info=models.InviteInfo(),
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
                                                query_suggestions=models.QuerySuggestionList(),
                                                invite_info=models.InviteInfo(),
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
                                                query_suggestions=models.QuerySuggestionList(),
                                                invite_info=models.InviteInfo(),
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
                                        remind_at=428745,
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
                                            query_suggestions=models.QuerySuggestionList(),
                                            invite_info=models.InviteInfo(),
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
                                            query_suggestions=models.QuerySuggestionList(),
                                            invite_info=models.InviteInfo(),
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
                                    remind_at=860420,
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
                                        query_suggestions=models.QuerySuggestionList(),
                                        invite_info=models.InviteInfo(),
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
                                        query_suggestions=models.QuerySuggestionList(),
                                        invite_info=models.InviteInfo(),
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
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(),
                                invite_info=models.InviteInfo(),
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
                text="Because its wavelengths are shorter, blue light is more strongly scattered than the longer-wavelength lights, red or green. Hence the result that when looking at the sky away from the direct incident sunlight, the human eye perceives the sky to be blue.",
            ),
            models.StructuredTextItem(
                link="https://en.wikipedia.org/wiki/Diffuse_sky_radiation",
                document=models.Document(
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
                                ],
                                query_suggestions=models.QuerySuggestionList(),
                                invite_info=models.InviteInfo(),
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
                                ],
                                query_suggestions=models.QuerySuggestionList(),
                                invite_info=models.InviteInfo(),
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
                                query_suggestions=models.QuerySuggestionList(),
                                invite_info=models.InviteInfo(),
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
                                query_suggestions=models.QuerySuggestionList(),
                                invite_info=models.InviteInfo(),
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
                        interactions=models.DocumentInteractions(),
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
                                        query_suggestions=models.QuerySuggestionList(),
                                        invite_info=models.InviteInfo(),
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
                                            query_suggestions=models.QuerySuggestionList(),
                                            invite_info=models.InviteInfo(),
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
                                            query_suggestions=models.QuerySuggestionList(),
                                            invite_info=models.InviteInfo(),
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
                                    remind_at=284120,
                                ),
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
                                ],
                                query_suggestions=models.QuerySuggestionList(),
                                invite_info=models.InviteInfo(),
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
                text="Because its wavelengths are shorter, blue light is more strongly scattered than the longer-wavelength lights, red or green. Hence the result that when looking at the sky away from the direct incident sunlight, the human eye perceives the sky to be blue.",
            ),
        ],
    }, audience_filters=[
        {
            "field_name": "type",
            "values": [
                {
                    "value": "Spreadsheet",
                    "relation_type": models.RelationType.EQUALS,
                },
                {
                    "value": "Presentation",
                    "relation_type": models.RelationType.EQUALS,
                },
            ],
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                             | Type                                                                                                                                                                                                  | Required                                                                                                                                                                                              | Description                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                                                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                    | The date and time at which the announcement becomes active.                                                                                                                                           |
| `end_time`                                                                                                                                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                    | The date and time at which the announcement expires.                                                                                                                                                  |
| `title`                                                                                                                                                                                               | *str*                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                    | The headline of the announcement.                                                                                                                                                                     |
| `body`                                                                                                                                                                                                | [Optional[models.StructuredText]](../../models/structuredtext.md)                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                    | N/A                                                                                                                                                                                                   |
| `emoji`                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | An emoji used to indicate the nature of the announcement.                                                                                                                                             |
| `thumbnail`                                                                                                                                                                                           | [Optional[models.Thumbnail]](../../models/thumbnail.md)                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                    | N/A                                                                                                                                                                                                   |
| `banner`                                                                                                                                                                                              | [Optional[models.Thumbnail]](../../models/thumbnail.md)                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                    | N/A                                                                                                                                                                                                   |
| `audience_filters`                                                                                                                                                                                    | List[[models.FacetFilter](../../models/facetfilter.md)]                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                    | Filters which restrict who should see the announcement. Values are taken from the corresponding filters in people search.                                                                             |
| `source_document_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | The Glean Document ID of the source document this Announcement was created from (e.g. Slack thread).                                                                                                  |
| `hide_attribution`                                                                                                                                                                                    | *Optional[bool]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                    | Whether or not to hide an author attribution.                                                                                                                                                         |
| `channel`                                                                                                                                                                                             | [Optional[models.CreateAnnouncementRequestChannel]](../../models/createannouncementrequestchannel.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                    | This determines whether this is a Social Feed post or a regular announcement.                                                                                                                         |
| `post_type`                                                                                                                                                                                           | [Optional[models.CreateAnnouncementRequestPostType]](../../models/createannouncementrequestposttype.md)                                                                                               | :heavy_minus_sign:                                                                                                                                                                                    | This determines whether this is an external-link post or a regular announcement post. TEXT - Regular announcement that can contain rich text. LINK - Announcement that is linked to an external site. |
| `is_prioritized`                                                                                                                                                                                      | *Optional[bool]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                    | Used by the Social Feed to pin posts to the front of the feed.                                                                                                                                        |
| `view_url`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | URL for viewing the announcement. It will be set to document URL for announcements from other datasources e.g. simpplr. Can only be written when channel="SOCIAL_FEED".                               |
| `retries`                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                   |

### Response

**[models.Announcement](../../models/announcement.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## delete

Delete an existing user-generated announcement.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    g_client.client.announcements.delete(id=545907)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | The opaque id of the announcement to be deleted.                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## update

Update a textual announcement visible to some set of users based on department and location.

### Example Usage

```python
from datetime import date
from glean import Glean, models
from glean.utils import parse_datetime
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.client.announcements.update(start_time=parse_datetime("2025-07-28T19:04:48.565Z"), end_time=parse_datetime("2024-10-16T10:52:42.015Z"), title="<value>", id=761625, body={
        "text": "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.",
        "structured_list": [
            models.StructuredTextItem(
                link="https://en.wikipedia.org/wiki/Diffuse_sky_radiation",
                document=models.Document(
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
                                            ],
                                            facet_bucket_size=488852,
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
                                                start_index=54062,
                                            ),
                                            models.TextRange(
                                                start_index=896501,
                                            ),
                                            models.TextRange(
                                                start_index=446863,
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
                                            facet_bucket_size=249440,
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
                                        input_details=models.SearchRequestInputDetails(
                                            has_copy_paste=True,
                                        ),
                                    ),
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
                                            facet_bucket_size=789275,
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
                                        input_details=models.SearchRequestInputDetails(
                                            has_copy_paste=True,
                                        ),
                                    ),
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
                                        values=[
                                            models.CustomFieldValueStr(),
                                            models.CustomFieldValueStr(),
                                            models.CustomFieldValueStr(),
                                        ],
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
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(),
                                invite_info=models.InviteInfo(),
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
                                        query_suggestions=models.QuerySuggestionList(),
                                        invite_info=models.InviteInfo(),
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
                                        query_suggestions=models.QuerySuggestionList(),
                                        invite_info=models.InviteInfo(),
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
                                        query_suggestions=models.QuerySuggestionList(),
                                        invite_info=models.InviteInfo(),
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
                                        query_suggestions=models.QuerySuggestionList(),
                                        invite_info=models.InviteInfo(),
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
                                        query_suggestions=models.QuerySuggestionList(),
                                        invite_info=models.InviteInfo(),
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
                                        query_suggestions=models.QuerySuggestionList(),
                                        invite_info=models.InviteInfo(),
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
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(),
                                invite_info=models.InviteInfo(),
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
                                query_suggestions=models.QuerySuggestionList(),
                                invite_info=models.InviteInfo(),
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
                                description="daintily certainly yak surprised beyond blah intensely",
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
                                                query_suggestions=models.QuerySuggestionList(),
                                                invite_info=models.InviteInfo(),
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
                                                query_suggestions=models.QuerySuggestionList(),
                                                invite_info=models.InviteInfo(),
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
                                                ],
                                                query_suggestions=models.QuerySuggestionList(),
                                                invite_info=models.InviteInfo(),
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
                                                ],
                                                query_suggestions=models.QuerySuggestionList(),
                                                invite_info=models.InviteInfo(),
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
                                id=249026,
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
                                        query_suggestions=models.QuerySuggestionList(),
                                        invite_info=models.InviteInfo(),
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
                                        query_suggestions=models.QuerySuggestionList(),
                                        invite_info=models.InviteInfo(),
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
                                        collection_id=784089,
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
                                                query_suggestions=models.QuerySuggestionList(),
                                                invite_info=models.InviteInfo(),
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
                                                    query_suggestions=models.QuerySuggestionList(),
                                                    invite_info=models.InviteInfo(),
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
                                                    query_suggestions=models.QuerySuggestionList(),
                                                    invite_info=models.InviteInfo(),
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
                                                            query_suggestions=models.QuerySuggestionList(),
                                                            invite_info=models.InviteInfo(),
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
                                                            query_suggestions=models.QuerySuggestionList(),
                                                            invite_info=models.InviteInfo(),
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
                                        collection_id=416023,
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
                                                query_suggestions=models.QuerySuggestionList(),
                                                invite_info=models.InviteInfo(),
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
                                                    query_suggestions=models.QuerySuggestionList(),
                                                    invite_info=models.InviteInfo(),
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
                                                    query_suggestions=models.QuerySuggestionList(),
                                                    invite_info=models.InviteInfo(),
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
                                        item_type=models.CollectionItemItemType.COLLECTION,
                                    ),
                                ],
                            ),
                            models.Collection(
                                name="<value>",
                                description="misjudge scare cinema ouch weary euphonium",
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
                                id=553539,
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
                                        query_suggestions=models.QuerySuggestionList(),
                                        invite_info=models.InviteInfo(),
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
                                        query_suggestions=models.QuerySuggestionList(),
                                        invite_info=models.InviteInfo(),
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
                            models.Collection(
                                name="<value>",
                                description="exotic fussy shadowy",
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
                                id=890948,
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
                                        query_suggestions=models.QuerySuggestionList(),
                                        invite_info=models.InviteInfo(),
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
                                        query_suggestions=models.QuerySuggestionList(),
                                        invite_info=models.InviteInfo(),
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
                                models.Reaction(),
                                models.Reaction(),
                            ],
                            shares=[
                                models.Share(
                                    num_days_ago=178177,
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
                                            query_suggestions=models.QuerySuggestionList(),
                                            invite_info=models.InviteInfo(),
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
                            state=models.State.UNVERIFIED,
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
                                        query_suggestions=models.QuerySuggestionList(),
                                        invite_info=models.InviteInfo(),
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
                                                query_suggestions=models.QuerySuggestionList(),
                                                invite_info=models.InviteInfo(),
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
                                                query_suggestions=models.QuerySuggestionList(),
                                                invite_info=models.InviteInfo(),
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
                                        remind_at=691669,
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
                                            query_suggestions=models.QuerySuggestionList(),
                                            invite_info=models.InviteInfo(),
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
                                            query_suggestions=models.QuerySuggestionList(),
                                            invite_info=models.InviteInfo(),
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
                                    remind_at=219050,
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
                                        query_suggestions=models.QuerySuggestionList(),
                                        invite_info=models.InviteInfo(),
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
                                        query_suggestions=models.QuerySuggestionList(),
                                        invite_info=models.InviteInfo(),
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
                                query_suggestions=models.QuerySuggestionList(),
                                invite_info=models.InviteInfo(),
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
                text="Because its wavelengths are shorter, blue light is more strongly scattered than the longer-wavelength lights, red or green. Hence the result that when looking at the sky away from the direct incident sunlight, the human eye perceives the sky to be blue.",
            ),
            models.StructuredTextItem(
                link="https://en.wikipedia.org/wiki/Diffuse_sky_radiation",
                document=models.Document(
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
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(),
                                invite_info=models.InviteInfo(),
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
                                query_suggestions=models.QuerySuggestionList(),
                                invite_info=models.InviteInfo(),
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
                                    models.DatasourceProfile(
                                        datasource="github",
                                        handle="<value>",
                                    ),
                                ],
                                query_suggestions=models.QuerySuggestionList(),
                                invite_info=models.InviteInfo(),
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
                                query_suggestions=models.QuerySuggestionList(),
                                invite_info=models.InviteInfo(),
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
                        interactions=models.DocumentInteractions(),
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
                                        query_suggestions=models.QuerySuggestionList(),
                                        invite_info=models.InviteInfo(),
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
                                            query_suggestions=models.QuerySuggestionList(),
                                            invite_info=models.InviteInfo(),
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
                                            query_suggestions=models.QuerySuggestionList(),
                                            invite_info=models.InviteInfo(),
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
                                    remind_at=358043,
                                ),
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
                                ],
                                query_suggestions=models.QuerySuggestionList(),
                                invite_info=models.InviteInfo(),
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
                text="Because its wavelengths are shorter, blue light is more strongly scattered than the longer-wavelength lights, red or green. Hence the result that when looking at the sky away from the direct incident sunlight, the human eye perceives the sky to be blue.",
            ),
        ],
    }, audience_filters=[
        {
            "field_name": "type",
            "values": [
                {
                    "value": "Spreadsheet",
                    "relation_type": models.RelationType.EQUALS,
                },
                {
                    "value": "Presentation",
                    "relation_type": models.RelationType.EQUALS,
                },
            ],
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                             | Type                                                                                                                                                                                                  | Required                                                                                                                                                                                              | Description                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                                                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                    | The date and time at which the announcement becomes active.                                                                                                                                           |
| `end_time`                                                                                                                                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                    | The date and time at which the announcement expires.                                                                                                                                                  |
| `title`                                                                                                                                                                                               | *str*                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                    | The headline of the announcement.                                                                                                                                                                     |
| `id`                                                                                                                                                                                                  | *int*                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                    | The opaque id of the announcement.                                                                                                                                                                    |
| `body`                                                                                                                                                                                                | [Optional[models.StructuredText]](../../models/structuredtext.md)                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                    | N/A                                                                                                                                                                                                   |
| `emoji`                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | An emoji used to indicate the nature of the announcement.                                                                                                                                             |
| `thumbnail`                                                                                                                                                                                           | [Optional[models.Thumbnail]](../../models/thumbnail.md)                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                    | N/A                                                                                                                                                                                                   |
| `banner`                                                                                                                                                                                              | [Optional[models.Thumbnail]](../../models/thumbnail.md)                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                    | N/A                                                                                                                                                                                                   |
| `audience_filters`                                                                                                                                                                                    | List[[models.FacetFilter](../../models/facetfilter.md)]                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                    | Filters which restrict who should see the announcement. Values are taken from the corresponding filters in people search.                                                                             |
| `source_document_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | The Glean Document ID of the source document this Announcement was created from (e.g. Slack thread).                                                                                                  |
| `hide_attribution`                                                                                                                                                                                    | *Optional[bool]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                    | Whether or not to hide an author attribution.                                                                                                                                                         |
| `channel`                                                                                                                                                                                             | [Optional[models.UpdateAnnouncementRequestChannel]](../../models/updateannouncementrequestchannel.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                    | This determines whether this is a Social Feed post or a regular announcement.                                                                                                                         |
| `post_type`                                                                                                                                                                                           | [Optional[models.UpdateAnnouncementRequestPostType]](../../models/updateannouncementrequestposttype.md)                                                                                               | :heavy_minus_sign:                                                                                                                                                                                    | This determines whether this is an external-link post or a regular announcement post. TEXT - Regular announcement that can contain rich text. LINK - Announcement that is linked to an external site. |
| `is_prioritized`                                                                                                                                                                                      | *Optional[bool]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                    | Used by the Social Feed to pin posts to the front of the feed.                                                                                                                                        |
| `view_url`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | URL for viewing the announcement. It will be set to document URL for announcements from other datasources e.g. simpplr. Can only be written when channel="SOCIAL_FEED".                               |
| `retries`                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                   |

### Response

**[models.Announcement](../../models/announcement.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |