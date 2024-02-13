/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as SeedTrace from "../../..";

export type ErrorInfo =
    | SeedTrace.ErrorInfo.CompileError
    /**
     * If the submission cannot be executed and throws a runtime error before getting to any of the testcases.
     *  */
    | SeedTrace.ErrorInfo.RuntimeError
    /**
     * If the trace backend encounters an unexpected error.
     *  */
    | SeedTrace.ErrorInfo.InternalError
    | SeedTrace.ErrorInfo._Unknown;

export declare namespace ErrorInfo {
    interface CompileError extends SeedTrace.CompileError, _Utils {
        type: "compileError";
    }

    interface RuntimeError extends SeedTrace.RuntimeError, _Utils {
        type: "runtimeError";
    }

    interface InternalError extends SeedTrace.InternalError, _Utils {
        type: "internalError";
    }

    interface _Unknown extends _Utils {
        type: void;
    }

    interface _Utils {
        _visit: <_Result>(visitor: SeedTrace.ErrorInfo._Visitor<_Result>) => _Result;
    }

    interface _Visitor<_Result> {
        compileError: (value: SeedTrace.CompileError) => _Result;
        runtimeError: (value: SeedTrace.RuntimeError) => _Result;
        internalError: (value: SeedTrace.InternalError) => _Result;
        _other: (value: { type: string }) => _Result;
    }
}

export const ErrorInfo = {
    compileError: (value: SeedTrace.CompileError): SeedTrace.ErrorInfo.CompileError => {
        return {
            ...value,
            type: "compileError",
            _visit: function <_Result>(
                this: SeedTrace.ErrorInfo.CompileError,
                visitor: SeedTrace.ErrorInfo._Visitor<_Result>
            ) {
                return SeedTrace.ErrorInfo._visit(this, visitor);
            },
        };
    },

    runtimeError: (value: SeedTrace.RuntimeError): SeedTrace.ErrorInfo.RuntimeError => {
        return {
            ...value,
            type: "runtimeError",
            _visit: function <_Result>(
                this: SeedTrace.ErrorInfo.RuntimeError,
                visitor: SeedTrace.ErrorInfo._Visitor<_Result>
            ) {
                return SeedTrace.ErrorInfo._visit(this, visitor);
            },
        };
    },

    internalError: (value: SeedTrace.InternalError): SeedTrace.ErrorInfo.InternalError => {
        return {
            ...value,
            type: "internalError",
            _visit: function <_Result>(
                this: SeedTrace.ErrorInfo.InternalError,
                visitor: SeedTrace.ErrorInfo._Visitor<_Result>
            ) {
                return SeedTrace.ErrorInfo._visit(this, visitor);
            },
        };
    },

    _unknown: (value: { type: string }): SeedTrace.ErrorInfo._Unknown => {
        return {
            ...(value as any),
            _visit: function <_Result>(
                this: SeedTrace.ErrorInfo._Unknown,
                visitor: SeedTrace.ErrorInfo._Visitor<_Result>
            ) {
                return SeedTrace.ErrorInfo._visit(this, visitor);
            },
        };
    },

    _visit: <_Result>(value: SeedTrace.ErrorInfo, visitor: SeedTrace.ErrorInfo._Visitor<_Result>): _Result => {
        switch (value.type) {
            case "compileError":
                return visitor.compileError(value);
            case "runtimeError":
                return visitor.runtimeError(value);
            case "internalError":
                return visitor.internalError(value);
            default:
                return visitor._other(value as any);
        }
    },
} as const;