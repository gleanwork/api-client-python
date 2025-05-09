"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .errormessage import ErrorMessage, ErrorMessageTypedDict
from .invalidoperatorvalueerror import (
    InvalidOperatorValueError,
    InvalidOperatorValueErrorTypedDict,
)
from glean.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GleanDataErrorTypedDict(TypedDict):
    bad_gmail_token: NotRequired[bool]
    r"""Indicates the gmail results could not be fetched due to bad token."""
    bad_outlook_token: NotRequired[bool]
    r"""Indicates the outlook results could not be fetched due to bad token."""
    invalid_operators: NotRequired[List[InvalidOperatorValueErrorTypedDict]]
    r"""Indicates results could not be fetched due to invalid operators in the query."""
    error_messages: NotRequired[List[ErrorMessageTypedDict]]


class GleanDataError(BaseModel):
    bad_gmail_token: Annotated[
        Optional[bool], pydantic.Field(alias="badGmailToken")
    ] = None
    r"""Indicates the gmail results could not be fetched due to bad token."""

    bad_outlook_token: Annotated[
        Optional[bool], pydantic.Field(alias="badOutlookToken")
    ] = None
    r"""Indicates the outlook results could not be fetched due to bad token."""

    invalid_operators: Annotated[
        Optional[List[InvalidOperatorValueError]],
        pydantic.Field(alias="invalidOperators"),
    ] = None
    r"""Indicates results could not be fetched due to invalid operators in the query."""

    error_messages: Annotated[
        Optional[List[ErrorMessage]], pydantic.Field(alias="errorMessages")
    ] = None
