# Receive updates on appointments via Acuity Scheduling

**[View Template](https://n8n.io/workflows/533-/)**  **Published Date:** 07/17/2020  **Created By:** amudhan  **Categories:**   

## Template Description

Companion workflow for Acuity Scheduling Trigger node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "Acuity Scheduling Trigger",
      "type": "n8n-nodes-base.acuitySchedulingTrigger",
      "position": [
        880,
        400
      ],
      "webhookId": "b326732d-9473-469f-a421-dd823d26b945",
      "parameters": {
        "event": "appointment.scheduled"
      },
      "credentials": {
        "acuitySchedulingApi": "acuity_creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {}
}
```
