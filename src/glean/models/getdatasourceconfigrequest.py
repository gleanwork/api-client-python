"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from glean.types import BaseModel
from typing_extensions import TypedDict


class GetDatasourceConfigRequestTypedDict(TypedDict):
    r"""Describes the request body of the /getdatasourceconfig API call"""

    datasource: str
    r"""Datasource name for which config is needed."""


class GetDatasourceConfigRequest(BaseModel):
    r"""Describes the request body of the /getdatasourceconfig API call"""

    datasource: str
    r"""Datasource name for which config is needed."""
