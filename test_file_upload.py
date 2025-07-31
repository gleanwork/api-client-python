#!/usr/bin/env python3
"""
Test script to verify the file upload fix works correctly.
"""

import os
import tempfile
from pprint import pprint

# Import the SDK
from glean.api_client import Glean, errors, models

# Create a test file
def create_test_file():
    """Create a temporary test file for upload."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write("This is a test file for Glean upload.\n")
        f.write("It contains some sample content.\n")
        return f.name

def test_file_upload():
    """Test the file upload functionality."""
    # Create a test file
    test_file_path = create_test_file()
    
    try:
        # Get API token from environment
        api_token = os.getenv("GLEAN_API_TOKEN")
        if not api_token:
            print("Error: GLEAN_API_TOKEN environment variable not set")
            return
        
        # Get instance from environment or use default
        instance = os.getenv("GLEAN_INSTANCE", "scio-prod")
        
        print(f"Testing file upload to instance: {instance}")
        print(f"Test file: {test_file_path}")
        
        with Glean(
            api_token=api_token,
            instance=instance,
        ) as glean:
            try:
                # Upload the file
                upload_response = glean.client.chat.upload_files(
                    files=[
                        models.File(
                            file_name=os.path.basename(test_file_path),
                            content=open(test_file_path, "rb"),
                            content_type="text/plain",
                        )
                    ]
                )
                
                print("✅ File upload successful!")
                print("Response:")
                pprint(upload_response)
                
            except errors.GleanError as e:
                print("❌ File upload failed!")
                print(f"Error: {e}")
                print(f"Status code: {e.status_code}")
                print(f"Raw response: {e.raw_response}")
                if hasattr(e, 'body'):
                    print(f"Response body: {e.body}")
                    
    finally:
        # Clean up the test file
        if os.path.exists(test_file_path):
            os.unlink(test_file_path)
            print(f"Cleaned up test file: {test_file_path}")

if __name__ == "__main__":
    test_file_upload()