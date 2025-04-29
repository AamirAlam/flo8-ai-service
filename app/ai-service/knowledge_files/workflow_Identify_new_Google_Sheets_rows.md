# Identify new Google Sheets rows

**[View Template](https://n8n.io/workflows/1754-/)**  **Published Date:** 07/08/2022  **Created By:** Tom  **Categories:** `Data & Storage` `Productivity`  

## Template Description



This workflow identifies new rows in Google Sheets using a separate column keeping track of already processed rows.

For this approach to work, the sheet needs to meet two requirements:
A unique identifier for each row is required
A column used to differentiate new/processed rows is present

Our example sheet looks like this:



So the row identifier is named ID, the new/processed column is called Processed. Update the workflow accordingly if your columns have different names.

Now if the workflow runs, it discovers all three rows as new. After processing them, it will add a timestamp to the Processed column:



The next time the workflow is executed it will skip the existing rows and only process newly added data:





## Template JSON

```
{
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        240,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Is new?",
      "type": "n8n-nodes-base.if",
      "position": [
        680,
        300
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json[\"Processed\"]}}",
              "operation": "isEmpty"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Do something here",
      "type": "n8n-nodes-base.noOp",
      "position": [
        900,
        100
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Mark Row as processed",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1120,
        300
      ],
      "parameters": {
        "key": "ID",
        "options": {},
        "sheetId": "1SdnwaIJ6xwaZl006FmK2j4f-b00tq7tT7iQgdfe7Qh4",
        "operation": "update",
        "authentication": "oAuth2"
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "228",
          "name": "Google Sheets account"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Read sheet",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        460,
        300
      ],
      "parameters": {
        "options": {},
        "sheetId": "1SdnwaIJ6xwaZl006FmK2j4f-b00tq7tT7iQgdfe7Qh4",
        "authentication": "oAuth2"
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "228",
          "name": "Google Sheets account"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Set processed value",
      "type": "n8n-nodes-base.set",
      "position": [
        900,
        300
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "Processed",
              "value": "={{ $now.toISO() }}"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "name": "Run every 5 minutes",
      "type": "n8n-nodes-base.interval",
      "position": [
        240,
        100
      ],
      "parameters": {
        "unit": "minutes",
        "interval": 5
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Is new?": {
      "main": [
        [
          {
            "node": "Do something here",
            "type": "main",
            "index": 0
          },
          {
            "node": "Set processed value",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Read sheet": {
      "main": [
        [
          {
            "node": "Is new?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Run every 5 minutes": {
      "main": [
        [
          {
            "node": "Read sheet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set processed value": {
      "main": [
        [
          {
            "node": "Mark Row as processed",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Read sheet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
