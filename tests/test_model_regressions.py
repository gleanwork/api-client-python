import json

from glean.api_client import Glean, models, utils


def test_answer_likes_normalizes_null_liked_by_after_sdk_init():
    payload = json.dumps(
        {
            "likedBy": None,
            "likedByUser": False,
            "numLikes": 0,
        }
    )

    with Glean(api_token="token", instance="test-instance"):
        likes = utils.unmarshal_json(payload, models.AnswerLikes)

    assert likes.liked_by == []
    assert likes.liked_by_user is False
    assert likes.num_likes == 0


def test_document_content_model_dump_keeps_alias_field_value():
    content = models.DocumentContent(fullTextList=["This is a test document."])

    dumped = content.model_dump()

    assert dumped["fullTextList"] == ["This is a test document."]
