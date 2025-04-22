# Get all leads from Zoho CRM

**[View Template](https://n8n.io/workflows/552-/)**  **Published Date:** 07/23/2020  **Created By:** amudhan  **Categories:** `Sales` `Communication`  

## Template Description

Companion workflow for Zoho CRM node docs



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
      "name": "Zoho CRM",
      "type": "n8n-nodes-base.zohoCrm",
      "position": [
        450,
        300
      ],
      "parameters": {
        "options": {},
        "operation": "getAll"
      },
      "credentials": {
        "zohoOAuth2Api": "zoho_creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Zoho CRM",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
