# Sync data between multiple Google Spreadsheets

**[View Template](https://n8n.io/workflows/6-/)**  **Published Date:** 08/31/2019  **Created By:** Jan Oberhauser  **Categories:** `Data & Storage` `Productivity`  

## Template Description



Triggers workflow all two minutes
Reads data from a Google Spreadsheet (in example Sheet Data columns A to G)
Write the data unchanged in two different Spreadsheets with same Sheet name and columns, expressions are optional)

## Template JSON

```
{
  "nodes": [
    {
      "name": "Read Sheet",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        700,
        300
      ],
      "parameters": {
        "range": "Data!A:G",
        "rawData": true
      },
      "typeVersion": 1
    },
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        500,
        300
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "mode": "custom",
              "cronExpression": "0 */2 * * * *"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Write Sheet 2",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        900,
        400
      ],
      "parameters": {
        "range": "={{$node[\"Read Sheet\"].parameter[\"range\"]}}",
        "rawData": true,
        "operation": "update"
      },
      "typeVersion": 1
    },
    {
      "name": "Write Sheet 1",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        900,
        200
      ],
      "parameters": {
        "range": "={{$node[\"Read Sheet\"].parameter[\"range\"]}}",
        "rawData": true,
        "operation": "update"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Cron": {
      "main": [
        [
          {
            "node": "Read Sheet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Read Sheet": {
      "main": [
        [
          {
            "node": "Write Sheet 2",
            "type": "main",
            "index": 0
          },
          {
            "node": "Write Sheet 1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
