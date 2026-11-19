"""Tests for the XGlean hook that sets X-Glean headers."""

import os
from unittest.mock import Mock

import httpx
import pytest

from src.glean.api_client._hooks.x_glean import (
    XGlean,
    EXCLUDE_DEPRECATED_AFTER_HEADER,
    INCLUDE_EXPERIMENTAL_HEADER,
    EXCLUDE_DEPRECATED_AFTER_ENV_VAR,
    INCLUDE_EXPERIMENTAL_ENV_VAR,
    INCLUDE_BETA_ENV_VAR,
)
from src.glean.api_client import Glean
from src.glean.api_client._hooks.types import BeforeRequestContext, HookContext
from src.glean.api_client.sdkconfiguration import SDKConfiguration


def create_mock_request() -> httpx.Request:
    """Create a mock HTTP request for testing."""
    return httpx.Request("GET", "https://example.com/api/test")


def create_mock_context(
    exclude_deprecated_after: str = None,
    include_experimental: bool = None,
    include_beta: bool = None,
) -> BeforeRequestContext:
    """Create a mock BeforeRequestContext with the given SDK configuration options."""
    config = Mock(spec=SDKConfiguration)
    config.exclude_deprecated_after = exclude_deprecated_after
    config.include_experimental = include_experimental
    config.include_beta = include_beta

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
        original_deprecated = os.environ.get(EXCLUDE_DEPRECATED_AFTER_ENV_VAR)
        original_experimental = os.environ.get(INCLUDE_EXPERIMENTAL_ENV_VAR)
        original_beta = os.environ.get(INCLUDE_BETA_ENV_VAR)

        # Clear for test
        os.environ.pop(EXCLUDE_DEPRECATED_AFTER_ENV_VAR, None)
        os.environ.pop(INCLUDE_EXPERIMENTAL_ENV_VAR, None)
        os.environ.pop(INCLUDE_BETA_ENV_VAR, None)

        yield

        if original_beta is not None:
            os.environ[INCLUDE_BETA_ENV_VAR] = original_beta
        else:
            os.environ.pop(INCLUDE_BETA_ENV_VAR, None)

        # Restore original values
        if original_deprecated is not None:
            os.environ[EXCLUDE_DEPRECATED_AFTER_ENV_VAR] = original_deprecated
        else:
            os.environ.pop(EXCLUDE_DEPRECATED_AFTER_ENV_VAR, None)

        if original_experimental is not None:
            os.environ[INCLUDE_EXPERIMENTAL_ENV_VAR] = original_experimental
        else:
            os.environ.pop(INCLUDE_EXPERIMENTAL_ENV_VAR, None)

    def test_no_headers_when_neither_options_nor_env_vars_set(self):
        """Should not set any X-Glean headers when nothing is configured."""
        hook = XGlean()
        request = create_mock_request()
        context = create_mock_context()

        result = hook.before_request(context, request)

        assert EXCLUDE_DEPRECATED_AFTER_HEADER not in result.headers
        assert INCLUDE_EXPERIMENTAL_HEADER not in result.headers

    def test_sets_deprecated_header_from_sdk_option(self):
        """Should set X-Glean-Exclude-Deprecated-After header from SDK option."""
        hook = XGlean()
        request = create_mock_request()
        context = create_mock_context(exclude_deprecated_after="2026-10-15")

        result = hook.before_request(context, request)

        assert result.headers.get(EXCLUDE_DEPRECATED_AFTER_HEADER) == "2026-10-15"

    def test_sets_experimental_header_when_include_experimental_is_true(self):
        """Should set X-Glean-Include-Experimental header when includeExperimental is True."""
        hook = XGlean()
        request = create_mock_request()
        context = create_mock_context(include_experimental=True)

        result = hook.before_request(context, request)

        assert result.headers.get(INCLUDE_EXPERIMENTAL_HEADER) == "true"

    def test_no_experimental_header_when_include_experimental_is_false(self):
        """Should not set X-Glean-Include-Experimental header when includeExperimental is False."""
        hook = XGlean()
        request = create_mock_request()
        context = create_mock_context(include_experimental=False)

        result = hook.before_request(context, request)

        assert INCLUDE_EXPERIMENTAL_HEADER not in result.headers

    def test_sets_both_headers_when_both_options_provided(self):
        """Should set both headers when both options are provided."""
        hook = XGlean()
        request = create_mock_request()
        context = create_mock_context(
            exclude_deprecated_after="2026-10-15",
            include_experimental=True,
        )

        result = hook.before_request(context, request)

        assert result.headers.get(EXCLUDE_DEPRECATED_AFTER_HEADER) == "2026-10-15"
        assert result.headers.get(INCLUDE_EXPERIMENTAL_HEADER) == "true"

    def test_sets_deprecated_header_from_env_var(self):
        """Should set X-Glean-Exclude-Deprecated-After header from environment variable."""
        os.environ[EXCLUDE_DEPRECATED_AFTER_ENV_VAR] = "2027-01-01"

        hook = XGlean()
        request = create_mock_request()
        context = create_mock_context()

        result = hook.before_request(context, request)

        assert result.headers.get(EXCLUDE_DEPRECATED_AFTER_HEADER) == "2027-01-01"

    def test_sets_experimental_header_from_env_var(self):
        """Should set X-Glean-Include-Experimental header from environment variable."""
        os.environ[INCLUDE_EXPERIMENTAL_ENV_VAR] = "true"

        hook = XGlean()
        request = create_mock_request()
        context = create_mock_context()

        result = hook.before_request(context, request)

        assert result.headers.get(INCLUDE_EXPERIMENTAL_HEADER) == "true"

    def test_sets_both_headers_from_env_vars(self):
        """Should set both headers from environment variables."""
        os.environ[EXCLUDE_DEPRECATED_AFTER_ENV_VAR] = "2027-06-15"
        os.environ[INCLUDE_EXPERIMENTAL_ENV_VAR] = "true"

        hook = XGlean()
        request = create_mock_request()
        context = create_mock_context()

        result = hook.before_request(context, request)

        assert result.headers.get(EXCLUDE_DEPRECATED_AFTER_HEADER) == "2027-06-15"
        assert result.headers.get(INCLUDE_EXPERIMENTAL_HEADER) == "true"

    def test_env_var_takes_precedence_for_deprecated(self):
        """Environment variable should take precedence over SDK option for deprecated."""
        os.environ[EXCLUDE_DEPRECATED_AFTER_ENV_VAR] = "2027-12-31"

        hook = XGlean()
        request = create_mock_request()
        context = create_mock_context(exclude_deprecated_after="2026-01-01")

        result = hook.before_request(context, request)

        assert result.headers.get(EXCLUDE_DEPRECATED_AFTER_HEADER) == "2027-12-31"

    def test_env_var_takes_precedence_for_experimental(self):
        """Environment variable should take precedence over SDK option for experimental."""
        os.environ[INCLUDE_EXPERIMENTAL_ENV_VAR] = "true"

        hook = XGlean()
        request = create_mock_request()
        context = create_mock_context(include_experimental=False)

        result = hook.before_request(context, request)

        assert result.headers.get(INCLUDE_EXPERIMENTAL_HEADER) == "true"

    def test_env_vars_take_precedence_for_both_headers(self):
        """Environment variables should take precedence for both headers when all are set."""
        os.environ[EXCLUDE_DEPRECATED_AFTER_ENV_VAR] = "2028-01-01"
        os.environ[INCLUDE_EXPERIMENTAL_ENV_VAR] = "true"

        hook = XGlean()
        request = create_mock_request()
        context = create_mock_context(
            exclude_deprecated_after="2026-06-01",
            include_experimental=False,
        )

        result = hook.before_request(context, request)

        assert result.headers.get(EXCLUDE_DEPRECATED_AFTER_HEADER) == "2028-01-01"
        assert result.headers.get(INCLUDE_EXPERIMENTAL_HEADER) == "true"

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
        assert result.headers.get(EXCLUDE_DEPRECATED_AFTER_HEADER) == "2026-10-15"
        assert result.headers.get(INCLUDE_EXPERIMENTAL_HEADER) == "true"

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


    def test_handles_multipart_streaming_request(self):
        """Should handle multipart requests without raising RequestNotRead.

        Multipart file uploads use a streaming body. The previous implementation
        reconstructed the request via httpx.Request(..., content=request.content),
        which raised httpx.RequestNotRead on streaming bodies.
        """
        hook = XGlean()
        request = httpx.Request(
            "POST",
            "https://example.com/rest/api/v1/uploadchatfiles",
            data={"field": "value"},
            files={"file": ("test.csv", b"a,b\n1,2", "text/csv")},
        )
        context = create_mock_context(include_experimental=True)

        result = hook.before_request(context, request)

        assert result.headers.get(INCLUDE_EXPERIMENTAL_HEADER) == "true"
        assert result.method == "POST"


