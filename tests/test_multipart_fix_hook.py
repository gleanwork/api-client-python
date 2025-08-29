"""Test for the multipart file field fix hook."""

from unittest.mock import Mock, patch

import pytest

from src.glean.api_client._hooks.multipart_fix_hook import MultipartFileFieldFixHook
from src.glean.api_client.httpclient import HttpClient


class TestMultipartFileFieldFixHook:
    """Test cases for the MultipartFileFieldFixHook."""

    def setup_method(self):
        """Set up test fixtures."""
        self.hook = MultipartFileFieldFixHook()
        self.mock_client = Mock(spec=HttpClient)

    def test_sdk_init_returns_unchanged_params(self):
        """Test that SDK init returns the same base_url and client."""
        base_url = "https://api.example.com"

        with patch.object(self.hook, "_patch_multipart_serialization"):
            result_url, result_client = self.hook.sdk_init(base_url, self.mock_client)

            assert result_url == base_url
            assert result_client == self.mock_client

    def test_sdk_init_calls_patch_function(self):
        """Test that SDK init calls the patch function."""
        base_url = "https://api.example.com"

        with patch.object(self.hook, "_patch_multipart_serialization") as mock_patch:
            self.hook.sdk_init(base_url, self.mock_client)
            mock_patch.assert_called_once()

    def test_is_file_field_data_identifies_file_content(self):
        """Test the file field data identification logic."""
        # Test file field formats
        assert self.hook._is_file_field_data(("test.txt", b"content"))
        assert self.hook._is_file_field_data(("test.txt", b"content", "text/plain"))
        assert self.hook._is_file_field_data(("test.txt", "string content"))

        # Test with file-like object
        mock_file = Mock()
        mock_file.read = Mock()
        assert self.hook._is_file_field_data(("test.txt", mock_file))

        # Test non-file field formats
        assert not self.hook._is_file_field_data("regular_value")
        assert not self.hook._is_file_field_data(123)
        assert not self.hook._is_file_field_data(("single_item",))
        assert not self.hook._is_file_field_data((None, None))

    @patch("src.glean.api_client._hooks.multipart_fix_hook.forms")
    def test_patch_multipart_serialization_replaces_function(self, mock_forms_module):
        """Test that the patching replaces the serialize_multipart_form function."""
        # Mock the original function
        original_function = Mock()
        mock_forms_module.serialize_multipart_form = original_function

        # Call the patch method
        self.hook._patch_multipart_serialization()

        # Verify that the function was replaced
        assert mock_forms_module.serialize_multipart_form != original_function

    @patch("src.glean.api_client._hooks.multipart_fix_hook.forms")
    def test_patched_function_fixes_file_field_names(self, mock_forms_module):
        """Test that the patched function correctly fixes file field names."""
        # Mock original function to return data with '[]' suffix
        original_function = Mock()
        original_function.return_value = (
            "multipart/form-data",
            {"regular_field": "value"},
            [
                ("file[]", ("test.txt", b"file content", "text/plain")),
                ("documents[]", ("doc.pdf", b"pdf content", "application/pdf")),
                ("regular_array[]", "regular_value"),  # This should not be changed
            ],
        )
        mock_forms_module.serialize_multipart_form = original_function

        # Apply the patch
        self.hook._patch_multipart_serialization()

        # Get the patched function
        patched_function = mock_forms_module.serialize_multipart_form

        # Call the patched function
        media_type, form_data, files_list = patched_function(
            "multipart/form-data", Mock()
        )

        # Verify the results
        assert media_type == "multipart/form-data"
        assert form_data == {"regular_field": "value"}

        # Check that file field names are fixed but regular fields are not
        expected_files = [
            ("file", ("test.txt", b"file content", "text/plain")),
            ("documents", ("doc.pdf", b"pdf content", "application/pdf")),
            ("regular_array[]", "regular_value"),  # Should remain unchanged
        ]
        assert files_list == expected_files

    @patch("src.glean.api_client._hooks.multipart_fix_hook.forms")
    def test_patched_function_preserves_correct_names(self, mock_forms_module):
        """Test that the patched function preserves already correct field names."""
        # Mock original function to return data without '[]' suffix
        original_function = Mock()
        original_function.return_value = (
            "multipart/form-data",
            {},
            [
                ("file", ("test.txt", b"file content", "text/plain")),
                ("document", ("doc.pdf", b"pdf content", "application/pdf")),
            ],
        )
        mock_forms_module.serialize_multipart_form = original_function

        # Apply the patch
        self.hook._patch_multipart_serialization()

        # Get the patched function
        patched_function = mock_forms_module.serialize_multipart_form

        # Call the patched function
        media_type, form_data, files_list = patched_function(
            "multipart/form-data", Mock()
        )

        # Verify that nothing was changed
        expected_files = [
            ("file", ("test.txt", b"file content", "text/plain")),
            ("document", ("doc.pdf", b"pdf content", "application/pdf")),
        ]
        assert files_list == expected_files

    @patch("src.glean.api_client._hooks.multipart_fix_hook.forms")
    def test_patched_function_handles_mixed_fields(self, mock_forms_module):
        """Test handling of mixed file and non-file fields."""
        # Mock original function with mixed field types
        original_function = Mock()
        original_function.return_value = (
            "multipart/form-data",
            {"form_field": "value"},
            [
                ("correct_file", ("test1.txt", b"content1", "text/plain")),
                ("wrong_file[]", ("test2.txt", b"content2", "text/plain")),
                ("form_array[]", "form_value"),  # Regular form field, should keep []
                (
                    "json_field[]",
                    ("", '{"key": "value"}', "application/json"),
                ),  # JSON field, might need []
            ],
        )
        mock_forms_module.serialize_multipart_form = original_function

        # Apply the patch
        self.hook._patch_multipart_serialization()

        # Get the patched function
        patched_function = mock_forms_module.serialize_multipart_form

        # Call the patched function
        media_type, form_data, files_list = patched_function(
            "multipart/form-data", Mock()
        )

        # Verify the results - only actual file fields should have [] removed
        expected_files = [
            ("correct_file", ("test1.txt", b"content1", "text/plain")),
            ("wrong_file", ("test2.txt", b"content2", "text/plain")),  # Fixed
            ("form_array[]", "form_value"),  # Preserved - not a file field
            (
                "json_field[]",
                ("", '{"key": "value"}', "application/json"),
            ),  # Preserved - JSON content
        ]
        assert files_list == expected_files

    def test_file_field_detection_edge_cases(self):
        """Test edge cases for file field detection."""
        # Empty content
        assert not self.hook._is_file_field_data(("test.txt", ""))

        # None content
        assert not self.hook._is_file_field_data(("test.txt", None))

        # List/tuple content (should be considered file-like)
        assert self.hook._is_file_field_data(("test.txt", [1, 2, 3]))
        assert self.hook._is_file_field_data(("test.txt", (1, 2, 3)))

        # String content (should be considered file content)
        assert self.hook._is_file_field_data(("test.txt", "string content"))

        # But not if it's the first element
        assert not self.hook._is_file_field_data(("string content",))


if __name__ == "__main__":
    pytest.main([__file__])
