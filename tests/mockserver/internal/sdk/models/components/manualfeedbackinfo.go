// Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT.

package components

import (
	"encoding/json"
	"fmt"
)

// ManualFeedbackInfoSource - The source associated with the Feedback.event.MANUAL_FEEDBACK event.
type ManualFeedbackInfoSource string

const (
	ManualFeedbackInfoSourceAutocomplete       ManualFeedbackInfoSource = "AUTOCOMPLETE"
	ManualFeedbackInfoSourceCalendar           ManualFeedbackInfoSource = "CALENDAR"
	ManualFeedbackInfoSourceChat               ManualFeedbackInfoSource = "CHAT"
	ManualFeedbackInfoSourceChatGeneral        ManualFeedbackInfoSource = "CHAT_GENERAL"
	ManualFeedbackInfoSourceConceptCard        ManualFeedbackInfoSource = "CONCEPT_CARD"
	ManualFeedbackInfoSourceDesktopApp         ManualFeedbackInfoSource = "DESKTOP_APP"
	ManualFeedbackInfoSourceDisambiguationCard ManualFeedbackInfoSource = "DISAMBIGUATION_CARD"
	ManualFeedbackInfoSourceExpertDetection    ManualFeedbackInfoSource = "EXPERT_DETECTION"
	ManualFeedbackInfoSourceFeed               ManualFeedbackInfoSource = "FEED"
	ManualFeedbackInfoSourceGeneratedQAndA     ManualFeedbackInfoSource = "GENERATED_Q_AND_A"
	ManualFeedbackInfoSourceInlineMenu         ManualFeedbackInfoSource = "INLINE_MENU"
	ManualFeedbackInfoSourceNativeResult       ManualFeedbackInfoSource = "NATIVE_RESULT"
	ManualFeedbackInfoSourceQAndA              ManualFeedbackInfoSource = "Q_AND_A"
	ManualFeedbackInfoSourceRelatedQuestions   ManualFeedbackInfoSource = "RELATED_QUESTIONS"
	ManualFeedbackInfoSourceReportIssue        ManualFeedbackInfoSource = "REPORT_ISSUE"
	ManualFeedbackInfoSourceSciobot            ManualFeedbackInfoSource = "SCIOBOT"
	ManualFeedbackInfoSourceSearch             ManualFeedbackInfoSource = "SEARCH"
	ManualFeedbackInfoSourceSidebar            ManualFeedbackInfoSource = "SIDEBAR"
	ManualFeedbackInfoSourceSummary            ManualFeedbackInfoSource = "SUMMARY"
)

func (e ManualFeedbackInfoSource) ToPointer() *ManualFeedbackInfoSource {
	return &e
}
func (e *ManualFeedbackInfoSource) UnmarshalJSON(data []byte) error {
	var v string
	if err := json.Unmarshal(data, &v); err != nil {
		return err
	}
	switch v {
	case "AUTOCOMPLETE":
		fallthrough
	case "CALENDAR":
		fallthrough
	case "CHAT":
		fallthrough
	case "CHAT_GENERAL":
		fallthrough
	case "CONCEPT_CARD":
		fallthrough
	case "DESKTOP_APP":
		fallthrough
	case "DISAMBIGUATION_CARD":
		fallthrough
	case "EXPERT_DETECTION":
		fallthrough
	case "FEED":
		fallthrough
	case "GENERATED_Q_AND_A":
		fallthrough
	case "INLINE_MENU":
		fallthrough
	case "NATIVE_RESULT":
		fallthrough
	case "Q_AND_A":
		fallthrough
	case "RELATED_QUESTIONS":
		fallthrough
	case "REPORT_ISSUE":
		fallthrough
	case "SCIOBOT":
		fallthrough
	case "SEARCH":
		fallthrough
	case "SIDEBAR":
		fallthrough
	case "SUMMARY":
		*e = ManualFeedbackInfoSource(v)
		return nil
	default:
		return fmt.Errorf("invalid value for ManualFeedbackInfoSource: %v", v)
	}
}

