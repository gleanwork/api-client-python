// Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT.

package operations

import (
	"mockserver/internal/sdk/models/components"
)

type EditcollectionResponse struct {
	HTTPMeta components.HTTPMetadata `json:"-"`
	// OK
	EditCollectionResponse *components.EditCollectionResponse
}

func (o *EditcollectionResponse) GetHTTPMeta() components.HTTPMetadata {
	if o == nil {
		return components.HTTPMetadata{}
	}
	return o.HTTPMeta
}

func (o *EditcollectionResponse) GetEditCollectionResponse() *components.EditCollectionResponse {
	if o == nil {
		return nil
	}
	return o.EditCollectionResponse
}
