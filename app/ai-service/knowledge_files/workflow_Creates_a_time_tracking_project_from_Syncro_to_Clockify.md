# Creates a time tracking project from Syncro to Clockify

**[View Template](https://n8n.io/workflows/1487-/)**  **Published Date:** 02/22/2022  **Created By:** Jonathan  **Categories:** `Productivity`  

## Template Description

This workflow creates a project in Clockify that any user can track time against. Syncro should be setup with a webhook via Notification Set for Ticket - created (for anyone).

&gt; This workflow is part of an MSP collection, The original can be found here: https://github.com/bionemesis/n8nsyncro

## Template JSON

```
{
  "id": "2",
  "name": "Syncro to Clockify",
  "nodes": [
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        490,
        300
      ],
      "webhookId": "43d196b0-63c4-440a-aaf6-9d893907cf3c",
      "parameters": {
        "path": "43d196b0-63c4-440a-aaf6-9d893907cf3c",
        "options": {},
        "httpMethod": "POST",
        "responseData": "allEntries",
        "responseMode": "lastNode"
      },
      "typeVersion": 1
    },
    {
      "name": "Clockify",
      "type": "n8n-nodes-base.clockify",
      "position": [
        690,
        300
      ],
      "parameters": {
        "name": "=Ticket {{$json[\"body\"][\"attributes\"][\"number\"]}} - {{$json[\"body\"][\"attributes\"][\"customer_business_then_name\"]}} [{{$json[\"body\"][\"attributes\"][\"id\"]}}]",
        "workspaceId": "xxx",
        "additionalFields": {}
      },
      "credentials": {
        "clockifyApi": "Clockify"
      },
      "typeVersion": 1
    }
  ],
  "active": true,
  "settings": {},
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Clockify",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
