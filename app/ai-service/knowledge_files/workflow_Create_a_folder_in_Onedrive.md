# Create a folder in Onedrive

**[View Template](https://n8n.io/workflows/565-/)**  **Published Date:** 07/28/2020  **Created By:** amudhan  **Categories:** `Data & Storage`  

## Template Description

Companion workflow for Onedrive node docs



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
      "name": "Microsoft OneDrive",
      "type": "n8n-nodes-base.microsoftOneDrive",
      "position": [
        450,
        300
      ],
      "parameters": {
        "name": "n8n-rocks",
        "options": {},
        "resource": "folder",
        "operation": "create"
      },
      "credentials": {
        "microsoftOneDriveOAuth2Api": "n8n-docs-creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Microsoft OneDrive",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
