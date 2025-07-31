# File Upload Fix for Glean SDK

## Issue Description

The Glean SDK was failing to upload files with a 400 error, even though the same request worked correctly when sent via cURL. The issue was in the multipart form data serialization logic.

## Root Cause

The problem was in the `serialize_multipart_form` function in `src/glean/api_client/utils/forms.py`. When handling arrays of files, the code was incorrectly appending `"[]"` to the field name:

```python
# Before fix (incorrect)
files.append((f_name + "[]", (file_name, content, content_type)))
```

This caused the SDK to send field names like `"files[]"` instead of the expected `"files"`.

## The Fix

**File:** `src/glean/api_client/utils/forms.py`

**Change:** Removed the `"[]"` suffix when handling file arrays in multipart form serialization.

```python
# After fix (correct)
files.append((f_name, (file_name, content, content_type)))
```

## Why This Fixes the Issue

1. **Server Expectation**: The Glean API server expects file uploads with the field name `"files"` (as shown in the working cURL example: `--form files=@test_input.txt`)

2. **SDK Behavior**: The SDK was sending `"files[]"` instead of `"files"`, causing the server to reject the request with a 400 error.

3. **Array Handling**: The `"[]"` suffix was being added to indicate array fields, but for file uploads, each file in the array should use the base field name `"files"`.

## Testing the Fix

You can test the fix using the provided test script:

```bash
# Set your API token
export GLEAN_API_TOKEN="your-api-token-here"

# Run the test
python test_file_upload.py
```

## Correct Usage Pattern

After the fix, the correct usage pattern remains the same:

```python
from glean.api_client import Glean, errors, models

with Glean(
    api_token=GLEAN_TOKEN,
    instance="scio-prod",
) as glean:
    try:
        upload_response = glean.client.chat.upload_files(
            files=[
                models.File(
                    file_name="test_input.txt",
                    content=open(DOCUMENT_PATH, "rb"),
                    content_type="text/plain",
                )
            ]
        )
    except GleanError as e:
        print(f"Error uploading file: {e}")
        print(e.raw_response)
```

## Files Modified

1. `src/glean/api_client/utils/forms.py` - Fixed multipart form serialization
2. `test_file_upload.py` - Test script to verify the fix
3. `file_upload_example.py` - Example showing correct usage
4. `FILE_UPLOAD_FIX.md` - This documentation

## Impact

This fix resolves the 400 error when uploading files through the Glean SDK, making the SDK behavior consistent with direct API calls via cURL.