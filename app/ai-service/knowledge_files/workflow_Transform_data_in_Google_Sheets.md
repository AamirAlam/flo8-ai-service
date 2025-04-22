# Transform data in Google Sheets

**[View Template](https://n8n.io/workflows/694-/)**  **Published Date:** 09/29/2020  **Created By:** ghagrawal17  **Categories:** `Data & Storage` `Productivity`  

## Template Description


This workflow appends, lookup, updates, and reads data from a Google Sheet spreadsheet.



Set node: The Set node is used to generate data that we want to add to Google Sheets. Depending on your use-case you might have data coming from a different source. For example, you might be fetching data from a WebHook call. Add the node that will fetch the data that you want to add to the Google Sheet.
Use can then use the Set node to set the data that you want to add to the Google Sheets.

Google Sheets node: This node will add the data from the Set node in a new row to the Google Sheet. You will have to enter the Spreadsheet ID and the Range to specify which sheet you want to add the data to.

Google Sheets1 node: This node looks for a specific value in the Google Sheet and returns all the rows that contain the value. In this example, we are looking for the value Berlin in our Google Sheet. If you want to look for a different value, enter that value in the Lookup Value field, and specify the column in the Lookup Column field.

Set1 node: The Set node sets the value of the rent by $100 for the houses in Berlin. We pass this new data to the next nodes in the workflow.

Google Sheets2 node: This node will update the rent for the houses in Berlin with the new rent set in the previous node. We are mapping the rows with their ID. Depending on your use-case, you might want to map the values with a different column. To set this enter the column name in the Key field.

Google Sheets3 node: This node returns the information from the Google Sheet. You can specify the columns that should get returned in the Range field. Currently, the node fetches the data for columns A to D. To fetch the data only for columns A to C set the range to A:C.

This workflow can be broken down into different workflows each with its own use case. For example, we can have a workflow that appends new data to a Google Sheet, and another workflow that lookups for a certain value and returns that value.

You can learn to build this workflow on the documentation page of the Google Sheets node.

## Template JSON

```
{
  "id": "5",
  "name": "Append, lookup, update, and read data from a Google Sheets spreadsheet",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        450,
        450
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Google Sheets2",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1450,
        450
      ],
      "parameters": {
        "key": "ID",
        "range": "A:D",
        "options": {
          "valueInputMode": "USER_ENTERED",
          "valueRenderMode": "UNFORMATTED_VALUE"
        },
        "sheetId": "1remFwo--5ehUgIU7UUndKldPI0Xm93e1T3DldD9GOg0",
        "operation": "update",
        "authentication": "oAuth2"
      },
      "credentials": {
        "googleSheetsOAuth2Api": "google-sheet"
      },
      "typeVersion": 1
    },
    {
      "name": "Set1",
      "type": "n8n-nodes-base.set",
      "position": [
        1250,
        450
      ],
      "parameters": {
        "values": {
          "number": [
            {
              "name": "Rent",
              "value": "={{$node[\"Google Sheets1\"].json[\"Rent\"]+100}}"
            },
            {
              "name": "ID",
              "value": "={{$node[\"Google Sheets1\"].json[\"ID\"]}}"
            }
          ],
          "string": [
            {
              "name": "Name",
              "value": "={{$node[\"Google Sheets1\"].json[\"Name\"]}}"
            },
            {
              "name": "City",
              "value": "={{$node[\"Google Sheets1\"].json[\"City\"]}}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "name": "Google Sheets1",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1050,
        450
      ],
      "parameters": {
        "range": "A:D",
        "options": {
          "valueRenderMode": "UNFORMATTED_VALUE",
          "returnAllMatches": true
        },
        "sheetId": "1remFwo--5ehUgIU7UUndKldPI0Xm93e1T3DldD9GOg0",
        "operation": "lookup",
        "lookupValue": "Berlin",
        "lookupColumn": "City",
        "authentication": "oAuth2"
      },
      "credentials": {
        "googleSheetsOAuth2Api": "google-sheet"
      },
      "typeVersion": 1
    },
    {
      "name": "Google Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        850,
        450
      ],
      "parameters": {
        "range": "A:D",
        "options": {
          "valueInputMode": "USER_ENTERED"
        },
        "sheetId": "1remFwo--5ehUgIU7UUndKldPI0Xm93e1T3DldD9GOg0",
        "operation": "append",
        "authentication": "oAuth2"
      },
      "credentials": {
        "googleSheetsOAuth2Api": "google-sheet"
      },
      "typeVersion": 1
    },
    {
      "name": "Google Sheets3",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1650,
        450
      ],
      "parameters": {
        "range": "A:D",
        "options": {
          "valueRenderMode": "FORMATTED_VALUE"
        },
        "sheetId": "1remFwo--5ehUgIU7UUndKldPI0Xm93e1T3DldD9GOg0",
        "authentication": "oAuth2"
      },
      "credentials": {
        "googleSheetsOAuth2Api": "google-sheet"
      },
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        650,
        450
      ],
      "parameters": {
        "values": {
          "number": [
            {
              "name": "ID",
              "value": "={{Math.floor(Math.random()*1000)}}"
            }
          ],
          "string": [
            {
              "name": "Name",
              "value": "John's Place"
            },
            {
              "name": "Rent",
              "value": "$1,000"
            },
            {
              "name": "City",
              "value": "Berlin"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Set": {
      "main": [
        [
          {
            "node": "Google Sheets",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set1": {
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
    "Google Sheets": {
      "main": [
        [
          {
            "node": "Google Sheets1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Sheets1": {
      "main": [
        [
          {
            "node": "Set1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Sheets2": {
      "main": [
        [
          {
            "node": "Google Sheets3",
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
