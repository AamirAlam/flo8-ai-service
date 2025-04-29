# Insert Excel data to Postgres

**[View Template](https://n8n.io/workflows/1-/)**  **Published Date:** 08/31/2019  **Created By:** Jan Oberhauser  **Categories:** `Data & Storage` `Development`  

## Template Description

Read XLS from file
Convert it to JSON
Insert it in Postgres

## Template JSON

```
{
  "nodes": [
    {
      "name": "Read Binary File",
      "type": "n8n-nodes-base.readBinaryFile",
      "position": [
        450,
        650
      ],
      "parameters": {
        "filePath": "spreadsheet.xls"
      },
      "typeVersion": 1
    },
    {
      "name": "Spreadsheet File1",
      "type": "n8n-nodes-base.spreadsheetFile",
      "position": [
        600,
        650
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Insert Rows1",
      "type": "n8n-nodes-base.postgres",
      "position": [
        750,
        650
      ],
      "parameters": {
        "table": "product",
        "columns": "name,ean"
      },
      "credentials": {
        "postgres": "postgres"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Read Binary File": {
      "main": [
        [
          {
            "node": "Spreadsheet File1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Spreadsheet File1": {
      "main": [
        [
          {
            "node": "Insert Rows1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
