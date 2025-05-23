// Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT.

package components

import (
	"encoding/json"
	"fmt"
)

// DocumentVisibilityUpdateResultOverride - The visibility-override state of the document.
type DocumentVisibilityUpdateResultOverride string

const (
	DocumentVisibilityUpdateResultOverrideNone                   DocumentVisibilityUpdateResultOverride = "NONE"
	DocumentVisibilityUpdateResultOverrideHideFromAll            DocumentVisibilityUpdateResultOverride = "HIDE_FROM_ALL"
	DocumentVisibilityUpdateResultOverrideHideFromGroups         DocumentVisibilityUpdateResultOverride = "HIDE_FROM_GROUPS"
	DocumentVisibilityUpdateResultOverrideHideFromAllExceptOwner DocumentVisibilityUpdateResultOverride = "HIDE_FROM_ALL_EXCEPT_OWNER"
)

func (e DocumentVisibilityUpdateResultOverride) ToPointer() *DocumentVisibilityUpdateResultOverride {
	return &e
}
func (e *DocumentVisibilityUpdateResultOverride) UnmarshalJSON(data []byte) error {
	var v string
	if err := json.Unmarshal(data, &v); err != nil {
		return err
	}
	switch v {
	case "NONE":
		fallthrough
	case "HIDE_FROM_ALL":
		fallthrough
	case "HIDE_FROM_GROUPS":
		fallthrough
	case "HIDE_FROM_ALL_EXCEPT_OWNER":
		*e = DocumentVisibilityUpdateResultOverride(v)
		return nil
	default:
		return fmt.Errorf("invalid value for DocumentVisibilityUpdateResultOverride: %v", v)
	}
}

type DocumentVisibilityUpdateResult struct {
	DocID *string `json:"docId,omitempty"`
	// The visibility-override state of the document.
	Override *DocumentVisibilityUpdateResultOverride `json:"override,omitempty"`
	// Whether this document was successfully set to its desired visibility state.
	Success *bool `json:"success,omitempty"`
}

func (o *DocumentVisibilityUpdateResult) GetDocID() *string {
	if o == nil {
		return nil
	}
	return o.DocID
}

func (o *DocumentVisibilityUpdateResult) GetOverride() *DocumentVisibilityUpdateResultOverride {
	if o == nil {
		return nil
	}
	return o.Override
}

func (o *DocumentVisibilityUpdateResult) GetSuccess() *bool {
	if o == nil {
		return nil
	}
	return o.Success
}
