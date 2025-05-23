"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from glean.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class IDType(str, Enum):
    r"""Type of the id in the incoming request."""

    CHANNEL_NAME = "CHANNEL_NAME"
    THREAD_ID = "THREAD_ID"
    CONVERSATION_ID = "CONVERSATION_ID"


class Direction(str, Enum):
    r"""The direction of the results asked with respect to the reference timestamp. Missing field defaults to OLDER. Only applicable when using a message_id."""

    OLDER = "OLDER"
    NEWER = "NEWER"


class Datasource(str, Enum):
    r"""The type of the data source. Missing field defaults to SLACK."""

    SLACK = "SLACK"
    MICROSOFTTEAMS = "MICROSOFTTEAMS"
    FACEBOOKWORKPLACE = "FACEBOOKWORKPLACE"


class MessagesRequestTypedDict(TypedDict):
    id_type: IDType
    r"""Type of the id in the incoming request."""
    id: str
    r"""ID corresponding to the requested idType. Note that channel and threads are represented by the underlying datasource's ID and conversations are represented by their document's ID."""
    workspace_id: NotRequired[str]
    r"""Id for the for the workspace in case of multiple workspaces."""
    direction: NotRequired[Direction]
    r"""The direction of the results asked with respect to the reference timestamp. Missing field defaults to OLDER. Only applicable when using a message_id."""
    timestamp_millis: NotRequired[int]
    r"""Timestamp in millis of the reference message. Only applicable when using a message_id."""
    include_root_message: NotRequired[bool]
    r"""Whether to include root message in response."""
    datasource: NotRequired[Datasource]
    r"""The type of the data source. Missing field defaults to SLACK."""
    datasource_instance_display_name: NotRequired[str]
    r"""The datasource instance display name from which the document was extracted. This is used for appinstance facet filter for datasources that support multiple instances."""


class MessagesRequest(BaseModel):
    id_type: Annotated[IDType, pydantic.Field(alias="idType")]
    r"""Type of the id in the incoming request."""

    id: str
    r"""ID corresponding to the requested idType. Note that channel and threads are represented by the underlying datasource's ID and conversations are represented by their document's ID."""

    workspace_id: Annotated[Optional[str], pydantic.Field(alias="workspaceId")] = None
    r"""Id for the for the workspace in case of multiple workspaces."""

    direction: Optional[Direction] = None
    r"""The direction of the results asked with respect to the reference timestamp. Missing field defaults to OLDER. Only applicable when using a message_id."""

    timestamp_millis: Annotated[
        Optional[int], pydantic.Field(alias="timestampMillis")
    ] = None
    r"""Timestamp in millis of the reference message. Only applicable when using a message_id."""

    include_root_message: Annotated[
        Optional[bool], pydantic.Field(alias="includeRootMessage")
    ] = None
    r"""Whether to include root message in response."""

    datasource: Optional[Datasource] = None
    r"""The type of the data source. Missing field defaults to SLACK."""

    datasource_instance_display_name: Annotated[
        Optional[str], pydantic.Field(alias="datasourceInstanceDisplayName")
    ] = None
    r"""The datasource instance display name from which the document was extracted. This is used for appinstance facet filter for datasources that support multiple instances."""
