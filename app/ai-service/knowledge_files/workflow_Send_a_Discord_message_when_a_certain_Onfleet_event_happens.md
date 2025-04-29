# Send a Discord message when a certain Onfleet event happens

**[View Template](https://n8n.io/workflows/1528-/)**  **Published Date:** 03/16/2022  **Created By:** James Li  **Categories:** `Communication` `HITL`  

## Template Description

Summary

Onfleet is a last-mile delivery software that provides end-to-end route planning, dispatch, communication, and analytics to handle the heavy lifting while you can focus on your customers.

This workflow template listens to an Onfleet event and communicates via a Discord message. You can easily streamline this with your Discord servers and users.

Configurations

Update the Onfleet trigger node with your own Onfleet credentials, to register for an Onfleet API key, please visit https://onfleet.com/signup to get started
You can easily change which Onfleet event to listen to. Learn more about Onfleet webhooks with Onfleet Support
Update the Discord node with your Discord server webhook URL, add your own expressions to the Text field

## Template JSON

```
{
  "id": 10,
  "name": "Onfleet --> Discord",
  "nodes": [
    {
      "name": "Discord",
      "type": "n8n-nodes-base.discord",
      "position": [
        680,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Onfleet Trigger",
      "type": "n8n-nodes-base.onfleetTrigger",
      "position": [
        460,
        300
      ],
      "webhookId": "58f99515-a1d6-4c56-8ecc-e9d921fa3276",
      "parameters": {
        "triggerOn": "taskStarted",
        "additionalFields": {}
      },
      "credentials": {
        "onfleetApi": {
          "id": "2",
          "name": "Onfleet API Key"
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
            "node": "Discord",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
