#  coding: utf-8 
from dotenv import load_dotenv
import os
import requests
from requests.auth import HTTPBasicAuth
import json

load_dotenv()

# Jira configuration from environment variables
JIRA_URL = "https://yashwardhansahu.atlassian.net/rest/api/3/issue"
EMAIL = os.getenv("JIRA_EMAIL")
API_TOKEN = os.getenv("JIRA_API_TOKEN")
PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY")

# Headers for the Jira API request
HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

def create_issue_payload(summary, description, issue_type="Task"):
    """
    Generate the JSON payload for creating a Jira ticket with description in ADF
    """
    return json.dumps({
        "fields": {
            "project": {
                "key": PROJECT_KEY
            },
            "summary": summary,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text",
                                "text": description
                            }
                        ]
                    }
                ]
            },
            "issuetype": {
                "name": issue_type  # e.g., Bug, Task, Story
            }
        }
    })

def create_jira_ticket(summary, description):
    """
    Create a Jira ticket using the Jira REST API
    """
    payload = create_issue_payload(summary, description)

    auth = HTTPBasicAuth(EMAIL, API_TOKEN)

    # Send the POST request to the Jira API
    response = requests.post(
        JIRA_URL,
        headers=HEADERS,
        data=payload,
        auth=auth
    )

    if response.status_code == 201:
        print("✅ Jira ticket created successfully!")
        print("Ticket URL:", response.json()['self'])
    else:
        print("❌ Failed to create Jira ticket")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

if __name__ == "__main__":
    # You can change the ticket details as needed
    summary = "Server CPU Usage Exceeded Threshold"
    description = "The CPU usage on production server exceeded 90%. Please investigate."
    
    create_jira_ticket(summary, description)