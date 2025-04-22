# Filter the feedback from Typeform and store in Google Sheets

**[View Template](https://n8n.io/workflows/1075-/)**  **Published Date:** 05/11/2021  **Created By:** Lorena  **Categories:** `Data & Storage` `Productivity`  

## Template Description

This workflow allows you to filter positive and negative feedback received from a Typeform and insert the data into Google Sheets.



Typeform Trigger node: Start the workflow when a new form is submitted via Typeform

Set node: Extract the information submitted in typeform

IF node: Filter positive and negative reviews (i.e. ratings above or below 3 out of 5).

Google Sheets node: Store the positive and negative reviews and ratings in two different sheets for each case.

## Template JSON

```
{
  "id": "1001",
  "name": "typeform feedback workflow",
  "nodes": [
    {
      "name": "Typeform Trigger",
      "type": "n8n-nodes-base.typeformTrigger",
      "notes": "course feedback",
      "position": [
        450,
        300
      ],
      "webhookId": "1234567890",
      "parameters": {
        "formId": "yxcvbnm"
      },
      "credentials": {
        "typeformApi": "typeform"
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "name": "IF",
      "type": "n8n-nodes-base.if",
      "notes": "filter feedback",
      "position": [
        850,
        300
      ],
      "parameters": {
        "conditions": {
          "number": [
            {
              "value1": "={{$json[\"usefulness\"]}}",
              "value2": 3,
              "operation": "largerEqual"
            }
          ],
          "string": [],
          "boolean": []
        }
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "name": "Google Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "notes": "positive feedback",
      "position": [
        1050,
        200
      ],
      "parameters": {
        "range": "positive_feedback!A:C",
        "options": {},
        "sheetId": "asdfghjkl\u00f6\u00e4",
        "operation": "append",
        "authentication": "oAuth2"
      },
      "credentials": {
        "googleSheetsOAuth2Api": "google_sheets_oauth"
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "notes": "capture typeform data",
      "position": [
        650,
        300
      ],
      "parameters": {
        "values": {
          "number": [
            {
              "name": "usefulness",
              "value": "={{$json[\"How useful was the course?\"]}}"
            }
          ],
          "string": [
            {
              "name": "opinion",
              "value": "={{$json[\"Your opinion on the course:\"]}}"
            }
          ],
          "boolean": []
        },
        "options": {},
        "keepOnlySet": true
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "name": "Google Sheets1",
      "type": "n8n-nodes-base.googleSheets",
      "notes": "negative feedback",
      "position": [
        1050,
        400
      ],
      "parameters": {
        "range": "negative_feedback!A:C",
        "keyRow": 1,
        "options": {},
        "sheetId": "qwertzuiop",
        "operation": "append",
        "authentication": "oAuth2"
      },
      "credentials": {
        "googleSheetsOAuth2Api": "google_sheets_oauth"
      },
      "notesInFlow": true,
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "IF": {
      "main": [
        [
          {
            "node": "Google Sheets",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Google Sheets1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set": {
      "main": [
        [
          {
            "node": "IF",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Typeform Trigger": {
      "main": [
        [
          {
            "node": "Set",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
