# Send n8n automation errors to a Monday.com board

**[View Template](https://n8n.io/workflows/2074-/)**  **Published Date:** 01/30/2024  **Created By:** Joey D’Anna  **Categories:** `Productivity` `Development` `Core Nodes`  

## Template Description

This template is an error handler that will log n8n workflow errors to a Monday.com board for troubleshooting and tracking.

Prerequisites
Monday account and Monday credential
Create a board on Monday for error logging, with the following columns and types:
	Timestamp (text)
	Error Message (text)
	Stack Trace (long text)
Determine the column IDs using Monday's instructions 

Setup
Edit the Monday nodes to use your credential
Edit the node labeled CREATE ERROR ITEM to point to your error log board and group name
Edit the column IDs in the "Column Values" field of the UPDATE node to match the IDs of the fields on your error log board
To trigger error logging, select this automation as the error workflow on any automation
	For more detailed logging, add Stop and Error nodes in your workflow to send specific error messages to your board.


## Template JSON

```
{
  "meta": {
    "instanceId": "257476b1ef58bf3cb6a46e65fac7ee34a53a5e1a8492d5c6e4da5f87c9b82833",
    "templateId": "2074"
  },
  "nodes": [
    {
      "id": "25a95fba-9367-48ca-b7a3-5ab1fb701869",
      "name": "Monday",
      "type": "n8n-nodes-base.mondayCom",
      "notes": "CREATE ERROR ITEM",
      "position": [
        620,
        240
      ],
      "parameters": {
        "name": "={{ \"\".concat($('Error Trigger').last().json.execution.id) }}",
        "boardId": "1382091189",
        "groupId": "topics",
        "resource": "boardItem",
        "additionalFields": {}
      },
      "credentials": {
        "mondayComApi": {
          "id": "SP53wbPUCBNJRq1G",
          "name": "Monday.com account"
        }
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "5fb18856-cd59-4f57-9e72-c637a206fa41",
      "name": "Date & Time",
      "type": "n8n-nodes-base.dateTime",
      "position": [
        840,
        240
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 2
    },
    {
      "id": "66baa154-b421-4942-99e9-f00f6870b3fa",
      "name": "Error Trigger",
      "type": "n8n-nodes-base.errorTrigger",
      "position": [
        380,
        240
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "34347458-7509-4e08-a501-1cee4a307bb7",
      "name": "Code",
      "type": "n8n-nodes-base.code",
      "notes": "GET STACKTRACE",
      "position": [
        1040,
        240
      ],
      "parameters": {
        "jsCode": "\nconsole.log($('Error Trigger').last().json.execution)\nstr = escape ($('Error Trigger').last().json.execution.error.stack )\nreturn { \"stack\": str}"
      },
      "notesInFlow": true,
      "typeVersion": 2
    },
    {
      "id": "92b6e47b-1c34-40eb-9f9a-57e197528c86",
      "name": "UPDATE",
      "type": "n8n-nodes-base.mondayCom",
      "notes": "POPULUATE MONDAY ITEM",
      "position": [
        1280,
        240
      ],
      "parameters": {
        "itemId": "={{ $('Monday').last().json.id }}",
        "boardId": "1382091189",
        "resource": "boardItem",
        "operation": "changeMultipleColumnValues",
        "columnValues": "={ \"column_id_for_workflow_name (text)\" : \"{{  $('Error Trigger').item.json.workflow.name }}\",\n\"column_id_for_error_stack (long text)\" : \"{{ $('Code').last().json.stack}}\",\n\"column_id_for_error_message (text)\": \"{{ $('Error Trigger').item.json.execution.error.message }}\",\n\"column_id_for_date (text)\": \"{{ $('Date & Time').last().json.currentDate }}\"\n}\n"
      },
      "credentials": {
        "mondayComApi": {
          "id": "SP53wbPUCBNJRq1G",
          "name": "Monday.com account"
        }
      },
      "notesInFlow": true,
      "typeVersion": 1
    }
  ],
  "pinData": {
    "Error Trigger": [
      {
        "workflow": {
          "name": "My WF"
        },
        "execution": {
          "id": 1,
          "error": {
            "stack": "Some error here haha",
            "message": "New error"
          }
        }
      }
    ]
  },
  "connections": {
    "Code": {
      "main": [
        [
          {
            "node": "UPDATE",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Monday": {
      "main": [
        [
          {
            "node": "Date & Time",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Date & Time": {
      "main": [
        [
          {
            "node": "Code",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Error Trigger": {
      "main": [
        [
          {
            "node": "Monday",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
