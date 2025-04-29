# Receive updates for events in Jira

**[View Template](https://n8n.io/workflows/569-/)**  **Published Date:** 07/29/2020  **Created By:** amudhan  **Categories:**   

## Template Description

Companion workflow for Jira Trigger node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "Jira Trigger",
      "type": "n8n-nodes-base.jiraTrigger",
      "position": [
        880,
        400
      ],
      "webhookId": "a3ddaf66-7f75-4494-b435-ef88ef1f1917",
      "parameters": {
        "events": [
          "*"
        ],
        "additionalFields": {}
      },
      "credentials": {
        "jiraSoftwareCloudApi": "n8n"
      },
      "typeVersion": 1
    }
  ],
  "connections": {}
}
```
