"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .debugdocumentrequest import DebugDocumentRequest, DebugDocumentRequestTypedDict
from glean.types import BaseModel
import pydantic
from typing import List
from typing_extensions import Annotated, TypedDict


class DebugDocumentsRequestTypedDict(TypedDict):
    r"""Describes the request body of the /debug/{datasource}/documents API call."""

    debug_documents: List[DebugDocumentRequestTypedDict]
    r"""Documents to fetch debug information for"""


class DebugDocumentsRequest(BaseModel):
    r"""Describes the request body of the /debug/{datasource}/documents API call."""

    debug_documents: Annotated[
        List[DebugDocumentRequest], pydantic.Field(alias="debugDocuments")
    ]
    r"""Documents to fetch debug information for"""
