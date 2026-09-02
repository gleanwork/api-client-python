"""Hook to normalize AnswerLikes payloads that return null likedBy values."""

from typing import Any, Tuple

from glean.api_client._hooks.types import SDKInitHook
from glean.api_client.httpclient import HttpClient


class AnswerLikesNullFixHook(SDKInitHook):
    """
    Normalizes API payloads where AnswerLikes.likedBy is null.

    The API can return {"likedBy": null, "likedByUser": ..., "numLikes": ...}
    even though the generated model expects likedBy to be a list. This hook patches the
    unmarshal step so SDK responses continue to validate after regeneration.
    """

    def sdk_init(self, base_url: str, client: HttpClient) -> Tuple[str, HttpClient]:
        self._patch_unmarshal()
        return base_url, client

    def _patch_unmarshal(self) -> None:
        from glean.api_client.utils import serializers

        if getattr(serializers.unmarshal, "_glean_answer_likes_null_fix", False):
            return

        original_unmarshal = serializers.unmarshal

        def fixed_unmarshal(val: Any, typ: Any) -> Any:
            return original_unmarshal(self._normalize_answer_likes_nulls(val), typ)

        fixed_unmarshal._glean_answer_likes_null_fix = True
        serializers.unmarshal = fixed_unmarshal

    def _normalize_answer_likes_nulls(self, val: Any) -> Any:
        if isinstance(val, list):
            for item in val:
                self._normalize_answer_likes_nulls(item)
            return val

        if isinstance(val, dict):
            for item in val.values():
                self._normalize_answer_likes_nulls(item)

            if self._is_answer_likes_payload(val) and val["likedBy"] is None:
                val["likedBy"] = []

        return val

    @staticmethod
    def _is_answer_likes_payload(val: Any) -> bool:
        return isinstance(val, dict) and all(
            key in val for key in ("likedBy", "likedByUser", "numLikes")
        )
