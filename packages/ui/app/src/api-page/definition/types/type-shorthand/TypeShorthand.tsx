import { FernRegistry } from "@fern-fern/registry";
import { ReferencedTypePreviewPart } from "./ReferencedTypePreviewPart";

export declare namespace TypeShorthand {
    export interface Props {
        type: FernRegistry.TypeReference;
        plural: boolean;
    }
}

export const TypeShorthand: React.FC<TypeShorthand.Props> = ({ type, plural }) => {
    return (
        <>
            {type._visit<JSX.Element | string>({
                id: (typeId) => <ReferencedTypePreviewPart typeId={typeId} plural={plural} />,
                primitive: (primitive) => {
                    return primitive._visit({
                        string: () => (plural ? "strings" : "string"),
                        integer: () => (plural ? "integers" : "integer"),
                        double: () => (plural ? "doubles" : "double"),
                        long: () => (plural ? "longs" : "long"),
                        boolean: () => (plural ? "booleans" : "boolean"),
                        datetime: () => (plural ? "datetimes" : "datetime"),
                        uuid: () => (plural ? "UUIDs" : "UUID"),
                        _other: () => "<unknown>",
                    });
                },
                optional: ({ itemType }) => (
                    <>
                        {"optional "}
                        <TypeShorthand type={itemType} plural={plural} />
                    </>
                ),
                list: ({ itemType }) => {
                    return (
                        <>
                            {plural ? "lists of " : "list of "}
                            <TypeShorthand type={itemType} plural />
                        </>
                    );
                },
                set: ({ itemType }) => {
                    return (
                        <>
                            {plural ? "sets of " : "set of "}
                            <TypeShorthand type={itemType} plural />
                        </>
                    );
                },
                map: ({ keyType, valueType }) => {
                    return (
                        <>
                            {plural ? "maps from " : "map from "}
                            <TypeShorthand type={keyType} plural />
                            {" to "}
                            <TypeShorthand type={valueType} plural />
                        </>
                    );
                },
                unknown: () => "any",
                _other: () => "<unknown>",
            })}
        </>
    );
};