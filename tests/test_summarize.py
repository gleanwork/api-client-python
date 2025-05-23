"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from glean import Glean
import os
from tests.test_client import create_test_http_client


def test_summarize_summarize():
    test_http_client = create_test_http_client("summarize")

    with Glean(
        server_url=os.getenv("TEST_SERVER_URL", "http://localhost:18080"),
        client=test_http_client,
        api_token=os.getenv("GLEAN_API_TOKEN", "value"),
    ) as g_client:
        assert g_client is not None

        res = g_client.client.documents.summarize(
            document_specs=[
                {},
                {},
            ]
        )
        assert res is not None
