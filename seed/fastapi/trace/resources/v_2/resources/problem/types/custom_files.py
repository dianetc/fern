# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ......core.datetime_utils import serialize_datetime
from ......core.pydantic_utilities import pydantic_v1
from .....commons.types.language import Language
from .basic_custom_files import BasicCustomFiles
from .files import Files

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def basic(self, value: BasicCustomFiles) -> CustomFiles:
        return CustomFiles(__root__=_CustomFiles.Basic(**value.dict(exclude_unset=True), type="basic"))

    def custom(self, value: typing.Dict[Language, Files]) -> CustomFiles:
        return CustomFiles(__root__=_CustomFiles.Custom(type="custom", value=value))


class CustomFiles(pydantic_v1.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_CustomFiles.Basic, _CustomFiles.Custom]:
        return self.__root__

    def visit(
        self,
        basic: typing.Callable[[BasicCustomFiles], T_Result],
        custom: typing.Callable[[typing.Dict[Language, Files]], T_Result],
    ) -> T_Result:
        if self.__root__.type == "basic":
            return basic(BasicCustomFiles(**self.__root__.dict(exclude_unset=True, exclude={"type"})))
        if self.__root__.type == "custom":
            return custom(self.__root__.value)

    __root__: typing.Annotated[
        typing.Union[_CustomFiles.Basic, _CustomFiles.Custom], pydantic_v1.Field(discriminator="type")
    ]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        extra = pydantic_v1.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}


class _CustomFiles:
    class Basic(BasicCustomFiles):
        type: typing.Literal["basic"] = "basic"

        class Config:
            allow_population_by_field_name = True
            populate_by_name = True

    class Custom(pydantic_v1.BaseModel):
        type: typing.Literal["custom"] = "custom"
        value: typing.Dict[Language, Files]


CustomFiles.update_forward_refs()
