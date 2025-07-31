#!/usr/bin/env python3
"""
Example showing the correct way to upload files using the Glean SDK.

This example demonstrates the fix for the file upload issue where the SDK
was incorrectly appending "[]" to field names in multipart form data.
"""

import os
from pprint import pprint
from glean.api_client import Glean, errors, models

def upload_file_example():
    """
    Example of uploading a file to Glean chat.
    
    This shows the correct usage pattern after the multipart form
    serialization fix.
    """
    
    # Configuration
    GLEAN_TOKEN = os.getenv("GLEAN_API_TOKEN")
    DOCUMENT_PATH = "test_input.txt"  # Your file path here
    
    if not GLEAN_TOKEN:
        print("Error: GLEAN_API_TOKEN environment variable not set")
        return
    
    if not os.path.exists(DOCUMENT_PATH):
        print(f"Error: File {DOCUMENT_PATH} does not exist")
        return
    
    print(f"Uploading file: {DOCUMENT_PATH}")
    
    with Glean(
        api_token=GLEAN_TOKEN,
        instance="scio-prod",
    ) as glean:
        try:
            # Upload the file using the corrected SDK
            upload_response = glean.client.chat.upload_files(
                files=[
                    models.File(
                        file_name=os.path.basename(DOCUMENT_PATH),
                        content=open(DOCUMENT_PATH, "rb"),
                        content_type="text/plain",
                    )
                ]
            )
            
            print("✅ File upload successful!")
            print("Upload response:")
            pprint(upload_response)
            
            # You can now use the uploaded file in chat
            print("\nFile uploaded successfully. You can now use it in chat conversations.")
            
        except errors.GleanError as e:
            print("❌ File upload failed!")
            print(f"Error: {e}")
            print(f"Status code: {e.status_code}")
            print(f"Raw response: {e.raw_response}")
            if hasattr(e, 'body'):
                print(f"Response body: {e.body}")

if __name__ == "__main__":
    upload_file_example()