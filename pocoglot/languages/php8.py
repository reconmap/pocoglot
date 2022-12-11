
from subprocess import run
import copy

TYPE_MAPPING = {
        "integer": "int",
        "boolean": "bool",
        "string": "string",
        "float": "float",
        None: "mixed",
}

def modify_data(data: dict) -> dict:
    new_data = copy.deepcopy(data) 
    for index, prop in enumerate(new_data["props"]):
        nullable_prefix = '?' if "nullable" in prop and prop["nullable"] else ""
        new_data["props"][index]["type"] = nullable_prefix + map_type(prop["type"])
        if "default" in prop:
            new_data["props"][index]["default"] = format_value(prop["default"])
    return new_data

def map_type(type_name: str) -> str:
    return TYPE_MAPPING[type_name]

def format_value(value) -> str:
    if type(value) == bool:
        return "true" if value else "false"

    if value is None:
        return "null"

    return value

def is_valid(file_name: str) -> bool:
    proc = run(['php', '-l', file_name])
    return proc.returncode == 0
