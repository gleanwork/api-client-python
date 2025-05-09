"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from glean.types import BaseModel
from typing import List, Optional, TYPE_CHECKING
from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    from .textrange import TextRange, TextRangeTypedDict


class RelatedQuestionTypedDict(TypedDict):
    question: NotRequired[str]
    r"""The text of the related question"""
    answer: NotRequired[str]
    r"""The answer for the related question"""
    ranges: NotRequired[List["TextRangeTypedDict"]]
    r"""Subsections of the answer string to which some special formatting should be applied (eg. bold)"""


class RelatedQuestion(BaseModel):
    question: Optional[str] = None
    r"""The text of the related question"""

    answer: Optional[str] = None
    r"""The answer for the related question"""

    ranges: Optional[List["TextRange"]] = None
    r"""Subsections of the answer string to which some special formatting should be applied (eg. bold)"""
