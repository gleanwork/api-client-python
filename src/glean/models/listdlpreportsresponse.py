"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .dlpreport import DlpReport, DlpReportTypedDict
from glean.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ListDlpReportsResponseTypedDict(TypedDict):
    reports: NotRequired[List[DlpReportTypedDict]]


class ListDlpReportsResponse(BaseModel):
    reports: Optional[List[DlpReport]] = None
