
from subprocess import run

TYPE_MAPPING = {
        "integer": "int",
        "boolean": "bool",
        "string": "string",
        "float": "float32", # @todo float64
}

def map_type(type_name: str) -> str:
    return TYPE_MAPPING[type_name]

def is_valid(file_name: str) -> bool:
    proc = run(['gofmt', '-e', file_name]) 
    return proc.returncode == 0
