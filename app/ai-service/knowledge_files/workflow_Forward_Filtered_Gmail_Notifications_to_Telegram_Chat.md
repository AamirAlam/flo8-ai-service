# Forward Filtered Gmail Notifications to Telegram Chat

**[View Template](https://n8n.io/workflows/3301-/)**  **Published Date:** 03/24/2025  **Created By:** WeblineIndia  **Categories:** `Communication` `HITL`  

## Template Description

This workflow automatically forwards incoming Gmail emails to a Telegram chat only if the email subject contains specific keywords (like "Urgent" or "Server Down").

The workflow extracts key details such as the sender, subject, and message body, and sends them as a formatted message to a specified Telegram chat.

This is useful for real-time notifications, security alerts, or monitoring important emails directly from Telegram — filtering out unnecessary emails.

Prerequisites: 

Before setting up the workflow, ensure the following:

The Gmail API should be enabled.
Create a bot using @BotFather and obtain the API key.
Retrieve the telegram Chat ID (for personal messages or group messages).
Set up OAuth2 for Gmail and use the Bot Token for Telegram.

Customisation Options :

Modify the subject keywords in the IF Node to change the filtering criteria.
Customize how the email details appear in Telegram (bold subject, italic body, etc.).
Extend the workflow to include email attachments in Telegram.

Steps :

Step 1: Gmail Trigger Node (On Message Received)

Select "Gmail Trigger" and add it to the workflow.
Authenticate with your Google Account.
Set Trigger Event to "Message Received".
(Optional) Add filters for specific senders, labels, or subjects.
Click "Execute Node" to test the connection.
Click "Save".

Step 2: IF Node (Conditional Filtering)

Add an "IF" Node after the Gmail Trigger.
Configure the condition to check if the email subject contains specific keywords (e.g., "Urgent", "Server Down", "Alert").
If the condition is true, proceed to the next step.
If false, you can stop or route it elsewhere (optional).

Step 3: Telegram Node (Send Message Action)

Click "Add Node" and search for Telegram.
Select "Send Message" as the action.
Authenticate using your Telegram Bot Token.
Set the Chat ID (personal or group chat).
Format the message using email details received from the email trigger node and set the message in text.

Steps 4. Connect & Test the Workflow

Link Gmail Trigger → if node → Telegram Send Message.
Save and execute the workflow manually.
Send a test email to your Gmail account.
Verify if the email details appear in your Telegram chat.

About the Creator, WeblineIndia

This workflow is created by the Agentic business process automation developers at WeblineIndia. We build automation and AI-driven tools that make life easier for your team. If you’re looking to hire dedicated developers who can customize workflows around your business, we’re just a click away.

## Template JSON

```
{
  "id": "AvXlqUiuc1qJSwxf",
  "meta": {
    "instanceId": "14e4c77104722ab186539dfea5182e419aecc83d85963fe13f6de862c875ebfa"
  },
  "name": "Forward Filtered Gmail Notifications to Telegram Chat",
  "tags": [],
  "nodes": [
    {
      "id": "99441348-1d5d-459f-961f-48bd593144f2",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -60,
        0
      ],
      "parameters": {
        "color": 4,
        "width": 1000,
        "height": 300,
        "content": "# Forward Filtered Gmail Notifications to Telegram Chat\n"
      },
      "typeVersion": 1
    },
    {
      "id": "eadf565c-e753-4682-a8c2-6bc630a30a27",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -60,
        320
      ],
      "parameters": {
        "color": 4,
        "width": 1000,
        "height": 200,
        "content": "## Description :\n### This n8n workflow automatically forwards incoming Gmail emails to a Telegram chat only if the email subject contains specific keywords (like \"Urgent\" or \"Server Down\"). The workflow extracts key details such as the sender, subject, and message body, and sends them as a formatted message to a specified Telegram chat. This is useful for real-time notifications, security alerts, or monitoring important emails directly from Telegram \u2014 filtering out unnecessary emails."
      },
      "typeVersion": 1
    },
    {
      "id": "bb2a78d7-91ba-4e8c-a9f1-af270a50bd8f",
      "name": "Incoming Email Monitor",
      "type": "n8n-nodes-base.gmailTrigger",
      "position": [
        20,
        100
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
          "id": "5V09QSJCeHoQoKUp",
          "name": "SM MaryP (Gmail)"
        }
      },
      "notesInFlow": false,
      "typeVersion": 1.2
    },
    {
      "id": "addffc7b-ef58-4fb5-9275-3db6fd84f4c0",
      "name": "Email Validation Check",
      "type": "n8n-nodes-base.if",
      "position": [
        340,
        100
      ],
      "parameters": {
        "options": {
          "ignoreCase": false
        },
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "loose"
          },
          "combinator": "or",
          "conditions": [
            {
              "id": "2496d01f-dbd5-4e23-84c3-f78decb87697",
              "operator": {
                "type": "string",
                "operation": "contains"
              },
              "leftValue": "={{ $json.Subject }}",
              "rightValue": "Urgent"
            },
            {
              "id": "274e9e05-5c74-487e-851d-0ca62210cb99",
              "operator": {
                "name": "filter.operator.equals",
                "type": "string",
                "operation": "equals"
              },
              "leftValue": "={{ $json.Subject }}",
              "rightValue": "Server Down"
            }
          ]
        },
        "looseTypeValidation": true
      },
      "typeVersion": 2.2
    },
    {
      "id": "e87d46b6-efc6-466f-a708-bfbf34bf001b",
      "name": "Send Telegram Message",
      "type": "n8n-nodes-base.telegram",
      "position": [
        700,
        80
      ],
      "webhookId": "c8f1d16f-b698-4af9-a795-9aaa277c2bf6",
      "parameters": {
        "text": "=From : {{ $json.From }}\nSubject :{{ $json.Subject }}\nMessage : {{ $json.snippet }}\n",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "notesInFlow": false,
      "typeVersion": 1.2
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "caf5eedb-4c6b-4bfa-9a0a-2d868291a83c",
  "connections": {
    "Email Validation Check": {
      "main": [
        [
          {
            "node": "Send Telegram Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Incoming Email Monitor": {
      "main": [
        [
          {
            "node": "Email Validation Check",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
