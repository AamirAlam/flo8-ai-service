# Receive transfer updates from Wise and add to Airtable

**[View Template](https://n8n.io/workflows/993-/)**  **Published Date:** 03/18/2021  **Created By:** ghagrawal17  **Categories:** `Data & Storage` `Finance & Accounting`  

## Template Description

This workflow allows you to receive updates from Wise and add information of a transfer to a base in Airtable.




Wise Trigger node: This node will trigger the workflow when the status of your transfer changes.

Wise node: This node will get the information about the transfer.

Set node: We use the Set node to ensure that only the data that we set in this node gets passed on to the next nodes in the workflow. We set the value of Transfer ID, Date, Reference, and Amount in this node.

Airtable node: This node will append the data that we set in the previous node to a table.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Wise Trigger",
      "type": "n8n-nodes-base.wiseTrigger",
      "position": [
        450,
        280
      ],
      "webhookId": "df8c0c06-7d40-4e57-aaff-60f458e6997c",
      "parameters": {
        "event": "tranferStateChange",
        "profileId": 16138858
      },
      "credentials": {
        "wiseApi": "Wise API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Wise",
      "type": "n8n-nodes-base.wise",
      "position": [
        650,
        280
      ],
      "parameters": {
        "resource": "transfer",
        "transferId": "={{$json[\"data\"][\"resource\"][\"id\"]}}"
      },
      "credentials": {
        "wiseApi": "Wise API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        850,
        280
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "Transfer ID",
              "value": "={{$json[\"id\"]}}"
            },
            {
              "name": "Date",
              "value": "={{$json[\"created\"]}}"
            },
            {
              "name": "Reference",
              "value": "={{$json[\"reference\"]}}"
            },
            {
              "name": "Amount",
              "value": "={{$json[\"sourceValue\"]}}"
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
        1050,
        280
      ],
      "parameters": {
        "table": "Table 1",
        "options": {},
        "operation": "append",
        "application": ""
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
    "Wise": {
      "main": [
        [
          {
            "node": "Set",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Wise Trigger": {
      "main": [
        [
          {
            "node": "Wise",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
