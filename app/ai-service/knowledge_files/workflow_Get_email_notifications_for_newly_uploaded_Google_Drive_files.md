# Get email notifications for newly uploaded Google Drive files

**[View Template](https://n8n.io/workflows/1283-/)**  **Published Date:** 10/25/2021  **Created By:** Tom  **Categories:** `Communication` `Core Nodes` `HITL`  

## Template Description

This workflow sends out email notifications when a new file has been uploaded to Google Drive.



The workflow uses two nodes:
Google Drive Trigger**: This node will trigger the workflow whenever a new file has been uploaded to a given folder
Send Email**: This node sends out the email using data from the previous Google Drive Trigger node.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Google Drive Trigger",
      "type": "n8n-nodes-base.googleDriveTrigger",
      "position": [
        250,
        150
      ],
      "parameters": {
        "event": "fileCreated",
        "options": {},
        "triggerOn": "specificFolder",
        "folderToWatch": "1HwOAKkkgveLji8vVpW9Xrg1EsBskwMNb"
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "28",
          "name": "Google Drive account"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Send Email",
      "type": "n8n-nodes-base.emailSend",
      "position": [
        450,
        150
      ],
      "parameters": {
        "text": "=A file in your Google Drive file folder has been created: {{$json[\"name\"]}}",
        "options": {},
        "subject": "File Update",
        "toEmail": "mutedjam@n8n.io",
        "fromEmail": "mutedjam@n8n.io"
      },
      "credentials": {
        "smtp": {
          "id": "14",
          "name": "SMTP account"
        }
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Google Drive Trigger": {
      "main": [
        [
          {
            "node": "Send Email",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
