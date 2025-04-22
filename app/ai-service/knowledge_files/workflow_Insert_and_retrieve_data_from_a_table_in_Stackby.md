# Insert and retrieve data from a table in Stackby

**[View Template](https://n8n.io/workflows/934-/)**  **Published Date:** 02/11/2021  **Created By:** ghagrawal17  **Categories:** `Data & Storage`  

## Template Description

This workflow allows you to insert and retrieve data from a table in Stackby.



Set node: The Set node is used to set the values for the name and id fields for a new record. You might want to add data from an external source, for example an API or a CRM. Based on your use-case, add the respective node before the Set node and configure your Set node accordingly.

Stackby node: This node appends data from the previous node to a table in Stackby. Based on the values you want add to your table, enter the column names in the Column field.

Stackby1 node: This node fetches all the data that is stored in the table in Stackby.

## Template JSON

```
{
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        250,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        450,
        300
      ],
      "parameters": {
        "values": {
          "number": [
            {
              "name": "ID",
              "value": 1
            }
          ],
          "string": [
            {
              "name": "Name",
              "value": "n8n"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "name": "Stackby",
      "type": "n8n-nodes-base.stackby",
      "position": [
        650,
        300
      ],
      "parameters": {
        "table": "Table 1",
        "columns": "ID, Name",
        "stackId": "stbgReRhlmmAgT2suT"
      },
      "credentials": {
        "stackbyApi": "Stackby API credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Stackby1",
      "type": "n8n-nodes-base.stackby",
      "position": [
        850,
        300
      ],
      "parameters": {
        "table": "={{$node[\"Stackby\"].parameter[\"table\"]}}",
        "stackId": "={{$node[\"Stackby\"].parameter[\"stackId\"]}}",
        "operation": "list",
        "additionalFields": {}
      },
      "credentials": {
        "stackbyApi": "Stackby API credentials"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Set": {
      "main": [
        [
          {
            "node": "Stackby",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Stackby": {
      "main": [
        [
          {
            "node": "Stackby1",
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
