# PlatformTriggerAuth

Optional caller credential sent as an HTTP auth header on each delivery, in addition to the HMAC signature. Lets the receiving endpoint authenticate the request. On update, omit `auth` to preserve the existing credential; there is no in-place removal — recreate the trigger to remove auth.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `type`                                                                 | [models.PlatformTriggerAuthType](../models/platformtriggerauthtype.md) | :heavy_check_mark:                                                     | Credential scheme.                                                     |                                                                        |
| `secret`                                                               | *str*                                                                  | :heavy_check_mark:                                                     | Secret credential value. Write-only; never returned on reads.          | secret_test_123                                                        |