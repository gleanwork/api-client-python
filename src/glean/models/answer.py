"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .documentspec_union import DocumentSpecUnion, DocumentSpecUnionTypedDict
from .facetfilter import FacetFilter, FacetFilterTypedDict
from .objectpermissions import ObjectPermissions, ObjectPermissionsTypedDict
from datetime import datetime
from enum import Enum
from glean.types import BaseModel
import pydantic
from typing import List, Optional, TYPE_CHECKING
from typing_extensions import Annotated, NotRequired, TypedDict

if TYPE_CHECKING:
    from .answerboard import AnswerBoard, AnswerBoardTypedDict
    from .answerlikes import AnswerLikes, AnswerLikesTypedDict
    from .collection import Collection, CollectionTypedDict
    from .document import Document, DocumentTypedDict
    from .person import Person, PersonTypedDict
    from .structuredtext import StructuredText, StructuredTextTypedDict
    from .userrolespecification import (
        UserRoleSpecification,
        UserRoleSpecificationTypedDict,
    )
    from .verification import Verification, VerificationTypedDict


class AnswerSourceType(str, Enum):
    DOCUMENT = "DOCUMENT"
    ASSISTANT = "ASSISTANT"


class AnswerTypedDict(TypedDict):
    id: int
    r"""The opaque ID of the Answer."""
    doc_id: NotRequired[str]
    r"""Glean Document ID of the Answer. The Glean Document ID is supported for cases where the Answer ID isn't available. If both are available, using the Answer ID is preferred."""
    question: NotRequired[str]
    question_variations: NotRequired[List[str]]
    r"""Additional ways of phrasing this question."""
    body_text: NotRequired[str]
    r"""The plain text answer to the question."""
    board_id: NotRequired[int]
    r"""The parent board ID of this Answer, or 0 if it's a floating Answer."""
    audience_filters: NotRequired[List[FacetFilterTypedDict]]
    r"""Filters which restrict who should see the answer. Values are taken from the corresponding filters in people search."""
    added_roles: NotRequired[List["UserRoleSpecificationTypedDict"]]
    r"""A list of user roles for the answer added by the owner."""
    removed_roles: NotRequired[List["UserRoleSpecificationTypedDict"]]
    r"""A list of user roles for the answer removed by the owner."""
    roles: NotRequired[List["UserRoleSpecificationTypedDict"]]
    r"""A list of roles for this answer explicitly granted by an owner, editor, or admin."""
    source_document_spec: NotRequired[DocumentSpecUnionTypedDict]
    source_type: NotRequired[AnswerSourceType]
    permissions: NotRequired[ObjectPermissionsTypedDict]
    combined_answer_text: NotRequired["StructuredTextTypedDict"]
    likes: NotRequired["AnswerLikesTypedDict"]
    author: NotRequired["PersonTypedDict"]
    create_time: NotRequired[datetime]
    r"""The time the answer was created in ISO format (ISO 8601)."""
    update_time: NotRequired[datetime]
    r"""The time the answer was last updated in ISO format (ISO 8601)."""
    updated_by: NotRequired["PersonTypedDict"]
    verification: NotRequired["VerificationTypedDict"]
    board: NotRequired["AnswerBoardTypedDict"]
    collections: NotRequired[List["CollectionTypedDict"]]
    r"""The collections to which the answer belongs."""
    document_category: NotRequired[str]
    r"""The document's document_category(.proto)."""
    source_document: NotRequired["DocumentTypedDict"]


class Answer(BaseModel):
    id: int
    r"""The opaque ID of the Answer."""

    doc_id: Annotated[Optional[str], pydantic.Field(alias="docId")] = None
    r"""Glean Document ID of the Answer. The Glean Document ID is supported for cases where the Answer ID isn't available. If both are available, using the Answer ID is preferred."""

    question: Optional[str] = None

    question_variations: Annotated[
        Optional[List[str]], pydantic.Field(alias="questionVariations")
    ] = None
    r"""Additional ways of phrasing this question."""

    body_text: Annotated[Optional[str], pydantic.Field(alias="bodyText")] = None
    r"""The plain text answer to the question."""

    board_id: Annotated[Optional[int], pydantic.Field(alias="boardId")] = None
    r"""The parent board ID of this Answer, or 0 if it's a floating Answer."""

    audience_filters: Annotated[
        Optional[List[FacetFilter]], pydantic.Field(alias="audienceFilters")
    ] = None
    r"""Filters which restrict who should see the answer. Values are taken from the corresponding filters in people search."""

    added_roles: Annotated[
        Optional[List["UserRoleSpecification"]], pydantic.Field(alias="addedRoles")
    ] = None
    r"""A list of user roles for the answer added by the owner."""

    removed_roles: Annotated[
        Optional[List["UserRoleSpecification"]], pydantic.Field(alias="removedRoles")
    ] = None
    r"""A list of user roles for the answer removed by the owner."""

    roles: Optional[List["UserRoleSpecification"]] = None
    r"""A list of roles for this answer explicitly granted by an owner, editor, or admin."""

    source_document_spec: Annotated[
        Optional[DocumentSpecUnion], pydantic.Field(alias="sourceDocumentSpec")
    ] = None

    source_type: Annotated[
        Optional[AnswerSourceType], pydantic.Field(alias="sourceType")
    ] = None

    permissions: Optional[ObjectPermissions] = None

    combined_answer_text: Annotated[
        Optional["StructuredText"], pydantic.Field(alias="combinedAnswerText")
    ] = None

    likes: Optional["AnswerLikes"] = None

    author: Optional["Person"] = None

    create_time: Annotated[Optional[datetime], pydantic.Field(alias="createTime")] = (
        None
    )
    r"""The time the answer was created in ISO format (ISO 8601)."""

    update_time: Annotated[Optional[datetime], pydantic.Field(alias="updateTime")] = (
        None
    )
    r"""The time the answer was last updated in ISO format (ISO 8601)."""

    updated_by: Annotated[Optional["Person"], pydantic.Field(alias="updatedBy")] = None

    verification: Optional["Verification"] = None

    board: Optional["AnswerBoard"] = None

    collections: Optional[List["Collection"]] = None
    r"""The collections to which the answer belongs."""

    document_category: Annotated[
        Optional[str], pydantic.Field(alias="documentCategory")
    ] = None
    r"""The document's document_category(.proto)."""

    source_document: Annotated[
        Optional["Document"], pydantic.Field(alias="sourceDocument")
    ] = None
