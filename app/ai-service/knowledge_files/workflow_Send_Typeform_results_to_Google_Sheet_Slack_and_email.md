# Send Typeform results to Google Sheet, Slack and email

**[View Template](https://n8n.io/workflows/29-/)**  **Published Date:** 10/06/2019  **Created By:** Jan Oberhauser  **Categories:** `Communication` `Core Nodes` `HITL` `Data & Storage` `Productivity`  

## Template Description



Trigger on new Typeform form submission
Write data to Google Sheet
Check severity of problem
If very severe post message to Slack
If not so severe just send an email

Assumptions

Google Sheet

Sheet in Spreadsheet called "Problems".

Columns Names:
 Name
 Email
 Severity
 Problem

Example Sheet: https://docs.google.com/spreadsheets/d/17fzSFl1BZ1njldTfp5lvh8HtS0-pNXH66b7qGZIiGRU

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
        450,
        300
      ],
      "parameters": {
        "formId": "UXuY0A"
      },
      "credentials": {
        "typeformApi": ""
      },
      "typeVersion": 1
    },
    {
      "name": "IF",
      "type": "n8n-nodes-base.if",
      "position": [
        850,
        300
      ],
      "parameters": {
        "conditions": {
          "number": [
            {
              "value1": "={{$node[\"Google Sheets\"].data[\"Severity\"]}}",
              "value2": 7,
              "operation": "larger"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Google Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        650,
        300
      ],
      "parameters": {
        "range": "Problems!A:D",
        "sheetId": "17fzSFl1BZ1njldTfp5lvh8HtS0-pNXH66b7qGZIiGRU",
        "operation": "append"
      },
      "credentials": {
        "googleApi": ""
      },
      "typeVersion": 1
    },
    {
      "name": "Send Email",
      "type": "n8n-nodes-base.emailSend",
      "position": [
        1050,
        400
      ],
      "parameters": {
        "text": "=Email: {{$node[\"IF\"].data[\"Email\"]}}\nName: {{$node[\"IF\"].data[\"Name\"]}}\nSeverity: {{$node[\"IF\"].data[\"Severity\"]}}\n\nProblem:\n{{$node[\"IF\"].data[\"Problem\"]}}",
        "subject": "User Reported Problem",
        "toEmail": "",
        "fromEmail": ""
      },
      "credentials": {
        "smtp": ""
      },
      "typeVersion": 1
    },
    {
      "name": "Slack",
      "type": "n8n-nodes-base.slack",
      "position": [
        1050,
        200
      ],
      "parameters": {
        "text": "=Email: {{$node[\"IF\"].data[\"Email\"]}}\nName: {{$node[\"IF\"].data[\"Name\"]}}\nSeverity: {{$node[\"IF\"].data[\"Severity\"]}}\n\nProblem:\n{{$node[\"IF\"].data[\"Problem\"]}}",
        "channel": "problems",
        "attachments": [],
        "otherOptions": {}
      },
      "credentials": {
        "slackApi": ""
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "IF": {
      "main": [
        [
          {
            "node": "Slack",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Send Email",
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
