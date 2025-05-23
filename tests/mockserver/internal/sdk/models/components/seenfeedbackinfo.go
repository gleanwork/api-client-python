// Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT.

package components

type SeenFeedbackInfo struct {
	// The confidence of the user seeing the object is high because they explicitly interacted with it e.g. answer impression in SERP with additional user interaction.
	IsExplicit *bool `json:"isExplicit,omitempty"`
}

func (o *SeenFeedbackInfo) GetIsExplicit() *bool {
	if o == nil {
		return nil
	}
	return o.IsExplicit
}
