// Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT.

package components

// IndexGroupRequest - Describes the request body of the /indexgroup API call
type IndexGroupRequest struct {
	// Version number for document for optimistic concurrency control. If absent or 0 then no version checks are done.
	Version *int64 `json:"version,omitempty"`
	// The datasource for which the group is added
	Datasource string `json:"datasource"`
	// describes a group in the datasource
	Group DatasourceGroupDefinition `json:"group"`
}

func (o *IndexGroupRequest) GetVersion() *int64 {
	if o == nil {
		return nil
	}
	return o.Version
}

func (o *IndexGroupRequest) GetDatasource() string {
	if o == nil {
		return ""
	}
	return o.Datasource
}

func (o *IndexGroupRequest) GetGroup() DatasourceGroupDefinition {
	if o == nil {
		return DatasourceGroupDefinition{}
	}
	return o.Group
}
