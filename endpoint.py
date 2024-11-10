from dataclasses import dataclass, field
from typing import Optional, List
from enum import Enum

class HttpMethod(Enum):
    GET = 'GET',
    POST = 'POST',
    PUT = 'PUT',
    PATCH = 'PATCH',
    DELETE = 'DELETE'

@dataclass
class Endpoint:
    url: str
    httpMethod: HttpMethod

    body: Optional[List[str]] = None
    formBody: Optional[List[str]] = None
    times: Optional[int] = 1
    timeout: Optional[int] = 5
