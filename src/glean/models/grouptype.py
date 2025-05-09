"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class GroupType(str, Enum):
    r"""The type of user group"""

    DEPARTMENT = "DEPARTMENT"
    ALL = "ALL"
    TEAM = "TEAM"
    JOB_TITLE = "JOB_TITLE"
    ROLE_TYPE = "ROLE_TYPE"
    LOCATION = "LOCATION"
    REGION = "REGION"
    EXTERNAL_GROUP = "EXTERNAL_GROUP"
