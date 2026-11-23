# StructuredLocation

Detailed location with information about country, state, city etc.


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `desk_location`                                           | *Optional[str]*                                           | :heavy_minus_sign:                                        | Desk number.                                              |
| `timezone`                                                | *Optional[str]*                                           | :heavy_minus_sign:                                        | Location's timezone, e.g. UTC, PST.                       |
| `address`                                                 | *Optional[str]*                                           | :heavy_minus_sign:                                        | Office address or name.                                   |
| `city`                                                    | *Optional[str]*                                           | :heavy_minus_sign:                                        | Name of the city.                                         |
| `state`                                                   | *Optional[str]*                                           | :heavy_minus_sign:                                        | State code.                                               |
| `region`                                                  | *Optional[str]*                                           | :heavy_minus_sign:                                        | Region information, e.g. NORAM, APAC.                     |
| `zip_code`                                                | *Optional[str]*                                           | :heavy_minus_sign:                                        | ZIP Code for the address.                                 |
| `country`                                                 | *Optional[str]*                                           | :heavy_minus_sign:                                        | Country name.                                             |
| `country_code`                                            | *Optional[str]*                                           | :heavy_minus_sign:                                        | Alpha-2 or Alpha-3 ISO 3166 country code, e.g. US or USA. |