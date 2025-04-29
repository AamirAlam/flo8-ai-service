# Get a board from monday.com

**[View Template](https://n8n.io/workflows/556-/)**  **Published Date:** 07/27/2020  **Created By:** amudhan  **Categories:** `Productivity`  

## Template Description

Companion workflow for monday.com node docs





## Template JSON

```
{
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
      "name": "Monday.com",
      "type": "n8n-nodes-base.mondayCom",
      "position": [
        450,
        300
      ],
      "parameters": {
        "boardId": "663435997",
        "operation": "get"
      },
      "credentials": {
        "mondayComApi": "monday"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Monday.com",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
