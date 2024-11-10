import json
import sys
from typing import Dict, List
import requests
from requests.exceptions import RequestException

from endpoint import Endpoint
from load_endpoints import load

def send_request(e: Endpoint, host: str) -> requests.Response:
    request_methods = {
        'GET': requests.get,
        'POST': requests.post,
        'PUT': requests.put,
        'PATCH': requests.patch,
        'DELETE': requests.delete
    }

    if e.httpMethod not in request_methods:
        print(f"Unsupported method {e.httpMethod} for {e.url}. Skipping.")
        raise RequestException(f"Unsupported method {e.httpMethod}")
    
    url = host + e.url
    if e.body:
        return request_methods[e.httpMethod](url, json=body_2_json(e.body), timeout=e.timeout)
    if e.formBody:
        return request_methods[e.httpMethod](url, data=e.formBody, timeout=e.timeout)
    
    return request_methods[e.httpMethod](url, timeout=e.timeout)


def body_2_json(body: List[str]):
    data_dict = {}
    for item in body:
        key, value = item.split(": ", 1)
        data_dict[str(key)] = str(value)

    return data_dict


def ping_endpoints(endpoints: List[Endpoint], host: str):
    for endpoint in endpoints:
        try:
            response = send_request(endpoint, host)
            if response.status_code == 200:
                print(f"Success: {endpoint.url} ({endpoint.httpMethod}) returned status code 200")
            else:
                print(f"Warning: {endpoint.url} ({endpoint.httpMethod}) returned status code {response.status_code}")

        except RequestException as e:
            print(f"Error: Could not reach {endpoint.url} ({endpoint.httpMethod}) - {e}")
        print()


def main():
    if len(sys.argv) < 2:
        print("Usage: python open_file.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    endpoints = load(file_path)
    ping_endpoints(endpoints, 'http://localhost:8080')


if __name__ == '__main__':
    main()
