
from subprocess import run
import copy

TYPE_MAPPING = {
        "integer": "int",
        "boolean": "bool",
        "string": "string",
        "float": "float32", # @todo float64
        None: "interface{}",
}

def modify_data(data: dict) -> dict:
    new_data = copy.deepcopy(data) 
    for index, prop in enumerate(new_data["props"]):
        new_data["props"][index]["type"] = map_type(prop["type"])
        new_data["props"][index]["name"] = format_variable_name(prop["name"])
    return new_data

def map_type(type_name: str) -> str:
    return TYPE_MAPPING[type_name]

def format_variable_name(name: str) -> str:
    if "id" == name:
        return "ID"
    return ''.join([part.capitalize() for part in name.split('_')])

def is_valid(file_name: str) -> bool:
    proc = run(['gofmt', '-e', file_name]) 
    return proc.returncode == 0
