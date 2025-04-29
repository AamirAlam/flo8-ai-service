# Send notification when deployment fails

**[View Template](https://n8n.io/workflows/1255-/)**  **Published Date:** 10/04/2021  **Created By:** ghagrawal17  **Categories:** `Communication` `HITL`  

## Template Description

This workflow sends a message on Slack when site deployment fails.



Netlify Trigger node: This node triggers the workflow when the site deployment fails.

Slack node: This node sends a message on Slack alerting the team about the failed deployment. If you want to send a message to a different platform, replace the Slack node with the node of the respective platform.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Netlify Trigger",
      "type": "n8n-nodes-base.netlifyTrigger",
      "position": [
        450,
        300
      ],
      "webhookId": "0654820c-1960-4c8b-80fc-c0a66ab96577",
      "parameters": {
        "event": "deployFailed",
        "siteId": "ab52947e-a696-4498-a5a1-fae7fbe30c84"
      },
      "credentials": {
        "netlifyApi": "Netlify account"
      },
      "typeVersion": 1
    },
    {
      "name": "Slack",
      "type": "n8n-nodes-base.slack",
      "position": [
        650,
        300
      ],
      "parameters": {
        "text": "=\ud83d\udea8 Deploy Failed \ud83d\udea8\nDeploy for the site {{$json[\"name\"]}} failed.\nError Message: {{$json[\"error_message\"]}}\nYou can find more information here: https://app.netlify.com/sites/{{$json[\"name\"]}}/deploys/{{$json[\"id\"]}}",
        "channel": "general",
        "attachments": [],
        "otherOptions": {}
      },
      "credentials": {
        "slackApi": "read-history"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Netlify Trigger": {
      "main": [
        [
          {
            "node": "Slack",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
