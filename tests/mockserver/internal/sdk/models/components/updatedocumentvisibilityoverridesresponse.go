// Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT.

package components

type UpdateDocumentVisibilityOverridesResponse struct {
	// The documents and whether their visibility was successfully updated.
	Results []DocumentVisibilityUpdateResult `json:"results,omitempty"`
}

func (o *UpdateDocumentVisibilityOverridesResponse) GetResults() []DocumentVisibilityUpdateResult {
	if o == nil {
		return nil
	}
	return o.Results
}
