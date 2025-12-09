"""Hook to fix multipart form file field names that incorrectly have '[]' suffix."""

from typing import Any, Dict, List, Tuple
from .types import SDKInitHook
from glean.api_client.httpclient import HttpClient
from glean.api_client.utils import forms


class MultipartFileFieldFixHook(SDKInitHook):
    """
    Fixes multipart form serialization where file field names incorrectly have '[]' suffix.

    Speakeasy sometimes generates code that adds '[]' to file field names in multipart forms,
    but this is incorrect. File fields should not have the array suffix, only regular form
    fields should use this convention.

    This hook patches the serialize_multipart_form function to fix the issue at the source.
    """

    def sdk_init(self, base_url: str, client: HttpClient) -> Tuple[str, HttpClient]:
        """Initialize the SDK and patch the multipart form serialization."""
        self._patch_multipart_serialization()
        return base_url, client

    def _patch_multipart_serialization(self):
        """Patch the serialize_multipart_form function to fix file field names."""
        # Store reference to original function
        original_serialize_multipart_form = forms.serialize_multipart_form

        def fixed_serialize_multipart_form(
            media_type: str, request: Any
        ) -> Tuple[str, Dict[str, Any], List[Tuple[str, Any]]]:
            """Fixed version of serialize_multipart_form that doesn't add '[]' to file field names."""
            # Call the original function
            result_media_type, form_data, files_list = (
                original_serialize_multipart_form(media_type, request)
            )

            # Fix file field names in the files list
            fixed_files = []
            for item in files_list:
                if isinstance(item, tuple) and len(item) >= 2:
                    field_name = item[0]
                    file_data = item[1]

                    # Remove '[]' suffix from file field names only
                    # We can identify file fields by checking if the data looks like file content
                    if field_name.endswith("[]") and self._is_file_field_data(
                        file_data
                    ):
                        fixed_field_name = field_name[:-2]  # Remove '[]' suffix
                        fixed_item = (fixed_field_name,) + item[1:]
                        fixed_files.append(fixed_item)
                    else:
                        fixed_files.append(item)
                else:
                    fixed_files.append(item)

            return result_media_type, form_data, fixed_files

        # Replace the original function with our fixed version
        forms.serialize_multipart_form = fixed_serialize_multipart_form

    def _is_file_field_data(self, file_data: Any) -> bool:
        """
        Determine if the data represents file field content.

        File fields typically have tuple format: (filename, content) or (filename, content, content_type)
        where content is bytes, file-like object, or similar.
        """
        if isinstance(file_data, tuple) and len(file_data) >= 2:
            # Check the structure: (filename, content, [optional content_type])
            filename = file_data[0]
            content = file_data[1]

            # If filename is empty, this is likely JSON content, not a file
            if filename == "":
                return False

            # File content is typically bytes, string, or file-like object
            # But exclude empty strings and None values
            if content is None or content == "":
                return False

            return (
                isinstance(content, (bytes, str))
                or hasattr(content, "read")  # File-like object
                or (
                    hasattr(content, "__iter__") and not isinstance(content, str)
                )  # Iterable but not string
            )
        return False
