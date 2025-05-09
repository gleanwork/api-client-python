// Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT.

package components

import (
	"encoding/json"
	"fmt"
)

type GetAnswerErrorErrorType string

const (
	GetAnswerErrorErrorTypeNoPermission GetAnswerErrorErrorType = "NO_PERMISSION"
	GetAnswerErrorErrorTypeInvalidID    GetAnswerErrorErrorType = "INVALID_ID"
)

func (e GetAnswerErrorErrorType) ToPointer() *GetAnswerErrorErrorType {
	return &e
}
func (e *GetAnswerErrorErrorType) UnmarshalJSON(data []byte) error {
	var v string
	if err := json.Unmarshal(data, &v); err != nil {
		return err
	}
	switch v {
	case "NO_PERMISSION":
		fallthrough
	case "INVALID_ID":
		*e = GetAnswerErrorErrorType(v)
		return nil
	default:
		return fmt.Errorf("invalid value for GetAnswerErrorErrorType: %v", v)
	}
}

type GetAnswerError struct {
	ErrorType    *GetAnswerErrorErrorType `json:"errorType,omitempty"`
	AnswerAuthor *Person                  `json:"answerAuthor,omitempty"`
}

func (o *GetAnswerError) GetErrorType() *GetAnswerErrorErrorType {
	if o == nil {
		return nil
	}
	return o.ErrorType
}

func (o *GetAnswerError) GetAnswerAuthor() *Person {
	if o == nil {
		return nil
	}
	return o.AnswerAuthor
}
