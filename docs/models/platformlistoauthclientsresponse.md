# PlatformListOAuthClientsResponse

One page of OAuth clients.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `results`                                                                | List[[models.PlatformOAuthClient](../models/platformoauthclient.md)]     | :heavy_check_mark:                                                       | The clients on this page, ordered by display_name and then by client_id. |
| `has_more`                                                               | *bool*                                                                   | :heavy_check_mark:                                                       | Whether more clients are available after this page.                      |
| `next_cursor`                                                            | *OptionalNullable[str]*                                                  | :heavy_minus_sign:                                                       | Opaque cursor for the next page; null or absent when has_more is false.  |
| `request_id`                                                             | *str*                                                                    | :heavy_check_mark:                                                       | Request identifier for correlating this response.                        |