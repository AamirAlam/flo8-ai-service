# Incident Response Workflow - Part 2

**[View Template](https://n8n.io/workflows/354-/)**  **Published Date:** 04/29/2020  **Created By:** tanaypant  **Categories:** `Communication` `Development`  

## Template Description

This workflow is the second of three. You can find the other workflkows here:

Incident Response Workflow - Part 1
Incident Response Workflow - Part 2
Incident Response Workflow - Part 3


We have the following nodes in the workflow:
Webhook node: This trigger node listens to the event when the Acknowledge button is clicked.
PagerDuty node: This node changes the status of the incident report from 'Triggered' to 'Acknowledged' in PagerDuty.
Mattermost node: This node publishes a message in the auxiliary channel saying that the status of the incident report has been changed to Acknowledged.


## Template JSON

```
{
  "nodes": [
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        450,
        300
      ],
      "webhookId": "213324b6-b84d-42f9-af3b-42804cc71cd1",
      "parameters": {
        "path": "213324b6-b84d-42f9-af3b-42804cc71cd1",
        "options": {},
        "httpMethod": "POST"
      },
      "typeVersion": 1
    },
    {
      "name": "PagerDuty",
      "type": "n8n-nodes-base.pagerDuty",
      "position": [
        650,
        300
      ],
      "parameters": {
        "email": "n8ndocsburner@gmail.com",
        "operation": "update",
        "incidentId": "={{$json[\"body\"][\"context\"][\"pagerduty_incident\"]}}",
        "updateFields": {
          "status": "acknowledged"
        }
      },
      "credentials": {
        "pagerDutyApi": "PagerDuty Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Mattermost",
      "type": "n8n-nodes-base.mattermost",
      "position": [
        850,
        300
      ],
      "parameters": {
        "message": "\ud83d\udcaa\ud83c\udffc Incident status has been changed to Acknowledged on PagerDuty.",
        "channelId": "={{$node[\"Webhook\"].json[\"body\"][\"channel_id\"]}}",
        "attachments": [],
        "otherOptions": {}
      },
      "credentials": {
        "mattermostApi": "Mattermost Credentials"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "PagerDuty",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "PagerDuty": {
      "main": [
        [
          {
            "node": "Mattermost",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
