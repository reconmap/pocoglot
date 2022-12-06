
from subprocess import run

TYPE_MAPPING = {
        "integer": "int",
        "boolean": "bool",
        "string": "str",
        "float": "float",
}

def modify_data(data: dict) -> dict:
    return data

def map_type(type_name: str) -> str:
    return TYPE_MAPPING[type_name]

def is_valid(file_name: str) -> bool:
    proc = run(['python3', '-m', 'py_compile', file_name]) 
    return proc.returncode == 0
