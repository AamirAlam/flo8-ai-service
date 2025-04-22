# Store the output of a phantom in Airtable

**[View Template](https://n8n.io/workflows/882-/)**  **Published Date:** 01/08/2021  **Created By:** ghagrawal17  **Categories:** `Data & Storage` `Sales` `Marketing`  

## Template Description

This workflow allows you to store the output of a phantom in Airtable. This workflow uses the LinkedIn Profile Scraper phantom. Configure and launch this phantom from your Phantombuster account before executing the workflow.



The workflow uses the following node:

Phantombuster node: The Phantombuster node gets the output of the LinkedIn Profile Scraper phantom that ran earlier. You can select a different phantom from the Agent dropdown list, but make sure to configure the workflow accordingly.

Set node: Using the Set node we are setting the data for the workflow. The data that we set in this node will be used by the next nodes in the workflow. Based on your use-case, you can modify the node.

Airtable node: The Airtable node allows us to append the data in an Airtable. Based on your use-case you can replace this node with any other node.

Instead of storing the data in Airtable, you can store the data in a database or Google Sheet, or send it as an email using the Send Email node, Gmail node, or Microsoft Outlook node.

## Template JSON

```
{
  "id": "201",
  "name": "Store the output of a phantom in Airtable",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        270,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Phantombuster",
      "type": "n8n-nodes-base.phantombuster",
      "position": [
        470,
        300
      ],
      "parameters": {
        "agentId": "",
        "operation": "getOutput",
        "additionalFields": {}
      },
      "credentials": {
        "phantombusterApi": "Phantombuster Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        670,
        300
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "Name",
              "value": "={{$node[\"Phantombuster\"].json[\"general\"][\"fullName\"]}}"
            },
            {
              "name": "Email",
              "value": "={{$node[\"Phantombuster\"].json[\"details\"][\"mail\"]}}"
            },
            {
              "name": "Company",
              "value": "={{$node[\"Phantombuster\"].json[\"jobs\"][0][\"companyName\"]}}"
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
        300
      ],
      "parameters": {
        "table": "",
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
  "active": false,
  "settings": {},
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
    "Phantombuster": {
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
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Phantombuster",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
