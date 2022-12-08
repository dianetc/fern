# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ....commons.language import Language
from .function_implementation import FunctionImplementation


class FunctionImplementationForMultipleLanguages(pydantic.BaseModel):
    code_by_language: typing.Dict[Language, FunctionImplementation] = pydantic.Field(alias="codeByLanguage")

    class Partial(typing_extensions.TypedDict):
        code_by_language: typing_extensions.NotRequired[typing.Dict[Language, FunctionImplementation]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @FunctionImplementationForMultipleLanguages.Validators.root()
            def validate(values: FunctionImplementationForMultipleLanguages.Partial) -> FunctionImplementationForMultipleLanguages.Partial:
                ...

            @FunctionImplementationForMultipleLanguages.Validators.field("code_by_language")
            def validate_code_by_language(code_by_language: typing.Dict[Language, FunctionImplementation], values: FunctionImplementationForMultipleLanguages.Partial) -> typing.Dict[Language, FunctionImplementation]:
                ...
        """

        _pre_validators: typing.ClassVar[
            typing.List[FunctionImplementationForMultipleLanguages.Validators._RootValidator]
        ] = []
        _post_validators: typing.ClassVar[
            typing.List[FunctionImplementationForMultipleLanguages.Validators._RootValidator]
        ] = []
        _code_by_language_pre_validators: typing.ClassVar[
            typing.List[FunctionImplementationForMultipleLanguages.Validators.CodeByLanguageValidator]
        ] = []
        _code_by_language_post_validators: typing.ClassVar[
            typing.List[FunctionImplementationForMultipleLanguages.Validators.CodeByLanguageValidator]
        ] = []

        @classmethod
        def root(
            cls, *, pre: bool = False
        ) -> typing.Callable[
            [FunctionImplementationForMultipleLanguages.Validators._RootValidator],
            FunctionImplementationForMultipleLanguages.Validators._RootValidator,
        ]:
            def decorator(
                validator: FunctionImplementationForMultipleLanguages.Validators._RootValidator,
            ) -> FunctionImplementationForMultipleLanguages.Validators._RootValidator:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["code_by_language"], *, pre: bool = False
        ) -> typing.Callable[
            [FunctionImplementationForMultipleLanguages.Validators.CodeByLanguageValidator],
            FunctionImplementationForMultipleLanguages.Validators.CodeByLanguageValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "code_by_language":
                    if pre:
                        cls._code_by_language_pre_validators.append(validator)
                    else:
                        cls._code_by_language_post_validators.append(validator)
                return validator

            return decorator

        class CodeByLanguageValidator(typing_extensions.Protocol):
            def __call__(
                self,
                __v: typing.Dict[Language, FunctionImplementation],
                __values: FunctionImplementationForMultipleLanguages.Partial,
            ) -> typing.Dict[Language, FunctionImplementation]:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(
                self, __values: FunctionImplementationForMultipleLanguages.Partial
            ) -> FunctionImplementationForMultipleLanguages.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(
        cls, values: FunctionImplementationForMultipleLanguages.Partial
    ) -> FunctionImplementationForMultipleLanguages.Partial:
        for validator in FunctionImplementationForMultipleLanguages.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(
        cls, values: FunctionImplementationForMultipleLanguages.Partial
    ) -> FunctionImplementationForMultipleLanguages.Partial:
        for validator in FunctionImplementationForMultipleLanguages.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("code_by_language", pre=True)
    def _pre_validate_code_by_language(
        cls,
        v: typing.Dict[Language, FunctionImplementation],
        values: FunctionImplementationForMultipleLanguages.Partial,
    ) -> typing.Dict[Language, FunctionImplementation]:
        for validator in FunctionImplementationForMultipleLanguages.Validators._code_by_language_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("code_by_language", pre=False)
    def _post_validate_code_by_language(
        cls,
        v: typing.Dict[Language, FunctionImplementation],
        values: FunctionImplementationForMultipleLanguages.Partial,
    ) -> typing.Dict[Language, FunctionImplementation]:
        for validator in FunctionImplementationForMultipleLanguages.Validators._code_by_language_post_validators:
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
        allow_population_by_field_name = True
