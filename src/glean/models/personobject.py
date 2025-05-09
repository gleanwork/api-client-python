"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from glean.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class PersonObjectTypedDict(TypedDict):
    name: str
    r"""The display name."""
    obfuscated_id: str
    r"""An opaque identifier that can be used to request metadata for a Person."""


class PersonObject(BaseModel):
    name: str
    r"""The display name."""

    obfuscated_id: Annotated[str, pydantic.Field(alias="obfuscatedId")]
    r"""An opaque identifier that can be used to request metadata for a Person."""
