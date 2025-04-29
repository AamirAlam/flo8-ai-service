# Receive updates for new events in Clockify

**[View Template](https://n8n.io/workflows/536-/)**  **Published Date:** 07/17/2020  **Created By:** amudhan  **Categories:**   

## Template Description

Companion workflow for Clockify Trigger node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "Clockify Trigger",
      "type": "n8n-nodes-base.clockifyTrigger",
      "position": [
        450,
        480
      ],
      "parameters": {
        "pollTimes": {
          "item": [
            {
              "mode": "everyMinute"
            }
          ]
        },
        "workspaceId": "5f115b31e3f0ad7f90326b39"
      },
      "credentials": {
        "clockifyApi": "clockify_creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {}
}
```