type Issue string

const (
	IssueInaccurateResponse    Issue = "INACCURATE_RESPONSE"
	IssueIncompleteOrNoAnswer  Issue = "INCOMPLETE_OR_NO_ANSWER"
	IssueIncorrectCitation     Issue = "INCORRECT_CITATION"
	IssueMissingCitation       Issue = "MISSING_CITATION"
	IssueOther                 Issue = "OTHER"
	IssueOutdatedResponse      Issue = "OUTDATED_RESPONSE"
	IssueResultMissing         Issue = "RESULT_MISSING"
	IssueResultShouldNotAppear Issue = "RESULT_SHOULD_NOT_APPEAR"
	IssueResultsHelpful        Issue = "RESULTS_HELPFUL"
	IssueResultsPoorOrder      Issue = "RESULTS_POOR_ORDER"
	IssueTooMuchOneKind        Issue = "TOO_MUCH_ONE_KIND"
)

func (e Issue) ToPointer() *Issue {
	return &e
}
func (e *Issue) UnmarshalJSON(data []byte) error {
	var v string
	if err := json.Unmarshal(data, &v); err != nil {
		return err
	}
	switch v {
	case "INACCURATE_RESPONSE":
		fallthrough
	case "INCOMPLETE_OR_NO_ANSWER":
		fallthrough
	case "INCORRECT_CITATION":
		fallthrough
	case "MISSING_CITATION":
		fallthrough
	case "OTHER":
		fallthrough
	case "OUTDATED_RESPONSE":
		fallthrough
	case "RESULT_MISSING":
		fallthrough
	case "RESULT_SHOULD_NOT_APPEAR":
		fallthrough
	case "RESULTS_HELPFUL":
		fallthrough
	case "RESULTS_POOR_ORDER":
		fallthrough
	case "TOO_MUCH_ONE_KIND":
		*e = Issue(v)
		return nil
	default:
		return fmt.Errorf("invalid value for Issue: %v", v)
	}
}

// Vote - The vote associated with the Feedback.event.MANUAL_FEEDBACK event.
type Vote string

const (
	VoteUpvote   Vote = "UPVOTE"
	VoteDownvote Vote = "DOWNVOTE"
)

func (e Vote) ToPointer() *Vote {
	return &e
}
func (e *Vote) UnmarshalJSON(data []byte) error {
	var v string
	if err := json.Unmarshal(data, &v); err != nil {
		return err
	}
	switch v {
	case "UPVOTE":
		fallthrough
	case "DOWNVOTE":
		*e = Vote(v)
		return nil
	default:
		return fmt.Errorf("invalid value for Vote: %v", v)
	}
}

