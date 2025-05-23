"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class DlpFrequency(str, Enum):
    r"""Interval between scans. DAILY is deprecated."""

    ONCE = "ONCE"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    CONTINUOUS = "CONTINUOUS"
    NONE = "NONE"