@pytest.fixture(name="clean_x_glean_env")
def fixture_clean_x_glean_env(monkeypatch):
    """Unset every X-Glean environment variable for the test."""
    for name in (
        EXCLUDE_DEPRECATED_AFTER_ENV_VAR,
        INCLUDE_EXPERIMENTAL_ENV_VAR,
        INCLUDE_BETA_ENV_VAR,
    ):
        monkeypatch.delenv(name, raising=False)
    return monkeypatch


@pytest.mark.parametrize(
    "beta_env, experimental_env, config, expected",
    [
        pytest.param(None, None, {}, None, id="neither option set"),
        pytest.param(None, None, {"include_beta": True}, "true", id="include_beta alone"),
        pytest.param(None, None, {"include_beta": False}, None, id="include_beta false"),
        pytest.param(
            None, None, {"include_experimental": True}, "true", id="include_experimental alone"
        ),
        pytest.param(
            None,
            None,
            {"include_beta": True, "include_experimental": True},
            "true",
            id="both options true",
        ),
        pytest.param(
            None,
            None,
            {"include_beta": True, "include_experimental": False},
            "true",
            id="include_beta true, include_experimental false",
        ),
        pytest.param("true", None, {}, "true", id="X_GLEAN_INCLUDE_BETA alone"),
        pytest.param(" TRUE ", None, {}, "true", id="X_GLEAN_INCLUDE_BETA is case-insensitive"),
        pytest.param("true", "true", {}, "true", id="both env vars true"),
        pytest.param(
            "false",
            None,
            {"include_beta": True},
            None,
            id="X_GLEAN_INCLUDE_BETA=false overrides include_beta",
        ),
        pytest.param(
            "true",
            None,
            {"include_beta": False},
            "true",
            id="X_GLEAN_INCLUDE_BETA=true overrides include_beta=False",
        ),
        pytest.param(
            " ",
            None,
            {"include_beta": True},
            "true",
            id="empty X_GLEAN_INCLUDE_BETA falls back to include_beta",
        ),
        pytest.param(
            "false",
            None,
            {"include_experimental": True},
            "true",
            id="X_GLEAN_INCLUDE_BETA=false does not turn off include_experimental",
        ),
        pytest.param(
            "false",
            "true",
            {},
            "true",
            id="X_GLEAN_INCLUDE_BETA=false does not turn off X_GLEAN_INCLUDE_EXPERIMENTAL",
        ),
        pytest.param(
            None,
            "false",
            {"include_beta": True},
            "true",
            id="X_GLEAN_INCLUDE_EXPERIMENTAL=false does not turn off include_beta",
        ),
    ],
)
def test_include_beta(clean_x_glean_env, beta_env, experimental_env, config, expected):
    """include_beta and its include_experimental alias both set X-Glean-Include-Experimental."""
    if beta_env is not None:
        clean_x_glean_env.setenv(INCLUDE_BETA_ENV_VAR, beta_env)
    if experimental_env is not None:
        clean_x_glean_env.setenv(INCLUDE_EXPERIMENTAL_ENV_VAR, experimental_env)

    result = XGlean().before_request(create_mock_context(**config), create_mock_request())

    assert result.headers.get(INCLUDE_EXPERIMENTAL_HEADER) == expected
    assert "X-Glean-Beta" not in result.headers


