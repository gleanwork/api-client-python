// Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT.

package components

import (
	"encoding/json"
	"fmt"
)

// UserActivityAction - The action for the activity
type UserActivityAction string

const (
	UserActivityActionAdd         UserActivityAction = "ADD"
	UserActivityActionAddReminder UserActivityAction = "ADD_REMINDER"
	UserActivityActionClick       UserActivityAction = "CLICK"
	UserActivityActionComment     UserActivityAction = "COMMENT"
	UserActivityActionDelete      UserActivityAction = "DELETE"
	UserActivityActionDismiss     UserActivityAction = "DISMISS"
	UserActivityActionEdit        UserActivityAction = "EDIT"
	UserActivityActionMention     UserActivityAction = "MENTION"
	UserActivityActionMove        UserActivityAction = "MOVE"
	UserActivityActionOther       UserActivityAction = "OTHER"
	UserActivityActionRestore     UserActivityAction = "RESTORE"
	UserActivityActionUnknown     UserActivityAction = "UNKNOWN"
	UserActivityActionVerify      UserActivityAction = "VERIFY"
	UserActivityActionView        UserActivityAction = "VIEW"
)

func (e UserActivityAction) ToPointer() *UserActivityAction {
	return &e
}
func (e *UserActivityAction) UnmarshalJSON(data []byte) error {
	var v string
	if err := json.Unmarshal(data, &v); err != nil {
		return err
	}
	switch v {
	case "ADD":
		fallthrough
	case "ADD_REMINDER":
		fallthrough
	case "CLICK":
		fallthrough
	case "COMMENT":
		fallthrough
	case "DELETE":
		fallthrough
	case "DISMISS":
		fallthrough
	case "EDIT":
		fallthrough
	case "MENTION":
		fallthrough
	case "MOVE":
		fallthrough
	case "OTHER":
		fallthrough
	case "RESTORE":
		fallthrough
	case "UNKNOWN":
		fallthrough
	case "VERIFY":
		fallthrough
	case "VIEW":
		*e = UserActivityAction(v)
		return nil
	default:
		return fmt.Errorf("invalid value for UserActivityAction: %v", v)
	}
}

type UserActivity struct {
	Actor *Person `json:"actor,omitempty"`
	// Unix timestamp of the activity (in seconds since epoch UTC).
	Timestamp *int64 `json:"timestamp,omitempty"`
	// The action for the activity
	Action              *UserActivityAction `json:"action,omitempty"`
	AggregateVisitCount *CountInfo          `json:"aggregateVisitCount,omitempty"`
}

func (o *UserActivity) GetActor() *Person {
	if o == nil {
		return nil
	}
	return o.Actor
}

func (o *UserActivity) GetTimestamp() *int64 {
	if o == nil {
		return nil
	}
	return o.Timestamp
}

func (o *UserActivity) GetAction() *UserActivityAction {
	if o == nil {
		return nil
	}
	return o.Action
}

func (o *UserActivity) GetAggregateVisitCount() *CountInfo {
	if o == nil {
		return nil
	}
	return o.AggregateVisitCount
}
