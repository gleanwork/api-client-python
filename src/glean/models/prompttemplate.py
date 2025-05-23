"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .chatrestrictionfilters import (
    ChatRestrictionFilters,
    ChatRestrictionFiltersTypedDict,
)
from .objectpermissions import ObjectPermissions, ObjectPermissionsTypedDict
from .person import Person, PersonTypedDict
from .userrolespecification import UserRoleSpecification, UserRoleSpecificationTypedDict
from glean.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PromptTemplateTypedDict(TypedDict):
    template: str
    r"""The actual template string."""
    name: NotRequired[str]
    r"""The user-given identifier for this prompt template."""
    application_id: NotRequired[str]
    r"""The Application Id the prompt template should be created under. Empty for default assistant."""
    inclusions: NotRequired[ChatRestrictionFiltersTypedDict]
    added_roles: NotRequired[List[UserRoleSpecificationTypedDict]]
    r"""A list of added user roles for the Workflow."""
    removed_roles: NotRequired[List[UserRoleSpecificationTypedDict]]
    r"""A list of removed user roles for the Workflow."""
    permissions: NotRequired[ObjectPermissionsTypedDict]
    id: NotRequired[str]
    r"""Opaque id for this prompt template"""
    author: NotRequired[PersonTypedDict]
    create_timestamp: NotRequired[int]
    r"""Server Unix timestamp of the creation time."""
    last_update_timestamp: NotRequired[int]
    r"""Server Unix timestamp of the last update time."""
    last_updated_by: NotRequired[PersonTypedDict]
    roles: NotRequired[List[UserRoleSpecificationTypedDict]]
    r"""A list of roles for this prompt template explicitly granted."""


class PromptTemplate(BaseModel):
    template: str
    r"""The actual template string."""

    name: Optional[str] = None
    r"""The user-given identifier for this prompt template."""

    application_id: Annotated[Optional[str], pydantic.Field(alias="applicationId")] = (
        None
    )
    r"""The Application Id the prompt template should be created under. Empty for default assistant."""

    inclusions: Optional[ChatRestrictionFilters] = None

    added_roles: Annotated[
        Optional[List[UserRoleSpecification]], pydantic.Field(alias="addedRoles")
    ] = None
    r"""A list of added user roles for the Workflow."""

    removed_roles: Annotated[
        Optional[List[UserRoleSpecification]], pydantic.Field(alias="removedRoles")
    ] = None
    r"""A list of removed user roles for the Workflow."""

    permissions: Optional[ObjectPermissions] = None

    id: Optional[str] = None
    r"""Opaque id for this prompt template"""

    author: Optional[Person] = None

    create_timestamp: Annotated[
        Optional[int], pydantic.Field(alias="createTimestamp")
    ] = None
    r"""Server Unix timestamp of the creation time."""

    last_update_timestamp: Annotated[
        Optional[int], pydantic.Field(alias="lastUpdateTimestamp")
    ] = None
    r"""Server Unix timestamp of the last update time."""

    last_updated_by: Annotated[
        Optional[Person], pydantic.Field(alias="lastUpdatedBy")
    ] = None

    roles: Optional[List[UserRoleSpecification]] = None
    r"""A list of roles for this prompt template explicitly granted."""
