# Airtable Applicant Updater

This script interacts with the Airtable API to find applicants in the
"Applicants" table whose `Stage` is **Interviewing**. For every matching
record it stores the email address, uploads a file to the `Attachments`
column and sets the `Stage` to **Decision needed**.

## Requirements

- Python 3.11
- `requests` library (install with `pip install requests` if needed)

## Environment variables

- `AIRTABLE_API_KEY` – your Airtable API key or personal access token
- `AIRTABLE_BASE_ID` – the base ID for "Simple applicant tracker"
- `ATTACHMENT_URL` – URL of the file to attach (defaults to a placeholder)

## Running

```bash
python3 airtable_update.py
```

The script prints the list of processed email addresses when finished.
