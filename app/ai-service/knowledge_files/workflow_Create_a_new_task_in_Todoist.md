# Create a new task in Todoist

**[View Template](https://n8n.io/workflows/481-/)**  **Published Date:** 07/11/2020  **Created By:** tanaypant  **Categories:** `Productivity`  

## Template Description



## Template JSON

```
{
  "id": "100",
  "name": "Create a new task in Todoist",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        550,
        250
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Todoist",
      "type": "n8n-nodes-base.todoist",
      "position": [
        750,
        250
      ],
      "parameters": {
        "content": "",
        "options": {}
      },
      "credentials": {
        "todoistApi": ""
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
            "node": "Todoist",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
