# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import pydantic_v1

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def fern(self, value: typing.Literal["fern"]) -> UnionWithLiteral:
        return UnionWithLiteral(__root__=_UnionWithLiteral.Fern(type="fern", value=value))


class UnionWithLiteral(pydantic_v1.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_UnionWithLiteral.Fern]:
        return self.__root__

    def visit(self, fern: typing.Callable[[typing.Literal["fern"]], T_Result]) -> T_Result:
        if self.__root__.type == "fern":
            return fern(self.__root__.value)

    __root__: typing.Union[_UnionWithLiteral.Fern]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        extra = pydantic_v1.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}


class _UnionWithLiteral:
    class Fern(pydantic_v1.BaseModel):
        type: typing.Literal["fern"] = "fern"
        value: typing.Literal["fern"]


UnionWithLiteral.update_forward_refs()
