# Screen and Score Resumes from Gmail to Sheets with AI

**[View Template](https://n8n.io/workflows/3546-/)**  **Published Date:** 04/14/2025  **Created By:** Aditya Sharma  **Categories:** `Data & Storage` `Productivity` `AI` `Langchain`  

## Template Description

Description

This intelligent n8n automation streamlines the process of collecting, extracting, and scoring resumes sent to a Gmail inbox—making it an ideal solution for recruiters who regularly receive hundreds of applications. The workflow scans incoming emails with attachments, extracts relevant candidate information from resumes using AI, evaluates each candidate based on customizable criteria, and logs their scores alongside contact details in a connected Google Sheet.

Who Is This For?

Recruiters & Hiring Managers**: Automate the resume screening process and save hours of manual work.
HR Teams at Startups & SMBs**: Quickly evaluate talent without needing large HR ops infrastructure.
Agencies & Talent Acquisition Firms**: Screen large volumes of resumes efficiently and with consistent criteria.
Solo Founders Hiring for Roles**: Use AI to help score and shortlist top candidates from email applications.

What Problem Does This Workflow Solve?

Manually reviewing resumes is time-consuming, error-prone, and inconsistent. This workflow solves these challenges by:

Automatically detecting and extracting resumes from Gmail attachments.
Using OpenAI to intelligently extract candidate info from unstructured PDFs.
Scoring resumes using customizable evaluation criteria (e.g., relevant experience, skills, education).
Logging all candidate data (Name, Email, LinkedIn, Score) in a centralized, filterable Google Sheet.
Enabling faster, fairer, and more efficient candidate screening.

How It Works

1. Gmail Trigger
Runs on a scheduled interval (e.g., every 6 or 24 hours).
Scans a connected Gmail inbox (using OAuth credentials) for unread emails that contain PDF attachments.

2. Extract Attachments
Downloads the attached resumes from matching emails.

3. Parse Resume Text
Sends the PDF file to OpenAI's API (via GPT-4 or GPT-3.5 with file support or via base64 + PDF-to-text tool).
Prompts GPT with a structured format to extract fields like Name, Email, LinkedIn, Skills, and Education.

4. Score Resume
Evaluates the resume on predefined scoring logic using AI or logic inside the workflow (e.g., "Has X skill = +10 points").

5. Log to Google Sheets
Appends a new row in a connected Google Sheet, including:
  Candidate Name
  Email Address
  LinkedIn URL
  Resume Score

Setup

Accounts & API Keys
You’ll need accounts and credentials for:

n8n** (hosted or self-hosted)
Google Cloud Platform** (for Gmail, Drive, and Sheets APIs)
OpenAI** (for GPT model access)

Google Sheet
Make a Google Sheet and connect it via Google Sheets node in n8n. Columns should include:
  Name
  Email
  LinkedIn
  Score

Configuration

Google Cloud:
Enable Gmail API and Google Sheets API.
Set up OAuth 2.0 Credentials in Google Console.
Connect n8n Gmail, Drive, and Sheets nodes to these credentials.

OpenAI:
Generate an API Key.
Use the HTTP Request node or official OpenAI node to send prompt requests.

n8n Workflow:
Add Gmail Trigger.
Add extraction logic (e.g., filter PDFs).
Add OpenAI prompt for resume parsing and scoring.
Connect structured output to a Google Sheets node.

Requirements

Accounts:
n8n**
Google** (Gmail, Sheets, Drive, Cloud Console)
OpenAI**

API Keys & Credentials:
OpenAI API Key
Google Cloud OAuth Credentials
Gmail Access Scopes (for reading attachments)
Configured Google Sheet
OpenAI usage (after free tier)
Google Cloud API usage (if exceeding free quota)


## Template JSON

```
{
  "meta": {
    "instanceId": "ddc2592f2c048b3a9255de9457632cead183ed1f8d682593ea74c5b20f968a76",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "53cc8017-5310-4205-85e0-8cc839693601",
      "name": "Structured Output Parser",
      "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
      "position": [
        720,
        400
      ],
      "parameters": {
        "schemaType": "manual",
        "inputSchema": "{\n\t\"type\": \"object\",\n\t\"properties\": {\n\t\t\"name\": {\n\t\t\t\"type\": \"string\"\n\t\t},\n      \"email\": {\n\t\t\t\"type\": \"string\"\n\t\t},\n      \"linkedin\": {\n\t\t\t\"type\": \"string\"\n\t\t},\n      \"score\": {\n\t\t\t\"type\": \"string\"\n\t\t}\n\t\t\n\t}\n}"
      },
      "typeVersion": 1.2
    },
    {
      "id": "ea0c00d3-25c8-4523-88ff-d61d6665ecf7",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -760,
        160
      ],
      "parameters": {
        "width": 480,
        "height": 260,
        "content": "## Resume Screener from Gmail to Sheets\n\n### \ud83d\udcc3Before you get started, you'll need:\n- [n8n installation](https://n8n.partnerlinks.io/n8nTTVideoGenTemplate) \n- [OpenAI API Key](https://platform.openai.com/api-keys)\n- Google Sheets API enabled in [Google Cloud Console](https://console.cloud.google.com/apis/api/sheets.googleapis.com/overview)\n- Google Drive API enabled in [Google Cloud Console](https://console.cloud.google.com/apis/api/drive.googleapis.com/overview)\n- OAuth 2.0 Client ID and Client Secret from your [Google Cloud Console Credentials](https://console.cloud.google.com/apis/credentials)\n"
      },
      "typeVersion": 1
    },
    {
      "id": "e4f3aef9-750a-48bb-899b-bd4a810032f2",
      "name": "Extract text from PDF File",
      "type": "n8n-nodes-base.extractFromFile",
      "position": [
        320,
        180
      ],
      "parameters": {
        "options": {},
        "operation": "pdf",
        "binaryPropertyName": "attachment_0"
      },
      "typeVersion": 1
    },
    {
      "id": "5418cfae-25da-4f58-99ef-d6957d8819a8",
      "name": "AI Agent to evaluate Resume",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        540,
        180
      ],
      "parameters": {
        "text": "=Here is the resume:\n\n{{ $json.text }}",
        "options": {
          "systemMessage": "You are an invaluable assistant. You were given a resume. You have to help me analyze the resume and give it a score based on the details available in the resume. Also, extract the name, email, and LinkedIn profile from the resume."
        },
        "promptType": "define",
        "hasOutputParser": true
      },
      "typeVersion": 1.8
    },
    {
      "id": "dce8e431-9d5c-4aa1-a0eb-c2a27de2d7f9",
      "name": "OpenAI Chat Model (GPT 4o-mini)",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        520,
        400
      ],
      "parameters": {
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o-mini"
        },
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "PMxepoh6OuVxbpg1",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "e7fdaf75-11ad-40c2-84a0-13c52f6f2eb1",
      "name": "Add Resume Evaluation to Google Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        920,
        180
      ],
      "parameters": {
        "columns": {
          "value": {
            "Name": "={{ $json.output.name }}",
            "Email": "={{ $json.output.email }}",
            "Score": "={{ $json.output.score }}",
            "LinkedIn": "={{ $json.output.linkedin }}",
            "Resume text": "={{ $('Extract text from PDF File').item.json.text }}"
          },
          "schema": [
            {
              "id": "Name",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Name",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Email",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Email",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "LinkedIn",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "LinkedIn",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Score",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Score",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Resume text",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Resume text",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {
          "useAppend": true
        },
        "operation": "append",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": 781640061,
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1SGYsuJI2YJVztZZmSLsFZ0lbUHnxm0V9r3c8S5-2q74/edit#gid=781640061",
          "cachedResultName": "Resume Score"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1SGYsuJI2YJVztZZmSLsFZ0lbUHnxm0V9r3c8S5-2q74",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1SGYsuJI2YJVztZZmSLsFZ0lbUHnxm0V9r3c8S5-2q74/edit?usp=drivesdk",
          "cachedResultName": "Lead Generation"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "kzZGQmdAV5cPfymZ",
          "name": "Google Sheets (server@hic)"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "0ad65e2b-665d-4b77-a941-b15a7ffbfb89",
      "name": "Trigger on new Email Received",
      "type": "n8n-nodes-base.gmailTrigger",
      "position": [
        60,
        180
      ],
      "parameters": {
        "simple": false,
        "filters": {
          "q": "has:attachment",
          "labelIds": [
            "UNREAD"
          ],
          "readStatus": "unread"
        },
        "options": {
          "downloadAttachments": true
        },
        "pollTimes": {
          "item": [
            {
              "mode": "everyHour",
              "minute": 1
            }
          ]
        }
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "tPOAqAl9y3adqJD6",
          "name": "Gmail account (hire@hic)"
        }
      },
      "typeVersion": 1.2
    }
  ],
  "pinData": {},
  "connections": {
    "Structured Output Parser": {
      "ai_outputParser": [
        [
          {
            "node": "AI Agent to evaluate Resume",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    },
    "Extract text from PDF File": {
      "main": [
        [
          {
            "node": "AI Agent to evaluate Resume",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AI Agent to evaluate Resume": {
      "main": [
        [
          {
            "node": "Add Resume Evaluation to Google Sheets",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Trigger on new Email Received": {
      "main": [
        [
          {
            "node": "Extract text from PDF File",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model (GPT 4o-mini)": {
      "ai_languageModel": [
        [
          {
            "node": "AI Agent to evaluate Resume",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
