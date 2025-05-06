# To run the example:
# poetry install
# poetry run python examples/ask_example.py

from glean import Glean, errors, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
    domain="customerName"
) as glean:
    try:
        res = glean.client.chat.start(messages=[
            {
                "fragments": [
                    models.ChatMessageFragment(
                        text="What are the company holidays this year?",
                    ),
                ],
            },
        ], timeout_millis=30000)
        
        # Handle response
        print(res)
    except errors.GleanError as e:
        print(e.message)
        print(e.status_code)
        print(e.raw_response)
        print(e.body)