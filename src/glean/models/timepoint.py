"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from glean.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class TimePointTypedDict(TypedDict):
    epoch_seconds: NotRequired[int]
    r"""Epoch seconds. Has precedence over daysFromNow."""
    days_from_now: NotRequired[int]
    r"""The number of days from now. Specification relative to current time. Can be negative."""


class TimePoint(BaseModel):
    epoch_seconds: Annotated[Optional[int], pydantic.Field(alias="epochSeconds")] = None
    r"""Epoch seconds. Has precedence over daysFromNow."""

    days_from_now: Annotated[Optional[int], pydantic.Field(alias="daysFromNow")] = None
    r"""The number of days from now. Specification relative to current time. Can be negative."""
