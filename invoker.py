import sys
from typing import List
import requests
from requests.exceptions import RequestException

from endpoint import Endpoint
from load_endpoints import load

request_methods = {
    'GET': requests.get,
    'POST': requests.post,
    'PUT': requests.put,
    'PATCH': requests.patch,
    'DELETE': requests.delete
}

def send_request(e: Endpoint, host: str) -> requests.Response:
    if e.httpMethod not in request_methods:
        print(f"Unsupported method {e.httpMethod} for {e.url}. Skipping.")
        raise RequestException(f"Unsupported method {e.httpMethod}")
    
    url = host + e.url
    timeout = e.timeout if e.timeout and e.timeout > 1 else 5
    if e.body:
        return request_methods[e.httpMethod](url, json=body_2_json(e.body), timeout=timeout)
    if e.formBody:
        return request_methods[e.httpMethod](url, data=e.formBody, timeout=timeout)
    
    return request_methods[e.httpMethod](url, timeout=timeout)


def body_2_json(body: List[str]):
    data_dict = {}
    for item in body:
        key, value = item.split(": ", 1)
        value_trimmed = value.strip()
        if value_trimmed.startswith('[') and value_trimmed.endswith(']'):
            items = value_trimmed[1:-1]
            if items:
                data_dict[str(key)] = list(items.split(","))
            else:
                data_dict[str(key)] = []
        else:
            data_dict[str(key)] = str(value)

    return data_dict


def ping_endpoints(endpoints: List[Endpoint], host: str):
    for endpoint in endpoints:
        try:
            times = endpoint.times
            if times is None or times < 1 :
                print(f"Warning: {endpoint.url} ({endpoint.httpMethod}) has times set to {times}. Skipping.")
                continue
            for _ in range(times):
                response = send_request(endpoint, host)
                print(response.text)
                print(response.request.body)
                if response.status_code == 200:
                    print(f"Success: {endpoint.url} ({endpoint.httpMethod}) returned status code 200")
                else:
                    print(f"Warning: {endpoint.url} ({endpoint.httpMethod}) returned status code {response.status_code}")

        except RequestException as e:
            print(f"Error: Could not reach {endpoint.url} ({endpoint.httpMethod}) - {e}")
        print()


def main():
    if len(sys.argv) != 3:
        print("Usage: python invoker.py <file_path> <host>")
        sys.exit(1)

    file_path = sys.argv[1]
    host = sys.argv[2]
    endpoints = load(file_path)
    ping_endpoints(endpoints, host)


if __name__ == '__main__':
    main()
