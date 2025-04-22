# Validate emails in a table using Mailcheck

**[View Template](https://n8n.io/workflows/1055-/)**  **Published Date:** 04/27/2021  **Created By:** ghagrawal17  **Categories:** `Data & Storage` `Utility` `Marketing`  

## Template Description

This workflow allows you to validate emails stored in a table using the Mailcheck node.



Airtable node: This node will list all the records from a table. Based on your use case, you might want to replace this node.

Mailcheck node: This node will check the emails that got returned by the previous node.

Set node: We will use the Set node to ensure that only the data that we set in this node gets passed on to the next nodes in the workflow.

Airtable1 node: This node will update the Valid field in the table. Based on your use case, you might want to replace this node.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Airtable",
      "type": "n8n-nodes-base.airtable",
      "position": [
        470,
        200
      ],
      "parameters": {
        "table": "Table 1",
        "operation": "list",
        "additionalOptions": {}
      },
      "credentials": {
        "airtableApi": ""
      },
      "typeVersion": 1
    },
    {
      "name": "Mailcheck",
      "type": "n8n-nodes-base.mailcheck",
      "position": [
        670,
        200
      ],
      "parameters": {
        "email": "={{$json[\"fields\"][\"Email\"]}}"
      },
      "credentials": {
        "mailcheckApi": "Mailcheck API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        870,
        200
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "ID",
              "value": "={{$node[\"Airtable\"].json[\"id\"]}}"
            }
          ],
          "boolean": [
            {
              "name": "Valid",
              "value": "={{$json[\"mxExists\"]}}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "name": "Airtable1",
      "type": "n8n-nodes-base.airtable",
      "position": [
        1070,
        200
      ],
      "parameters": {
        "id": "={{$json[\"ID\"]}}",
        "table": "=Table 1",
        "fields": [
          "Valid"
        ],
        "options": {},
        "operation": "update",
        "application": "={{$node[\"Airtable\"].parameter[\"application\"]}}",
        "updateAllFields": false
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
            "node": "Airtable1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Airtable": {
      "main": [
        [
          {
            "node": "Mailcheck",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Mailcheck": {
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
