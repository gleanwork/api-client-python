# AddCollectionItemsRequest


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `collection_id`                                                                | *float*                                                                        | :heavy_check_mark:                                                             | The ID of the Collection to add items to.                                      |
| `added_collection_item_descriptors`                                            | List[[models.CollectionItemDescriptor](../models/collectionitemdescriptor.md)] | :heavy_minus_sign:                                                             | The CollectionItemDescriptors of the items being added.                        |