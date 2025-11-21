# To run the example:
# poetry install
# poetry run python examples/agent_with_file_upload.py

from glean.api_client import Glean, models
import os


def main():
    with Glean(
        api_token=os.getenv("GLEAN_API_TOKEN", ""),
        domain=os.getenv("GLEAN_DOMAIN", "customerName"),
    ) as glean:

        # 1. Upload the file first
        file_content = b"name,role\nAlice,Engineer\nBob,Manager"

        upload_result = glean.client.chat.upload_files(
            files=[
                models.File(
                    file_name="employees.csv",
                    content=file_content
                )
            ]
        )

        # 2. Get the ID (string) from the response
        file_id = upload_result.files[0].id

        # 3. Run the agent passing the file ID (NOT the file object)
        res = glean.client.agents.run(
            agent_id=os.getenv("GLEAN_AGENT_ID", "<agent-id>"),
            input={
                # Pass the file ID string to the input parameter
                "file": file_id,
                "query": "Who is the manager?"
            }
        )

        print(res)

if __name__ == "__main__":
    main()
