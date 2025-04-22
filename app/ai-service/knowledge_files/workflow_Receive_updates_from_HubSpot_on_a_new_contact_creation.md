# Receive updates from HubSpot on a new contact creation

**[View Template](https://n8n.io/workflows/628-/)**  **Published Date:** 08/31/2020  **Created By:** amudhan  **Categories:**   

## Template Description

Companion workflow for HubSpot Trigger node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "Hubspot Trigger",
      "type": "n8n-nodes-base.hubspotTrigger",
      "position": [
        700,
        260
      ],
      "webhookId": "9fe8c037-be4f-4809-a7c2-96e509bfc52e",
      "parameters": {
        "appId": "dghert3",
        "additionalFields": {
          "maxConcurrentRequests": 5
        }
      },
      "credentials": {
        "hubspotDeveloperApi": "hubspot_trigger"
      },
      "typeVersion": 1
    }
  ],
  "connections": {}
}
```
