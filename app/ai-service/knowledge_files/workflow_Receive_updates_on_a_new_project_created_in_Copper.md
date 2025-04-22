# Receive updates on a new project created in Copper

**[View Template](https://n8n.io/workflows/537-/)**  **Published Date:** 07/20/2020  **Created By:** amudhan  **Categories:**   

## Template Description

Companion workflow for Copper Trigger node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "Copper Trigger",
      "type": "n8n-nodes-base.copperTrigger",
      "position": [
        890,
        400
      ],
      "webhookId": "493ce79a-6a08-4062-86d9-7f4618b6c1ea",
      "parameters": {
        "event": "new",
        "resource": "project"
      },
      "credentials": {
        "copperApi": "copper_creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {}
}
```
