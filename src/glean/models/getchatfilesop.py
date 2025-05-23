"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .getchatfilesrequest import GetChatFilesRequest, GetChatFilesRequestTypedDict
from glean.types import BaseModel
from glean.utils import FieldMetadata, QueryParamMetadata, RequestMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetchatfilesRequestRequestTypedDict(TypedDict):
    get_chat_files_request: GetChatFilesRequestTypedDict
    timezone_offset: NotRequired[int]
    r"""The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC."""


class GetchatfilesRequestRequest(BaseModel):
    get_chat_files_request: Annotated[
        GetChatFilesRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    timezone_offset: Annotated[
        Optional[int],
        pydantic.Field(alias="timezoneOffset"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC."""
