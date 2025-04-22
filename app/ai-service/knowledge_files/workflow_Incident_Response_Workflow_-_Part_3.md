# Incident Response Workflow - Part 3

**[View Template](https://n8n.io/workflows/355-/)**  **Published Date:** 04/29/2020  **Created By:** tanaypant  **Categories:** `Communication` `Productivity` `Development`  

## Template Description

This workflow is the third of three. You can find the other workflkows here:

Incident Response Workflow - Part 1
Incident Response Workflow - Part 2
Incident Response Workflow - Part 3

We have the following nodes in the workflow:
Webhook node: This trigger node listens to the event when the Resolve button is clicked.
PagerDuty node: This node changes the status of the incident report from Acknowledged to Resolved in PagerDuty.
Jira Software node: This node moves the incident issue to Done.
Mattermost node: This node publishes a message in the auxiliary channel mentioning that the incident has been marked as resolved in PagerDuty and Jira.
Mattermost node: This node publishes a message in the specified Incidents channel that the incident has been resolved by the on-call team.


## Template JSON

```
{
  "nodes": [
    {
      "name": "Mattermost",
      "type": "n8n-nodes-base.mattermost",
      "position": [
        1050,
        200
      ],
      "parameters": {
        "message": "\ud83d\udcaa This issue got closed in PagerDuty and Jira.",
        "channelId": "={{$node[\"Webhook\"].json[\"body\"][\"channel_id\"]}}",
        "attachments": [],
        "otherOptions": {}
      },
      "credentials": {
        "mattermostApi": "Mattermost Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Mattermost1",
      "type": "n8n-nodes-base.mattermost",
      "position": [
        1050,
        400
      ],
      "parameters": {
        "message": "=\ud83c\udf89 The incident ({{$node[\"PagerDuty\"].json[\"summary\"]}}) was resolved by the lovely folks in the on-call team!",
        "channelId": "k1h3du9r9byyfg7sys8ib6p3ey",
        "attachments": [],
        "otherOptions": {}
      },
      "credentials": {
        "mattermostApi": "Mattermost Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Jira",
      "type": "n8n-nodes-base.jira",
      "position": [
        850,
        300
      ],
      "parameters": {
        "issueKey": "={{$node[\"Webhook\"].json[\"body\"][\"context\"][\"jira_key\"]}}",
        "operation": "update",
        "updateFields": {
          "statusId": "31"
        }
      },
      "credentials": {
        "jiraSoftwareCloudApi": "jira"
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
          "status": "resolved"
        }
      },
      "credentials": {
        "pagerDutyApi": "PagerDuty Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        450,
        300
      ],
      "webhookId": "1bd40693-c7dd-43f5-97d9-6d8986e62fc1",
      "parameters": {
        "path": "1bd40693-c7dd-43f5-97d9-6d8986e62fc1",
        "options": {},
        "httpMethod": "POST"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Jira": {
      "main": [
        [
          {
            "node": "Mattermost",
            "type": "main",
            "index": 0
          },
          {
            "node": "Mattermost1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
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
            "node": "Jira",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
