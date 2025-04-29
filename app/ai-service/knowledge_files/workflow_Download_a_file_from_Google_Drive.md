# Download a file from Google Drive

**[View Template](https://n8n.io/workflows/515-/)**  **Published Date:** 07/15/2020  **Created By:** amudhan  **Categories:** `Data & Storage`  

## Template Description

Companion workflow for Google Drive node docs



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
      "name": "Google Drive",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        450,
        300
      ],
      "parameters": {
        "fileId": "1dJEBaECGmua09YP7W6WCBu66icIq32yRadQpk",
        "options": {},
        "operation": "download"
      },
      "credentials": {
        "googleApi": "n8n-test-service-account"
      },
      "typeVersion": 1
    },
    {
      "name": "Write Binary File",
      "type": "n8n-nodes-base.writeBinaryFile",
      "position": [
        650,
        300
      ],
      "parameters": {
        "fileName": "/data/downloaded_file.pdf"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Google Drive": {
      "main": [
        [
          {
            "node": "Write Binary File",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Google Drive",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
