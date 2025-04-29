# Receive updates for Stripe events

**[View Template](https://n8n.io/workflows/545-/)**  **Published Date:** 07/21/2020  **Created By:** amudhan  **Categories:**   

## Template Description

Companion workflow for Stripe Trigger node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "Stripe Trigger",
      "type": "n8n-nodes-base.stripeTrigger",
      "position": [
        890,
        400
      ],
      "webhookId": "4b359a40-a292-4c58-bc15-842b4d8eb3ca",
      "parameters": {
        "events": [
          "*"
        ]
      },
      "credentials": {
        "stripeApi": "stripe_creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {}
}
```
