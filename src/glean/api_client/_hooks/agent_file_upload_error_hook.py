"""Custom hook to provide helpful error messages for agent file upload issues."""

from typing import Optional, Tuple, Union
import httpx
from glean.api_client._hooks.types import AfterErrorContext, AfterErrorHook


class AgentFileUploadErrorHook(AfterErrorHook):
    """
    Hook that detects when users incorrectly pass file objects to agents.run()
    and provides clear guidance on the correct two-step upload workflow.

    This hook intercepts 400 errors from agent run operations that contain
    "permission" in the error message, which typically indicates a file was
    passed incorrectly instead of a file ID.
    """

    def after_error(
        self,
        hook_ctx: AfterErrorContext,
        response: Optional[httpx.Response],
        error: Optional[Exception],
    ) -> Union[Tuple[Optional[httpx.Response], Optional[Exception]], Exception]:
        """
        Intercept agent run errors and enhance them with helpful file upload guidance.

        Args:
            hook_ctx: Context about the operation being performed
            response: The HTTP response (if available)
            error: The exception that was raised

        Returns:
            Either a tuple of (response, error) to continue normal error handling,
            or a new Exception to replace the original error.
        """
        # Only intercept 400 errors from agent run operations
        if (
            response is not None
            and response.status_code == 400
            and hook_ctx.operation_id in ["createAndWaitRun", "createAndStreamRun"]
        ):
            error_message = str(error) if error else ""

            # Check if this looks like a file upload error
            # (API returns "permission" error when file objects are passed incorrectly)
            if "permission" in error_message.lower():
                # Create enhanced error message with clear instructions
                enhanced_message = (
                    "Agent file upload error: When using agents with file inputs, "
                    "you must follow a two-step process:\n"
                    "\n"
                    "1. First, upload files using client.chat.upload_files():\n"
                    "   from glean.api_client import models\n"
                    "   \n"
                    "   # Upload the file\n"
                    "   upload_result = client.chat.upload_files(\n"
                    "       files=[\n"
                    "           models.File(\n"
                    "               file_name='data.csv',\n"
                    "               content=file_content  # bytes or file-like object\n"
                    "           )\n"
                    "       ]\n"
                    "   )\n"
                    "\n"
                    "2. Then, pass the returned file IDs (not file objects) in the input field:\n"
                    "   result = client.agents.run(\n"
                    "       agent_id='<agent-id>',\n"
                    "       input={\n"
                    "           'my_file': upload_result.files[0].id  # Use the file ID string\n"
                    "       }\n"
                    "   )\n"
                    "\n"
                    "For a complete example, see: examples/agent_with_file_upload.py\n"
                    f"\nOriginal error: {error_message}"
                )

                # Return new exception with enhanced message
                return Exception(enhanced_message)

        # Pass through all other errors unchanged
        return response, error
