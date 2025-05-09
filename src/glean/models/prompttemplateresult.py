"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .countinfo import CountInfo, CountInfoTypedDict
from .favoriteinfo import FavoriteInfo, FavoriteInfoTypedDict
from .prompttemplate import PromptTemplate, PromptTemplateTypedDict
from glean.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PromptTemplateResultTypedDict(TypedDict):
    prompt_template: NotRequired[PromptTemplateTypedDict]
    tracking_token: NotRequired[str]
    r"""An opaque token that represents this prompt template"""
    favorite_info: NotRequired[FavoriteInfoTypedDict]
    run_count: NotRequired[CountInfoTypedDict]


class PromptTemplateResult(BaseModel):
    prompt_template: Annotated[
        Optional[PromptTemplate], pydantic.Field(alias="promptTemplate")
    ] = None

    tracking_token: Annotated[Optional[str], pydantic.Field(alias="trackingToken")] = (
        None
    )
    r"""An opaque token that represents this prompt template"""

    favorite_info: Annotated[
        Optional[FavoriteInfo], pydantic.Field(alias="favoriteInfo")
    ] = None

    run_count: Annotated[Optional[CountInfo], pydantic.Field(alias="runCount")] = None
