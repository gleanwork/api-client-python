# DlpExportFindingsRequestExportType

The type of export to perform. FINDINGS, DOCUMENTS and ISSUES produce JSONL; FINDINGS_CSV produces one CSV row per finding.

## Example Usage

```python
from glean.api_client.models import DlpExportFindingsRequestExportType

value = DlpExportFindingsRequestExportType.FINDINGS
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `FINDINGS`     | FINDINGS       |
| `DOCUMENTS`    | DOCUMENTS      |
| `ISSUES`       | ISSUES         |
| `FINDINGS_CSV` | FINDINGS_CSV   |