# Import data from MySQL into Google Sheets

**[View Template](https://n8n.io/workflows/1753-/)**  **Published Date:** 07/07/2022  **Created By:** Lorena  **Categories:** `Data & Storage` `Productivity` `Development`  

## Template Description

This workflow queries a table in MySQL and inserts the data into Google Sheets.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        100,
        420
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "hour": 5,
              "mode": "everyWeek"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "MySQL - select",
      "type": "n8n-nodes-base.mySql",
      "position": [
        300,
        420
      ],
      "parameters": {
        "query": "SELECT * FROM books;",
        "operation": "executeQuery"
      },
      "credentials": {
        "mySql": {
          "id": "82",
          "name": "MySQL account"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Google Sheets - write",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        500,
        420
      ],
      "parameters": {
        "options": {},
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
      "typeVersion": 1
    }
  ],
  "connections": {
    "Cron": {
      "main": [
        [
          {
            "node": "MySQL - select",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "MySQL - select": {
      "main": [
        [
          {
            "node": "Google Sheets - write",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
