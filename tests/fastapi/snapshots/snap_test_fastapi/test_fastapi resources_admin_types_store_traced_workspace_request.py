# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...submission.types.trace_response import TraceResponse
from ...submission.types.workspace_run_details import WorkspaceRunDetails


class StoreTracedWorkspaceRequest(pydantic.BaseModel):
    workspace_run_details: WorkspaceRunDetails = pydantic.Field(alias="workspaceRunDetails")
    trace_responses: typing.List[TraceResponse] = pydantic.Field(
        alias="traceResponses", description=('the trace responses from the "server"\n')
    )

    class Partial(typing_extensions.TypedDict):
        workspace_run_details: typing_extensions.NotRequired[WorkspaceRunDetails]
        trace_responses: typing_extensions.NotRequired[typing.List[TraceResponse]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @StoreTracedWorkspaceRequest.Validators.root()
            def validate(values: StoreTracedWorkspaceRequest.Partial) -> StoreTracedWorkspaceRequest.Partial:
                ...

            @StoreTracedWorkspaceRequest.Validators.field("workspace_run_details")
            def validate_workspace_run_details(workspace_run_details: WorkspaceRunDetails, values: StoreTracedWorkspaceRequest.Partial) -> WorkspaceRunDetails:
                ...

            @StoreTracedWorkspaceRequest.Validators.field("trace_responses")
            def validate_trace_responses(trace_responses: typing.List[TraceResponse], values: StoreTracedWorkspaceRequest.Partial) -> typing.List[TraceResponse]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[StoreTracedWorkspaceRequest.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[StoreTracedWorkspaceRequest.Validators._RootValidator]] = []
        _workspace_run_details_pre_validators: typing.ClassVar[
            typing.List[StoreTracedWorkspaceRequest.Validators.WorkspaceRunDetailsValidator]
        ] = []
        _workspace_run_details_post_validators: typing.ClassVar[
            typing.List[StoreTracedWorkspaceRequest.Validators.WorkspaceRunDetailsValidator]
        ] = []
        _trace_responses_pre_validators: typing.ClassVar[
            typing.List[StoreTracedWorkspaceRequest.Validators.TraceResponsesValidator]
        ] = []
        _trace_responses_post_validators: typing.ClassVar[
            typing.List[StoreTracedWorkspaceRequest.Validators.TraceResponsesValidator]
        ] = []

        @classmethod
        def root(
            cls, *, pre: bool = False
        ) -> typing.Callable[
            [StoreTracedWorkspaceRequest.Validators._RootValidator],
            StoreTracedWorkspaceRequest.Validators._RootValidator,
        ]:
            def decorator(
                validator: StoreTracedWorkspaceRequest.Validators._RootValidator,
            ) -> StoreTracedWorkspaceRequest.Validators._RootValidator:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["workspace_run_details"], *, pre: bool = False
        ) -> typing.Callable[
            [StoreTracedWorkspaceRequest.Validators.WorkspaceRunDetailsValidator],
            StoreTracedWorkspaceRequest.Validators.WorkspaceRunDetailsValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["trace_responses"], *, pre: bool = False
        ) -> typing.Callable[
            [StoreTracedWorkspaceRequest.Validators.TraceResponsesValidator],
            StoreTracedWorkspaceRequest.Validators.TraceResponsesValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "workspace_run_details":
                    if pre:
                        cls._workspace_run_details_pre_validators.append(validator)
                    else:
                        cls._workspace_run_details_post_validators.append(validator)
                if field_name == "trace_responses":
                    if pre:
                        cls._trace_responses_pre_validators.append(validator)
                    else:
                        cls._trace_responses_post_validators.append(validator)
                return validator

            return decorator

        class WorkspaceRunDetailsValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: WorkspaceRunDetails, __values: StoreTracedWorkspaceRequest.Partial
            ) -> WorkspaceRunDetails:
                ...

        class TraceResponsesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[TraceResponse], __values: StoreTracedWorkspaceRequest.Partial
            ) -> typing.List[TraceResponse]:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: StoreTracedWorkspaceRequest.Partial) -> StoreTracedWorkspaceRequest.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: StoreTracedWorkspaceRequest.Partial) -> StoreTracedWorkspaceRequest.Partial:
        for validator in StoreTracedWorkspaceRequest.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: StoreTracedWorkspaceRequest.Partial) -> StoreTracedWorkspaceRequest.Partial:
        for validator in StoreTracedWorkspaceRequest.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("workspace_run_details", pre=True)
    def _pre_validate_workspace_run_details(
        cls, v: WorkspaceRunDetails, values: StoreTracedWorkspaceRequest.Partial
    ) -> WorkspaceRunDetails:
        for validator in StoreTracedWorkspaceRequest.Validators._workspace_run_details_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("workspace_run_details", pre=False)
    def _post_validate_workspace_run_details(
        cls, v: WorkspaceRunDetails, values: StoreTracedWorkspaceRequest.Partial
    ) -> WorkspaceRunDetails:
        for validator in StoreTracedWorkspaceRequest.Validators._workspace_run_details_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("trace_responses", pre=True)
    def _pre_validate_trace_responses(
        cls, v: typing.List[TraceResponse], values: StoreTracedWorkspaceRequest.Partial
    ) -> typing.List[TraceResponse]:
        for validator in StoreTracedWorkspaceRequest.Validators._trace_responses_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("trace_responses", pre=False)
    def _post_validate_trace_responses(
        cls, v: typing.List[TraceResponse], values: StoreTracedWorkspaceRequest.Partial
    ) -> typing.List[TraceResponse]:
        for validator in StoreTracedWorkspaceRequest.Validators._trace_responses_post_validators:
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
