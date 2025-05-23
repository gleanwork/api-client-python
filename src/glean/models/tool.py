"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .toolparameter import ToolParameter, ToolParameterTypedDict
from enum import Enum
from glean.types import BaseModel
import pydantic
from typing import Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ToolType(str, Enum):
    r"""Type of tool (READ, WRITE)"""

    READ = "READ"
    WRITE = "WRITE"


class ToolTypedDict(TypedDict):
    type: NotRequired[ToolType]
    r"""Type of tool (READ, WRITE)"""
    name: NotRequired[str]
    r"""Unique identifier for the tool"""
    display_name: NotRequired[str]
    r"""Human-readable name"""
    description: NotRequired[str]
    r"""LLM friendly description of the tool"""
    parameters: NotRequired[Dict[str, ToolParameterTypedDict]]
    r"""The parameters for the tool. Each key is the name of the parameter and the value is the parameter object."""


class Tool(BaseModel):
    type: Optional[ToolType] = None
    r"""Type of tool (READ, WRITE)"""

    name: Optional[str] = None
    r"""Unique identifier for the tool"""

    display_name: Annotated[Optional[str], pydantic.Field(alias="displayName")] = None
    r"""Human-readable name"""

    description: Optional[str] = None
    r"""LLM friendly description of the tool"""

    parameters: Optional[Dict[str, ToolParameter]] = None
    r"""The parameters for the tool. Each key is the name of the parameter and the value is the parameter object."""
