// Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT.

package components

// Share - Search endpoint will only fill out numDays ago since that's all we need to display shared badge; docmetadata endpoint will fill out all the fields so that we can display shared badge tooltip
type Share struct {
	// The number of days that has passed since the share happened
	NumDaysAgo      int64     `json:"numDaysAgo"`
	Sharer          *Person   `json:"sharer,omitempty"`
	SharingDocument *Document `json:"sharingDocument,omitempty"`
}

func (o *Share) GetNumDaysAgo() int64 {
	if o == nil {
		return 0
	}
	return o.NumDaysAgo
}

func (o *Share) GetSharer() *Person {
	if o == nil {
		return nil
	}
	return o.Sharer
}

func (o *Share) GetSharingDocument() *Document {
	if o == nil {
		return nil
	}
	return o.SharingDocument
}
