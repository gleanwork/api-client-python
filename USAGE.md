<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from glean import Glean, models
from glean.utils import parse_datetime
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.client.activity.report(events=[
        {
            "action": models.ActivityEventAction.HISTORICAL_VIEW,
            "timestamp": parse_datetime("2000-01-23T04:56:07.000Z"),
            "url": "https://example.com/",
        },
        {
            "action": models.ActivityEventAction.SEARCH,
            "params": {
                "query": "query",
            },
            "timestamp": parse_datetime("2000-01-23T04:56:07.000Z"),
            "url": "https://example.com/search?q=query",
        },
        {
            "action": models.ActivityEventAction.VIEW,
            "params": {
                "duration": 20,
                "referrer": "https://example.com/document",
            },
            "timestamp": parse_datetime("2000-01-23T04:56:07.000Z"),
            "url": "https://example.com/",
        },
    ])

    # Use the SDK ...
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from glean import Glean, models
from glean.utils import parse_datetime
import os

async def main():

    async with Glean(
        bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
    ) as g_client:

        await g_client.client.activity.report_async(events=[
            {
                "action": models.ActivityEventAction.HISTORICAL_VIEW,
                "timestamp": parse_datetime("2000-01-23T04:56:07.000Z"),
                "url": "https://example.com/",
            },
            {
                "action": models.ActivityEventAction.SEARCH,
                "params": {
                    "query": "query",
                },
                "timestamp": parse_datetime("2000-01-23T04:56:07.000Z"),
                "url": "https://example.com/search?q=query",
            },
            {
                "action": models.ActivityEventAction.VIEW,
                "params": {
                    "duration": 20,
                    "referrer": "https://example.com/document",
                },
                "timestamp": parse_datetime("2000-01-23T04:56:07.000Z"),
                "url": "https://example.com/",
            },
        ])

        # Use the SDK ...

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->