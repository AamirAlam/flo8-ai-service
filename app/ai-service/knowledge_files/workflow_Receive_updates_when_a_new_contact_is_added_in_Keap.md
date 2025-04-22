# Receive updates when a new contact is added in Keap

**[View Template](https://n8n.io/workflows/554-/)**  **Published Date:** 07/23/2020  **Created By:** amudhan  **Categories:**   

## Template Description

Companion workflow for Keap Trigger node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "Keap Trigger",
      "type": "n8n-nodes-base.keapTrigger",
      "position": [
        440,
        320
      ],
      "webhookId": "1df33e6f-7e5c-4d70-b90d-d5666aaf63e7",
      "parameters": {
        "eventId": "contact.add"
      },
      "credentials": {
        "keapOAuth2Api": "keap_creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {}
}
```
