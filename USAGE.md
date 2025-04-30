<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.chat.start(messages=[
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
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from glean import Glean, models
import os

async def main():

    async with Glean(
        bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
    ) as g_client:

        res = await g_client.client.chat.start_async(messages=[
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

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->