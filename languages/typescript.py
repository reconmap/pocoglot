
from subprocess import run

TYPE_MAPPING = {
        "integer": "number",
        "boolean": "boolean",
        "string": "string",
        "float": "number",
}

def map_type(type_name: str) -> str:
    return TYPE_MAPPING[type_name]

def is_valid(file_name: str) -> bool:
    return True
