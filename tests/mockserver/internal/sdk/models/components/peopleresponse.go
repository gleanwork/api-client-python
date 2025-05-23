// Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT.

package components

type PeopleResponse struct {
	// A Person for each ID in the request, each with PersonMetadata populated.
	Results []Person `json:"results,omitempty"`
	// A list of documents related to this people response. This is only included if DOCUMENT_ACTIVITY is requested and only 1 person is included in the request.
	RelatedDocuments []RelatedDocuments `json:"relatedDocuments,omitempty"`
	// A list of IDs that could not be found.
	Errors []string `json:"errors,omitempty"`
}

func (o *PeopleResponse) GetResults() []Person {
	if o == nil {
		return nil
	}
	return o.Results
}

func (o *PeopleResponse) GetRelatedDocuments() []RelatedDocuments {
	if o == nil {
		return nil
	}
	return o.RelatedDocuments
}

func (o *PeopleResponse) GetErrors() []string {
	if o == nil {
		return nil
	}
	return o.Errors
}
