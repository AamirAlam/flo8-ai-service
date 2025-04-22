# Get invoices from Xero

**[View Template](https://n8n.io/workflows/543-/)**  **Published Date:** 07/20/2020  **Created By:** amudhan  **Categories:** `Finance & Accounting`  

## Template Description

Companion workflow for Xero node docs



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
      "name": "Xero",
      "type": "n8n-nodes-base.xero",
      "position": [
        450,
        300
      ],
      "parameters": {
        "options": {},
        "operation": "getAll",
        "organizationId": "ab7e9014-5d01-418f-a64c-dbb6bf5ba2ea"
      },
      "credentials": {
        "xeroOAuth2Api": "n8n_xero"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Xero",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
