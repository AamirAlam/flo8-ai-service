# Get multiple clients' data from Invoice Ninja

**[View Template](https://n8n.io/workflows/534-/)**  **Published Date:** 07/17/2020  **Created By:** amudhan  **Categories:** `Finance & Accounting`  

## Template Description

Companion workflow for Invoice Ninja node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        220,
        310
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Invoice Ninja",
      "type": "n8n-nodes-base.invoiceNinja",
      "position": [
        410,
        310
      ],
      "parameters": {
        "options": {},
        "operation": "getAll"
      },
      "credentials": {
        "invoiceNinjaApi": "invoice_ninja_creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Invoice Ninja",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