type ManualFeedbackInfo struct {
	// The email address of the user who submitted the Feedback.event.MANUAL_FEEDBACK event.
	Email *string `json:"email,omitempty"`
	// The source associated with the Feedback.event.MANUAL_FEEDBACK event.
	Source *ManualFeedbackInfoSource `json:"source,omitempty"`
	// The issue the user indicated in the feedback.
	//
	// Deprecated: This will be removed in a future release, please migrate away from it as soon as possible.
	Issue *string `json:"issue,omitempty"`
	// The issue(s) the user indicated in the feedback.
	Issues []Issue `json:"issues,omitempty"`
	// URLs of images uploaded by user when providing feedback
	ImageUrls []string `json:"imageUrls,omitempty"`
	// The query associated with the Feedback.event.MANUAL_FEEDBACK event.
	Query *string `json:"query,omitempty"`
	// The query associated with the Feedback.event.MANUAL_FEEDBACK event, but obscured such that the vowels are replaced with special characters. For search feedback events only.
	ObscuredQuery *string `json:"obscuredQuery,omitempty"`
	// Which tabs the user had chosen at the time of the Feedback.event.MANUAL_FEEDBACK event. For search feedback events only.
	ActiveTab *string `json:"activeTab,omitempty"`
	// The comments users can optionally add to the Feedback.event.MANUAL_FEEDBACK events.
	Comments *string `json:"comments,omitempty"`
	// The array of search result Glean Document IDs, ordered by top to bottom result.
	SearchResults []string `json:"searchResults,omitempty"`
	// The array of previous messages in a chat session, ordered by oldest to newest.
	PreviousMessages []string `json:"previousMessages,omitempty"`
	// Array of previous request/response exchanges, ordered by oldest to newest.
	ChatTranscript []FeedbackChatExchange `json:"chatTranscript,omitempty"`
	// How many times this query has been run in the past.
	NumQueriesFromFirstRun *int64 `json:"numQueriesFromFirstRun,omitempty"`
	// The vote associated with the Feedback.event.MANUAL_FEEDBACK event.
	Vote *Vote `json:"vote,omitempty"`
	// A rating associated with the user feedback. The value will be between one and the maximum given by ratingScale, inclusive.
	Rating *int64 `json:"rating,omitempty"`
	// A description of the rating that contextualizes how it appeared to the user, e.g. "satisfied".
	RatingKey *string `json:"ratingKey,omitempty"`
	// The scale of comparison for a rating associated with the feedback. Rating values start from one and go up to the maximum specified by ratingScale. For example, a five-option satisfaction rating will have a ratingScale of 5 and a thumbs-up/thumbs-down rating will have a ratingScale of 2.
	RatingScale *int64 `json:"ratingScale,omitempty"`
}

func (o *ManualFeedbackInfo) GetEmail() *string {
	if o == nil {
		return nil
	}
	return o.Email
}

func (o *ManualFeedbackInfo) GetSource() *ManualFeedbackInfoSource {
	if o == nil {
		return nil
	}
	return o.Source
}

func (o *ManualFeedbackInfo) GetIssue() *string {
	if o == nil {
		return nil
	}
	return o.Issue
}

func (o *ManualFeedbackInfo) GetIssues() []Issue {
	if o == nil {
		return nil
	}
	return o.Issues
}

func (o *ManualFeedbackInfo) GetImageUrls() []string {
	if o == nil {
		return nil
	}
	return o.ImageUrls
}

func (o *ManualFeedbackInfo) GetQuery() *string {
	if o == nil {
		return nil
	}
	return o.Query
}

func (o *ManualFeedbackInfo) GetObscuredQuery() *string {
	if o == nil {
		return nil
	}
	return o.ObscuredQuery
}

func (o *ManualFeedbackInfo) GetActiveTab() *string {
	if o == nil {
		return nil
	}
	return o.ActiveTab
}

func (o *ManualFeedbackInfo) GetComments() *string {
	if o == nil {
		return nil
	}
	return o.Comments
}

func (o *ManualFeedbackInfo) GetSearchResults() []string {
	if o == nil {
		return nil
	}
	return o.SearchResults
}

func (o *ManualFeedbackInfo) GetPreviousMessages() []string {
	if o == nil {
		return nil
	}
	return o.PreviousMessages
}

func (o *ManualFeedbackInfo) GetChatTranscript() []FeedbackChatExchange {
	if o == nil {
		return nil
	}
	return o.ChatTranscript
}

func (o *ManualFeedbackInfo) GetNumQueriesFromFirstRun() *int64 {
	if o == nil {
		return nil
	}
	return o.NumQueriesFromFirstRun
}

func (o *ManualFeedbackInfo) GetVote() *Vote {
	if o == nil {
		return nil
	}
	return o.Vote
}

func (o *ManualFeedbackInfo) GetRating() *int64 {
	if o == nil {
		return nil
	}
	return o.Rating
}

func (o *ManualFeedbackInfo) GetRatingKey() *string {
	if o == nil {
		return nil
	}
	return o.RatingKey
}

func (o *ManualFeedbackInfo) GetRatingScale() *int64 {
	if o == nil {
		return nil
	}
	return o.RatingScale
}
