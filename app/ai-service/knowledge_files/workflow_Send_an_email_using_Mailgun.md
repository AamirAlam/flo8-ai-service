# Send an email using Mailgun

**[View Template](https://n8n.io/workflows/522-/)**  **Published Date:** 07/15/2020  **Created By:** amudhan  **Categories:** `Development` `Communication`  

## Template Description

Companion workflow for Mailgun node docs



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
      "name": "Mailgun",
      "type": "n8n-nodes-base.mailgun",
      "position": [
        450,
        300
      ],
      "parameters": {
        "text": "This is a test message ",
        "subject": "This is a Subject",
        "toEmail": "user2@example.com",
        "fromEmail": "user@example.com"
      },
      "credentials": {
        "mailgunApi": "mailgun-creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Mailgun",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
