
from subprocess import run

TYPE_MAPPING = {
        "integer": "int",
        "char": "char",
        "boolean": "boolean",
        "string": "String",
        "float": "float",
}

def map_type(type_name: str) -> str:
    return TYPE_MAPPING[type_name]

def is_valid(file_name: str) -> bool:
    return True

