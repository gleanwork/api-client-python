"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .agentrun import AgentRun, AgentRunTypedDict
from .message import Message, MessageTypedDict
from glean.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class AgentRunWaitResponseTypedDict(TypedDict):
    run: NotRequired[AgentRunTypedDict]
    messages: NotRequired[List[MessageTypedDict]]
    r"""The messages returned by the run."""


class AgentRunWaitResponse(BaseModel):
    run: Optional[AgentRun] = None

    messages: Optional[List[Message]] = None
    r"""The messages returned by the run."""
