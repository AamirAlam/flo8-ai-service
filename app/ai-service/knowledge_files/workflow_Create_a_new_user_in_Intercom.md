# Create a new user in Intercom

**[View Template](https://n8n.io/workflows/464-/)**  **Published Date:** 07/09/2020  **Created By:** tanaypant  **Categories:** `Sales` `Communication`  

## Template Description



## Template JSON

```
{
  "id": "91",
  "name": "Create a new user in Intercom",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        600,
        250
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Intercom",
      "type": "n8n-nodes-base.intercom",
      "position": [
        800,
        250
      ],
      "parameters": {
        "idValue": "",
        "identifierType": "email",
        "additionalFields": {}
      },
      "credentials": {
        "intercomApi": ""
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
            "node": "Intercom",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
