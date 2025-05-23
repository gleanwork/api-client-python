// Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT.

package operations

import (
	"mockserver/internal/sdk/models/components"
)

type SetdocvisibilityResponse struct {
	HTTPMeta components.HTTPMetadata `json:"-"`
	// OK
	UpdateDocumentVisibilityOverridesResponse *components.UpdateDocumentVisibilityOverridesResponse
}

func (o *SetdocvisibilityResponse) GetHTTPMeta() components.HTTPMetadata {
	if o == nil {
		return components.HTTPMetadata{}
	}
	return o.HTTPMeta
}

func (o *SetdocvisibilityResponse) GetUpdateDocumentVisibilityOverridesResponse() *components.UpdateDocumentVisibilityOverridesResponse {
	if o == nil {
		return nil
	}
	return o.UpdateDocumentVisibilityOverridesResponse
}
