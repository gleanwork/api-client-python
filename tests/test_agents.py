"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from glean import Glean
import os
import pytest
from tests.test_client import create_test_http_client


@pytest.mark.skip(
    reason="incomplete test found please make sure to address the following errors: [`workflow step runagent.test referencing operation runagent not found in document`]"
)
def test_agents_runagent():
    pass


@pytest.mark.skip(
    reason="incomplete test found please make sure to address the following errors: [`workflow step listagents.test referencing operation listagents not found in document`]"
)
def test_agents_listagents():
    pass


@pytest.mark.skip(
    reason="incomplete test found please make sure to address the following errors: [`workflow step getagentinputs.test referencing operation getagentinputs not found in document`]"
)
def test_agents_getagentinputs():
    pass


def test_agents_get_agent():
    test_http_client = create_test_http_client("getAgent")

    with Glean(
        server_url=os.getenv("TEST_SERVER_URL", "http://localhost:18080"),
        client=test_http_client,
        api_token=os.getenv("GLEAN_API_TOKEN", "value"),
    ) as g_client:
        assert g_client is not None

        res = g_client.client.agents.retrieve(agent_id="<id>")
        assert res is not None


def test_agents_get_agent_schemas():
    test_http_client = create_test_http_client("getAgentSchemas")

    with Glean(
        server_url=os.getenv("TEST_SERVER_URL", "http://localhost:18080"),
        client=test_http_client,
        api_token=os.getenv("GLEAN_API_TOKEN", "value"),
    ) as g_client:
        assert g_client is not None

        res = g_client.client.agents.retrieve_schemas(agent_id="<id>")
        assert res is not None


@pytest.mark.skip(
    reason="incomplete test found please make sure to address the following errors: [`workflow step searchAgents.test referencing operation searchAgents is missing required request body`]"
)
def test_agents_search_agents():
    pass


@pytest.mark.skip(
    reason="incomplete test found please make sure to address the following errors: [`workflow step createAndStreamRun.test referencing operation createAndStreamRun is not currently supported`]"
)
def test_agents_create_and_stream_run():
    pass


@pytest.mark.skip(
    reason="incomplete test found please make sure to address the following errors: [`workflow step createAndWaitRun.test referencing operation createAndWaitRun is missing required request body`]"
)
def test_agents_create_and_wait_run():
    pass
