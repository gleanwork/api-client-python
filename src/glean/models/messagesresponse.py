"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .searchresponse import SearchResponse, SearchResponseTypedDict
from .searchresult import SearchResult, SearchResultTypedDict
from glean.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class MessagesResponseTypedDict(TypedDict):
    has_more: bool
    r"""Whether there are more results for client to continue requesting."""
    search_response: NotRequired[SearchResponseTypedDict]
    root_message: NotRequired[SearchResultTypedDict]


class MessagesResponse(BaseModel):
    has_more: Annotated[bool, pydantic.Field(alias="hasMore")]
    r"""Whether there are more results for client to continue requesting."""

    search_response: Annotated[
        Optional[SearchResponse], pydantic.Field(alias="searchResponse")
    ] = None

    root_message: Annotated[
        Optional[SearchResult], pydantic.Field(alias="rootMessage")
    ] = None
