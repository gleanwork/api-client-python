"""Tests for the server URL normalizer hook."""

from unittest.mock import Mock

import pytest

from src.glean.api_client._hooks.server_url_normalizer import (
    ServerURLNormalizerHook,
    normalize_server_url,
)
from src.glean.api_client.httpclient import HttpClient


class TestNormalizeServerUrl:
    """Test cases for the normalize_server_url function."""

    def test_no_scheme_prepends_https(self):
        assert normalize_server_url("example.glean.com") == "https://example.glean.com"

    def test_https_preserved(self):
        assert normalize_server_url("https://example.glean.com") == "https://example.glean.com"

    def test_http_localhost_preserved(self):
        assert normalize_server_url("http://localhost:8080") == "http://localhost:8080"

    def test_http_non_localhost_preserved(self):
        assert normalize_server_url("http://example.glean.com") == "http://example.glean.com"

    def test_trailing_slash_stripped(self):
        assert normalize_server_url("https://example.glean.com/") == "https://example.glean.com"

    def test_multiple_trailing_slashes_stripped(self):
        assert normalize_server_url("https://example.glean.com///") == "https://example.glean.com"

    def test_no_scheme_with_trailing_slash(self):
        assert normalize_server_url("example.glean.com/") == "https://example.glean.com"

    def test_url_with_path(self):
        assert normalize_server_url("https://example.glean.com/api/v1") == "https://example.glean.com/api/v1"

    def test_url_with_path_and_trailing_slash(self):
        assert normalize_server_url("https://example.glean.com/api/v1/") == "https://example.glean.com/api/v1"

    def test_no_scheme_with_path(self):
        assert normalize_server_url("example.glean.com/api/v1") == "https://example.glean.com/api/v1"

    def test_case_insensitive_scheme(self):
        assert normalize_server_url("HTTPS://example.glean.com") == "HTTPS://example.glean.com"
        assert normalize_server_url("HTTP://localhost") == "HTTP://localhost"


class TestServerURLNormalizerHook:
    """Test cases for the ServerURLNormalizerHook."""

    def setup_method(self):
        self.hook = ServerURLNormalizerHook()
        self.mock_client = Mock(spec=HttpClient)

    def test_sdk_init_normalizes_url(self):
        result_url, result_client = self.hook.sdk_init("example.glean.com", self.mock_client)
        assert result_url == "https://example.glean.com"
        assert result_client == self.mock_client

    def test_sdk_init_preserves_client(self):
        result_url, result_client = self.hook.sdk_init("https://example.glean.com", self.mock_client)
        assert result_url == "https://example.glean.com"
        assert result_client is self.mock_client


if __name__ == "__main__":
    pytest.main([__file__])
