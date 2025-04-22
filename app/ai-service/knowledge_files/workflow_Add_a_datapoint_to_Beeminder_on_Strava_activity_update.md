# Add a datapoint to Beeminder on Strava activity update

**[View Template](https://n8n.io/workflows/900-/)**  **Published Date:** 01/21/2021  **Created By:** ghagrawal17  **Categories:** `Productivity`  

## Template Description

This workflow allows you to add a datapoint to Beeminder when a new activity is added to Strava.

You can use this workflow to keep a track of your fitness activities and connect Strava with Beeminder.

If you want to keep a track of different activities like the number of hours worked in a week or the number of tasks completed, you can use the relevant node. For example, you can use the Clockify Trigger node or the Toggl Trigger node.




## Template JSON

```
{
  "id": "208",
  "name": "Add a datapoint to Beeminder when new activity is added to Strava",
  "nodes": [
    {
      "name": "Strava Trigger",
      "type": "n8n-nodes-base.stravaTrigger",
      "position": [
        470,
        300
      ],
      "webhookId": "2b0c6812-ac24-42e5-b15e-8d1fb7606908",
      "parameters": {
        "event": "create",
        "options": {}
      },
      "credentials": {
        "stravaOAuth2Api": "strava"
      },
      "typeVersion": 1
    },
    {
      "name": "Beeminder",
      "type": "n8n-nodes-base.beeminder",
      "position": [
        670,
        300
      ],
      "parameters": {
        "goalName": "testing",
        "additionalFields": {
          "comment": "={{$json[\"object_data\"][\"name\"]}}"
        }
      },
      "credentials": {
        "beeminderApi": "Beeminder credentials"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Strava Trigger": {
      "main": [
        [
          {
            "node": "Beeminder",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
