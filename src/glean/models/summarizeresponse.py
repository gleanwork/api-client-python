"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .summary import Summary, SummaryTypedDict
from glean.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ErrorTypedDict(TypedDict):
    message: NotRequired[str]


class Error(BaseModel):
    message: Optional[str] = None


class SummarizeResponseTypedDict(TypedDict):
    error: NotRequired[ErrorTypedDict]
    summary: NotRequired[SummaryTypedDict]
    tracking_token: NotRequired[str]
    r"""An opaque token that represents this summary in this particular query. To be used for /feedback reporting."""


class SummarizeResponse(BaseModel):
    error: Optional[Error] = None

    summary: Optional[Summary] = None

    tracking_token: Annotated[Optional[str], pydantic.Field(alias="trackingToken")] = (
        None
    )
    r"""An opaque token that represents this summary in this particular query. To be used for /feedback reporting."""
