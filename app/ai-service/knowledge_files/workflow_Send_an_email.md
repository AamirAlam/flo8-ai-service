# Send an email

**[View Template](https://n8n.io/workflows/584-/)**  **Published Date:** 08/03/2020  **Created By:** amudhan  **Categories:** `Communication` `Core Nodes` `HITL`  

## Template Description

Companion workflow for Send Email node docs



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
      "name": "Send Email",
      "type": "n8n-nodes-base.emailSend",
      "position": [
        450,
        300
      ],
      "parameters": {
        "text": "This is a message to demonstrate the n8n Send Email workflow!",
        "options": {
          "allowUnauthorizedCerts": false
        },
        "subject": "n8n rocks!",
        "toEmail": "user@example.com",
        "fromEmail": "user@from.email"
      },
      "credentials": {
        "smtp": "your@smtp_creds.here"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
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
