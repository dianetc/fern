import { constructHttpPath } from "@fern-api/ir-generator";
import { RawSchemas } from "@fern-api/yaml-schema";
import chalk from "chalk";
import capitalize from "lodash-es/capitalize";
import { Rule, RuleViolation } from "../../Rule";

export const NoUndefinedPathParametersRule: Rule = {
    name: "no-undefined-path-parameters",
    create: () => {
        return {
            serviceFile: {
                httpService: ({ service }) => {
                    return getPathParameterRuleViolations({
                        path: service["base-path"],
                        pathParameters: service["path-parameters"] ?? {},
                        pathType: "service",
                    });
                },
                httpEndpoint: ({ endpoint }) => {
                    return getPathParameterRuleViolations({
                        path: endpoint.path,
                        pathParameters: endpoint["path-parameters"] ?? {},
                        pathType: "endpoint",
                    });
                },
            },
        };
    },
};

function getPathParameterRuleViolations({
    path,
    pathParameters,
    pathType,
}: {
    path: string;
    pathParameters: Record<string, RawSchemas.HttpPathParameterSchema>;
    pathType: "service" | "endpoint";
}): RuleViolation[] {
    const errors: RuleViolation[] = [];

    const urlPathParameters = new Set();
    const httpPath = constructHttpPath(path);
    httpPath.parts.forEach((part) => {
        if (urlPathParameters.has(part.pathParameter)) {
            errors.push({
                severity: "error",
                message: `${capitalize(pathType)} has duplicate path parameter: ${chalk.bold(part.pathParameter)}.`,
            });
        }
        urlPathParameters.add(part.pathParameter);
    });

    const definedPathParameters = new Set(Object.keys(pathParameters));

    // path parameters present in the url but are not defined
    const undefinedPathParameters = getDifference(urlPathParameters, definedPathParameters);
    undefinedPathParameters.forEach((pathParameter) => {
        errors.push({
            severity: "error",
            message: `${capitalize(pathType)} has missing path-parameter: ${chalk.bold(pathParameter)}.`,
        });
    });

    // path parameters that are defined but not present in the url
    const missingUrlPathParameters = getDifference(definedPathParameters, urlPathParameters);
    missingUrlPathParameters.forEach((pathParameter) => {
        errors.push({
            severity: "error",
            message: `Path parameter is unreferenced in ${pathType}: ${chalk.bold(pathParameter)}.`,
        });
    });

    return errors;
}

function getDifference<T>(setA: Set<T>, setB: Set<T>): Set<T> {
    return new Set([...setA].filter((element) => !setB.has(element)));
}
