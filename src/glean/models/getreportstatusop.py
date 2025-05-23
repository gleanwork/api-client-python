"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from glean.types import BaseModel
from glean.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class GetreportstatusRequestTypedDict(TypedDict):
    id: str
    r"""The id of the report to get run status for."""


class GetreportstatusRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The id of the report to get run status for."""
