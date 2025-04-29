# Get all Excel workbooks

**[View Template](https://n8n.io/workflows/566-/)**  **Published Date:** 07/28/2020  **Created By:** amudhan  **Categories:** `Data & Storage` `Productivity`  

## Template Description

Companion workflow for Excel node docs



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
      "name": "Microsoft Excel",
      "type": "n8n-nodes-base.microsoftExcel",
      "position": [
        450,
        300
      ],
      "parameters": {
        "filters": {},
        "operation": "getAll"
      },
      "credentials": {
        "microsoftExcelOAuth2Api": "ms-oauth-creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Microsoft Excel",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
