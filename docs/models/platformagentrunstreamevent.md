# PlatformAgentRunStreamEvent

One server-sent event from a streaming agent run. The SSE `event` field selects the payload. Successful runs emit `message` events. A terminal failure after the stream has started emits exactly one `run.failed` event, then the stream closes. This schema describes a parsed event, not the raw HTTP body. A typical stream is:
id: 1
event: message
data: {"messages":[{"role":"GLEAN_AI","content":[{"text":"Hello","type":"text"}]}]}

id: 2
event: run.failed
data: {"error":{"type":"https://developers.glean.com/errors/spend-limit-exceeded","title":"Spend Limit Exceeded","status":403,"detail":"You've reached the monthly limit set by your admin.","code":"spend_limit_exceeded","request_id":"req_123","documentation_url":"https://developers.glean.com/errors/spend-limit-exceeded"}}



## Supported Types

### `models.PlatformAgentRunMessageEvent`

```python
value: models.PlatformAgentRunMessageEvent = /* values here */
```

### `models.PlatformAgentRunFailedEvent`

```python
value: models.PlatformAgentRunFailedEvent = /* values here */
```

