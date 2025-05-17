# Answers
(*client.answers*)

## Overview

### Available Operations

* [create](#create) - Create Answer
* [delete](#delete) - Delete Answer
* [update](#update) - Update Answer
* [retrieve](#retrieve) - Read Answer
* [list](#list) - List Answers

## create

Create a user-generated Answer that contains a question and answer.

### Example Usage

```python
from datetime import date
from glean import Glean, models
from glean.utils import parse_datetime
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.client.answers.create(data={
        "question": "Why is the sky blue?",
        "body_text": "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.",
        "audience_filters": [
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
        ],
        "added_roles": [
            models.UserRoleSpecification(
                person=models.Person(
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
                                    facet_bucket_size=708564,
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
                                        start_index=945729,
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
                                                    ),
                                                ],
                                                collections=[
                                                    models.Collection(
                                                        name="<value>",
                                                        description="via vain astride question",
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
                                                        id=51416,
                                                        items=[
                                                            models.CollectionItem(
                                                                collection_id=33920,
                                                                shortcut=models.Shortcut(
                                                                    input_alias="<value>",
                                                                ),
                                                                item_type=models.CollectionItemItemType.TEXT,
                                                            ),
                                                            models.CollectionItem(
                                                                collection_id=33920,
                                                                shortcut=models.Shortcut(
                                                                    input_alias="<value>",
                                                                ),
                                                                item_type=models.CollectionItemItemType.TEXT,
                                                            ),
                                                            models.CollectionItem(
                                                                collection_id=33920,
                                                                shortcut=models.Shortcut(
                                                                    input_alias="<value>",
                                                                ),
                                                                item_type=models.CollectionItemItemType.TEXT,
                                                            ),
                                                        ],
                                                    ),
                                                    models.Collection(
                                                        name="<value>",
                                                        description="via vain astride question",
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
                                                        id=51416,
                                                        items=[
                                                            models.CollectionItem(
                                                                collection_id=33920,
                                                                shortcut=models.Shortcut(
                                                                    input_alias="<value>",
                                                                ),
                                                                item_type=models.CollectionItemItemType.TEXT,
                                                            ),
                                                            models.CollectionItem(
                                                                collection_id=33920,
                                                                shortcut=models.Shortcut(
                                                                    input_alias="<value>",
                                                                ),
                                                                item_type=models.CollectionItemItemType.TEXT,
                                                            ),
                                                            models.CollectionItem(
                                                                collection_id=33920,
                                                                shortcut=models.Shortcut(
                                                                    input_alias="<value>",
                                                                ),
                                                                item_type=models.CollectionItemItemType.TEXT,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                interactions=models.DocumentInteractions(
                                                    reacts=[
                                                        models.Reaction(),
                                                        models.Reaction(),
                                                        models.Reaction(),
                                                    ],
                                                    shares=[
                                                        models.Share(
                                                            num_days_ago=85387,
                                                        ),
                                                    ],
                                                ),
                                                verification=models.Verification(
                                                    state=models.State.VERIFIED,
                                                    metadata=models.VerificationMetadata(
                                                        reminders=[
                                                            models.Reminder(
                                                                assignee=models.Person(
                                                                    name="George Clooney",
                                                                    obfuscated_id="abc123",
                                                                ),
                                                                remind_at=161639,
                                                            ),
                                                        ],
                                                        last_reminder=models.Reminder(
                                                            assignee=models.Person(
                                                                name="George Clooney",
                                                                obfuscated_id="abc123",
                                                            ),
                                                            remind_at=613051,
                                                        ),
                                                    ),
                                                ),
                                                shortcuts=[
                                                    models.Shortcut(
                                                        input_alias="<value>",
                                                    ),
                                                    models.Shortcut(
                                                        input_alias="<value>",
                                                    ),
                                                    models.Shortcut(
                                                        input_alias="<value>",
                                                    ),
                                                ],
                                                custom_data={
                                                    "someCustomField": models.CustomDataValue(),
                                                },
                                            ),
                                        ),
                                    ),
                                    models.TextRange(
                                        start_index=945729,
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
                                                    ),
                                                ],
                                                collections=[
                                                    models.Collection(
                                                        name="<value>",
                                                        description="via vain astride question",
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
                                                        id=51416,
                                                        items=[
                                                            models.CollectionItem(
                                                                collection_id=33920,
                                                                shortcut=models.Shortcut(
                                                                    input_alias="<value>",
                                                                ),
                                                                item_type=models.CollectionItemItemType.TEXT,
                                                            ),
                                                            models.CollectionItem(
                                                                collection_id=33920,
                                                                shortcut=models.Shortcut(
                                                                    input_alias="<value>",
                                                                ),
                                                                item_type=models.CollectionItemItemType.TEXT,
                                                            ),
                                                            models.CollectionItem(
                                                                collection_id=33920,
                                                                shortcut=models.Shortcut(
                                                                    input_alias="<value>",
                                                                ),
                                                                item_type=models.CollectionItemItemType.TEXT,
                                                            ),
                                                        ],
                                                    ),
                                                    models.Collection(
                                                        name="<value>",
                                                        description="via vain astride question",
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
                                                        id=51416,
                                                        items=[
                                                            models.CollectionItem(
                                                                collection_id=33920,
                                                                shortcut=models.Shortcut(
                                                                    input_alias="<value>",
                                                                ),
                                                                item_type=models.CollectionItemItemType.TEXT,
                                                            ),
                                                            models.CollectionItem(
                                                                collection_id=33920,
                                                                shortcut=models.Shortcut(
                                                                    input_alias="<value>",
                                                                ),
                                                                item_type=models.CollectionItemItemType.TEXT,
                                                            ),
                                                            models.CollectionItem(
                                                                collection_id=33920,
                                                                shortcut=models.Shortcut(
                                                                    input_alias="<value>",
                                                                ),
                                                                item_type=models.CollectionItemItemType.TEXT,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                interactions=models.DocumentInteractions(
                                                    reacts=[
                                                        models.Reaction(),
                                                        models.Reaction(),
                                                        models.Reaction(),
                                                    ],
                                                    shares=[
                                                        models.Share(
                                                            num_days_ago=85387,
                                                        ),
                                                    ],
                                                ),
                                                verification=models.Verification(
                                                    state=models.State.VERIFIED,
                                                    metadata=models.VerificationMetadata(
                                                        reminders=[
                                                            models.Reminder(
                                                                assignee=models.Person(
                                                                    name="George Clooney",
                                                                    obfuscated_id="abc123",
                                                                ),
                                                                remind_at=161639,
                                                            ),
                                                        ],
                                                        last_reminder=models.Reminder(
                                                            assignee=models.Person(
                                                                name="George Clooney",
                                                                obfuscated_id="abc123",
                                                            ),
                                                            remind_at=613051,
                                                        ),
                                                    ),
                                                ),
                                                shortcuts=[
                                                    models.Shortcut(
                                                        input_alias="<value>",
                                                    ),
                                                    models.Shortcut(
                                                        input_alias="<value>",
                                                    ),
                                                    models.Shortcut(
                                                        input_alias="<value>",
                                                    ),
                                                ],
                                                custom_data={
                                                    "someCustomField": models.CustomDataValue(),
                                                },
                                            ),
                                        ),
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
                                    facet_bucket_size=708564,
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
                                        start_index=945729,
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
                                                    ),
                                                ],
                                                collections=[
                                                    models.Collection(
                                                        name="<value>",
                                                        description="via vain astride question",
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
                                                        id=51416,
                                                        items=[
                                                            models.CollectionItem(
                                                                collection_id=33920,
                                                                shortcut=models.Shortcut(
                                                                    input_alias="<value>",
                                                                ),
                                                                item_type=models.CollectionItemItemType.TEXT,
                                                            ),
                                                            models.CollectionItem(
                                                                collection_id=33920,
                                                                shortcut=models.Shortcut(
                                                                    input_alias="<value>",
                                                                ),
                                                                item_type=models.CollectionItemItemType.TEXT,
                                                            ),
                                                            models.CollectionItem(
                                                                collection_id=33920,
                                                                shortcut=models.Shortcut(
                                                                    input_alias="<value>",
                                                                ),
                                                                item_type=models.CollectionItemItemType.TEXT,
                                                            ),
                                                        ],
                                                    ),
                                                    models.Collection(
                                                        name="<value>",
                                                        description="via vain astride question",
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
                                                        id=51416,
                                                        items=[
                                                            models.CollectionItem(
                                                                collection_id=33920,
                                                                shortcut=models.Shortcut(
                                                                    input_alias="<value>",
                                                                ),
                                                                item_type=models.CollectionItemItemType.TEXT,
                                                            ),
                                                            models.CollectionItem(
                                                                collection_id=33920,
                                                                shortcut=models.Shortcut(
                                                                    input_alias="<value>",
                                                                ),
                                                                item_type=models.CollectionItemItemType.TEXT,
                                                            ),
                                                            models.CollectionItem(
                                                                collection_id=33920,
                                                                shortcut=models.Shortcut(
                                                                    input_alias="<value>",
                                                                ),
                                                                item_type=models.CollectionItemItemType.TEXT,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                interactions=models.DocumentInteractions(
                                                    reacts=[
                                                        models.Reaction(),
                                                        models.Reaction(),
                                                        models.Reaction(),
                                                    ],
                                                    shares=[
                                                        models.Share(
                                                            num_days_ago=85387,
                                                        ),
                                                    ],
                                                ),
                                                verification=models.Verification(
                                                    state=models.State.VERIFIED,
                                                    metadata=models.VerificationMetadata(
                                                        reminders=[
                                                            models.Reminder(
                                                                assignee=models.Person(
                                                                    name="George Clooney",
                                                                    obfuscated_id="abc123",
                                                                ),
                                                                remind_at=161639,
                                                            ),
                                                        ],
                                                        last_reminder=models.Reminder(
                                                            assignee=models.Person(
                                                                name="George Clooney",
                                                                obfuscated_id="abc123",
                                                            ),
                                                            remind_at=613051,
                                                        ),
                                                    ),
                                                ),
                                                shortcuts=[
                                                    models.Shortcut(
                                                        input_alias="<value>",
                                                    ),
                                                    models.Shortcut(
                                                        input_alias="<value>",
                                                    ),
                                                    models.Shortcut(
                                                        input_alias="<value>",
                                                    ),
                                                ],
                                                custom_data={
                                                    "someCustomField": models.CustomDataValue(),
                                                },
                                            ),
                                        ),
                                    ),
                                    models.TextRange(
                                        start_index=945729,
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
                                                    ),
                                                ],
                                                collections=[
                                                    models.Collection(
                                                        name="<value>",
                                                        description="via vain astride question",
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
                                                        id=51416,
                                                        items=[
                                                            models.CollectionItem(
                                                                collection_id=33920,
                                                                shortcut=models.Shortcut(
                                                                    input_alias="<value>",
                                                                ),
                                                                item_type=models.CollectionItemItemType.TEXT,
                                                            ),
                                                            models.CollectionItem(
                                                                collection_id=33920,
                                                                shortcut=models.Shortcut(
                                                                    input_alias="<value>",
                                                                ),
                                                                item_type=models.CollectionItemItemType.TEXT,
                                                            ),
                                                            models.CollectionItem(
                                                                collection_id=33920,
                                                                shortcut=models.Shortcut(
                                                                    input_alias="<value>",
                                                                ),
                                                                item_type=models.CollectionItemItemType.TEXT,
                                                            ),
                                                        ],
                                                    ),
                                                    models.Collection(
                                                        name="<value>",
                                                        description="via vain astride question",
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
                                                        id=51416,
                                                        items=[
                                                            models.CollectionItem(
                                                                collection_id=33920,
                                                                shortcut=models.Shortcut(
                                                                    input_alias="<value>",
                                                                ),
                                                                item_type=models.CollectionItemItemType.TEXT,
                                                            ),
                                                            models.CollectionItem(
                                                                collection_id=33920,
                                                                shortcut=models.Shortcut(
                                                                    input_alias="<value>",
                                                                ),
                                                                item_type=models.CollectionItemItemType.TEXT,
                                                            ),
                                                            models.CollectionItem(
                                                                collection_id=33920,
                                                                shortcut=models.Shortcut(
                                                                    input_alias="<value>",
                                                                ),
                                                                item_type=models.CollectionItemItemType.TEXT,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                interactions=models.DocumentInteractions(
                                                    reacts=[
                                                        models.Reaction(),
                                                        models.Reaction(),
                                                        models.Reaction(),
                                                    ],
                                                    shares=[
                                                        models.Share(
                                                            num_days_ago=85387,
                                                        ),
                                                    ],
                                                ),
                                                verification=models.Verification(
                                                    state=models.State.VERIFIED,
                                                    metadata=models.VerificationMetadata(
                                                        reminders=[
                                                            models.Reminder(
                                                                assignee=models.Person(
                                                                    name="George Clooney",
                                                                    obfuscated_id="abc123",
                                                                ),
                                                                remind_at=161639,
                                                            ),
                                                        ],
                                                        last_reminder=models.Reminder(
                                                            assignee=models.Person(
                                                                name="George Clooney",
                                                                obfuscated_id="abc123",
                                                            ),
                                                            remind_at=613051,
                                                        ),
                                                    ),
                                                ),
                                                shortcuts=[
                                                    models.Shortcut(
                                                        input_alias="<value>",
                                                    ),
                                                    models.Shortcut(
                                                        input_alias="<value>",
                                                    ),
                                                    models.Shortcut(
                                                        input_alias="<value>",
                                                    ),
                                                ],
                                                custom_data={
                                                    "someCustomField": models.CustomDataValue(),
                                                },
                                            ),
                                        ),
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
                                    models.CustomFieldValueStr(),
                                ],
                            ),
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
                                values=[
                                    models.CustomFieldValueStr(),
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
                role=models.UserRole.EDITOR,
            ),
        ],
        "removed_roles": [
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
                role=models.UserRole.OWNER,
            ),
        ],
        "roles": [
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
        "combined_answer_text": {
            "text": "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `data`                                                              | [models.AnswerCreationData](../../models/answercreationdata.md)     | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Answer](../../models/answer.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## delete

Delete an existing user-generated Answer.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    g_client.client.answers.delete(id=3, doc_id="ANSWERS_answer_3")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                   | Type                                                                                                                                                                        | Required                                                                                                                                                                    | Description                                                                                                                                                                 | Example                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                        | *int*                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                          | The opaque ID of the Answer.                                                                                                                                                | 3                                                                                                                                                                           |
| `doc_id`                                                                                                                                                                    | *Optional[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | Glean Document ID of the Answer. The Glean Document ID is supported for cases where the Answer ID isn't available. If both are available, using the Answer ID is preferred. | ANSWERS_answer_3                                                                                                                                                            |
| `retries`                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                            | :heavy_minus_sign:                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                         |                                                                                                                                                                             |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## update

Update an existing user-generated Answer.

### Example Usage

```python
from datetime import date
from glean import Glean, models
from glean.utils import parse_datetime
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.client.answers.update(id=3, doc_id="ANSWERS_answer_3", question="Why is the sky blue?", body_text="From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.", audience_filters=[
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
    ], added_roles=[
        models.UserRoleSpecification(
            person=models.Person(
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
                                facet_bucket_size=552856,
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
                                    start_index=23264,
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
                                                ),
                                            ],
                                            collections=[
                                                models.Collection(
                                                    name="<value>",
                                                    description="boohoo hunger energetic who whoa grimy vibrant wisely",
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
                                                    id=919335,
                                                    items=[
                                                        models.CollectionItem(
                                                            collection_id=972120,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                        models.CollectionItem(
                                                            collection_id=972120,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            interactions=models.DocumentInteractions(
                                                reacts=[
                                                    models.Reaction(),
                                                ],
                                                shares=[
                                                    models.Share(
                                                        num_days_ago=439797,
                                                    ),
                                                    models.Share(
                                                        num_days_ago=439797,
                                                    ),
                                                ],
                                            ),
                                            verification=models.Verification(
                                                state=models.State.VERIFIED,
                                                metadata=models.VerificationMetadata(
                                                    reminders=[
                                                        models.Reminder(
                                                            assignee=models.Person(
                                                                name="George Clooney",
                                                                obfuscated_id="abc123",
                                                            ),
                                                            remind_at=996442,
                                                        ),
                                                        models.Reminder(
                                                            assignee=models.Person(
                                                                name="George Clooney",
                                                                obfuscated_id="abc123",
                                                            ),
                                                            remind_at=996442,
                                                        ),
                                                    ],
                                                    last_reminder=models.Reminder(
                                                        assignee=models.Person(
                                                            name="George Clooney",
                                                            obfuscated_id="abc123",
                                                        ),
                                                        remind_at=886538,
                                                    ),
                                                ),
                                            ),
                                            shortcuts=[
                                                models.Shortcut(
                                                    input_alias="<value>",
                                                ),
                                                models.Shortcut(
                                                    input_alias="<value>",
                                                ),
                                                models.Shortcut(
                                                    input_alias="<value>",
                                                ),
                                            ],
                                            custom_data={
                                                "someCustomField": models.CustomDataValue(),
                                            },
                                        ),
                                    ),
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
            role=models.UserRole.OWNER,
        ),
        models.UserRoleSpecification(
            person=models.Person(
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
                                facet_bucket_size=552856,
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
                                    start_index=23264,
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
                                                ),
                                            ],
                                            collections=[
                                                models.Collection(
                                                    name="<value>",
                                                    description="boohoo hunger energetic who whoa grimy vibrant wisely",
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
                                                    id=919335,
                                                    items=[
                                                        models.CollectionItem(
                                                            collection_id=972120,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                        models.CollectionItem(
                                                            collection_id=972120,
                                                            shortcut=models.Shortcut(
                                                                input_alias="<value>",
                                                            ),
                                                            item_type=models.CollectionItemItemType.TEXT,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            interactions=models.DocumentInteractions(
                                                reacts=[
                                                    models.Reaction(),
                                                ],
                                                shares=[
                                                    models.Share(
                                                        num_days_ago=439797,
                                                    ),
                                                    models.Share(
                                                        num_days_ago=439797,
                                                    ),
                                                ],
                                            ),
                                            verification=models.Verification(
                                                state=models.State.VERIFIED,
                                                metadata=models.VerificationMetadata(
                                                    reminders=[
                                                        models.Reminder(
                                                            assignee=models.Person(
                                                                name="George Clooney",
                                                                obfuscated_id="abc123",
                                                            ),
                                                            remind_at=996442,
                                                        ),
                                                        models.Reminder(
                                                            assignee=models.Person(
                                                                name="George Clooney",
                                                                obfuscated_id="abc123",
                                                            ),
                                                            remind_at=996442,
                                                        ),
                                                    ],
                                                    last_reminder=models.Reminder(
                                                        assignee=models.Person(
                                                            name="George Clooney",
                                                            obfuscated_id="abc123",
                                                        ),
                                                        remind_at=886538,
                                                    ),
                                                ),
                                            ),
                                            shortcuts=[
                                                models.Shortcut(
                                                    input_alias="<value>",
                                                ),
                                                models.Shortcut(
                                                    input_alias="<value>",
                                                ),
                                                models.Shortcut(
                                                    input_alias="<value>",
                                                ),
                                            ],
                                            custom_data={
                                                "someCustomField": models.CustomDataValue(),
                                            },
                                        ),
                                    ),
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
            role=models.UserRole.OWNER,
        ),
    ], removed_roles=[
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
    ], roles=[
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
            role=models.UserRole.EDITOR,
        ),
    ], combined_answer_text={
        "text": "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                   | Type                                                                                                                                                                        | Required                                                                                                                                                                    | Description                                                                                                                                                                 | Example                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                        | *int*                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                          | The opaque ID of the Answer.                                                                                                                                                | 3                                                                                                                                                                           |
| `doc_id`                                                                                                                                                                    | *Optional[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | Glean Document ID of the Answer. The Glean Document ID is supported for cases where the Answer ID isn't available. If both are available, using the Answer ID is preferred. | ANSWERS_answer_3                                                                                                                                                            |
| `question`                                                                                                                                                                  | *Optional[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | N/A                                                                                                                                                                         | Why is the sky blue?                                                                                                                                                        |
| `question_variations`                                                                                                                                                       | List[*str*]                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                          | Additional ways of phrasing this question.                                                                                                                                  |                                                                                                                                                                             |
| `body_text`                                                                                                                                                                 | *Optional[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | The plain text answer to the question.                                                                                                                                      | From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.                       |
| `board_id`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | The parent board ID of this Answer, or 0 if it's a floating Answer.                                                                                                         |                                                                                                                                                                             |
| `audience_filters`                                                                                                                                                          | List[[models.FacetFilter](../../models/facetfilter.md)]                                                                                                                     | :heavy_minus_sign:                                                                                                                                                          | Filters which restrict who should see the answer. Values are taken from the corresponding filters in people search.                                                         |                                                                                                                                                                             |
| `added_roles`                                                                                                                                                               | List[[models.UserRoleSpecification](../../models/userrolespecification.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                                          | A list of user roles for the answer added by the owner.                                                                                                                     |                                                                                                                                                                             |
| `removed_roles`                                                                                                                                                             | List[[models.UserRoleSpecification](../../models/userrolespecification.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                                          | A list of user roles for the answer removed by the owner.                                                                                                                   |                                                                                                                                                                             |
| `roles`                                                                                                                                                                     | List[[models.UserRoleSpecification](../../models/userrolespecification.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                                          | A list of roles for this answer explicitly granted by an owner, editor, or admin.                                                                                           |                                                                                                                                                                             |
| `source_document_spec`                                                                                                                                                      | [Optional[models.DocumentSpecUnion]](../../models/documentspecunion.md)                                                                                                     | :heavy_minus_sign:                                                                                                                                                          | N/A                                                                                                                                                                         |                                                                                                                                                                             |
| `source_type`                                                                                                                                                               | [Optional[models.EditAnswerRequestSourceType]](../../models/editanswerrequestsourcetype.md)                                                                                 | :heavy_minus_sign:                                                                                                                                                          | N/A                                                                                                                                                                         |                                                                                                                                                                             |
| `added_collections`                                                                                                                                                         | List[*int*]                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                          | IDs of Collections to which a document is added.                                                                                                                            |                                                                                                                                                                             |
| `removed_collections`                                                                                                                                                       | List[*int*]                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                          | IDs of Collections from which a document is removed.                                                                                                                        |                                                                                                                                                                             |
| `combined_answer_text`                                                                                                                                                      | [Optional[models.StructuredTextMutableProperties]](../../models/structuredtextmutableproperties.md)                                                                         | :heavy_minus_sign:                                                                                                                                                          | N/A                                                                                                                                                                         |                                                                                                                                                                             |
| `retries`                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                            | :heavy_minus_sign:                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                         |                                                                                                                                                                             |

### Response

**[models.Answer](../../models/answer.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## retrieve

Read the details of a particular Answer given its ID.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.client.answers.retrieve(request={
        "id": 3,
        "doc_id": "ANSWERS_answer_3",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GetAnswerRequest](../../models/getanswerrequest.md)         | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAnswerResponse](../../models/getanswerresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |

## list

List Answers created by the current user.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.client.answers.list(request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ListAnswersRequest](../../models/listanswersrequest.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListAnswersResponse](../../models/listanswersresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |