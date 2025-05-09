"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from glean import Glean, models
import os
from tests.test_client import create_test_http_client


def test_messages_messages():
    test_http_client = create_test_http_client("messages")

    with Glean(
        server_url=os.getenv("TEST_SERVER_URL", "http://localhost:18080"),
        client=test_http_client,
        api_token=os.getenv("GLEAN_API_TOKEN", "value"),
    ) as g_client:
        assert g_client is not None

        res = g_client.client.messages.retrieve(
            id_type=models.IDType.CONVERSATION_ID, id="<id>", timestamp_millis=558834
        )
        assert res is not None
