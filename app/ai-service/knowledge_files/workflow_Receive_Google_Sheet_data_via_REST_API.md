# Receive Google Sheet data via REST API

**[View Template](https://n8n.io/workflows/226-/)**  **Published Date:** 01/01/2020  **Created By:** Jan Oberhauser  **Categories:** `Data & Storage` `Productivity`  

## Template Description



Simple workflow which allows to receive data from a Google Sheet via "REST" endpoint.

Wait for Webhook Call
Get data from Google Sheet
Return data


Example Sheet: https://docs.google.com/spreadsheets/d/17fzSFl1BZ1njldTfp5lvh8HtS0-pNXH66b7qGZIiGRU


## Template JSON

```
{
  "nodes": [
    {
      "name": "Google Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        700,
        300
      ],
      "parameters": {
        "range": "Problems!A:D",
        "options": {},
        "sheetId": "17fzSFl1BZ1njldTfp5lvh8HtS0-pNXH66b7qGZIiGRU"
      },
      "credentials": {
        "googleApi": ""
      },
      "typeVersion": 1
    },
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        500,
        300
      ],
      "parameters": {
        "path": "webhook",
        "options": {},
        "responseData": "allEntries",
        "responseMode": "lastNode"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Google Sheets",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
