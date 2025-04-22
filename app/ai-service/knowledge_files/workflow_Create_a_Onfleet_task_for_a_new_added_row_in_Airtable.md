# Create a Onfleet task for a new added row in Airtable

**[View Template](https://n8n.io/workflows/1524-/)**  **Published Date:** 03/15/2022  **Created By:** James Li  **Categories:** `Miscellaneous`  

## Template Description

Summary

Onfleet is a last-mile delivery software that provides end-to-end route planning, dispatch, communication, and analytics to handle the heavy lifting while you can focus on your customers.

This workflow template automatically creates an Onfleet delivery task when you add in a new row in Airtable. 

Configurations

Update the Airtable trigger node with your own Airtable Base ID, and the table name accordingly
You will also need to configure how often this Airtable trigger polls, the default in this template is every 10 minutes
Update the Onfleet node with your own Onfleet credentials, to register for an Onfleet API key, please visit https://onfleet.com/signup to get started
You can easily change how the Onfleet task is created by mapping to additional data in the Airtable

Airtable format should adhere to Onfleet's task import functionalities, for more details please visit the Onfleet Support Center.


## Template JSON

```
{
  "id": 9,
  "name": "Airtable -> Onfleet",
  "nodes": [
    {
      "name": "Airtable Trigger",
      "type": "n8n-nodes-base.airtableTrigger",
      "position": [
        280,
        600
      ],
      "parameters": {
        "pollTimes": {
          "item": [
            {
              "mode": "everyX",
              "unit": "minutes",
              "value": 10
            }
          ]
        },
        "triggerField": "Address_Line1",
        "additionalFields": {}
      },
      "credentials": {
        "airtableApi": {
          "id": "8",
          "name": "Airtable account"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Onfleet",
      "type": "n8n-nodes-base.onfleet",
      "position": [
        500,
        600
      ],
      "parameters": {
        "operation": "create",
        "destination": {
          "destinationProperties": {
            "address": "={{$node[\"Airtable Trigger\"].json[\"fields\"][\"Address_Line1\"]}}, {{$node[\"Airtable Trigger\"].json[\"fields\"][\"City/Town\"]}}, {{$node[\"Airtable Trigger\"].json[\"fields\"][\"State/Province\"]}}, {{$node[\"Airtable Trigger\"].json[\"fields\"][\"Country\"]}}, {{$node[\"Airtable Trigger\"].json[\"fields\"][\"Postal_Code\"]}}",
            "unparsed": true
          }
        },
        "additionalFields": {
          "notes": "={{$node[\"Airtable Trigger\"].json[\"fields\"][\"Task_Details\"][1]}} \n{{$node[\"Airtable Trigger\"].json[\"fields\"][\"Task_Details\"][0]}}",
          "recipient": {
            "recipientProperties": {
              "recipientName": "={{$node[\"Airtable Trigger\"].json[\"fields\"][\"Recipient_Name\"]}}",
              "recipientNotes": "={{$node[\"Airtable Trigger\"].json[\"fields\"][\"Recipient_Notes\"]}}",
              "recipientPhone": "=+1{{$node[\"Airtable Trigger\"].json[\"fields\"][\"Recipient_Phone\"]}}"
            }
          },
          "completeAfter": "= {{$node[\"Airtable Trigger\"].json[\"fields\"][\"completeAfter\"]}}",
          "completeBefore": "= {{$node[\"Airtable Trigger\"].json[\"fields\"][\"completeBefore\"]}}"
        }
      },
      "credentials": {
        "onfleetApi": {
          "id": "2",
          "name": "Onfleet API Key"
        }
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Airtable Trigger": {
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
