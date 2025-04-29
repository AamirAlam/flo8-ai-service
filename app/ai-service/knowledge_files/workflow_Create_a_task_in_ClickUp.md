# Create a task in ClickUp

**[View Template](https://n8n.io/workflows/485-/)**  **Published Date:** 07/12/2020  **Created By:** tanaypant  **Categories:** `Productivity` `Communication`  

## Template Description



## Template JSON

```
{
  "id": "105",
  "name": "Create a task in ClickUp",
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
      "name": "ClickUp",
      "type": "n8n-nodes-base.clickUp",
      "position": [
        450,
        300
      ],
      "parameters": {
        "list": "",
        "name": "",
        "team": "",
        "space": "",
        "folder": "",
        "additionalFields": {}
      },
      "credentials": {
        "clickUpApi": ""
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
            "node": "ClickUp",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
