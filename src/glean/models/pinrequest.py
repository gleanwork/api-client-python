"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .facetfilter import FacetFilter, FacetFilterTypedDict
from glean.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PinRequestTypedDict(TypedDict):
    queries: NotRequired[List[str]]
    r"""The query strings for which the pinned result will show."""
    audience_filters: NotRequired[List[FacetFilterTypedDict]]
    r"""Filters which restrict who should see the pinned document. Values are taken from the corresponding filters in people search."""
    document_id: NotRequired[str]
    r"""The document to be pinned."""


class PinRequest(BaseModel):
    queries: Optional[List[str]] = None
    r"""The query strings for which the pinned result will show."""

    audience_filters: Annotated[
        Optional[List[FacetFilter]], pydantic.Field(alias="audienceFilters")
    ] = None
    r"""Filters which restrict who should see the pinned document. Values are taken from the corresponding filters in people search."""

    document_id: Annotated[Optional[str], pydantic.Field(alias="documentId")] = None
    r"""The document to be pinned."""
