// Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT.

package components

// Badge - Displays a user's accomplishment or milestone
type Badge struct {
	// An auto generated unique identifier.
	Key *string `json:"key,omitempty"`
	// The badge name displayed to users
	DisplayName *string `json:"displayName,omitempty"`
	// Defines how to render an icon
	IconConfig *IconConfig `json:"iconConfig,omitempty"`
	// The badge should be shown on the PersonAttribution
	Pinned *bool `json:"pinned,omitempty"`
}

func (o *Badge) GetKey() *string {
	if o == nil {
		return nil
	}
	return o.Key
}

func (o *Badge) GetDisplayName() *string {
	if o == nil {
		return nil
	}
	return o.DisplayName
}

func (o *Badge) GetIconConfig() *IconConfig {
	if o == nil {
		return nil
	}
	return o.IconConfig
}

func (o *Badge) GetPinned() *bool {
	if o == nil {
		return nil
	}
	return o.Pinned
}
