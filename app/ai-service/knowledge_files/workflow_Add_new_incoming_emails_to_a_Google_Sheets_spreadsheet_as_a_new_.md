# Add new incoming emails to a Google Sheets spreadsheet as a new row

**[View Template](https://n8n.io/workflows/3319-/)**  **Published Date:** 03/25/2025  **Created By:** WeblineIndia  **Categories:** `Data & Storage` `Productivity`  

## Template Description

This n8n workflow automates the process of capturing and storing incoming email details in a structured spreadsheet format, such as Google Sheets or Excel. Whenever a new email is received, the workflow extracts key details—including the sender’s email, subject, email body, and optional attachments—and logs them as a new row in the spreadsheet.

You can customise this workflow to extract additional details, filter emails based on specific criteria, or send notifications when new entries are added.

Pre-conditions & Requirements

Before setting up this workflow, ensure that:

You have access to the email provider (e.g., Gmail, Outlook, or IMAP-supported email services).
The Gmail Node must be enabled in n8n.
You must authenticate n8n with Google OAuth2 to access your inbox.
Ensure that the Gmail API is enabled in the Google Cloud Console.
You have an existing Google Sheet where data will be stored.
The Google Sheets API is enabled.
You authenticate n8n with your Google account.

Steps

Step 1: Add the Gmail Trigger Node

Click on "Add Node" and search for "Gmail".
Select "Gmail Trigger" and click to add it.
Under Authentication, click "Create New" and authenticate with your Google account. (If you have already connected your Google account, simply select it.)
In the Trigger Event field, select "Message Received".
Under Filters, you can specify:
	Label/Mailbox: If you want to listen to emails from a specific folder (optional).
	From Address: If you only want to receive emails from specific senders (optional).
Click "Execute Node" to test the connection.
Click "Save".

What This Does:
This node listens for new incoming emails in your Gmail inbox.
Step 2: Store Email Data in Google Sheets

Click on "Add Node" and search for "Google Sheets" (or Microsoft Excel, if applicable)
Under Authentication, connect your Google account
Select the target Spreadsheet and Sheet Name where the data will be stored
Set the Operation to "Append Row"
Map the extracted email data to the correct columns.
Click "Execute Node" to test and verify data storage
Click "Save"

What This Does:
This node automatically adds a new row for each incoming email, ensuring a structured and searchable email log.
Final Step
Attach both node and execute the workflow.

Who’s behind this?

WeblineIndia’s AI development team. 

We've delivered 3500+ software projects across 25+ countries since 1999. From no-code automations to complex AI systems — our AI team builds tools that drive results. 

Looking to hire AI developers? Start with us.

## Template JSON

```
{
  "id": "dCLvOuZgc8tToQwu",
  "meta": {
    "instanceId": "14e4c77104722ab186539dfea5182e419aecc83d85963fe13f6de862c875ebfa",
    "templateCredsSetupCompleted": true
  },
  "name": "Add new incoming emails to a Google Sheets spreadsheet as a new row.",
  "tags": [],
  "nodes": [
    {
      "id": "4db1f92f-6425-41c4-8f26-94e13ef5cd1f",
      "name": "Gmail Trigger",
      "type": "n8n-nodes-base.gmailTrigger",
      "notes": "Gmail Trigger\n",
      "position": [
        -200,
        -20
      ],
      "parameters": {
        "filters": {},
        "pollTimes": {
          "item": [
            {
              "mode": "everyMinute"
            }
          ]
        }
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "",
          "name": ""
        }
      },
      "notesInFlow": true,
      "typeVersion": 1.2
    },
    {
      "id": "77c70cbd-fca7-4925-9a47-e2c903b8a64e",
      "name": "Google Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        180,
        -20
      ],
      "parameters": {
        "columns": {
          "value": {
            "body": "={{ $json.snippet }}",
            "Subject": "={{ $json.Subject }}",
            "Sender Email": "={{ $json.From }}"
          },
          "schema": [
            {
              "id": "Sender Email",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Sender Email",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Subject",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Subject",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "body",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "body",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {},
        "operation": "append",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "",
          "cachedResultName": ""
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1o28BFBtzzsnwN01VTcfRp2BUyAFi9e-91H_b920_gJc",
          "cachedResultUrl": "",
          "cachedResultName": ""
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "",
          "name": ""
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "0bc68783-e959-40f7-8cc3-a8800e62029a",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -260,
        -80
      ],
      "parameters": {
        "color": 2,
        "width": 660,
        "height": 260,
        "content": "### Add new incoming emails to a Google Sheets spreadsheet as a new row.\n"
      },
      "typeVersion": 1
    },
    {
      "id": "90a94a4d-60fc-40d2-8b1e-1bf01c98d789",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -260,
        200
      ],
      "parameters": {
        "color": 2,
        "width": 660,
        "content": "## Description :\nThis n8n workflow automates the process of storing email details in a spreadsheet whenever a new email is received. It utilizes the Email Trigger node to detect incoming emails and then extracts the sender, subject, and email content, which are subsequently saved into a spreadsheet (e.g., Google Sheets or an Excel file). This ensures a structured record of emails for further processing, analysis, or reporting.\n\nYou can customize this workflow as per your requirements, such as adding additional columns in the spreadsheet to store more details or modifying it for different use cases, like lead tracking, customer inquiries, or automated email logging. "
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "d8ab2b16-b091-455b-ad43-8e117a49e297",
  "connections": {
    "Gmail Trigger": {
      "main": [
        [
          {
            "node": "Google Sheets",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
