"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .dlpconfig import DlpConfig, DlpConfigTypedDict
from .dlpfrequency import DlpFrequency
from .dlpperson import DlpPerson, DlpPersonTypedDict
from .dlpreportstatus import DlpReportStatus
from enum import Enum
from glean.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class LastScanStatus(str, Enum):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    CANCELLED = "CANCELLED"
    CANCELLING = "CANCELLING"
    ACTIVE = "ACTIVE"


class DlpReportTypedDict(TypedDict):
    r"""Full policy information that will be used for scans."""

    id: NotRequired[str]
    name: NotRequired[str]
    config: NotRequired[DlpConfigTypedDict]
    r"""Detailed configuration of what documents and sensitive content will be scanned."""
    frequency: NotRequired[DlpFrequency]
    r"""Interval between scans. DAILY is deprecated."""
    status: NotRequired[DlpReportStatus]
    r"""The status of the policy/report. Only ACTIVE status will be picked for scans."""
    created_by: NotRequired[DlpPersonTypedDict]
    r"""Details about the person who created this report/policy."""
    created_at: NotRequired[str]
    r"""Timestamp at which the policy was created."""
    last_updated_at: NotRequired[str]
    r"""Timestamp at which the policy was last updated."""
    auto_hide_docs: NotRequired[bool]
    r"""Auto hide documents with findings in the policy."""
    last_scan_status: NotRequired[LastScanStatus]
    last_scan_start_time: NotRequired[str]
    r"""The timestamp at which the report's last run/scan began."""
    updated_by: NotRequired[DlpPersonTypedDict]
    r"""Details about the person who created this report/policy."""


class DlpReport(BaseModel):
    r"""Full policy information that will be used for scans."""

    id: Optional[str] = None

    name: Optional[str] = None

    config: Optional[DlpConfig] = None
    r"""Detailed configuration of what documents and sensitive content will be scanned."""

    frequency: Optional[DlpFrequency] = None
    r"""Interval between scans. DAILY is deprecated."""

    status: Optional[DlpReportStatus] = None
    r"""The status of the policy/report. Only ACTIVE status will be picked for scans."""

    created_by: Annotated[Optional[DlpPerson], pydantic.Field(alias="createdBy")] = None
    r"""Details about the person who created this report/policy."""

    created_at: Annotated[Optional[str], pydantic.Field(alias="createdAt")] = None
    r"""Timestamp at which the policy was created."""

    last_updated_at: Annotated[Optional[str], pydantic.Field(alias="lastUpdatedAt")] = (
        None
    )
    r"""Timestamp at which the policy was last updated."""

    auto_hide_docs: Annotated[Optional[bool], pydantic.Field(alias="autoHideDocs")] = (
        None
    )
    r"""Auto hide documents with findings in the policy."""

    last_scan_status: Annotated[
        Optional[LastScanStatus], pydantic.Field(alias="lastScanStatus")
    ] = None

    last_scan_start_time: Annotated[
        Optional[str], pydantic.Field(alias="lastScanStartTime")
    ] = None
    r"""The timestamp at which the report's last run/scan began."""

    updated_by: Annotated[Optional[DlpPerson], pydantic.Field(alias="updatedBy")] = None
    r"""Details about the person who created this report/policy."""
