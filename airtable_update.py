import os
import requests
from typing import List

def get_candidates(base_id: str, api_key: str) -> List[dict]:
    """Fetch candidates in Stage 'Interviewing' from the Applicants table."""
    url = f"https://api.airtable.com/v0/{base_id}/Applicants"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    params = {
        "filterByFormula": "Stage='Interviewing'",
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json().get("records", [])

def update_candidate(base_id: str, api_key: str, record_id: str, attachment_url: str) -> None:
    """Attach a file and update the candidate stage."""
    url = f"https://api.airtable.com/v0/{base_id}/Applicants/{record_id}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {
        "fields": {
            "Attachments": [{"url": attachment_url}],
            "Stage": "Decision needed",
        }
    }
    response = requests.patch(url, headers=headers, json=data)
    response.raise_for_status()

def main() -> None:
    base_id = os.environ.get("AIRTABLE_BASE_ID")
    api_key = os.environ.get("AIRTABLE_API_KEY")
    attachment_url = os.environ.get("ATTACHMENT_URL", "https://example.com/file.pdf")

    if not base_id or not api_key:
        raise SystemExit("AIRTABLE_BASE_ID and AIRTABLE_API_KEY must be set")

    records = get_candidates(base_id, api_key)
    emails = []

    for record in records:
        fields = record.get("fields", {})
        email = fields.get("Email")
        if email:
            emails.append(email)
        record_id = record.get("id")
        if record_id:
            update_candidate(base_id, api_key, record_id, attachment_url)

    print("Processed emails:", emails)

if __name__ == "__main__":
    main()
