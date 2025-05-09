"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from glean.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class DocumentInteractionsDefinitionTypedDict(TypedDict):
    r"""describes the interactions on the document"""

    num_views: NotRequired[int]
    num_likes: NotRequired[int]
    num_comments: NotRequired[int]


class DocumentInteractionsDefinition(BaseModel):
    r"""describes the interactions on the document"""

    num_views: Annotated[Optional[int], pydantic.Field(alias="numViews")] = None

    num_likes: Annotated[Optional[int], pydantic.Field(alias="numLikes")] = None

    num_comments: Annotated[Optional[int], pydantic.Field(alias="numComments")] = None
