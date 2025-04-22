# Create a new contact in Agile CRM

**[View Template](https://n8n.io/workflows/474-/)**  **Published Date:** 07/10/2020  **Created By:** tanaypant  **Categories:** `Sales` `Marketing`  

## Template Description



## Template JSON

```
{
  "id": "96",
  "name": "Create a new contact in Agile CRM",
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
      "name": "AgileCRM",
      "type": "n8n-nodes-base.agileCrm",
      "position": [
        450,
        300
      ],
      "parameters": {
        "operation": "create",
        "additionalFields": {
          "lastName": "",
          "firstName": ""
        }
      },
      "credentials": {
        "agileCrmApi": ""
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
            "node": "AgileCRM",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
