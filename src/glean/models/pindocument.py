"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .facetfilter import FacetFilter, FacetFilterTypedDict
from datetime import datetime
from glean.types import BaseModel
import pydantic
from typing import List, Optional, TYPE_CHECKING
from typing_extensions import Annotated, NotRequired, TypedDict

if TYPE_CHECKING:
    from .person import Person, PersonTypedDict


class PinDocumentTypedDict(TypedDict):
    document_id: str
    r"""The document which should be a pinned result."""
    queries: NotRequired[List[str]]
    r"""The query strings for which the pinned result will show."""
    audience_filters: NotRequired[List[FacetFilterTypedDict]]
    r"""Filters which restrict who should see the pinned document. Values are taken from the corresponding filters in people search."""
    id: NotRequired[str]
    r"""The opaque id of the pin."""
    attribution: NotRequired["PersonTypedDict"]
    updated_by: NotRequired["PersonTypedDict"]
    create_time: NotRequired[datetime]
    update_time: NotRequired[datetime]


class PinDocument(BaseModel):
    document_id: Annotated[str, pydantic.Field(alias="documentId")]
    r"""The document which should be a pinned result."""

    queries: Optional[List[str]] = None
    r"""The query strings for which the pinned result will show."""

    audience_filters: Annotated[
        Optional[List[FacetFilter]], pydantic.Field(alias="audienceFilters")
    ] = None
    r"""Filters which restrict who should see the pinned document. Values are taken from the corresponding filters in people search."""

    id: Optional[str] = None
    r"""The opaque id of the pin."""

    attribution: Optional["Person"] = None

    updated_by: Annotated[Optional["Person"], pydantic.Field(alias="updatedBy")] = None

    create_time: Annotated[Optional[datetime], pydantic.Field(alias="createTime")] = (
        None
    )

    update_time: Annotated[Optional[datetime], pydantic.Field(alias="updateTime")] = (
        None
    )
