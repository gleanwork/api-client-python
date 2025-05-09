"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .shortcut import Shortcut, ShortcutTypedDict
from .shortcuterror import ShortcutError, ShortcutErrorTypedDict
from glean.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CreateShortcutResponseTypedDict(TypedDict):
    shortcut: NotRequired[ShortcutTypedDict]
    error: NotRequired[ShortcutErrorTypedDict]


class CreateShortcutResponse(BaseModel):
    shortcut: Optional[Shortcut] = None

    error: Optional[ShortcutError] = None
