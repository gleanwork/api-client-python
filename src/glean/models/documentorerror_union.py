"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .document import Document, DocumentTypedDict
from glean.types import BaseModel
from typing import Optional, Union
from typing_extensions import NotRequired, TypeAliasType, TypedDict


class DocumentOrErrorTypedDict(TypedDict):
    error: NotRequired[str]
    r"""The text for error, reason."""


class DocumentOrError(BaseModel):
    error: Optional[str] = None
    r"""The text for error, reason."""


DocumentOrErrorUnionTypedDict = TypeAliasType(
    "DocumentOrErrorUnionTypedDict", Union[DocumentOrErrorTypedDict, DocumentTypedDict]
)


DocumentOrErrorUnion = TypeAliasType(
    "DocumentOrErrorUnion", Union[DocumentOrError, Document]
)
