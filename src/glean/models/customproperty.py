"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from glean.types import BaseModel
from typing import Any, Optional
from typing_extensions import NotRequired, TypedDict


class CustomPropertyTypedDict(TypedDict):
    r"""Describes the custom properties of the object."""

    name: NotRequired[str]
    value: NotRequired[Any]
    r"""Must either be a string or an array of strings. An integer, boolean, etc. is not valid. When OpenAPI Generator supports `oneOf`, we can semantically enforce this."""


class CustomProperty(BaseModel):
    r"""Describes the custom properties of the object."""

    name: Optional[str] = None

    value: Optional[Any] = None
    r"""Must either be a string or an array of strings. An integer, boolean, etc. is not valid. When OpenAPI Generator supports `oneOf`, we can semantically enforce this."""
