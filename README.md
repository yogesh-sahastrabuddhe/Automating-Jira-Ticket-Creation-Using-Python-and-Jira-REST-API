# Automating-Jira-Ticket-Creation-Using-Python-and-Jira-REST-API

> This article provides a Python script for creating Jira tickets via the Jira REST API, a popular tool for issue tracking, project management, and agile development, which can automate reporting incidents or tasks directly into Jira.

![License](https://img.shields.io/badge/license-Unlicense-green) ![Version](https://img.shields.io/badge/version-1.0.0-blue) ![Language](https://img.shields.io/badge/language-Python-yellow) ![GitHub](https://img.shields.io/badge/GitHub-yogesh-sahastrabuddhe/Automating-Jira-Ticket-Creation-Using-Python-and-Jira-REST-API-black?logo=github) ![Build Status](https://img.shields.io/github/actions/workflow/status/yogesh-sahastrabuddhe/Automating-Jira-Ticket-Creation-Using-Python-and-Jira-REST-API/ci.yml?branch=main)

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Prerequisites](#custom-1758209867853)
- [Code overview](#custom-1758209968930)
- [Troubleshooting](#custom-1758210104272)

## ℹ️ Project Information

- **👤 Author:** yogesh-sahastrabuddhe
- **📦 Version:** 1.0.0
- **📄 License:** Unlicense
- **📂 Repository:** [https://github.com/yogesh-sahastrabuddhe/Automating-Jira-Ticket-Creation-Using-Python-and-Jira-REST-API](https://github.com/yogesh-sahastrabuddhe/Automating-Jira-Ticket-Creation-Using-Python-and-Jira-REST-API)
- **🏷️ Keywords:** automation, python, Jira, issue ticket creation

## Features

- Create Jira tickets with customizable summaries and descriptions
- Supports different issue types such as Task, Bug, or Story
- Uses JSON payload formatted for Jira's Atlassian Document Format (ADF)
- Securely manages credentials with environment variables (`.env` file)

## Installation


1. Clone this repository or download the script file.

2. Install required Python libraries: pip install python-dotenv requests

3.  Create a `.env` file in the project directory with the following variables : JIRA_EMAIL=your-email@example.com   JIRA_API_TOKEN=your_api_token_here
      
      JIRA_PROJECT_KEY=PROJECTKEY


- Replace `your-email@example.com` with your Jira login email.
- Generate an API token from [Atlassian API Tokens](https://id.atlassian.com/manage-profile/security/api-tokens) and paste it here.
- Replace `PROJECTKEY` with your Jira project key from project settings.

## Usage

Run the Python script `jira_ticket_creator.py` to create a Jira ticket:

By default, the script will create a ticket with the following details:

- **Summary:** Server CPU Usage Exceeded Threshold
- **Description:** The CPU usage on production server exceeded 90%. Please investigate.

You can customize the summary and description inside the `__main__` block of the script.

## Code Overview

The script uses the following key functions:

- `create_issue_payload(summary, description, issue_type="Task")`  
  Generates the JSON payload for Jira ticket creation in ADF format.

- `create_jira_ticket(summary, description)`  
  Sends a POST request to the Jira API endpoint using the credentials from the environment.

## Troubleshooting

- Ensure your network allows HTTPS requests to https://your-domain.atlassian.net
- Verify that your API token and email in `.env` are correct
- The Jira user must have permissions to create issues in the project

## License

This project is licensed under the MIT License.

---

For more information on Jira API usage, visit the [Atlassian Jira REST API documentation](https://developer.atlassian.com/server/jira/platform/jira-rest-api-examples/).


## Usage

Run the Python script jira_ticket_creator.py to create a Jira ticket:

By default, the script will create a ticket with the following details:

Summary: Server CPU Usage Exceeded Threshold
Description: The CPU usage on production server exceeded 90%. Please investigate.
You can customize the summary and description inside the __main__ block of the script.

## Prerequisites


- Python 3.x installed on your system
- A Jira Cloud account with permissions to create issues
- Jira API token generated from your Atlassian account
- `pip` package manager for Python libraries

## Code overview

The script uses the following key functions:

- `create_issue_payload(summary, description, issue_type="Task")`  
  Generates the JSON payload for Jira ticket creation in ADF format.

- `create_jira_ticket(summary, description)`  
  Sends a POST request to the Jira API endpoint using the credentials from the environment.


## Troubleshooting

- Ensure your network allows HTTPS requests to https://your-domain.atlassian.net
- Verify that your API token and email in `.env` are correct
- The Jira user must have permissions to create issues in the project
- If you encounter errors related to UTF-8 encoding (e.g., "UnicodeDecodeError" or "Invalid UTF-8 middle byte"), please note:
  - This usually happens due to special or non-ASCII characters in the summary or description fields.
  - Ensure your Python script and terminal/editor use UTF-8 encoding.
  - You may need to handle or sanitize special characters before sending data to Jira.
  - Sometimes, the Jira API or server may have issues with certain UTF-8 bytes; try removing or replacing problematic characters.
  - If needed, you can explicitly encode strings in UTF-8 using Python’s `encode('utf-8')` method before sending requests.

If you continue to face encoding issues, reviewing Jira API documentation or consulting Atlassian support can help resolve specific encoding constraints.


