// Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT.

package operations

import (
	"mockserver/internal/sdk/models/components"
)

type CreateAndWaitRunResponse struct {
	HTTPMeta components.HTTPMetadata `json:"-"`
	// Success
	AgentRunWaitResponse *components.AgentRunWaitResponse
}

func (o *CreateAndWaitRunResponse) GetHTTPMeta() components.HTTPMetadata {
	if o == nil {
		return components.HTTPMetadata{}
	}
	return o.HTTPMeta
}

func (o *CreateAndWaitRunResponse) GetAgentRunWaitResponse() *components.AgentRunWaitResponse {
	if o == nil {
		return nil
	}
	return o.AgentRunWaitResponse
}
