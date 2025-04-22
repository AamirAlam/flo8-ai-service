# Transfer data from Postgres to Excel

**[View Template](https://n8n.io/workflows/2-/)**  **Published Date:** 08/31/2019  **Created By:** Jan Oberhauser  **Categories:** `Data & Storage` `Development`  

## Template Description



Read data from Postgres
Converting it to XLS
Save it to disk

## Template JSON

```
{
  "nodes": [
    {
      "name": "Run Query",
      "type": "n8n-nodes-base.postgres",
      "position": [
        450,
        450
      ],
      "parameters": {
        "query": "SELECT name, ean FROM product",
        "operation": "executeQuery"
      },
      "credentials": {
        "postgres": "postgres"
      },
      "typeVersion": 1
    },
    {
      "name": "Spreadsheet File",
      "type": "n8n-nodes-base.spreadsheetFile",
      "position": [
        600,
        450
      ],
      "parameters": {
        "operation": "toFile"
      },
      "typeVersion": 1
    },
    {
      "name": "Write Binary File",
      "type": "n8n-nodes-base.writeBinaryFile",
      "position": [
        750,
        450
      ],
      "parameters": {
        "fileName": "spreadsheet.xls"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Run Query": {
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
    "Spreadsheet File": {
      "main": [
        [
          {
            "node": "Write Binary File",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
