# Receive updates for Calendly events

**[View Template](https://n8n.io/workflows/540-/)**  **Published Date:** 07/20/2020  **Created By:** amudhan  **Categories:**   

## Template Description

Companion workflow for Calendly Trigger node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "Calendly Trigger",
      "type": "n8n-nodes-base.calendlyTrigger",
      "position": [
        880,
        400
      ],
      "webhookId": "9d13bcea-781a-4462-a9af-44bfb1fb6891",
      "parameters": {
        "events": [
          "invitee.created",
          "invitee.canceled"
        ]
      },
      "credentials": {
        "calendlyApi": "calendly_creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {}
}
```
