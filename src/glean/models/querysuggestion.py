"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .searchproviderinfo import SearchProviderInfo, SearchProviderInfoTypedDict
from .searchrequestinputdetails import (
    SearchRequestInputDetails,
    SearchRequestInputDetailsTypedDict,
)
from .searchrequestoptions import SearchRequestOptions, SearchRequestOptionsTypedDict
from glean.types import BaseModel
import pydantic
from typing import List, Optional, TYPE_CHECKING
from typing_extensions import Annotated, NotRequired, TypedDict

if TYPE_CHECKING:
    from .textrange import TextRange, TextRangeTypedDict


class QuerySuggestionTypedDict(TypedDict):
    query: str
    r"""The query being suggested (e.g. enforcing the missing term from the original query)."""
    missing_term: NotRequired[str]
    r"""A query term missing from the original query on which this suggestion is based."""
    search_provider_info: NotRequired[SearchProviderInfoTypedDict]
    label: NotRequired[str]
    r"""A user-facing description to display for the suggestion."""
    datasource: NotRequired[str]
    r"""The datasource associated with the suggestion."""
    request_options: NotRequired[SearchRequestOptionsTypedDict]
    ranges: NotRequired[List["TextRangeTypedDict"]]
    r"""The bolded ranges within the query of the QuerySuggestion."""
    input_details: NotRequired[SearchRequestInputDetailsTypedDict]


class QuerySuggestion(BaseModel):
    query: str
    r"""The query being suggested (e.g. enforcing the missing term from the original query)."""

    missing_term: Annotated[Optional[str], pydantic.Field(alias="missingTerm")] = None
    r"""A query term missing from the original query on which this suggestion is based."""

    search_provider_info: Annotated[
        Optional[SearchProviderInfo], pydantic.Field(alias="searchProviderInfo")
    ] = None

    label: Optional[str] = None
    r"""A user-facing description to display for the suggestion."""

    datasource: Optional[str] = None
    r"""The datasource associated with the suggestion."""

    request_options: Annotated[
        Optional[SearchRequestOptions], pydantic.Field(alias="requestOptions")
    ] = None

    ranges: Optional[List["TextRange"]] = None
    r"""The bolded ranges within the query of the QuerySuggestion."""

    input_details: Annotated[
        Optional[SearchRequestInputDetails], pydantic.Field(alias="inputDetails")
    ] = None
