# Read a spreadsheet file

**[View Template](https://n8n.io/workflows/586-/)**  **Published Date:** 08/04/2020  **Created By:** amudhan  **Categories:**   

## Template Description

Companion workflow for Spreadsheet File node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        250,
        320
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Spreadsheet File",
      "type": "n8n-nodes-base.spreadsheetFile",
      "position": [
        650,
        320
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "name": "Read Binary File",
      "type": "n8n-nodes-base.readBinaryFile",
      "position": [
        450,
        320
      ],
      "parameters": {
        "filePath": "/data/sample_spreadsheet.csv"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Read Binary File": {
      "main": [
        [
          {
            "node": "Spreadsheet File",
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
            "node": "Read Binary File",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
