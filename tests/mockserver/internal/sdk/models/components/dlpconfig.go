// Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT.

package components

// DlpConfig - Detailed configuration of what documents and sensitive content will be scanned.
type DlpConfig struct {
	// Synonymous with report/policy id.
	Version *int64 `json:"version,omitempty"`
	// DEPRECATED - use `sensitiveContentOptions` instead.
	//
	// Deprecated: This will be removed in a future release, please migrate away from it as soon as possible.
	SensitiveInfoTypes []SensitiveInfoType `json:"sensitiveInfoTypes,omitempty"`
	// Controls which data-sources and what time-range to include in scans.
	InputOptions *InputOptions `json:"inputOptions,omitempty"`
	// Deprecated: This will be removed in a future release, please migrate away from it as soon as possible.
	ExternalSharingOptions *ExternalSharingOptions `json:"externalSharingOptions,omitempty"`
	// Controls how "shared" a document must be to get picked for scans.
	BroadSharingOptions *SharingOptions `json:"broadSharingOptions,omitempty"`
	// Options for defining sensitive content within scanned documents.
	SensitiveContentOptions *SensitiveContentOptions `json:"sensitiveContentOptions,omitempty"`
	ReportName              *string                  `json:"reportName,omitempty"`
	// Interval between scans.
	Frequency *string `json:"frequency,omitempty"`
	// Details about the person who created this report/policy.
	CreatedBy *DlpPerson `json:"createdBy,omitempty"`
	// Timestamp at which this configuration was created.
	CreatedAt *string `json:"createdAt,omitempty"`
	// redact quote in findings of the report
	RedactQuote *bool `json:"redactQuote,omitempty"`
	// auto hide documents with findings in the report
	AutoHideDocs *bool `json:"autoHideDocs,omitempty"`
	// Terms that are allow-listed during the scans. If any finding picked up by a rule exactly matches a term in the allow-list, it will not be counted as a violation.
	AllowlistOptions *AllowlistOptions `json:"allowlistOptions,omitempty"`
}

func (o *DlpConfig) GetVersion() *int64 {
	if o == nil {
		return nil
	}
	return o.Version
}

func (o *DlpConfig) GetSensitiveInfoTypes() []SensitiveInfoType {
	if o == nil {
		return nil
	}
	return o.SensitiveInfoTypes
}

func (o *DlpConfig) GetInputOptions() *InputOptions {
	if o == nil {
		return nil
	}
	return o.InputOptions
}

func (o *DlpConfig) GetExternalSharingOptions() *ExternalSharingOptions {
	if o == nil {
		return nil
	}
	return o.ExternalSharingOptions
}

func (o *DlpConfig) GetBroadSharingOptions() *SharingOptions {
	if o == nil {
		return nil
	}
	return o.BroadSharingOptions
}

func (o *DlpConfig) GetSensitiveContentOptions() *SensitiveContentOptions {
	if o == nil {
		return nil
	}
	return o.SensitiveContentOptions
}

func (o *DlpConfig) GetReportName() *string {
	if o == nil {
		return nil
	}
	return o.ReportName
}

func (o *DlpConfig) GetFrequency() *string {
	if o == nil {
		return nil
	}
	return o.Frequency
}

func (o *DlpConfig) GetCreatedBy() *DlpPerson {
	if o == nil {
		return nil
	}
	return o.CreatedBy
}

func (o *DlpConfig) GetCreatedAt() *string {
	if o == nil {
		return nil
	}
	return o.CreatedAt
}

func (o *DlpConfig) GetRedactQuote() *bool {
	if o == nil {
		return nil
	}
	return o.RedactQuote
}

func (o *DlpConfig) GetAutoHideDocs() *bool {
	if o == nil {
		return nil
	}
	return o.AutoHideDocs
}

func (o *DlpConfig) GetAllowlistOptions() *AllowlistOptions {
	if o == nil {
		return nil
	}
	return o.AllowlistOptions
}
