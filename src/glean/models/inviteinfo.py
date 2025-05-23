"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from glean.types import BaseModel
import pydantic
from typing import List, Optional, TYPE_CHECKING
from typing_extensions import Annotated, NotRequired, TypedDict

if TYPE_CHECKING:
    from .channelinviteinfo import ChannelInviteInfo, ChannelInviteInfoTypedDict
    from .person import Person, PersonTypedDict


class InviteInfoTypedDict(TypedDict):
    r"""Information regarding the invite status of a person."""

    sign_up_time: NotRequired[datetime]
    r"""The time this person signed up in ISO format (ISO 8601)."""
    invites: NotRequired[List["ChannelInviteInfoTypedDict"]]
    r"""Latest invites received by the user for each channel"""
    inviter: NotRequired["PersonTypedDict"]
    invite_time: NotRequired[datetime]
    r"""The time this person was invited in ISO format (ISO 8601)."""
    reminder_time: NotRequired[datetime]
    r"""The time this person was reminded in ISO format (ISO 8601) if a reminder was sent."""


class InviteInfo(BaseModel):
    r"""Information regarding the invite status of a person."""

    sign_up_time: Annotated[Optional[datetime], pydantic.Field(alias="signUpTime")] = (
        None
    )
    r"""The time this person signed up in ISO format (ISO 8601)."""

    invites: Optional[List["ChannelInviteInfo"]] = None
    r"""Latest invites received by the user for each channel"""

    inviter: Optional["Person"] = None

    invite_time: Annotated[
        Optional[datetime],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.",
            alias="inviteTime",
        ),
    ] = None
    r"""The time this person was invited in ISO format (ISO 8601)."""

    reminder_time: Annotated[
        Optional[datetime],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.",
            alias="reminderTime",
        ),
    ] = None
    r"""The time this person was reminded in ISO format (ISO 8601) if a reminder was sent."""
