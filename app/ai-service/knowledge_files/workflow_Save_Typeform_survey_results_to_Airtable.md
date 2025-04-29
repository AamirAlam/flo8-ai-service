# Save Typeform survey results to Airtable

**[View Template](https://n8n.io/workflows/384-/)**  **Published Date:** 05/28/2020  **Created By:** tanaypant  **Categories:** `Data & Storage`  

## Template Description

With this workflow, you can collect the data from Typeform with the Typeform Trigger node every time someone submits a response and save it to Airtable with the Airtable node.

## Template JSON

```
{
  "id": "54",
  "name": "CFP Selection 1",
  "nodes": [
    {
      "name": "Typeform Trigger",
      "type": "n8n-nodes-base.typeformTrigger",
      "position": [
        450,
        250
      ],
      "parameters": {
        "formId": ""
      },
      "credentials": {
        "typeformApi": "Typeform"
      },
      "typeVersion": 1
    },
    {
      "name": "Airtable",
      "type": "n8n-nodes-base.airtable",
      "position": [
        660,
        250
      ],
      "parameters": {
        "table": "",
        "operation": "append",
        "application": ""
      },
      "credentials": {
        "airtableApi": "Airtable"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Typeform Trigger": {
      "main": [
        [
          {
            "node": "Airtable",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
