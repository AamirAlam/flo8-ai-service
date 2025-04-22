# Send an email using Mailjet

**[View Template](https://n8n.io/workflows/520-/)**  **Published Date:** 07/15/2020  **Created By:** amudhan  **Categories:** `Development` `Communication`  

## Template Description

Companion workflow for Mailjet node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        250,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Mailjet",
      "type": "n8n-nodes-base.mailjet",
      "position": [
        450,
        300
      ],
      "parameters": {
        "text": "This is a test message",
        "subject": "Sample Subject",
        "toEmail": "user2@example.com",
        "fromEmail": "user@example.com",
        "additionalFields": {}
      },
      "credentials": {
        "mailjetEmailApi": "mailjet creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Mailjet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
