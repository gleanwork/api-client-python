"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .chatfile import ChatFile, ChatFileTypedDict
from glean.types import BaseModel
from typing import Dict, Optional
from typing_extensions import NotRequired, TypedDict


class GetChatFilesResponseTypedDict(TypedDict):
    files: NotRequired[Dict[str, ChatFileTypedDict]]
    r"""A map of file IDs to ChatFile structs."""


class GetChatFilesResponse(BaseModel):
    files: Optional[Dict[str, ChatFile]] = None
    r"""A map of file IDs to ChatFile structs."""
