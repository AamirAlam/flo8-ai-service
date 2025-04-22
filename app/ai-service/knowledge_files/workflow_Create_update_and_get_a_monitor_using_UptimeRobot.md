# Create, update, and get a monitor using UptimeRobot

**[View Template](https://n8n.io/workflows/1112-/)**  **Published Date:** 06/04/2021  **Created By:** ghagrawal17  **Categories:** `Development`  

## Template Description

This workflow allows you to create, update, and get a monitor using the UptimeRobot node.



UptimeRobot node: This node creates a new monitor of the type HTTP(S).

UptimeRobot1 node: This node will update the monitor that we created in the previous node.

UptimeRobot2 node: This node will get the information of the monitor that we created in the previous node.

## Template JSON

```
{
  "nodes": [
    {
      "name": "UptimeRobot2",
      "type": "n8n-nodes-base.uptimeRobot",
      "position": [
        890,
        320
      ],
      "parameters": {
        "id": "={{$json[\"id\"]}}",
        "resource": "monitor",
        "operation": "get"
      },
      "credentials": {
        "uptimeRobotApi": "UptimeRobot API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "UptimeRobot",
      "type": "n8n-nodes-base.uptimeRobot",
      "position": [
        490,
        320
      ],
      "parameters": {
        "url": "https://n8n.io",
        "type": 1,
        "resource": "monitor",
        "operation": "create",
        "friendlyName": "n8n"
      },
      "credentials": {
        "uptimeRobotApi": "UptimeRobot API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "UptimeRobot1",
      "type": "n8n-nodes-base.uptimeRobot",
      "position": [
        690,
        320
      ],
      "parameters": {
        "id": "={{$json[\"id\"]}}",
        "resource": "monitor",
        "operation": "update",
        "updateFields": {
          "friendly_name": "n8n website"
        }
      },
      "credentials": {
        "uptimeRobotApi": "UptimeRobot API Credentials"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "UptimeRobot": {
      "main": [
        [
          {
            "node": "UptimeRobot1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "UptimeRobot1": {
      "main": [
        [
          {
            "node": "UptimeRobot2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
