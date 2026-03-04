"""Hook to normalize server URLs, prepending https:// if no scheme is provided."""

import re
from typing import Tuple
from .types import SDKInitHook
from glean.api_client.httpclient import HttpClient


def normalize_server_url(url: str) -> str:
    normalized = url
    if not re.match(r'^https?://', normalized, re.IGNORECASE):
        normalized = f'https://{normalized}'
    normalized = normalized.rstrip('/')
    return normalized


class ServerURLNormalizerHook(SDKInitHook):
    """Normalizes server URLs by prepending https:// if no scheme is provided."""

    def sdk_init(self, base_url: str, client: HttpClient) -> Tuple[str, HttpClient]:
        return normalize_server_url(base_url), client
