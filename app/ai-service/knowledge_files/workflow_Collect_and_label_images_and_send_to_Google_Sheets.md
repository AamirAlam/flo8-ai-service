# Collect and label images and send to Google Sheets

**[View Template](https://n8n.io/workflows/1401-/)**  **Published Date:** 01/17/2022  **Created By:** Lorena  **Categories:** `Data & Storage` `Productivity` `Development` `Core Nodes`  

## Template Description

This workflow collects images from web search on a specific query, detects labels in them, and stores this information in a Google Sheet.



## Template JSON

```
{
  "nodes": [
    {
      "name": "HTTP Request1",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        500,
        540
      ],
      "parameters": {
        "url": "https://www.googleapis.com/customsearch/v1?imgType=photo&key=AIzaSyBQry407hE5VwMaDedHogPuwJeIbAIidQU&cx=e51ced3f3563dfac9&q=street&searchType=image",
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "name": "AWS Rekognition1",
      "type": "n8n-nodes-base.awsRekognition",
      "position": [
        680,
        540
      ],
      "parameters": {
        "type": "detectLabels",
        "binaryData": true,
        "additionalFields": {}
      },
      "credentials": {
        "aws": {
          "id": "9",
          "name": "aws"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Google Sheets2",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1040,
        540
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
    },
    {
      "name": "Set3",
      "type": "n8n-nodes-base.set",
      "position": [
        860,
        540
      ],
      "parameters": {
        "values": {
          "number": [],
          "string": [
            {
              "name": "img_name",
              "value": "={{$node[\"HTTP Request1\"].json[\"items\"][0][\"title\"]}}"
            },
            {
              "name": "img_link",
              "value": "={{$node[\"HTTP Request1\"].json[\"items\"][0][\"link\"]}}"
            },
            {
              "name": "img_labels",
              "value": "={{$node[\"AWS Rekognition\"][\"Labels\"][\"Name\"]}}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Set3": {
      "main": [
        [
          {
            "node": "Google Sheets2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request1": {
      "main": [
        [
          {
            "node": "AWS Rekognition1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AWS Rekognition1": {
      "main": [
        [
          {
            "node": "Set3",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
