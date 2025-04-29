# Convert Typeform data into Spreadsheet

**[View Template](https://n8n.io/workflows/179-/)**  **Published Date:** 11/14/2019  **Created By:** Jan Oberhauser  **Categories:** `Data & Storage`  

## Template Description

Trigger on new Typeform form submission
Get existing spreadsheet-file from NextCloud
Read data from file into flow
Append a new row to flow-data
Convert flow-data to a spreadsheet-file
Save updated spreadsheet-file to NextCloud

Assumptions

Spreadsheet file

Named: Problems.xls in folder "examples".

Columns Names:
 Name
 Email
 Severity
 Problem

Typeform

Typeform formular with questions named exactly like the columns of the Google Sheet.


## Template JSON

```
{
  "nodes": [
    {
      "name": "Typeform Trigger",
      "type": "n8n-nodes-base.typeformTrigger",
      "position": [
        500,
        520
      ],
      "parameters": {
        "formId": ""
      },
      "credentials": {
        "typeformApi": ""
      },
      "typeVersion": 1
    },
    {
      "name": "NextCloud",
      "type": "n8n-nodes-base.nextCloud",
      "position": [
        650,
        300
      ],
      "parameters": {
        "path": "examples/Problems.xls",
        "operation": "download"
      },
      "credentials": {
        "nextCloudApi": ""
      },
      "typeVersion": 1
    },
    {
      "name": "Spreadsheet File",
      "type": "n8n-nodes-base.spreadsheetFile",
      "position": [
        800,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Merge",
      "type": "n8n-nodes-base.merge",
      "position": [
        1000,
        470
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Spreadsheet File1",
      "type": "n8n-nodes-base.spreadsheetFile",
      "position": [
        1150,
        470
      ],
      "parameters": {
        "operation": "toFile"
      },
      "typeVersion": 1
    },
    {
      "name": "NextCloud1",
      "type": "n8n-nodes-base.nextCloud",
      "position": [
        1300,
        470
      ],
      "parameters": {
        "path": "={{$node[\"NextCloud\"].parameter[\"path\"]}}",
        "binaryDataUpload": true
      },
      "credentials": {
        "nextCloudApi": ""
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Merge": {
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
    "NextCloud": {
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
            "node": "Merge",
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
            "node": "Merge",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "Spreadsheet File1": {
      "main": [
        [
          {
            "node": "NextCloud1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