def send_query(**kwargs) -> httpx.Request:
    """Send one request through a real Glean client and return what went out."""
    captured = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return httpx.Response(200, json={})

    glean = Glean(
        api_token="test-token",
        server_url="https://example.com",
        client=httpx.Client(transport=httpx.MockTransport(handler)),
        **kwargs,
    )
    try:
        glean.search.query(query="test")
    except Exception:  # pylint: disable=broad-exception-caught
        pass  # The empty response body may not validate; only the request matters.

    assert captured, "expected a request to be sent"
    return captured[0]


@pytest.mark.parametrize(
    "env, expected",
    [
        pytest.param({}, None, id="neither env var"),
        pytest.param({INCLUDE_BETA_ENV_VAR: "true"}, "true", id="X_GLEAN_INCLUDE_BETA"),
        pytest.param(
            {INCLUDE_EXPERIMENTAL_ENV_VAR: "true"}, "true", id="X_GLEAN_INCLUDE_EXPERIMENTAL"
        ),
        pytest.param(
            {INCLUDE_BETA_ENV_VAR: "true", INCLUDE_EXPERIMENTAL_ENV_VAR: "true"},
            "true",
            id="both env vars",
        ),
    ],
)
def test_sdk_sends_include_experimental_header(clean_x_glean_env, env, expected):
    """A real Glean client sends the header that the env vars ask for."""
    for name, value in env.items():
        clean_x_glean_env.setenv(name, value)

    request = send_query()

    assert request.headers.get(INCLUDE_EXPERIMENTAL_HEADER) == expected
    assert "X-Glean-Beta" not in request.headers


