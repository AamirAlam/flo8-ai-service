# Create an Onfleet task when a file in Google Drive is updated

**[View Template](https://n8n.io/workflows/1547-/)**  **Published Date:** 03/22/2022  **Created By:** James Li  **Categories:** `Miscellaneous`  

## Template Description

Summary

Onfleet is a last-mile delivery software that provides end-to-end route planning, dispatch, communication, and analytics to handle the heavy lifting while you can focus on your customers.

This workflow template listens to a Google Drive update event and creates an Onfleet delivery task. You can easily change which Onfleet entity to interact with.

Configurations

Connect to Google Drive with your own Google credentials
Specify the Poll Times and File URL or ID to your own preference, the poll time determines the frequency of this check while the file URL/ID specifies which file to monitor
Update the Onfleet node with your own Onfleet credentials, to register for an Onfleet API key, please visit https://onfleet.com/signup to get started

## Template JSON

```
{
  "name": "Create an Onfleet task when a file in Google Drive is updated",
  "nodes": [
    {
      "name": "Google Drive Trigger",
      "type": "n8n-nodes-base.googleDriveTrigger",
      "position": [
        460,
        300
      ],
      "parameters": {
        "pollTimes": {
          "item": [
            {
              "mode": "everyMinute"
            }
          ]
        },
        "triggerOn": "specificFile",
        "fileToWatch": "<some_id>"
      },
      "typeVersion": 1
    },
    {
      "name": "Onfleet",
      "type": "n8n-nodes-base.onfleet",
      "position": [
        680,
        300
      ],
      "parameters": {
        "operation": "create",
        "additionalFields": {}
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Google Drive Trigger": {
      "main": [
        [
          {
            "node": "Onfleet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
