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

<!-- UsageSnippet language="python" operationID="createannouncement" method="post" path="/rest/api/v1/createannouncement" -->
```python
from glean.api_client import Glean, models
from glean.api_client.utils import parse_datetime
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.announcements.create(start_time=parse_datetime("2023-05-01T12:02:10.816Z"), end_time=parse_datetime("2024-03-17T14:19:30.278Z"), title="<value>", body={
        "text": "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.",
        "structured_list": [
            models.StructuredTextItem(
                link="https://en.wikipedia.org/wiki/Diffuse_sky_radiation",
                document=models.Document(
                    container_document=models.Document(
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
                                name="name",
                                obfuscated_id="<id>",
                            ),
                            components=[
                                "Backend",
                                "Networking",
                            ],
                            status="[\"Done\"]",
                            custom_data={
                                "someCustomField": models.CustomDataValue(),
                            },
                        ),
                    ),
                    parent_document=models.Document(
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
                                name="name",
                                obfuscated_id="<id>",
                            ),
                            components=[
                                "Backend",
                                "Networking",
                            ],
                            status="[\"Done\"]",
                            custom_data={
                                "someCustomField": models.CustomDataValue(),
                            },
                        ),
                    ),
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
                            name="name",
                            obfuscated_id="<id>",
                        ),
                        components=[
                            "Backend",
                            "Networking",
                        ],
                        status="[\"Done\"]",
                        custom_data={
                            "someCustomField": models.CustomDataValue(),
                        },
                    ),
                ),
                text="Because its wavelengths are shorter, blue light is more strongly scattered than the longer-wavelength lights, red or green. Hence the result that when looking at the sky away from the direct incident sunlight, the human eye perceives the sky to be blue.",
                structured_result=models.StructuredResult(
                    document=models.Document(
                        container_document=models.Document(
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
                                    name="name",
                                    obfuscated_id="<id>",
                                ),
                                components=[
                                    "Backend",
                                    "Networking",
                                ],
                                status="[\"Done\"]",
                                custom_data={
                                    "someCustomField": models.CustomDataValue(),
                                },
                            ),
                        ),
                        parent_document=models.Document(
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
                                    name="name",
                                    obfuscated_id="<id>",
                                ),
                                components=[
                                    "Backend",
                                    "Networking",
                                ],
                                status="[\"Done\"]",
                                custom_data={
                                    "someCustomField": models.CustomDataValue(),
                                },
                            ),
                        ),
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
                                name="name",
                                obfuscated_id="<id>",
                            ),
                            components=[
                                "Backend",
                                "Networking",
                            ],
                            status="[\"Done\"]",
                            custom_data={
                                "someCustomField": models.CustomDataValue(),
                            },
                        ),
                    ),
                    person=models.Person(
                        name="George Clooney",
                        obfuscated_id="abc123",
                    ),
                    customer=models.Customer(
                        id="<id>",
                        company=models.Company(
                            name="<value>",
                            location="New York City",
                            industry="Finances",
                            about="Financial, software, data, and media company headquartered in Midtown Manhattan, New York City",
                        ),
                        poc=[
                            models.Person(
                                name="George Clooney",
                                obfuscated_id="abc123",
                            ),
                        ],
                        merged_customers=[
                            models.Customer(
                                id="<id>",
                                company=models.Company(
                                    name="<value>",
                                    location="New York City",
                                    industry="Finances",
                                    about="Financial, software, data, and media company headquartered in Midtown Manhattan, New York City",
                                ),
                                notes="CIO is interested in trying out the product.",
                            ),
                        ],
                        notes="CIO is interested in trying out the product.",
                    ),
                    team=models.Team(
                        id="<id>",
                        name="<value>",
                        members=[
                            models.PersonToTeamRelationship(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                            ),
                        ],
                        custom_fields=[
                            models.CustomFieldData(
                                label="<value>",
                                values=[
                                    models.CustomFieldValuePerson(
                                        person=models.Person(
                                            name="George Clooney",
                                            obfuscated_id="abc123",
                                        ),
                                    ),
                                ],
                            ),
                        ],
                        datasource_profiles=[
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                        ],
                    ),
                    custom_entity=models.CustomEntity(
                        roles=[
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                                role=models.UserRole.ANSWER_MODERATOR,
                            ),
                        ],
                    ),
                    answer=models.Answer(
                        id=3,
                        doc_id="ANSWERS_answer_3",
                        question="Why is the sky blue?",
                        body_text="From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.",
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
                        added_roles=[
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                                role=models.UserRole.VERIFIER,
                            ),
                        ],
                        removed_roles=[
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                                role=models.UserRole.VERIFIER,
                            ),
                        ],
                        combined_answer_text=models.StructuredText(
                            text="From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.",
                        ),
                        likes=models.AnswerLikes(
                            liked_by=[
                                models.AnswerLike(
                                    user=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                    ),
                                ),
                            ],
                            liked_by_user=False,
                            num_likes=852982,
                        ),
                        author=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                        ),
                        verification=models.Verification(
                            state=models.State.DEPRECATED,
                            metadata=models.VerificationMetadata(
                                last_verifier=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                                document=models.Document(
                                    container_document=models.Document(
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
                                                name="name",
                                                obfuscated_id="<id>",
                                            ),
                                            components=[
                                                "Backend",
                                                "Networking",
                                            ],
                                            status="[\"Done\"]",
                                            custom_data={
                                                "someCustomField": models.CustomDataValue(),
                                            },
                                        ),
                                    ),
                                    parent_document=models.Document(
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
                                                name="name",
                                                obfuscated_id="<id>",
                                            ),
                                            components=[
                                                "Backend",
                                                "Networking",
                                            ],
                                            status="[\"Done\"]",
                                            custom_data={
                                                "someCustomField": models.CustomDataValue(),
                                            },
                                        ),
                                    ),
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
                                            name="name",
                                            obfuscated_id="<id>",
                                        ),
                                        components=[
                                            "Backend",
                                            "Networking",
                                        ],
                                        status="[\"Done\"]",
                                        custom_data={
                                            "someCustomField": models.CustomDataValue(),
                                        },
                                    ),
                                ),
                                reminders=[
                                    models.Reminder(
                                        assignee=models.Person(
                                            name="George Clooney",
                                            obfuscated_id="abc123",
                                        ),
                                        requestor=models.Person(
                                            name="George Clooney",
                                            obfuscated_id="abc123",
                                        ),
                                        remind_at=627080,
                                    ),
                                ],
                                last_reminder=models.Reminder(
                                    assignee=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                    ),
                                    requestor=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                    ),
                                    remind_at=642543,
                                ),
                                candidate_verifiers=[
                                    models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                    ),
                                ],
                            ),
                        ),
                        board=models.AnswerBoard(
                            name="<value>",
                            description="actual even swift curse while puppet outlandish since urgently",
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
                            id=812610,
                            creator=models.Person(
                                name="George Clooney",
                                obfuscated_id="abc123",
                            ),
                            updated_by=models.Person(
                                name="George Clooney",
                                obfuscated_id="abc123",
                            ),
                        ),
                        collections=[
                            models.Collection(
                                name="<value>",
                                description="minus mindless prudent better elderly",
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
                                id=953622,
                                creator=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                                updated_by=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                                items=[
                                    models.CollectionItem(
                                        collection_id=164413,
                                        created_by=models.Person(
                                            name="George Clooney",
                                            obfuscated_id="abc123",
                                        ),
                                        document=models.Document(
                                            container_document=models.Document(
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
                                                        name="name",
                                                        obfuscated_id="<id>",
                                                    ),
                                                    components=[
                                                        "Backend",
                                                        "Networking",
                                                    ],
                                                    status="[\"Done\"]",
                                                    custom_data={
                                                        "someCustomField": models.CustomDataValue(),
                                                    },
                                                ),
                                            ),
                                            parent_document=models.Document(
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
                                                        name="name",
                                                        obfuscated_id="<id>",
                                                    ),
                                                    components=[
                                                        "Backend",
                                                        "Networking",
                                                    ],
                                                    status="[\"Done\"]",
                                                    custom_data={
                                                        "someCustomField": models.CustomDataValue(),
                                                    },
                                                ),
                                            ),
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
                                                    name="name",
                                                    obfuscated_id="<id>",
                                                ),
                                                components=[
                                                    "Backend",
                                                    "Networking",
                                                ],
                                                status="[\"Done\"]",
                                                custom_data={
                                                    "someCustomField": models.CustomDataValue(),
                                                },
                                            ),
                                        ),
                                        shortcut=models.Shortcut(
                                            input_alias="<value>",
                                            created_by=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                            ),
                                            updated_by=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                            ),
                                            destination_document=models.Document(
                                                container_document=models.Document(
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
                                                            name="name",
                                                            obfuscated_id="<id>",
                                                        ),
                                                        components=[
                                                            "Backend",
                                                            "Networking",
                                                        ],
                                                        status="[\"Done\"]",
                                                        custom_data={
                                                            "someCustomField": models.CustomDataValue(),
                                                        },
                                                    ),
                                                ),
                                                parent_document=models.Document(
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
                                                            name="name",
                                                            obfuscated_id="<id>",
                                                        ),
                                                        components=[
                                                            "Backend",
                                                            "Networking",
                                                        ],
                                                        status="[\"Done\"]",
                                                        custom_data={
                                                            "someCustomField": models.CustomDataValue(),
                                                        },
                                                    ),
                                                ),
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
                                                        name="name",
                                                        obfuscated_id="<id>",
                                                    ),
                                                    components=[
                                                        "Backend",
                                                        "Networking",
                                                    ],
                                                    status="[\"Done\"]",
                                                    custom_data={
                                                        "someCustomField": models.CustomDataValue(),
                                                    },
                                                ),
                                            ),
                                        ),
                                        collection=models.Collection(
                                            name="<value>",
                                            description="instead calmly after ick headline inasmuch forenenst westernize grouper amidst",
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
                                            id=345597,
                                            creator=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                            ),
                                            updated_by=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                            ),
                                            children=[
                                                models.Collection(
                                                    name="<value>",
                                                    description="boulevard pale collaborate pertinent comparison drat yum rejigger nor finding",
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
                                                    id=654575,
                                                    creator=models.Person(
                                                        name="George Clooney",
                                                        obfuscated_id="abc123",
                                                    ),
                                                    updated_by=models.Person(
                                                        name="George Clooney",
                                                        obfuscated_id="abc123",
                                                    ),
                                                ),
                                            ],
                                        ),
                                        item_type=models.CollectionItemItemType.DOCUMENT,
                                    ),
                                ],
                            ),
                        ],
                        source_document=models.Document(
                            container_document=models.Document(
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
                                        name="name",
                                        obfuscated_id="<id>",
                                    ),
                                    components=[
                                        "Backend",
                                        "Networking",
                                    ],
                                    status="[\"Done\"]",
                                    custom_data={
                                        "someCustomField": models.CustomDataValue(),
                                    },
                                ),
                            ),
                            parent_document=models.Document(
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
                                        name="name",
                                        obfuscated_id="<id>",
                                    ),
                                    components=[
                                        "Backend",
                                        "Networking",
                                    ],
                                    status="[\"Done\"]",
                                    custom_data={
                                        "someCustomField": models.CustomDataValue(),
                                    },
                                ),
                            ),
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
                                    name="name",
                                    obfuscated_id="<id>",
                                ),
                                components=[
                                    "Backend",
                                    "Networking",
                                ],
                                status="[\"Done\"]",
                                custom_data={
                                    "someCustomField": models.CustomDataValue(),
                                },
                            ),
                        ),
                    ),
                    extracted_qn_a=models.ExtractedQnA(
                        question_result=models.SearchResult(
                            title="title",
                            url="https://example.com/foo/bar",
                            native_app_url="slack://foo/bar",
                            snippets=[
                                models.SearchResultSnippet(
                                    snippet="snippet",
                                    mime_type="mimeType",
                                ),
                            ],
                            must_include_suggestions=models.QuerySuggestionList(
                                suggestions=[
                                    models.QuerySuggestion(
                                        query="app:github type:pull author:mortimer",
                                        label="Mortimer's PRs",
                                        datasource="github",
                                    ),
                                ],
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                            ),
                        ),
                    ),
                    meeting=models.Meeting(
                        attendees=models.CalendarAttendees(
                            people=[
                                models.CalendarAttendee(
                                    person=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                    ),
                                    group_attendees=[
                                        models.CalendarAttendee(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),
                    collection=models.Collection(
                        name="<value>",
                        description="instead calmly after ick headline inasmuch forenenst westernize grouper amidst",
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
                        id=345597,
                        creator=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                        ),
                        children=[
                            models.Collection(
                                name="<value>",
                                description="boulevard pale collaborate pertinent comparison drat yum rejigger nor finding",
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
                                id=654575,
                                creator=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                                updated_by=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                            ),
                        ],
                    ),
                    answer_board=models.AnswerBoard(
                        name="<value>",
                        description="capitalise rubric championship snowplow",
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
                        id=920771,
                        creator=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                        ),
                    ),
                    code=models.Code(
                        repo_name="scio",
                        file_name="README.md",
                    ),
                    shortcut=models.Shortcut(
                        input_alias="<value>",
                        created_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                        ),
                        destination_document=models.Document(
                            container_document=models.Document(
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
                                        name="name",
                                        obfuscated_id="<id>",
                                    ),
                                    components=[
                                        "Backend",
                                        "Networking",
                                    ],
                                    status="[\"Done\"]",
                                    custom_data={
                                        "someCustomField": models.CustomDataValue(),
                                    },
                                ),
                            ),
                            parent_document=models.Document(
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
                                        name="name",
                                        obfuscated_id="<id>",
                                    ),
                                    components=[
                                        "Backend",
                                        "Networking",
                                    ],
                                    status="[\"Done\"]",
                                    custom_data={
                                        "someCustomField": models.CustomDataValue(),
                                    },
                                ),
                            ),
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
                                    name="name",
                                    obfuscated_id="<id>",
                                ),
                                components=[
                                    "Backend",
                                    "Networking",
                                ],
                                status="[\"Done\"]",
                                custom_data={
                                    "someCustomField": models.CustomDataValue(),
                                },
                            ),
                        ),
                    ),
                    query_suggestions=models.QuerySuggestionList(
                        person=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                        ),
                    ),
                    related_documents=[
                        models.RelatedDocuments(
                            query_suggestion=models.QuerySuggestion(
                                query="app:github type:pull author:mortimer",
                                label="Mortimer's PRs",
                                datasource="github",
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
                                    must_include_suggestions=models.QuerySuggestionList(
                                        person=models.Person(
                                            name="George Clooney",
                                            obfuscated_id="abc123",
                                        ),
                                    ),
                                ),
                            ],
                        ),
                    ],
                    related_question=models.RelatedQuestion(
                        ranges=[
                            models.TextRange(
                                start_index=254608,
                                document=models.Document(
                                    container_document=models.Document(
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
                                                name="name",
                                                obfuscated_id="<id>",
                                            ),
                                            components=[
                                                "Backend",
                                                "Networking",
                                            ],
                                            status="[\"Done\"]",
                                            custom_data={
                                                "someCustomField": models.CustomDataValue(),
                                            },
                                        ),
                                    ),
                                    parent_document=models.Document(
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
                                                name="name",
                                                obfuscated_id="<id>",
                                            ),
                                            components=[
                                                "Backend",
                                                "Networking",
                                            ],
                                            status="[\"Done\"]",
                                            custom_data={
                                                "someCustomField": models.CustomDataValue(),
                                            },
                                        ),
                                    ),
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
                                            name="name",
                                            obfuscated_id="<id>",
                                        ),
                                        components=[
                                            "Backend",
                                            "Networking",
                                        ],
                                        status="[\"Done\"]",
                                        custom_data={
                                            "someCustomField": models.CustomDataValue(),
                                        },
                                    ),
                                ),
                            ),
                        ],
                    ),
                ),
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

<!-- UsageSnippet language="python" operationID="deleteannouncement" method="post" path="/rest/api/v1/deleteannouncement" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    glean.client.announcements.delete(id=458809)

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

<!-- UsageSnippet language="python" operationID="updateannouncement" method="post" path="/rest/api/v1/updateannouncement" -->
```python
from glean.api_client import Glean, models
from glean.api_client.utils import parse_datetime
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.announcements.update(start_time=parse_datetime("2023-10-24T01:53:24.440Z"), end_time=parse_datetime("2024-10-30T07:24:12.087Z"), title="<value>", id=210913, body={
        "text": "From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.",
        "structured_list": [
            models.StructuredTextItem(
                link="https://en.wikipedia.org/wiki/Diffuse_sky_radiation",
                document=models.Document(
                    container_document=models.Document(
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
                                name="name",
                                obfuscated_id="<id>",
                            ),
                            components=[
                                "Backend",
                                "Networking",
                            ],
                            status="[\"Done\"]",
                            custom_data={
                                "someCustomField": models.CustomDataValue(),
                            },
                        ),
                    ),
                    parent_document=models.Document(
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
                                name="name",
                                obfuscated_id="<id>",
                            ),
                            components=[
                                "Backend",
                                "Networking",
                            ],
                            status="[\"Done\"]",
                            custom_data={
                                "someCustomField": models.CustomDataValue(),
                            },
                        ),
                    ),
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
                            name="name",
                            obfuscated_id="<id>",
                        ),
                        components=[
                            "Backend",
                            "Networking",
                        ],
                        status="[\"Done\"]",
                        custom_data={
                            "someCustomField": models.CustomDataValue(),
                        },
                    ),
                ),
                text="Because its wavelengths are shorter, blue light is more strongly scattered than the longer-wavelength lights, red or green. Hence the result that when looking at the sky away from the direct incident sunlight, the human eye perceives the sky to be blue.",
                structured_result=models.StructuredResult(
                    document=models.Document(
                        container_document=models.Document(
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
                                    name="name",
                                    obfuscated_id="<id>",
                                ),
                                components=[
                                    "Backend",
                                    "Networking",
                                ],
                                status="[\"Done\"]",
                                custom_data={
                                    "someCustomField": models.CustomDataValue(),
                                },
                            ),
                        ),
                        parent_document=models.Document(
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
                                    name="name",
                                    obfuscated_id="<id>",
                                ),
                                components=[
                                    "Backend",
                                    "Networking",
                                ],
                                status="[\"Done\"]",
                                custom_data={
                                    "someCustomField": models.CustomDataValue(),
                                },
                            ),
                        ),
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
                                name="name",
                                obfuscated_id="<id>",
                            ),
                            components=[
                                "Backend",
                                "Networking",
                            ],
                            status="[\"Done\"]",
                            custom_data={
                                "someCustomField": models.CustomDataValue(),
                            },
                        ),
                    ),
                    person=models.Person(
                        name="George Clooney",
                        obfuscated_id="abc123",
                    ),
                    customer=models.Customer(
                        id="<id>",
                        company=models.Company(
                            name="<value>",
                            location="New York City",
                            industry="Finances",
                            about="Financial, software, data, and media company headquartered in Midtown Manhattan, New York City",
                        ),
                        poc=[
                            models.Person(
                                name="George Clooney",
                                obfuscated_id="abc123",
                            ),
                        ],
                        merged_customers=[
                            models.Customer(
                                id="<id>",
                                company=models.Company(
                                    name="<value>",
                                    location="New York City",
                                    industry="Finances",
                                    about="Financial, software, data, and media company headquartered in Midtown Manhattan, New York City",
                                ),
                                notes="CIO is interested in trying out the product.",
                            ),
                        ],
                        notes="CIO is interested in trying out the product.",
                    ),
                    team=models.Team(
                        id="<id>",
                        name="<value>",
                        members=[
                            models.PersonToTeamRelationship(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                            ),
                        ],
                        custom_fields=[
                            models.CustomFieldData(
                                label="<value>",
                                values=[
                                    models.CustomFieldValuePerson(
                                        person=models.Person(
                                            name="George Clooney",
                                            obfuscated_id="abc123",
                                        ),
                                    ),
                                ],
                            ),
                        ],
                        datasource_profiles=[
                            models.DatasourceProfile(
                                datasource="github",
                                handle="<value>",
                            ),
                        ],
                    ),
                    custom_entity=models.CustomEntity(
                        roles=[
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                                role=models.UserRole.VIEWER,
                            ),
                        ],
                    ),
                    answer=models.Answer(
                        id=3,
                        doc_id="ANSWERS_answer_3",
                        question="Why is the sky blue?",
                        body_text="From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.",
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
                        added_roles=[
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                                role=models.UserRole.ANSWER_MODERATOR,
                            ),
                        ],
                        removed_roles=[
                            models.UserRoleSpecification(
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                                role=models.UserRole.OWNER,
                            ),
                        ],
                        combined_answer_text=models.StructuredText(
                            text="From https://en.wikipedia.org/wiki/Diffuse_sky_radiation, the sky is blue because blue light is more strongly scattered than longer-wavelength light.",
                        ),
                        likes=models.AnswerLikes(
                            liked_by=[
                                models.AnswerLike(
                                    user=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                    ),
                                ),
                            ],
                            liked_by_user=True,
                            num_likes=768439,
                        ),
                        author=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                        ),
                        verification=models.Verification(
                            state=models.State.VERIFIED,
                            metadata=models.VerificationMetadata(
                                last_verifier=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                                document=models.Document(
                                    container_document=models.Document(
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
                                                name="name",
                                                obfuscated_id="<id>",
                                            ),
                                            components=[
                                                "Backend",
                                                "Networking",
                                            ],
                                            status="[\"Done\"]",
                                            custom_data={
                                                "someCustomField": models.CustomDataValue(),
                                            },
                                        ),
                                    ),
                                    parent_document=models.Document(
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
                                                name="name",
                                                obfuscated_id="<id>",
                                            ),
                                            components=[
                                                "Backend",
                                                "Networking",
                                            ],
                                            status="[\"Done\"]",
                                            custom_data={
                                                "someCustomField": models.CustomDataValue(),
                                            },
                                        ),
                                    ),
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
                                            name="name",
                                            obfuscated_id="<id>",
                                        ),
                                        components=[
                                            "Backend",
                                            "Networking",
                                        ],
                                        status="[\"Done\"]",
                                        custom_data={
                                            "someCustomField": models.CustomDataValue(),
                                        },
                                    ),
                                ),
                                reminders=[
                                    models.Reminder(
                                        assignee=models.Person(
                                            name="George Clooney",
                                            obfuscated_id="abc123",
                                        ),
                                        requestor=models.Person(
                                            name="George Clooney",
                                            obfuscated_id="abc123",
                                        ),
                                        remind_at=69479,
                                    ),
                                ],
                                last_reminder=models.Reminder(
                                    assignee=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                    ),
                                    requestor=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                    ),
                                    remind_at=877321,
                                ),
                                candidate_verifiers=[
                                    models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                    ),
                                ],
                            ),
                        ),
                        board=models.AnswerBoard(
                            name="<value>",
                            description="litter anenst happy probable birdcage till",
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
                            id=34422,
                            creator=models.Person(
                                name="George Clooney",
                                obfuscated_id="abc123",
                            ),
                            updated_by=models.Person(
                                name="George Clooney",
                                obfuscated_id="abc123",
                            ),
                        ),
                        collections=[
                            models.Collection(
                                name="<value>",
                                description="ew or every verbally",
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
                                id=297273,
                                creator=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                                updated_by=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                                items=[
                                    models.CollectionItem(
                                        collection_id=896121,
                                        created_by=models.Person(
                                            name="George Clooney",
                                            obfuscated_id="abc123",
                                        ),
                                        document=models.Document(
                                            container_document=models.Document(
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
                                                        name="name",
                                                        obfuscated_id="<id>",
                                                    ),
                                                    components=[
                                                        "Backend",
                                                        "Networking",
                                                    ],
                                                    status="[\"Done\"]",
                                                    custom_data={
                                                        "someCustomField": models.CustomDataValue(),
                                                    },
                                                ),
                                            ),
                                            parent_document=models.Document(
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
                                                        name="name",
                                                        obfuscated_id="<id>",
                                                    ),
                                                    components=[
                                                        "Backend",
                                                        "Networking",
                                                    ],
                                                    status="[\"Done\"]",
                                                    custom_data={
                                                        "someCustomField": models.CustomDataValue(),
                                                    },
                                                ),
                                            ),
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
                                                    name="name",
                                                    obfuscated_id="<id>",
                                                ),
                                                components=[
                                                    "Backend",
                                                    "Networking",
                                                ],
                                                status="[\"Done\"]",
                                                custom_data={
                                                    "someCustomField": models.CustomDataValue(),
                                                },
                                            ),
                                        ),
                                        shortcut=models.Shortcut(
                                            input_alias="<value>",
                                            created_by=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                            ),
                                            updated_by=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                            ),
                                            destination_document=models.Document(
                                                container_document=models.Document(
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
                                                            name="name",
                                                            obfuscated_id="<id>",
                                                        ),
                                                        components=[
                                                            "Backend",
                                                            "Networking",
                                                        ],
                                                        status="[\"Done\"]",
                                                        custom_data={
                                                            "someCustomField": models.CustomDataValue(),
                                                        },
                                                    ),
                                                ),
                                                parent_document=models.Document(
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
                                                            name="name",
                                                            obfuscated_id="<id>",
                                                        ),
                                                        components=[
                                                            "Backend",
                                                            "Networking",
                                                        ],
                                                        status="[\"Done\"]",
                                                        custom_data={
                                                            "someCustomField": models.CustomDataValue(),
                                                        },
                                                    ),
                                                ),
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
                                                        name="name",
                                                        obfuscated_id="<id>",
                                                    ),
                                                    components=[
                                                        "Backend",
                                                        "Networking",
                                                    ],
                                                    status="[\"Done\"]",
                                                    custom_data={
                                                        "someCustomField": models.CustomDataValue(),
                                                    },
                                                ),
                                            ),
                                        ),
                                        collection=models.Collection(
                                            name="<value>",
                                            description="shy versus chunder monocle",
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
                                            id=455912,
                                            creator=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                            ),
                                            updated_by=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                            ),
                                            children=[
                                                models.Collection(
                                                    name="<value>",
                                                    description="though mismatch noisily jive worth meh following hmph analyse guidance",
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
                                                    id=432713,
                                                    creator=models.Person(
                                                        name="George Clooney",
                                                        obfuscated_id="abc123",
                                                    ),
                                                    updated_by=models.Person(
                                                        name="George Clooney",
                                                        obfuscated_id="abc123",
                                                    ),
                                                ),
                                            ],
                                        ),
                                        item_type=models.CollectionItemItemType.URL,
                                    ),
                                ],
                            ),
                        ],
                        source_document=models.Document(
                            container_document=models.Document(
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
                                        name="name",
                                        obfuscated_id="<id>",
                                    ),
                                    components=[
                                        "Backend",
                                        "Networking",
                                    ],
                                    status="[\"Done\"]",
                                    custom_data={
                                        "someCustomField": models.CustomDataValue(),
                                    },
                                ),
                            ),
                            parent_document=models.Document(
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
                                        name="name",
                                        obfuscated_id="<id>",
                                    ),
                                    components=[
                                        "Backend",
                                        "Networking",
                                    ],
                                    status="[\"Done\"]",
                                    custom_data={
                                        "someCustomField": models.CustomDataValue(),
                                    },
                                ),
                            ),
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
                                    name="name",
                                    obfuscated_id="<id>",
                                ),
                                components=[
                                    "Backend",
                                    "Networking",
                                ],
                                status="[\"Done\"]",
                                custom_data={
                                    "someCustomField": models.CustomDataValue(),
                                },
                            ),
                        ),
                    ),
                    extracted_qn_a=models.ExtractedQnA(
                        question_result=models.SearchResult(
                            title="title",
                            url="https://example.com/foo/bar",
                            native_app_url="slack://foo/bar",
                            snippets=[
                                models.SearchResultSnippet(
                                    snippet="snippet",
                                    mime_type="mimeType",
                                ),
                            ],
                            must_include_suggestions=models.QuerySuggestionList(
                                suggestions=[
                                    models.QuerySuggestion(
                                        query="app:github type:pull author:mortimer",
                                        label="Mortimer's PRs",
                                        datasource="github",
                                    ),
                                ],
                                person=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                            ),
                        ),
                    ),
                    meeting=models.Meeting(
                        attendees=models.CalendarAttendees(
                            people=[
                                models.CalendarAttendee(
                                    person=models.Person(
                                        name="George Clooney",
                                        obfuscated_id="abc123",
                                    ),
                                    group_attendees=[
                                        models.CalendarAttendee(
                                            person=models.Person(
                                                name="George Clooney",
                                                obfuscated_id="abc123",
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),
                    collection=models.Collection(
                        name="<value>",
                        description="shy versus chunder monocle",
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
                        id=455912,
                        creator=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                        ),
                        children=[
                            models.Collection(
                                name="<value>",
                                description="though mismatch noisily jive worth meh following hmph analyse guidance",
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
                                id=432713,
                                creator=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                                updated_by=models.Person(
                                    name="George Clooney",
                                    obfuscated_id="abc123",
                                ),
                            ),
                        ],
                    ),
                    answer_board=models.AnswerBoard(
                        name="<value>",
                        description="bookend dense second-hand",
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
                        id=964771,
                        creator=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                        ),
                    ),
                    code=models.Code(
                        repo_name="scio",
                        file_name="README.md",
                    ),
                    shortcut=models.Shortcut(
                        input_alias="<value>",
                        created_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                        ),
                        updated_by=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                        ),
                        destination_document=models.Document(
                            container_document=models.Document(
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
                                        name="name",
                                        obfuscated_id="<id>",
                                    ),
                                    components=[
                                        "Backend",
                                        "Networking",
                                    ],
                                    status="[\"Done\"]",
                                    custom_data={
                                        "someCustomField": models.CustomDataValue(),
                                    },
                                ),
                            ),
                            parent_document=models.Document(
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
                                        name="name",
                                        obfuscated_id="<id>",
                                    ),
                                    components=[
                                        "Backend",
                                        "Networking",
                                    ],
                                    status="[\"Done\"]",
                                    custom_data={
                                        "someCustomField": models.CustomDataValue(),
                                    },
                                ),
                            ),
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
                                    name="name",
                                    obfuscated_id="<id>",
                                ),
                                components=[
                                    "Backend",
                                    "Networking",
                                ],
                                status="[\"Done\"]",
                                custom_data={
                                    "someCustomField": models.CustomDataValue(),
                                },
                            ),
                        ),
                    ),
                    query_suggestions=models.QuerySuggestionList(
                        person=models.Person(
                            name="George Clooney",
                            obfuscated_id="abc123",
                        ),
                    ),
                    related_documents=[
                        models.RelatedDocuments(
                            query_suggestion=models.QuerySuggestion(
                                query="app:github type:pull author:mortimer",
                                label="Mortimer's PRs",
                                datasource="github",
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
                                    must_include_suggestions=models.QuerySuggestionList(
                                        person=models.Person(
                                            name="George Clooney",
                                            obfuscated_id="abc123",
                                        ),
                                    ),
                                ),
                            ],
                        ),
                    ],
                    related_question=models.RelatedQuestion(
                        ranges=[
                            models.TextRange(
                                start_index=766177,
                                document=models.Document(
                                    container_document=models.Document(
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
                                                name="name",
                                                obfuscated_id="<id>",
                                            ),
                                            components=[
                                                "Backend",
                                                "Networking",
                                            ],
                                            status="[\"Done\"]",
                                            custom_data={
                                                "someCustomField": models.CustomDataValue(),
                                            },
                                        ),
                                    ),
                                    parent_document=models.Document(
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
                                                name="name",
                                                obfuscated_id="<id>",
                                            ),
                                            components=[
                                                "Backend",
                                                "Networking",
                                            ],
                                            status="[\"Done\"]",
                                            custom_data={
                                                "someCustomField": models.CustomDataValue(),
                                            },
                                        ),
                                    ),
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
                                            name="name",
                                            obfuscated_id="<id>",
                                        ),
                                        components=[
                                            "Backend",
                                            "Networking",
                                        ],
                                        status="[\"Done\"]",
                                        custom_data={
                                            "someCustomField": models.CustomDataValue(),
                                        },
                                    ),
                                ),
                            ),
                        ],
                    ),
                ),
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