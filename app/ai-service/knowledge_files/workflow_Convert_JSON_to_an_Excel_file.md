# Convert JSON to an Excel file

**[View Template](https://n8n.io/workflows/1435-/)**  **Published Date:** 02/04/2022  **Created By:** Dick  **Categories:**   

## Template Description

Send a simple JSON array via HTTP POST and get an Excel file. The default filename is Export.xlsx. By adding the (optional) request ?filename=xyz you can specify the filename.

NOTE: do not forget to change the webhook path!

## Template JSON

```
{
  "nodes": [
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        340,
        0
      ],
      "webhookId": "c1616754-4dec-4b00-a8b5-d1cb5f75bf11",
      "parameters": {
        "path": "c1616754-4dec-4b00-a8b5-d1cb5f75bf11",
        "options": {},
        "httpMethod": "POST",
        "responseMode": "responseNode"
      },
      "typeVersion": 1
    },
    {
      "name": "Item Lists",
      "type": "n8n-nodes-base.itemLists",
      "position": [
        560,
        0
      ],
      "parameters": {
        "options": {},
        "fieldToSplitOut": "=body"
      },
      "typeVersion": 1
    },
    {
      "name": "Spreadsheet File",
      "type": "n8n-nodes-base.spreadsheetFile",
      "position": [
        780,
        0
      ],
      "parameters": {
        "options": {},
        "operation": "toFile",
        "fileFormat": "xlsx"
      },
      "typeVersion": 1
    },
    {
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        1020,
        0
      ],
      "parameters": {
        "options": {
          "responseHeaders": {
            "entries": [
              {
                "name": "content-disposition",
                "value": "=attachment; filename=\"{{$node[\"Webhook\"].json[\"query\"][\"filename\"]? $node[\"Webhook\"].json[\"query\"][\"filename\"] : \"Export\"}}.xlsx\""
              }
            ]
          }
        },
        "respondWith": "binary"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Item Lists",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Item Lists": {
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
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
