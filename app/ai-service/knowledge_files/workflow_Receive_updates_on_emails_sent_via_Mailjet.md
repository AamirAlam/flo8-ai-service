# Receive updates on emails sent via Mailjet

**[View Template](https://n8n.io/workflows/521-/)**  **Published Date:** 07/15/2020  **Created By:** amudhan  **Categories:**   

## Template Description

Companion workflow for Mailjet Trigger node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "Mailjet Trigger",
      "type": "n8n-nodes-base.mailjetTrigger",
      "position": [
        530,
        400
      ],
      "parameters": {
        "event": "sent"
      },
      "credentials": {
        "mailjetEmailApi": "mailjet creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {}
}
```
