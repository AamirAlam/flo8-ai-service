# Add new contacts from Autopilot to Airtable

**[View Template](https://n8n.io/workflows/991-/)**  **Published Date:** 03/18/2021  **Created By:** ghagrawal17  **Categories:** `Data & Storage`  

## Template Description

This workflow allows you to receive updates when a new contact is added in Autopilot and add them to a base in Airtable.



Autopilot Trigger node:  The Autopilot Trigger node will trigger the workflow when a new contact is added in Autopilot.

Set node: We use the Set node to ensure that only the data that we set in this node gets passed on to the next nodes in the workflow.

Airtable node: This node will store the data coming from the previous node in a table in Airtable.


## Template JSON

```
{
  "nodes": [
    {
      "name": "Autopilot Trigger",
      "type": "n8n-nodes-base.autopilotTrigger",
      "position": [
        470,
        200
      ],
      "webhookId": "d7aa9691-49cb-4b01-8ecc-9a38fd708cf2",
      "parameters": {
        "event": "contactAdded"
      },
      "credentials": {
        "autopilotApi": "Autopilot API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        670,
        200
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "First Name",
              "value": "={{$json[\"contact\"][\"FirstName\"]}}"
            },
            {
              "name": "Last Name",
              "value": "={{$json[\"contact\"][\"LastName\"]}}"
            },
            {
              "name": "Email",
              "value": "={{$json[\"contact\"][\"Email\"]}}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "name": "Airtable",
      "type": "n8n-nodes-base.airtable",
      "position": [
        870,
        200
      ],
      "parameters": {
        "table": "Table 1",
        "options": {},
        "operation": "append",
        "application": "appflT9EkWRGsSFM2"
      },
      "credentials": {
        "airtableApi": "Airtable Credentials n8n"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Set": {
      "main": [
        [
          {
            "node": "Airtable",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Autopilot Trigger": {
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