@pytest.mark.parametrize(
    "kwargs, expected_experimental, expected_deprecated",
    [
        pytest.param({}, None, None, id="no options"),
        pytest.param({"include_beta": True}, "true", None, id="include_beta=True"),
        pytest.param({"include_beta": False}, None, None, id="include_beta=False"),
        pytest.param(
            {"include_experimental": True}, "true", None, id="include_experimental=True"
        ),
        pytest.param(
            {"include_beta": False, "include_experimental": True},
            "true",
            None,
            id="include_beta=False does not turn off include_experimental",
        ),
        pytest.param(
            {"exclude_deprecated_after": "2026-10-15"},
            None,
            "2026-10-15",
            id="exclude_deprecated_after",
        ),
        pytest.param(
            {"exclude_deprecated_after": "2026-10-15", "include_beta": True},
            "true",
            "2026-10-15",
            id="all options",
        ),
    ],
)
def test_sdk_constructor_options(
    clean_x_glean_env, kwargs, expected_experimental, expected_deprecated
):
    """The Glean constructor accepts the X-Glean options and sends their headers.

    These options live in generated files (sdk.py and sdkconfiguration.py) and a
    regeneration has dropped them before, so this guards against that.
    """
    request = send_query(**kwargs)

    assert request.headers.get(INCLUDE_EXPERIMENTAL_HEADER) == expected_experimental
    assert request.headers.get(EXCLUDE_DEPRECATED_AFTER_HEADER) == expected_deprecated
    assert "X-Glean-Beta" not in request.headers


def test_env_var_overrides_constructor_option(clean_x_glean_env):
    """X_GLEAN_INCLUDE_BETA takes precedence over the include_beta constructor option."""
    clean_x_glean_env.setenv(INCLUDE_BETA_ENV_VAR, "false")

    request = send_query(include_beta=True)

    assert INCLUDE_EXPERIMENTAL_HEADER not in request.headers


if __name__ == "__main__":
    pytest.main([__file__])
