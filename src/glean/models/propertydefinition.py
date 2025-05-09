"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from glean.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PropertyType(str, Enum):
    r"""The type of custom property - this governs the search and faceting behavior. Note that MULTIPICKLIST is not yet supported."""

    TEXT = "TEXT"
    DATE = "DATE"
    INT = "INT"
    USERID = "USERID"
    PICKLIST = "PICKLIST"
    TEXTLIST = "TEXTLIST"
    MULTIPICKLIST = "MULTIPICKLIST"


class UIOptions(str, Enum):
    NONE = "NONE"
    SEARCH_RESULT = "SEARCH_RESULT"
    DOC_HOVERCARD = "DOC_HOVERCARD"


class PropertyDefinitionTypedDict(TypedDict):
    name: NotRequired[str]
    r"""The name of the property in the `DocumentMetadata` (e.g. 'createTime', 'updateTime', 'author', 'container'). In the future, this will support custom properties too."""
    display_label: NotRequired[str]
    r"""The user friendly label for the property."""
    display_label_plural: NotRequired[str]
    r"""The user friendly label for the property that will be used if a plural context."""
    property_type: NotRequired[PropertyType]
    r"""The type of custom property - this governs the search and faceting behavior. Note that MULTIPICKLIST is not yet supported."""
    ui_options: NotRequired[UIOptions]
    hide_ui_facet: NotRequired[bool]
    r"""If true then the property will not show up as a facet in the UI."""
    ui_facet_order: NotRequired[int]
    r"""Will be used to set the order of facets in the UI, if present. If set for one facet, must be set for all non-hidden UI facets. Must take on an integer value from 1 (shown at the top) to N (shown last), where N is the number of non-hidden UI facets. These facets will be ordered below the built-in \"Type\" and \"Tag\" operators."""
    skip_indexing: NotRequired[bool]
    r"""If true then the property will not be indexed for retrieval and ranking."""
    group: NotRequired[str]
    r"""The unique identifier of the `PropertyGroup` to which this property belongs."""


class PropertyDefinition(BaseModel):
    name: Optional[str] = None
    r"""The name of the property in the `DocumentMetadata` (e.g. 'createTime', 'updateTime', 'author', 'container'). In the future, this will support custom properties too."""

    display_label: Annotated[Optional[str], pydantic.Field(alias="displayLabel")] = None
    r"""The user friendly label for the property."""

    display_label_plural: Annotated[
        Optional[str], pydantic.Field(alias="displayLabelPlural")
    ] = None
    r"""The user friendly label for the property that will be used if a plural context."""

    property_type: Annotated[
        Optional[PropertyType], pydantic.Field(alias="propertyType")
    ] = None
    r"""The type of custom property - this governs the search and faceting behavior. Note that MULTIPICKLIST is not yet supported."""

    ui_options: Annotated[Optional[UIOptions], pydantic.Field(alias="uiOptions")] = None

    hide_ui_facet: Annotated[Optional[bool], pydantic.Field(alias="hideUiFacet")] = None
    r"""If true then the property will not show up as a facet in the UI."""

    ui_facet_order: Annotated[Optional[int], pydantic.Field(alias="uiFacetOrder")] = (
        None
    )
    r"""Will be used to set the order of facets in the UI, if present. If set for one facet, must be set for all non-hidden UI facets. Must take on an integer value from 1 (shown at the top) to N (shown last), where N is the number of non-hidden UI facets. These facets will be ordered below the built-in \"Type\" and \"Tag\" operators."""

    skip_indexing: Annotated[Optional[bool], pydantic.Field(alias="skipIndexing")] = (
        None
    )
    r"""If true then the property will not be indexed for retrieval and ranking."""

    group: Optional[str] = None
    r"""The unique identifier of the `PropertyGroup` to which this property belongs."""
