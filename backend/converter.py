import yaml
from typing import Any


def convert_json_to_yaml(data: Any) -> str:
    try:
        yaml_data = yaml.dump(data, allow_unicode=True)
        return yaml_data
    except Exception as e:
        raise ValueError(f"Error converting to YAML: {str(e)}")
