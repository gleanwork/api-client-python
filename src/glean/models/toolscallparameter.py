"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from glean.types import BaseModel
from typing import Dict, List, Optional
from typing_extensions import NotRequired, TypedDict


class ToolsCallParameterTypedDict(TypedDict):
    name: str
    r"""The name of the parameter"""
    value: str
    r"""The value of the parameter (for primitive types)"""
    items: NotRequired[List[ToolsCallParameterTypedDict]]
    r"""The value of the parameter (for array types)"""
    properties: NotRequired[Dict[str, ToolsCallParameterTypedDict]]
    r"""The value of the parameter (for object types)"""


class ToolsCallParameter(BaseModel):
    name: str
    r"""The name of the parameter"""

    value: str
    r"""The value of the parameter (for primitive types)"""

    items: Optional[List[ToolsCallParameter]] = None
    r"""The value of the parameter (for array types)"""

    properties: Optional[Dict[str, ToolsCallParameter]] = None
    r"""The value of the parameter (for object types)"""
