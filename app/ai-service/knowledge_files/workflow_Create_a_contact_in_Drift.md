# Create a contact in Drift

**[View Template](https://n8n.io/workflows/497-/)**  **Published Date:** 07/13/2020  **Created By:** tanaypant  **Categories:** `Sales`  

## Template Description



## Template JSON

```
{
  "id": "125",
  "name": "Create a contact in Drift",
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
      "name": "Drift ",
      "type": "n8n-nodes-base.drift",
      "position": [
        450,
        300
      ],
      "parameters": {
        "email": "",
        "additionalFields": {}
      },
      "credentials": {
        "driftApi": ""
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
            "node": "Drift ",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
