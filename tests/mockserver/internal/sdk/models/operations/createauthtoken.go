// Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT.

package operations

import (
	"mockserver/internal/sdk/models/components"
)

type CreateauthtokenResponse struct {
	HTTPMeta components.HTTPMetadata `json:"-"`
	// OK
	CreateAuthTokenResponse *components.CreateAuthTokenResponse
}

func (o *CreateauthtokenResponse) GetHTTPMeta() components.HTTPMetadata {
	if o == nil {
		return components.HTTPMetadata{}
	}
	return o.HTTPMeta
}

func (o *CreateauthtokenResponse) GetCreateAuthTokenResponse() *components.CreateAuthTokenResponse {
	if o == nil {
		return nil
	}
	return o.CreateAuthTokenResponse
}
