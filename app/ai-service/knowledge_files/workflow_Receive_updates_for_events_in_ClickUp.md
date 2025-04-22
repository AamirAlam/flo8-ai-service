# Receive updates for events in ClickUp

**[View Template](https://n8n.io/workflows/487-/)**  **Published Date:** 07/12/2020  **Created By:** tanaypant  **Categories:**   

## Template Description



## Template JSON

```
{
  "id": "110",
  "name": "Receive updates for events in ClickUp",
  "nodes": [
    {
      "name": "ClickUp Trigger",
      "type": "n8n-nodes-base.clickUpTrigger",
      "position": [
        700,
        250
      ],
      "parameters": {
        "team": "",
        "events": [
          "*"
        ],
        "filters": {}
      },
      "credentials": {
        "clickUpApi": ""
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {}
}
```
