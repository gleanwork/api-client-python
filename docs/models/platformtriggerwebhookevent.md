# PlatformTriggerWebhookEvent

Every delivered webhook is one of these two variants. A trigger with a cron schedule carries no document and so cannot be delivered over a webhook.


## Supported Types

### `models.PlatformDocumentChangeWebhookEvent`

```python
value: models.PlatformDocumentChangeWebhookEvent = /* values here */
```

### `models.PlatformContentScheduleWebhookEvent`

```python
value: models.PlatformContentScheduleWebhookEvent = /* values here */
```

