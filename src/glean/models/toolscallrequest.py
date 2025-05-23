"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .toolscallparameter import ToolsCallParameter, ToolsCallParameterTypedDict
from glean.types import BaseModel
from typing import Dict
from typing_extensions import TypedDict


class ToolsCallRequestTypedDict(TypedDict):
    name: str
    r"""Required name of the tool to execute"""
    parameters: Dict[str, ToolsCallParameterTypedDict]
    r"""The parameters for the tool. Each key is the name of the parameter and the value is the parameter object."""


class ToolsCallRequest(BaseModel):
    name: str
    r"""Required name of the tool to execute"""

    parameters: Dict[str, ToolsCallParameter]
    r"""The parameters for the tool. Each key is the name of the parameter and the value is the parameter object."""
