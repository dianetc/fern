import { DeclaredErrorName, ErrorDeclaration } from "@fern-fern/ir-model/errors";
import { DeclaredServiceName } from "@fern-fern/ir-model/services/commons";
import { HttpEndpoint } from "@fern-fern/ir-model/services/http";
import { DeclaredTypeName, TypeReference } from "@fern-fern/ir-model/types";
import { ExpressionReferenceNode, TypeReferenceNode, Zurg } from "@fern-typescript/commons-v2";
import { ts } from "ts-morph";
import { ParsedAuthSchemes } from "./ParsedAuthSchemes";
import { ParsedEnvironments } from "./ParsedEnvironments";
import { ParsedGlobalHeaders } from "./ParsedGlobalHeaders";
import { Reference } from "./Reference";
import { TypeContext } from "./TypeContext";

export interface SdkFile extends TypeContext {
    // types
    convertExpressionToString: (expression: ts.Expression, type: TypeReference) => ExpressionReferenceNode;

    // schemas
    getReferenceToRawType: (typeReference: TypeReference) => TypeReferenceNode;
    getReferenceToRawNamedType: (typeReference: DeclaredTypeName) => Reference;
    getSchemaOfTypeReference: (typeReference: TypeReference) => Zurg.Schema;
    getSchemaOfNamedType: (typeName: DeclaredTypeName) => Zurg.Schema;

    // errors
    getErrorDeclaration: (errorName: DeclaredErrorName) => ErrorDeclaration;
    getReferenceToError: (errorName: DeclaredErrorName) => Reference;
    getReferenceToRawError: (errorName: DeclaredErrorName) => Reference;
    getErrorSchema: (errorName: DeclaredErrorName) => Zurg.Schema;

    // services
    getReferenceToService: (serviceName: DeclaredServiceName, options: { importAlias: string }) => Reference;
    getReferenceToEndpointFileExport: (
        serviceName: DeclaredServiceName,
        endpoint: HttpEndpoint,
        export_: string | string[]
    ) => Reference;
    getReferenceToEndpointSchemaFileExport: (
        serviceName: DeclaredServiceName,
        endpoint: HttpEndpoint,
        export_: string | string[]
    ) => Reference;

    // misc
    authSchemes: ParsedAuthSchemes;
    environments: ParsedEnvironments | undefined;
    globalHeaders: ParsedGlobalHeaders;
}
