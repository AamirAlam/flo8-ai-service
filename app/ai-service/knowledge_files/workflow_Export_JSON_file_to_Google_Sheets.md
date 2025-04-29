# Export JSON file to Google Sheets

**[View Template](https://n8n.io/workflows/1736-/)**  **Published Date:** 06/30/2022  **Created By:** Lorena  **Categories:** `Data & Storage` `Productivity`  

## Template Description

This workflow exports the contents of a JSON file to Google Sheets.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Google Sheets1",
      "type": "n8n-nodes-base.googleSheets",
      "notes": "Append data to sheet",
      "position": [
        980,
        -120
      ],
      "parameters": {
        "range": "A:C",
        "options": {
          "usePathForKeyRow": true
        },
        "sheetId": "qwertz",
        "operation": "append",
        "authentication": "oAuth2"
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "2",
          "name": "google_sheets_oauth"
        }
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "name": "read json file",
      "type": "n8n-nodes-base.readBinaryFile",
      "position": [
        620,
        -120
      ],
      "parameters": {
        "filePath": "/username/users_spreadsheet.json"
      },
      "typeVersion": 1
    },
    {
      "name": "move binary data 2",
      "type": "n8n-nodes-base.moveBinaryData",
      "position": [
        800,
        -120
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "read json file": {
      "main": [
        [
          {
            "node": "move binary data 2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "move binary data 2": {
      "main": [
        [
          {
            "node": "Google Sheets1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
