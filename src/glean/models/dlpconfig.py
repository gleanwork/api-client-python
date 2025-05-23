"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .allowlistoptions import AllowlistOptions, AllowlistOptionsTypedDict
from .dlpperson import DlpPerson, DlpPersonTypedDict
from .externalsharingoptions import (
    ExternalSharingOptions,
    ExternalSharingOptionsTypedDict,
)
from .inputoptions import InputOptions, InputOptionsTypedDict
from .sensitivecontentoptions import (
    SensitiveContentOptions,
    SensitiveContentOptionsTypedDict,
)
from .sensitiveinfotype import SensitiveInfoType, SensitiveInfoTypeTypedDict
from .sharingoptions import SharingOptions, SharingOptionsTypedDict
from glean.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class DlpConfigTypedDict(TypedDict):
    r"""Detailed configuration of what documents and sensitive content will be scanned."""

    version: NotRequired[int]
    r"""Synonymous with report/policy id."""
    sensitive_info_types: NotRequired[List[SensitiveInfoTypeTypedDict]]
    r"""DEPRECATED - use `sensitiveContentOptions` instead."""
    input_options: NotRequired[InputOptionsTypedDict]
    r"""Controls which data-sources and what time-range to include in scans."""
    external_sharing_options: NotRequired[ExternalSharingOptionsTypedDict]
    broad_sharing_options: NotRequired[SharingOptionsTypedDict]
    r"""Controls how \"shared\" a document must be to get picked for scans."""
    sensitive_content_options: NotRequired[SensitiveContentOptionsTypedDict]
    r"""Options for defining sensitive content within scanned documents."""
    report_name: NotRequired[str]
    frequency: NotRequired[str]
    r"""Interval between scans."""
    created_by: NotRequired[DlpPersonTypedDict]
    r"""Details about the person who created this report/policy."""
    created_at: NotRequired[str]
    r"""Timestamp at which this configuration was created."""
    redact_quote: NotRequired[bool]
    r"""redact quote in findings of the report"""
    auto_hide_docs: NotRequired[bool]
    r"""auto hide documents with findings in the report"""
    allowlist_options: NotRequired[AllowlistOptionsTypedDict]
    r"""Terms that are allow-listed during the scans. If any finding picked up by a rule exactly matches a term in the allow-list, it will not be counted as a violation."""


class DlpConfig(BaseModel):
    r"""Detailed configuration of what documents and sensitive content will be scanned."""

    version: Optional[int] = None
    r"""Synonymous with report/policy id."""

    sensitive_info_types: Annotated[
        Optional[List[SensitiveInfoType]],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.",
            alias="sensitiveInfoTypes",
        ),
    ] = None
    r"""DEPRECATED - use `sensitiveContentOptions` instead."""

    input_options: Annotated[
        Optional[InputOptions], pydantic.Field(alias="inputOptions")
    ] = None
    r"""Controls which data-sources and what time-range to include in scans."""

    external_sharing_options: Annotated[
        Optional[ExternalSharingOptions],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.",
            alias="externalSharingOptions",
        ),
    ] = None

    broad_sharing_options: Annotated[
        Optional[SharingOptions], pydantic.Field(alias="broadSharingOptions")
    ] = None
    r"""Controls how \"shared\" a document must be to get picked for scans."""

    sensitive_content_options: Annotated[
        Optional[SensitiveContentOptions],
        pydantic.Field(alias="sensitiveContentOptions"),
    ] = None
    r"""Options for defining sensitive content within scanned documents."""

    report_name: Annotated[Optional[str], pydantic.Field(alias="reportName")] = None

    frequency: Optional[str] = None
    r"""Interval between scans."""

    created_by: Annotated[Optional[DlpPerson], pydantic.Field(alias="createdBy")] = None
    r"""Details about the person who created this report/policy."""

    created_at: Annotated[Optional[str], pydantic.Field(alias="createdAt")] = None
    r"""Timestamp at which this configuration was created."""

    redact_quote: Annotated[Optional[bool], pydantic.Field(alias="redactQuote")] = None
    r"""redact quote in findings of the report"""

    auto_hide_docs: Annotated[Optional[bool], pydantic.Field(alias="autoHideDocs")] = (
        None
    )
    r"""auto hide documents with findings in the report"""

    allowlist_options: Annotated[
        Optional[AllowlistOptions], pydantic.Field(alias="allowlistOptions")
    ] = None
    r"""Terms that are allow-listed during the scans. If any finding picked up by a rule exactly matches a term in the allow-list, it will not be counted as a violation."""
