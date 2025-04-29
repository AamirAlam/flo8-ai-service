# Create a ticket in Zendesk

**[View Template](https://n8n.io/workflows/496-/)**  **Published Date:** 07/13/2020  **Created By:** tanaypant  **Categories:** `Communication`  

## Template Description



## Template JSON

```
{
  "id": "123",
  "name": "Create a ticket in Zendesk",
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
      "name": "Zendesk",
      "type": "n8n-nodes-base.zendesk",
      "position": [
        450,
        300
      ],
      "parameters": {
        "description": "",
        "additionalFields": {}
      },
      "credentials": {
        "zendeskApi": ""
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
            "node": "Zendesk",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
