"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from glean.types import BaseModel
from glean.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class DownloadpolicycsvRequestTypedDict(TypedDict):
    id: str
    r"""The id of the policy to download violations for."""


class DownloadpolicycsvRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The id of the policy to download violations for."""
