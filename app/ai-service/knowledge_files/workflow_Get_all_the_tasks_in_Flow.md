# Get all the tasks in Flow

**[View Template](https://n8n.io/workflows/506-/)**  **Published Date:** 07/14/2020  **Created By:** tanaypant  **Categories:** `Productivity`  

## Template Description



## Template JSON

```
{
  "id": "130",
  "name": "Get all the tasks in Flow",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        250,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Flow",
      "type": "n8n-nodes-base.flow",
      "position": [
        450,
        300
      ],
      "parameters": {
        "filters": {},
        "operation": "getAll",
        "returnAll": true
      },
      "credentials": {
        "flowApi": ""
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Flow",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
