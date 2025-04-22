# Receive updates for specified tasks in Flow

**[View Template](https://n8n.io/workflows/508-/)**  **Published Date:** 07/14/2020  **Created By:** tanaypant  **Categories:**   

## Template Description



## Template JSON

```
{
  "id": "133",
  "name": "Receive updates for specified tasks in Flow",
  "nodes": [
    {
      "name": "Flow Trigger",
      "type": "n8n-nodes-base.flowTrigger",
      "position": [
        650,
        250
      ],
      "parameters": {
        "taskIds": "",
        "resource": "task"
      },
      "credentials": {
        "flowApi": ""
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {}
}
```
