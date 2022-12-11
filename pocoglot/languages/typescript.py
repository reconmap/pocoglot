
import copy
from subprocess import run

TYPE_MAPPING = {
    "integer": "number",
    "boolean": "boolean",
    "string": "string",
    "float": "number",
    None: "any",
}


def modify_data(data: dict) -> dict:
    new_data = copy.deepcopy(data)
    for index, prop in enumerate(new_data["props"]):
        nullable_affix = '?' if "nullable" in prop and prop["nullable"] else ""
        new_data["props"][index]["raw_name"] = new_data["props"][index]["name"]
        new_data["props"][index]["type"] = map_type(prop["type"])
        new_data["props"][index]["name"] = prop["name"] + nullable_affix
        if "default" in prop:
            new_data["props"][index]["default"] = format_value(prop["default"], prop["type"])
    return new_data


def map_type(type_name: str) -> str:
    return TYPE_MAPPING[type_name]


def format_value(value, prop_type) -> str:
    if type(value) == bool:
        return "true" if value else "false"

    if value is None:
        return "null" if prop_type not in ["number", "string"] else "undefined"

    return value


def is_valid(file_name: str) -> bool:
    return True
