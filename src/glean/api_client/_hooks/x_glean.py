"""Hook to set X-Glean headers for experimental features and deprecation testing."""

import os
from typing import Optional, Union
import httpx
from glean.api_client._hooks.types import BeforeRequestContext, BeforeRequestHook


def _get_first_value(
    env_value: Optional[str],
    config_value: Optional[str],
) -> Optional[str]:
    """Get the first non-empty value from the provided arguments.

    Environment variables take precedence over SDK constructor options.
    """
    if env_value:
        return env_value
    if config_value:
        return config_value
    return None


class XGlean(BeforeRequestHook):
    """
    Hook that sets X-Glean headers for experimental features and deprecation testing.

    This hook adds the following headers when configured:
    - X-Glean-Exclude-Deprecated-After: Excludes API endpoints deprecated after this date
    - X-Glean-Experimental: Enables experimental API features

    Configuration can be done via environment variables or SDK constructor options.
    Environment variables take precedence over SDK constructor options.
    """

    def before_request(
        self, hook_ctx: BeforeRequestContext, request: httpx.Request
    ) -> Union[httpx.Request, Exception]:
        """
        Add X-Glean headers to the request based on configuration.

        Args:
            hook_ctx: Context containing SDK configuration
            request: The HTTP request being made

        Returns:
            The modified request with X-Glean headers added
        """
        # Get deprecated value - env var takes precedence
        deprecated_value = _get_first_value(
            os.environ.get("X_GLEAN_EXCLUDE_DEPRECATED_AFTER"),
            getattr(hook_ctx.config, "exclude_deprecated_after", None),
        )

        # Get experimental value - env var takes precedence
        config_experimental = (
            "true" if getattr(hook_ctx.config, "include_experimental", None) is True else None
        )
        experimental_value = _get_first_value(
            os.environ.get("X_GLEAN_INCLUDE_EXPERIMENTAL"),
            config_experimental,
        )

        # Create new headers dict with existing headers
        new_headers = dict(request.headers)

        if deprecated_value:
            new_headers["X-Glean-Exclude-Deprecated-After"] = deprecated_value

        if experimental_value:
            new_headers["X-Glean-Experimental"] = experimental_value

        # Return new request with updated headers
        return httpx.Request(
            method=request.method,
            url=request.url,
            headers=new_headers,
            content=request.content,
            extensions=request.extensions,
        )
