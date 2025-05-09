// Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT.

package components

// BulkIndexTeamsRequest - Describes the request body of the /bulkindexteams API call
type BulkIndexTeamsRequest struct {
	// Unique id that must be used for this bulk upload instance
	UploadID string `json:"uploadId"`
	// true if this is the first page of the upload. Defaults to false
	IsFirstPage *bool `json:"isFirstPage,omitempty"`
	// true if this is the last page of the upload. Defaults to false
	IsLastPage *bool `json:"isLastPage,omitempty"`
	// Flag to discard previous upload attempts and start from scratch. Must be specified with isFirstPage=true
	ForceRestartUpload *bool `json:"forceRestartUpload,omitempty"`
	// Batch of team information
	Teams []TeamInfoDefinition `json:"teams"`
}

func (o *BulkIndexTeamsRequest) GetUploadID() string {
	if o == nil {
		return ""
	}
	return o.UploadID
}

func (o *BulkIndexTeamsRequest) GetIsFirstPage() *bool {
	if o == nil {
		return nil
	}
	return o.IsFirstPage
}

func (o *BulkIndexTeamsRequest) GetIsLastPage() *bool {
	if o == nil {
		return nil
	}
	return o.IsLastPage
}

func (o *BulkIndexTeamsRequest) GetForceRestartUpload() *bool {
	if o == nil {
		return nil
	}
	return o.ForceRestartUpload
}

func (o *BulkIndexTeamsRequest) GetTeams() []TeamInfoDefinition {
	if o == nil {
		return []TeamInfoDefinition{}
	}
	return o.Teams
}
