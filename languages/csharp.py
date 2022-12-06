
from subprocess import run

TYPE_MAPPING = {
        "integer": "int",
        "boolean": "bool",
        "string": "string",
        "float": "float",
}

def modify_data(data: dict) -> dict:
    return data

def map_type(type_name: str) -> str:
    return TYPE_MAPPING[type_name]

def is_valid(file_name: str) -> bool:
    return True

