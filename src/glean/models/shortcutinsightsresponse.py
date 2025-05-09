"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .shortcutinsight import ShortcutInsight, ShortcutInsightTypedDict
from glean.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ShortcutInsightsResponseTypedDict(TypedDict):
    last_log_timestamp: NotRequired[int]
    r"""Unix timestamp of the last activity processed to make the response (in seconds since epoch UTC)."""
    shortcut_insights: NotRequired[List[ShortcutInsightTypedDict]]
    r"""Insights for shortcuts."""
    departments: NotRequired[List[str]]
    r"""list of departments applicable for shortcuts tab."""
    min_visitor_threshold: NotRequired[int]
    r"""Min threshold in number of visitors while populating results, otherwise 0."""


class ShortcutInsightsResponse(BaseModel):
    last_log_timestamp: Annotated[
        Optional[int], pydantic.Field(alias="lastLogTimestamp")
    ] = None
    r"""Unix timestamp of the last activity processed to make the response (in seconds since epoch UTC)."""

    shortcut_insights: Annotated[
        Optional[List[ShortcutInsight]], pydantic.Field(alias="shortcutInsights")
    ] = None
    r"""Insights for shortcuts."""

    departments: Optional[List[str]] = None
    r"""list of departments applicable for shortcuts tab."""

    min_visitor_threshold: Annotated[
        Optional[int], pydantic.Field(alias="minVisitorThreshold")
    ] = None
    r"""Min threshold in number of visitors while populating results, otherwise 0."""
