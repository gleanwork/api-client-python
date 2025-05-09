// Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT.

package components

type Group struct {
	// The type of user group
	Type GroupType `json:"type"`
	// A unique identifier for the group. May be the same as name.
	ID string `json:"id"`
	// Name of the group.
	Name *string `json:"name,omitempty"`
}

func (o *Group) GetType() GroupType {
	if o == nil {
		return GroupType("")
	}
	return o.Type
}

func (o *Group) GetID() string {
	if o == nil {
		return ""
	}
	return o.ID
}

func (o *Group) GetName() *string {
	if o == nil {
		return nil
	}
	return o.Name
}
