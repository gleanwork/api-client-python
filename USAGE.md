<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from glean import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.client.chat.create(messages=[
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
        api_token=os.getenv("GLEAN_API_TOKEN", ""),
    ) as g_client:

        res = await g_client.client.chat.create_async(messages=[
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

```python
# Synchronous Example
from glean import Glean, models
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as g_client:

    res = g_client.client.chat.create_stream(messages=[
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
        api_token=os.getenv("GLEAN_API_TOKEN", ""),
    ) as g_client:

        res = await g_client.client.chat.create_stream_async(messages=[
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