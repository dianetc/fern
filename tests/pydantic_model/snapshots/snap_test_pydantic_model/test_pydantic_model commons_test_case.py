# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .variable_value import VariableValue


class TestCase(pydantic.BaseModel):
    id: str
    params: typing.List[VariableValue]

    class Partial(typing_extensions.TypedDict):
        id: typing_extensions.NotRequired[str]
        params: typing_extensions.NotRequired[typing.List[VariableValue]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestCase.Validators.root()
            def validate(values: TestCase.Partial) -> TestCase.Partial:
                ...

            @TestCase.Validators.field("id")
            def validate_id(id: str, values: TestCase.Partial) -> str:
                ...

            @TestCase.Validators.field("params")
            def validate_params(params: typing.List[VariableValue], values: TestCase.Partial) -> typing.List[VariableValue]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[TestCase.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[TestCase.Validators._RootValidator]] = []
        _id_pre_validators: typing.ClassVar[typing.List[TestCase.Validators.IdValidator]] = []
        _id_post_validators: typing.ClassVar[typing.List[TestCase.Validators.IdValidator]] = []
        _params_pre_validators: typing.ClassVar[typing.List[TestCase.Validators.ParamsValidator]] = []
        _params_post_validators: typing.ClassVar[typing.List[TestCase.Validators.ParamsValidator]] = []

        @classmethod
        def root(
            cls, *, pre: bool = False
        ) -> typing.Callable[[TestCase.Validators._RootValidator], TestCase.Validators._RootValidator]:
            def decorator(validator: TestCase.Validators._RootValidator) -> TestCase.Validators._RootValidator:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["id"], *, pre: bool = False
        ) -> typing.Callable[[TestCase.Validators.IdValidator], TestCase.Validators.IdValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["params"], *, pre: bool = False
        ) -> typing.Callable[[TestCase.Validators.ParamsValidator], TestCase.Validators.ParamsValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "id":
                    if pre:
                        cls._id_pre_validators.append(validator)
                    else:
                        cls._id_post_validators.append(validator)
                if field_name == "params":
                    if pre:
                        cls._params_pre_validators.append(validator)
                    else:
                        cls._params_post_validators.append(validator)
                return validator

            return decorator

        class IdValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: TestCase.Partial) -> str:
                ...

        class ParamsValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[VariableValue], __values: TestCase.Partial
            ) -> typing.List[VariableValue]:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: TestCase.Partial) -> TestCase.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: TestCase.Partial) -> TestCase.Partial:
        for validator in TestCase.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: TestCase.Partial) -> TestCase.Partial:
        for validator in TestCase.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("id", pre=True)
    def _pre_validate_id(cls, v: str, values: TestCase.Partial) -> str:
        for validator in TestCase.Validators._id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("id", pre=False)
    def _post_validate_id(cls, v: str, values: TestCase.Partial) -> str:
        for validator in TestCase.Validators._id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("params", pre=True)
    def _pre_validate_params(
        cls, v: typing.List[VariableValue], values: TestCase.Partial
    ) -> typing.List[VariableValue]:
        for validator in TestCase.Validators._params_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("params", pre=False)
    def _post_validate_params(
        cls, v: typing.List[VariableValue], values: TestCase.Partial
    ) -> typing.List[VariableValue]:
        for validator in TestCase.Validators._params_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
