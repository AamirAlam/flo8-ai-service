# Get all contacts from Keap

**[View Template](https://n8n.io/workflows/553-/)**  **Published Date:** 07/23/2020  **Created By:** amudhan  **Categories:** `Sales` `Communication`  

## Template Description

Companion workflow for Keap node docs



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
      "name": "Keap",
      "type": "n8n-nodes-base.keap",
      "position": [
        450,
        300
      ],
      "parameters": {
        "options": {},
        "resource": "contact",
        "operation": "getAll"
      },
      "credentials": {
        "keapOAuth2Api": "keap_creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Keap",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
