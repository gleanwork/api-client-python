"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from glean.types import BaseModel
import pydantic
from typing import List
from typing_extensions import Annotated, TypedDict


class DeleteChatFilesRequestTypedDict(TypedDict):
    file_ids: List[str]
    r"""IDs of files to delete."""


class DeleteChatFilesRequest(BaseModel):
    file_ids: Annotated[List[str], pydantic.Field(alias="fileIds")]
    r"""IDs of files to delete."""
