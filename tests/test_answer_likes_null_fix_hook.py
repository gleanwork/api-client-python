"""Tests for the AnswerLikes null fix hook."""

from unittest.mock import Mock

from glean.api_client import models
from glean.api_client._hooks.answer_likes_null_fix_hook import AnswerLikesNullFixHook
from glean.api_client.httpclient import HttpClient
from glean.api_client.utils import serializers


class TestAnswerLikesNullFixHook:
    """Test cases for the AnswerLikes null fix hook."""

    def setup_method(self):
        """Set up test fixtures."""
        self.hook = AnswerLikesNullFixHook()
        self.mock_client = Mock(spec=HttpClient)

    def test_sdk_init_returns_unchanged_params(self):
        """SDK init should not change the base URL or client."""
        base_url = "https://api.example.com"

        result_url, result_client = self.hook.sdk_init(base_url, self.mock_client)

        assert result_url == base_url
        assert result_client == self.mock_client

    def test_patch_unmarshal_is_idempotent(self, monkeypatch):
        """The unmarshal patch should only be applied once."""
        monkeypatch.setattr(serializers, "unmarshal", serializers.unmarshal)

        self.hook._patch_unmarshal()
        first = serializers.unmarshal

        self.hook._patch_unmarshal()
        second = serializers.unmarshal

        assert first is second
        assert getattr(first, "_glean_answer_likes_null_fix", False) is True

    def test_normalize_answer_likes_nulls_updates_nested_payloads(self):
        """Nested AnswerLikes payloads should convert null likedBy values to empty lists."""
        payload = {
            "message": {
                "likes": {
                    "likedBy": None,
                    "likedByUser": False,
                    "numLikes": 0,
                }
            }
        }

        normalized = self.hook._normalize_answer_likes_nulls(payload)

        assert normalized is payload
        assert payload["message"]["likes"]["likedBy"] == []

    def test_normalize_answer_likes_nulls_ignores_non_matching_payloads(self):
        """Unrelated payloads should not be modified."""
        payload = {"likedBy": None}

        normalized = self.hook._normalize_answer_likes_nulls(payload)

        assert normalized is payload
        assert payload["likedBy"] is None

    def test_patched_unmarshal_normalizes_null_liked_by(self, monkeypatch):
        """Patched unmarshal should make null likedBy payloads validate cleanly."""
        monkeypatch.setattr(serializers, "unmarshal", serializers.unmarshal)
        self.hook._patch_unmarshal()

        likes = serializers.unmarshal(
            {"likedBy": None, "likedByUser": False, "numLikes": 0},
            models.AnswerLikes,
        )

        assert likes.liked_by == []
