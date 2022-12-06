
from subprocess import run
import copy

TYPE_MAPPING = {
        "integer": "number",
        "boolean": "boolean",
        "string": "string",
        "float": "number",
}

def modify_data(data: dict) -> dict:
    new_data = copy.deepcopy(data) 
    for index, prop in enumerate(new_data["props"]):
        nullable_affix = '?' if "nullable" in prop and prop["nullable"] else ""
        new_data["props"][index]["type"] = map_type(prop["type"])
        new_data["props"][index]["name"] = prop["name"] + nullable_affix
        if "default" in prop:
            new_data["props"][index]["default"] = format_value(prop["default"])
    return new_data

def map_type(type_name: str) -> str:
    return TYPE_MAPPING[type_name]

def format_value(value) -> str:
    if type(value) == bool:
        return value

    if value is None:
        return "null"

    return value

def is_valid(file_name: str) -> bool:
    return True
