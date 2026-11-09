# GetChatPagination

Pagination cursors and page flags for a getchat message page.


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `start_cursor`                                                            | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | Cursor of the first (oldest) returned message. Omitted for an empty page. |
| `end_cursor`                                                              | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | Cursor of the last (newest) returned message. Omitted for an empty page.  |
| `has_next_page`                                                           | *bool*                                                                    | :heavy_check_mark:                                                        | Whether visible messages exist after endCursor in chronological order.    |
| `has_previous_page`                                                       | *bool*                                                                    | :heavy_check_mark:                                                        | Whether visible messages exist before startCursor in chronological order. |