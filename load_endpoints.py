from typing import List
import yaml

from endpoint import Endpoint

def load_file(path: str) -> str:
    try:
        with open(path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def load(path: str) -> List[Endpoint]:
    print(f"Loading endpoints from {path}...")
    content = load_file(path)
    endpoints = content.get('endpoints', [])
    result = []
    for endpoint in endpoints:
        result.append(Endpoint(**endpoint))
    return result
