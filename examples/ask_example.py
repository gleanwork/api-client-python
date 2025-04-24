# To run the example:
# poetry install
# poetry run python examples/ask_example.py

from glean import Glean, errors
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
    domain="customerName"
) as glean:
    try:
        res = glean.chat.ask()
        print(res)
    except errors.GleanDataError as e:
        print(e.data)
        print(e.data.errorMessage)
    except errors.GleanError as e:
        print(e.message)
        print(e.status_code)
        print(e.raw_response)
        print(e.body)
