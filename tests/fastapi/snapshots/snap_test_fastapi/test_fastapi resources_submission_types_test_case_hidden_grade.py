# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class TestCaseHiddenGrade(pydantic.BaseModel):
    passed: bool

    class Partial(typing_extensions.TypedDict):
        passed: typing_extensions.NotRequired[bool]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestCaseHiddenGrade.Validators.root()
            def validate(values: TestCaseHiddenGrade.Partial) -> TestCaseHiddenGrade.Partial:
                ...

            @TestCaseHiddenGrade.Validators.field("passed")
            def validate_passed(passed: bool, values: TestCaseHiddenGrade.Partial) -> bool:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[TestCaseHiddenGrade.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[TestCaseHiddenGrade.Validators._RootValidator]] = []
        _passed_pre_validators: typing.ClassVar[typing.List[TestCaseHiddenGrade.Validators.PassedValidator]] = []
        _passed_post_validators: typing.ClassVar[typing.List[TestCaseHiddenGrade.Validators.PassedValidator]] = []

        @classmethod
        def root(
            cls, *, pre: bool = False
        ) -> typing.Callable[
            [TestCaseHiddenGrade.Validators._RootValidator], TestCaseHiddenGrade.Validators._RootValidator
        ]:
            def decorator(
                validator: TestCaseHiddenGrade.Validators._RootValidator,
            ) -> TestCaseHiddenGrade.Validators._RootValidator:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["passed"], *, pre: bool = False
        ) -> typing.Callable[
            [TestCaseHiddenGrade.Validators.PassedValidator], TestCaseHiddenGrade.Validators.PassedValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "passed":
                    if pre:
                        cls._passed_pre_validators.append(validator)
                    else:
                        cls._passed_post_validators.append(validator)
                return validator

            return decorator

        class PassedValidator(typing_extensions.Protocol):
            def __call__(self, __v: bool, __values: TestCaseHiddenGrade.Partial) -> bool:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: TestCaseHiddenGrade.Partial) -> TestCaseHiddenGrade.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: TestCaseHiddenGrade.Partial) -> TestCaseHiddenGrade.Partial:
        for validator in TestCaseHiddenGrade.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: TestCaseHiddenGrade.Partial) -> TestCaseHiddenGrade.Partial:
        for validator in TestCaseHiddenGrade.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("passed", pre=True)
    def _pre_validate_passed(cls, v: bool, values: TestCaseHiddenGrade.Partial) -> bool:
        for validator in TestCaseHiddenGrade.Validators._passed_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("passed", pre=False)
    def _post_validate_passed(cls, v: bool, values: TestCaseHiddenGrade.Partial) -> bool:
        for validator in TestCaseHiddenGrade.Validators._passed_post_validators:
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
        extra = pydantic.Extra.forbid
