# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .submission_id import SubmissionId


class StderrResponse(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")
    stderr: str

    class Partial(typing_extensions.TypedDict):
        submission_id: typing_extensions.NotRequired[SubmissionId]
        stderr: typing_extensions.NotRequired[str]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @StderrResponse.Validators.root()
            def validate(values: StderrResponse.Partial) -> StderrResponse.Partial:
                ...

            @StderrResponse.Validators.field("submission_id")
            def validate_submission_id(submission_id: SubmissionId, values: StderrResponse.Partial) -> SubmissionId:
                ...

            @StderrResponse.Validators.field("stderr")
            def validate_stderr(stderr: str, values: StderrResponse.Partial) -> str:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[StderrResponse.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[StderrResponse.Validators._RootValidator]] = []
        _submission_id_pre_validators: typing.ClassVar[
            typing.List[StderrResponse.Validators.SubmissionIdValidator]
        ] = []
        _submission_id_post_validators: typing.ClassVar[
            typing.List[StderrResponse.Validators.SubmissionIdValidator]
        ] = []
        _stderr_pre_validators: typing.ClassVar[typing.List[StderrResponse.Validators.StderrValidator]] = []
        _stderr_post_validators: typing.ClassVar[typing.List[StderrResponse.Validators.StderrValidator]] = []

        @classmethod
        def root(
            cls, *, pre: bool = False
        ) -> typing.Callable[[StderrResponse.Validators._RootValidator], StderrResponse.Validators._RootValidator]:
            def decorator(
                validator: StderrResponse.Validators._RootValidator,
            ) -> StderrResponse.Validators._RootValidator:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["submission_id"], *, pre: bool = False
        ) -> typing.Callable[
            [StderrResponse.Validators.SubmissionIdValidator], StderrResponse.Validators.SubmissionIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["stderr"], *, pre: bool = False
        ) -> typing.Callable[[StderrResponse.Validators.StderrValidator], StderrResponse.Validators.StderrValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    if pre:
                        cls._submission_id_pre_validators.append(validator)
                    else:
                        cls._submission_id_post_validators.append(validator)
                if field_name == "stderr":
                    if pre:
                        cls._stderr_pre_validators.append(validator)
                    else:
                        cls._stderr_post_validators.append(validator)
                return validator

            return decorator

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: SubmissionId, __values: StderrResponse.Partial) -> SubmissionId:
                ...

        class StderrValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: StderrResponse.Partial) -> str:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: StderrResponse.Partial) -> StderrResponse.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: StderrResponse.Partial) -> StderrResponse.Partial:
        for validator in StderrResponse.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: StderrResponse.Partial) -> StderrResponse.Partial:
        for validator in StderrResponse.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("submission_id", pre=True)
    def _pre_validate_submission_id(cls, v: SubmissionId, values: StderrResponse.Partial) -> SubmissionId:
        for validator in StderrResponse.Validators._submission_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("submission_id", pre=False)
    def _post_validate_submission_id(cls, v: SubmissionId, values: StderrResponse.Partial) -> SubmissionId:
        for validator in StderrResponse.Validators._submission_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("stderr", pre=True)
    def _pre_validate_stderr(cls, v: str, values: StderrResponse.Partial) -> str:
        for validator in StderrResponse.Validators._stderr_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("stderr", pre=False)
    def _post_validate_stderr(cls, v: str, values: StderrResponse.Partial) -> str:
        for validator in StderrResponse.Validators._stderr_post_validators:
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
        extra = pydantic.Extra.forbid
