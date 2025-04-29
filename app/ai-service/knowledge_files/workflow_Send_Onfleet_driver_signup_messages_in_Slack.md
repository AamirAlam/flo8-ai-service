# Send Onfleet driver signup messages in Slack

**[View Template](https://n8n.io/workflows/1532-/)**  **Published Date:** 03/16/2022  **Created By:** James Li  **Categories:** `Communication` `HITL`  

## Template Description

Summary

Onfleet is a last-mile delivery software that provides end-to-end route planning, dispatch, communication, and analytics to handle the heavy lifting while you can focus on your customers.

This workflow template listens to Onfleet driver sign-up events and automatically notifies you on Slack.

Configurations

Update the Onfleet node with your own Onfleet credentials, to register for an Onfleet API key, please visit https://onfleet.com/signup to get started
Update the Slack node with your own Slack credentials
Update the Slack channel to something that exists in your Slack workspace, the default is set to #new-driver-signup in this example which may not apply to your workspace
Update the Slack message to something customized, ideally with driver information such as phone number and name


## Template JSON

```
{
  "id": 14,
  "name": "Onfleet Driver signup message in Slack",
  "nodes": [
    {
      "name": "Onfleet Trigger",
      "type": "n8n-nodes-base.onfleetTrigger",
      "position": [
        460,
        300
      ],
      "webhookId": "a005e163-13a2-4ea2-a127-6e00e30a82f4",
      "parameters": {
        "triggerOn": "workerCreated",
        "additionalFields": {}
      },
      "credentials": {
        "onfleetApi": {
          "id": "2",
          "name": "Onfleet API Key"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Slack",
      "type": "n8n-nodes-base.slack",
      "position": [
        680,
        300
      ],
      "parameters": {
        "text": "A new driver has signed up!",
        "channel": "#new-driver-signup",
        "attachments": [],
        "otherOptions": {}
      },
      "credentials": {
        "slackApi": {
          "id": "7",
          "name": "Slack account"
        }
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Onfleet Trigger": {
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
