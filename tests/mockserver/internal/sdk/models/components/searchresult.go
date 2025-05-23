// Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT.

package components

type SearchResult struct {
	// An array of entities in the work graph retrieved via a data request.
	StructuredResults []StructuredResult `json:"structuredResults,omitempty"`
	// An opaque token that represents this particular result in this particular query. To be used for /feedback reporting.
	TrackingToken *string   `json:"trackingToken,omitempty"`
	Document      *Document `json:"document,omitempty"`
	Title         *string   `json:"title,omitempty"`
	URL           string    `json:"url"`
	// A deep link, if available, into the datasource's native application for the user's platform (e.g. slack://...).
	NativeAppURL *string `json:"nativeAppUrl,omitempty"`
	// Text content from the result document which contains search query terms, if available.
	Snippets []SearchResultSnippet `json:"snippets,omitempty"`
	// The full body text of the result if not already contained in the snippets. Only populated for conversation results (e.g. results from a messaging app such as Slack).
	FullText *string `json:"fullText,omitempty"`
	// The full body text of the result if not already contained in the snippets; each item in the array represents a separate line in the original text. Only populated for conversation results (e.g. results from a messaging app such as Slack).
	FullTextList []string `json:"fullTextList,omitempty"`
	// A list of results related to this search result. Eg. for conversation results it contains individual messages from the conversation document which will be shown on SERP.
	RelatedResults []RelatedDocuments `json:"relatedResults,omitempty"`
	// A list of results that should be displayed as associated with this result.
	ClusteredResults []SearchResult `json:"clusteredResults,omitempty"`
	// A list of results that should be displayed as associated with this result.
	AllClusteredResults []ClusterGroup `json:"allClusteredResults,omitempty"`
	// The total number of attachments.
	AttachmentCount *int64 `json:"attachmentCount,omitempty"`
	// A (potentially partial) list of results representing documents attached to the main result document.
	Attachments []SearchResult `json:"attachments,omitempty"`
	// A list of results that should be displayed as backlinks of this result in reverse chronological order.
	BacklinkResults []SearchResult `json:"backlinkResults,omitempty"`
	// The reason for inclusion of clusteredResults.
	ClusterType            *ClusterTypeEnum     `json:"clusterType,omitempty"`
	MustIncludeSuggestions *QuerySuggestionList `json:"mustIncludeSuggestions,omitempty"`
	QuerySuggestion        *QuerySuggestion     `json:"querySuggestion,omitempty"`
	// The level of visual distinction that should be given to a result.
	//
	Prominence *SearchResultProminenceEnum `json:"prominence,omitempty"`
	// Additional context for the relationship between the result and the document it's attached to.
	AttachmentContext *string `json:"attachmentContext,omitempty"`
	// A list of pins associated with this search result.
	Pins []PinDocument `json:"pins,omitempty"`
}

func (o *SearchResult) GetStructuredResults() []StructuredResult {
	if o == nil {
		return nil
	}
	return o.StructuredResults
}

func (o *SearchResult) GetTrackingToken() *string {
	if o == nil {
		return nil
	}
	return o.TrackingToken
}

func (o *SearchResult) GetDocument() *Document {
	if o == nil {
		return nil
	}
	return o.Document
}

func (o *SearchResult) GetTitle() *string {
	if o == nil {
		return nil
	}
	return o.Title
}

func (o *SearchResult) GetURL() string {
	if o == nil {
		return ""
	}
	return o.URL
}

func (o *SearchResult) GetNativeAppURL() *string {
	if o == nil {
		return nil
	}
	return o.NativeAppURL
}

func (o *SearchResult) GetSnippets() []SearchResultSnippet {
	if o == nil {
		return nil
	}
	return o.Snippets
}

func (o *SearchResult) GetFullText() *string {
	if o == nil {
		return nil
	}
	return o.FullText
}

func (o *SearchResult) GetFullTextList() []string {
	if o == nil {
		return nil
	}
	return o.FullTextList
}

func (o *SearchResult) GetRelatedResults() []RelatedDocuments {
	if o == nil {
		return nil
	}
	return o.RelatedResults
}

func (o *SearchResult) GetClusteredResults() []SearchResult {
	if o == nil {
		return nil
	}
	return o.ClusteredResults
}

func (o *SearchResult) GetAllClusteredResults() []ClusterGroup {
	if o == nil {
		return nil
	}
	return o.AllClusteredResults
}

func (o *SearchResult) GetAttachmentCount() *int64 {
	if o == nil {
		return nil
	}
	return o.AttachmentCount
}

func (o *SearchResult) GetAttachments() []SearchResult {
	if o == nil {
		return nil
	}
	return o.Attachments
}

func (o *SearchResult) GetBacklinkResults() []SearchResult {
	if o == nil {
		return nil
	}
	return o.BacklinkResults
}

func (o *SearchResult) GetClusterType() *ClusterTypeEnum {
	if o == nil {
		return nil
	}
	return o.ClusterType
}

func (o *SearchResult) GetMustIncludeSuggestions() *QuerySuggestionList {
	if o == nil {
		return nil
	}
	return o.MustIncludeSuggestions
}

func (o *SearchResult) GetQuerySuggestion() *QuerySuggestion {
	if o == nil {
		return nil
	}
	return o.QuerySuggestion
}

func (o *SearchResult) GetProminence() *SearchResultProminenceEnum {
	if o == nil {
		return nil
	}
	return o.Prominence
}

func (o *SearchResult) GetAttachmentContext() *string {
	if o == nil {
		return nil
	}
	return o.AttachmentContext
}

func (o *SearchResult) GetPins() []PinDocument {
	if o == nil {
		return nil
	}
	return o.Pins
}
