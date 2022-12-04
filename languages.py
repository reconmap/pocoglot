
class Php8:

    @staticmethod
    def map_type(type_name: str) -> str:
        mapping = {
                "integer": "int",
                "boolean": "bool",
                "string": "string",
                "float": "float",
        }
        return mapping[type_name]
