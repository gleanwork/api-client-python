"""Tests for the XGlean hook that sets X-Glean headers."""

import os
from unittest.mock import Mock

import httpx
import pytest

from src.glean.api_client._hooks.x_glean import XGlean
from src.glean.api_client._hooks.types import BeforeRequestContext, HookContext
from src.glean.api_client.sdkconfiguration import SDKConfiguration


def create_mock_request() -> httpx.Request:
    """Create a mock HTTP request for testing."""
    return httpx.Request("GET", "https://example.com/api/test")


def create_mock_context(
    exclude_deprecated_after: str = None,
    include_experimental: bool = None,
) -> BeforeRequestContext:
    """Create a mock BeforeRequestContext with the given SDK configuration options."""
    config = Mock(spec=SDKConfiguration)
    config.exclude_deprecated_after = exclude_deprecated_after
    config.include_experimental = include_experimental

    hook_ctx = Mock(spec=HookContext)
    hook_ctx.config = config
    hook_ctx.base_url = "https://example.com"
    hook_ctx.operation_id = "test-operation"
    hook_ctx.oauth2_scopes = None
    hook_ctx.security_source = None

    context = BeforeRequestContext(hook_ctx)
    return context


class TestXGleanHook:
    """Test cases for the XGlean hook."""

    @pytest.fixture(autouse=True)
    def clear_env_vars(self):
        """Clear X-Glean environment variables before and after each test."""
        # Store original values
        original_deprecated = os.environ.get("X_GLEAN_EXCLUDE_DEPRECATED_AFTER")
        original_experimental = os.environ.get("X_GLEAN_INCLUDE_EXPERIMENTAL")

        # Clear for test
        os.environ.pop("X_GLEAN_EXCLUDE_DEPRECATED_AFTER", None)
        os.environ.pop("X_GLEAN_INCLUDE_EXPERIMENTAL", None)

        yield

        # Restore original values
        if original_deprecated is not None:
            os.environ["X_GLEAN_EXCLUDE_DEPRECATED_AFTER"] = original_deprecated
        else:
            os.environ.pop("X_GLEAN_EXCLUDE_DEPRECATED_AFTER", None)

        if original_experimental is not None:
            os.environ["X_GLEAN_INCLUDE_EXPERIMENTAL"] = original_experimental
        else:
            os.environ.pop("X_GLEAN_INCLUDE_EXPERIMENTAL", None)

    def test_no_headers_when_neither_options_nor_env_vars_set(self):
        """Should not set any X-Glean headers when nothing is configured."""
        hook = XGlean()
        request = create_mock_request()
        context = create_mock_context()

        result = hook.before_request(context, request)

        assert "X-Glean-Exclude-Deprecated-After" not in result.headers
        assert "X-Glean-Experimental" not in result.headers

    def test_sets_deprecated_header_from_sdk_option(self):
        """Should set X-Glean-Exclude-Deprecated-After header from SDK option."""
        hook = XGlean()
        request = create_mock_request()
        context = create_mock_context(exclude_deprecated_after="2026-10-15")

        result = hook.before_request(context, request)

        assert result.headers.get("X-Glean-Exclude-Deprecated-After") == "2026-10-15"

    def test_sets_experimental_header_when_include_experimental_is_true(self):
        """Should set X-Glean-Experimental header when includeExperimental is True."""
        hook = XGlean()
        request = create_mock_request()
        context = create_mock_context(include_experimental=True)

        result = hook.before_request(context, request)

        assert result.headers.get("X-Glean-Experimental") == "true"

    def test_no_experimental_header_when_include_experimental_is_false(self):
        """Should not set X-Glean-Experimental header when includeExperimental is False."""
        hook = XGlean()
        request = create_mock_request()
        context = create_mock_context(include_experimental=False)

        result = hook.before_request(context, request)

        assert "X-Glean-Experimental" not in result.headers

    def test_sets_both_headers_when_both_options_provided(self):
        """Should set both headers when both options are provided."""
        hook = XGlean()
        request = create_mock_request()
        context = create_mock_context(
            exclude_deprecated_after="2026-10-15",
            include_experimental=True,
        )

        result = hook.before_request(context, request)

        assert result.headers.get("X-Glean-Exclude-Deprecated-After") == "2026-10-15"
        assert result.headers.get("X-Glean-Experimental") == "true"

    def test_sets_deprecated_header_from_env_var(self):
        """Should set X-Glean-Exclude-Deprecated-After header from environment variable."""
        os.environ["X_GLEAN_EXCLUDE_DEPRECATED_AFTER"] = "2027-01-01"

        hook = XGlean()
        request = create_mock_request()
        context = create_mock_context()

        result = hook.before_request(context, request)

        assert result.headers.get("X-Glean-Exclude-Deprecated-After") == "2027-01-01"

    def test_sets_experimental_header_from_env_var(self):
        """Should set X-Glean-Experimental header from environment variable."""
        os.environ["X_GLEAN_INCLUDE_EXPERIMENTAL"] = "true"

        hook = XGlean()
        request = create_mock_request()
        context = create_mock_context()

        result = hook.before_request(context, request)

        assert result.headers.get("X-Glean-Experimental") == "true"

    def test_sets_both_headers_from_env_vars(self):
        """Should set both headers from environment variables."""
        os.environ["X_GLEAN_EXCLUDE_DEPRECATED_AFTER"] = "2027-06-15"
        os.environ["X_GLEAN_INCLUDE_EXPERIMENTAL"] = "true"

        hook = XGlean()
        request = create_mock_request()
        context = create_mock_context()

        result = hook.before_request(context, request)

        assert result.headers.get("X-Glean-Exclude-Deprecated-After") == "2027-06-15"
        assert result.headers.get("X-Glean-Experimental") == "true"

    def test_env_var_takes_precedence_for_deprecated(self):
        """Environment variable should take precedence over SDK option for deprecated."""
        os.environ["X_GLEAN_EXCLUDE_DEPRECATED_AFTER"] = "2027-12-31"

        hook = XGlean()
        request = create_mock_request()
        context = create_mock_context(exclude_deprecated_after="2026-01-01")

        result = hook.before_request(context, request)

        assert result.headers.get("X-Glean-Exclude-Deprecated-After") == "2027-12-31"

    def test_env_var_takes_precedence_for_experimental(self):
        """Environment variable should take precedence over SDK option for experimental."""
        os.environ["X_GLEAN_INCLUDE_EXPERIMENTAL"] = "true"

        hook = XGlean()
        request = create_mock_request()
        context = create_mock_context(include_experimental=False)

        result = hook.before_request(context, request)

        assert result.headers.get("X-Glean-Experimental") == "true"

    def test_env_vars_take_precedence_for_both_headers(self):
        """Environment variables should take precedence for both headers when all are set."""
        os.environ["X_GLEAN_EXCLUDE_DEPRECATED_AFTER"] = "2028-01-01"
        os.environ["X_GLEAN_INCLUDE_EXPERIMENTAL"] = "true"

        hook = XGlean()
        request = create_mock_request()
        context = create_mock_context(
            exclude_deprecated_after="2026-06-01",
            include_experimental=False,
        )

        result = hook.before_request(context, request)

        assert result.headers.get("X-Glean-Exclude-Deprecated-After") == "2028-01-01"
        assert result.headers.get("X-Glean-Experimental") == "true"

    def test_preserves_existing_headers(self):
        """Should preserve existing headers when adding X-Glean headers."""
        hook = XGlean()
        request = httpx.Request(
            "GET",
            "https://example.com/api/test",
            headers={"Authorization": "Bearer token", "Content-Type": "application/json"},
        )
        context = create_mock_context(
            exclude_deprecated_after="2026-10-15",
            include_experimental=True,
        )

        result = hook.before_request(context, request)

        assert result.headers.get("Authorization") == "Bearer token"
        assert result.headers.get("Content-Type") == "application/json"
        assert result.headers.get("X-Glean-Exclude-Deprecated-After") == "2026-10-15"
        assert result.headers.get("X-Glean-Experimental") == "true"

    def test_returns_httpx_request_instance(self):
        """Should return an httpx.Request instance."""
        hook = XGlean()
        request = create_mock_request()
        context = create_mock_context(include_experimental=True)

        result = hook.before_request(context, request)

        assert isinstance(result, httpx.Request)

    def test_preserves_request_method_and_url(self):
        """Should preserve the original request method and URL."""
        hook = XGlean()
        request = httpx.Request("POST", "https://api.example.com/v1/search")
        context = create_mock_context(include_experimental=True)

        result = hook.before_request(context, request)

        assert result.method == "POST"
        assert str(result.url) == "https://api.example.com/v1/search"


if __name__ == "__main__":
    pytest.main([__file__])
