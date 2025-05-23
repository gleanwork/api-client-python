"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from glean.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class CollectionErrorErrorCode(str, Enum):
    NAME_EXISTS = "NAME_EXISTS"
    NOT_FOUND = "NOT_FOUND"
    COLLECTION_PINNED = "COLLECTION_PINNED"
    CONCURRENT_HIERARCHY_EDIT = "CONCURRENT_HIERARCHY_EDIT"
    HEIGHT_VIOLATION = "HEIGHT_VIOLATION"
    WIDTH_VIOLATION = "WIDTH_VIOLATION"
    NO_PERMISSIONS = "NO_PERMISSIONS"


class CollectionErrorTypedDict(TypedDict):
    error_code: CollectionErrorErrorCode


class CollectionError(BaseModel):
    error_code: Annotated[CollectionErrorErrorCode, pydantic.Field(alias="errorCode")]
