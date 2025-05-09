// Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT.

package operations

import (
	"mockserver/internal/sdk/models/components"
)

type GetcollectionResponse struct {
	HTTPMeta components.HTTPMetadata `json:"-"`
	// OK
	GetCollectionResponse *components.GetCollectionResponse
}

func (o *GetcollectionResponse) GetHTTPMeta() components.HTTPMetadata {
	if o == nil {
		return components.HTTPMetadata{}
	}
	return o.HTTPMeta
}

func (o *GetcollectionResponse) GetGetCollectionResponse() *components.GetCollectionResponse {
	if o == nil {
		return nil
	}
	return o.GetCollectionResponse
}
