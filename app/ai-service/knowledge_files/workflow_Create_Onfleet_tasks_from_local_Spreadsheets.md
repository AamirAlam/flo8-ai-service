# Create Onfleet tasks from local Spreadsheets

**[View Template](https://n8n.io/workflows/1530-/)**  **Published Date:** 03/16/2022  **Created By:** James Li  **Categories:** `Miscellaneous`  

## Template Description

Summary

Onfleet is a last-mile delivery software that provides end-to-end route planning, dispatch, communication, and analytics to handle the heavy lifting while you can focus on your customers.

This workflow template loads in a spreadsheet from your local storage and automatically creates Onfleet tasks on a one-time basis upon workflow trigger. You can use this workflow as a task importer.

Configurations

Update the Read Binary File node with the absolute file path to the local spreadsheet of interest
Update the Onfleet node with your own Onfleet credentials, to register for an Onfleet API key, please visit https://onfleet.com/signup to get started
You can easily change how the Onfleet task is created by mapping to additional data in the spreadsheet
For import templates, visit Onfleet Support to learn more 👍

## Template JSON

```
{
  "id": 12,
  "name": "Create Onfleet tasks from Spreadsheets",
  "nodes": [
    {
      "name": "Onfleet",
      "type": "n8n-nodes-base.onfleet",
      "position": [
        900,
        280
      ],
      "parameters": {
        "operation": "create",
        "destination": {
          "destinationProperties": {
            "address": "={{$json[\"Address_Line1\"]}}, {{$json[\"Address_Line2\"]}}, {{$json[\"City/Town\"]}} {{$json[\"State/Province\"]}}, {{$json[\"Country\"]}}, {{$json[\"Postal_Code\"]}}",
            "unparsed": true,
            "addressNotes": "=",
            "addressApartment": "={{$json[\"Address_Line2\"]}}"
          }
        },
        "additionalFields": {
          "notes": "={{$json[\"Task_Details\"]}}",
          "recipient": {
            "recipientProperties": {
              "recipientName": "={{$json[\"Recipient_Name\"]}}",
              "recipientNotes": "={{$json[\"Recipient_Notes\"]}}",
              "recipientPhone": "=+1{{$json[\"Recipient_Phone\"]}}"
            }
          }
        }
      },
      "credentials": {
        "onfleetApi": {
          "id": "2",
          "name": "Onfleet API Key"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Read Binary File",
      "type": "n8n-nodes-base.readBinaryFile",
      "position": [
        500,
        280
      ],
      "parameters": {
        "filePath": "=/Users/jamesli/Downloads/Onfleet Import Google Sheet.xlsx"
      },
      "typeVersion": 1
    },
    {
      "name": "Spreadsheet File1",
      "type": "n8n-nodes-base.spreadsheetFile",
      "position": [
        700,
        280
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Read Binary File": {
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
    "Spreadsheet File1": {
      "main": [
        [
          {
            "node": "Onfleet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
