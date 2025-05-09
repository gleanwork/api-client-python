"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from glean.types import BaseModel
import pydantic
from typing import List, Optional, TYPE_CHECKING
from typing_extensions import Annotated, NotRequired, TypedDict

if TYPE_CHECKING:
    from .person import Person, PersonTypedDict


class ResponseStatus(str, Enum):
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"
    NO_RESPONSE = "NO_RESPONSE"
    TENTATIVE = "TENTATIVE"


class CalendarAttendeeTypedDict(TypedDict):
    person: "PersonTypedDict"
    is_organizer: NotRequired[bool]
    r"""Whether or not this attendee is an organizer."""
    is_in_group: NotRequired[bool]
    r"""Whether or not this attendee is in a group. Needed temporarily at least to support both flat attendees and tree for compatibility."""
    group_attendees: NotRequired[List[CalendarAttendeeTypedDict]]
    r"""If this attendee is a group, represents the list of individual attendees in the group."""
    response_status: NotRequired[ResponseStatus]


class CalendarAttendee(BaseModel):
    person: "Person"

    is_organizer: Annotated[Optional[bool], pydantic.Field(alias="isOrganizer")] = None
    r"""Whether or not this attendee is an organizer."""

    is_in_group: Annotated[Optional[bool], pydantic.Field(alias="isInGroup")] = None
    r"""Whether or not this attendee is in a group. Needed temporarily at least to support both flat attendees and tree for compatibility."""

    group_attendees: Annotated[
        Optional[List[CalendarAttendee]], pydantic.Field(alias="groupAttendees")
    ] = None
    r"""If this attendee is a group, represents the list of individual attendees in the group."""

    response_status: Annotated[
        Optional[ResponseStatus], pydantic.Field(alias="responseStatus")
    ] = None
