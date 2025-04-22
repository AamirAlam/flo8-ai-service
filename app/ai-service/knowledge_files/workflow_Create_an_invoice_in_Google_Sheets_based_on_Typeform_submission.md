# Create an invoice in Google Sheets based on Typeform submission

**[View Template](https://n8n.io/workflows/398-/)**  **Published Date:** 06/07/2020  **Created By:** alex  **Categories:** `Communication` `Core Nodes` `HITL` `Data & Storage` `Productivity`  

## Template Description

This form takes data from a Typeform submission and creates an invoice on Google Sheets

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
