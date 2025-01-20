import yaml
from typing import Any


def convert_json_to_yaml(data: Any) -> str:
    try:
        return yaml.dump(data, allow_unicode=True)
    except Exception as e:
        raise ValueError(f"Error converting to YAML: {str(e)}")


def convert_yaml_to_json(data: str) -> Any:
    try:
        return yaml.safe_load(data)
    except Exception as e:
        raise ValueError(f"Error converting to JSON: {str(e)}")
