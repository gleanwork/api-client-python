"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .document import Document, DocumentTypedDict
from glean.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetDocumentsByFacetsResponseTypedDict(TypedDict):
    documents: NotRequired[List[DocumentTypedDict]]
    r"""The document details, ordered by score."""
    has_more_results: NotRequired[bool]
    r"""Whether more results are available. Use cursor to retrieve them."""
    cursor: NotRequired[str]
    r"""Cursor that indicates the start of the next page of results. To be passed in \"more\" requests for this query."""


class GetDocumentsByFacetsResponse(BaseModel):
    documents: Optional[List[Document]] = None
    r"""The document details, ordered by score."""

    has_more_results: Annotated[
        Optional[bool], pydantic.Field(alias="hasMoreResults")
    ] = None
    r"""Whether more results are available. Use cursor to retrieve them."""

    cursor: Optional[str] = None
    r"""Cursor that indicates the start of the next page of results. To be passed in \"more\" requests for this query."""
