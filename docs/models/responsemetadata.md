# ResponseMetadata

Metadata about the response (e.g., latency, token count).


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `latency_ms`                                         | *Optional[int]*                                      | :heavy_minus_sign:                                   | Time taken to generate the response in milliseconds. |
| `token_count`                                        | *Optional[int]*                                      | :heavy_minus_sign:                                   | Number of tokens in the response.                    |
| `model_used`                                         | *Optional[str]*                                      | :heavy_minus_sign:                                   | The specific model version used.                     |