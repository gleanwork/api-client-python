"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .dlpconfig import DlpConfig, DlpConfigTypedDict
from .dlpfrequency import DlpFrequency
from .dlpreportstatus import DlpReportStatus
from glean.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateDlpReportRequestTypedDict(TypedDict):
    config: NotRequired[DlpConfigTypedDict]
    r"""Detailed configuration of what documents and sensitive content will be scanned."""
    frequency: NotRequired[DlpFrequency]
    r"""Interval between scans. DAILY is deprecated."""
    status: NotRequired[DlpReportStatus]
    r"""The status of the policy/report. Only ACTIVE status will be picked for scans."""
    auto_hide_docs: NotRequired[bool]
    r"""The new autoHideDoc boolean the policy will be updated to if provided."""
    report_name: NotRequired[str]
    r"""The new name of the policy if provided."""


class UpdateDlpReportRequest(BaseModel):
    config: Optional[DlpConfig] = None
    r"""Detailed configuration of what documents and sensitive content will be scanned."""

    frequency: Optional[DlpFrequency] = None
    r"""Interval between scans. DAILY is deprecated."""

    status: Optional[DlpReportStatus] = None
    r"""The status of the policy/report. Only ACTIVE status will be picked for scans."""

    auto_hide_docs: Annotated[Optional[bool], pydantic.Field(alias="autoHideDocs")] = (
        None
    )
    r"""The new autoHideDoc boolean the policy will be updated to if provided."""

    report_name: Annotated[Optional[str], pydantic.Field(alias="reportName")] = None
    r"""The new name of the policy if provided."""
