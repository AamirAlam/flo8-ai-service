# Add Google Sheets data to the Mautic contact

**[View Template](https://n8n.io/workflows/636-/)**  **Published Date:** 09/07/2020  **Created By:** dichvuhuuich  **Categories:** `Data & Storage` `Productivity` `Communication` `Marketing`  

## Template Description

Automatically import the name and email in Google Sheet to the mautic contact each time the lead is filled to the sheet.

## Template JSON

```
{
  "nodes": [
    {
      "name": "GS Read Data2",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        240,
        750
      ],
      "parameters": {
        "range": "Data!A:P",
        "options": {
          "valueRenderMode": "FORMATTED_VALUE"
        },
        "sheetId": "1jKYwPE9DMFOYf1AeDuTvQ3GSM2GqaEJhGYNoisxSLpM"
      },
      "credentials": {
        "googleApi": "n8n API"
      },
      "typeVersion": 1
    },
    {
      "name": "Mautic",
      "type": "n8n-nodes-base.mautic",
      "position": [
        450,
        750
      ],
      "parameters": {
        "email": "={{$node[\"GS Read Data2\"].json[\"email\"]}}",
        "options": {},
        "firstName": "={{$node[\"GS Read Data2\"].json[\"firstname\"]}}",
        "additionalFields": {
          "mobile": "={{$node[\"GS Read Data2\"].json[\"mobile\"]}}"
        }
      },
      "credentials": {
        "mauticApi": "MauticAPI"
      },
      "notesInFlow": false,
      "typeVersion": 1
    },
    {
      "name": "GS Read Data2",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        240,
        750
      ],
      "parameters": {
        "range": "Data!A:P",
        "options": {
          "valueRenderMode": "FORMATTED_VALUE"
        },
        "sheetId": "1jKYwPE9DMFOYf1AeDuTvQ3GSM2GqaEJhGYNoisxSLpM"
      },
      "credentials": {
        "googleApi": "n8n API"
      },
      "typeVersion": 1
    },
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        40,
        750
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "mode": "everyX",
              "unit": "minutes",
              "value": 5
            }
          ]
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
            "node": "GS Read Data2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "GS Read Data2": {
      "main": [
        [
          {
            "node": "Mautic",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
