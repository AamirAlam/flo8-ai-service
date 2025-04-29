# Create a user profile in Vero

**[View Template](https://n8n.io/workflows/499-/)**  **Published Date:** 07/13/2020  **Created By:** tanaypant  **Categories:** `Communication`  

## Template Description



## Template JSON

```
{
  "id": "127",
  "name": "Create a user profile in Vero",
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
      "name": "Vero",
      "type": "n8n-nodes-base.vero",
      "position": [
        450,
        300
      ],
      "parameters": {
        "id": "",
        "additionalFields": {}
      },
      "credentials": {
        "veroApi": ""
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
            "node": "Vero",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
