// Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT.

package operations

import (
	"mockserver/internal/sdk/models/components"
)

type DeletechatsRequest struct {
	// The offset of the client's timezone in minutes from UTC. e.g. PDT is -420 because it's 7 hours behind UTC.
	TimezoneOffset     *int64                        `queryParam:"style=form,explode=true,name=timezoneOffset"`
	DeleteChatsRequest components.DeleteChatsRequest `request:"mediaType=application/json"`
}

func (o *DeletechatsRequest) GetTimezoneOffset() *int64 {
	if o == nil {
		return nil
	}
	return o.TimezoneOffset
}

func (o *DeletechatsRequest) GetDeleteChatsRequest() components.DeleteChatsRequest {
	if o == nil {
		return components.DeleteChatsRequest{}
	}
	return o.DeleteChatsRequest
}

type DeletechatsResponse struct {
	HTTPMeta components.HTTPMetadata `json:"-"`
}

func (o *DeletechatsResponse) GetHTTPMeta() components.HTTPMetadata {
	if o == nil {
		return components.HTTPMetadata{}
	}
	return o.HTTPMeta
}
