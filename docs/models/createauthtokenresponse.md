# CreateAuthTokenResponse


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `token`                                                                              | *str*                                                                                | :heavy_check_mark:                                                                   | An authentication token that can be passed to any endpoint via Bearer Authentication |
| `expiration_time`                                                                    | *int*                                                                                | :heavy_check_mark:                                                                   | Unix timestamp for when this token expires (in seconds since epoch UTC).             |