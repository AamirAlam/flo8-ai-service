# Manage contacts via Autopilot

**[View Template](https://n8n.io/workflows/990-/)**  **Published Date:** 03/18/2021  **Created By:** ghagrawal17  **Categories:** `Marketing`  

## Template Description

This workflow allows you to create a new list, add a new contact to that list, update the contact, and get all contacts in the list using the Autopilot node.



Autopilot node: This node will create a new list called n8n-docs in Autopilot.

Autopilot1 node: This node creates a new contact and adds it to the list created in the previous node.

Autopilot2 node: This node updates the information of the contact that we created in the previous node.

Autopilot3 node: This node returns all the contacts of the n8n-docs list that we created using the Autopilot node.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Autopilot",
      "type": "n8n-nodes-base.autopilot",
      "position": [
        470,
        320
      ],
      "parameters": {
        "name": "n8n-docs",
        "resource": "list"
      },
      "credentials": {
        "autopilotApi": "Autopilot API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Autopilot1",
      "type": "n8n-nodes-base.autopilot",
      "position": [
        670,
        320
      ],
      "parameters": {
        "email": "",
        "additionalFields": {
          "autopilotList": "={{$json[\"list_id\"]}}"
        }
      },
      "credentials": {
        "autopilotApi": "Autopilot API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Autopilot2",
      "type": "n8n-nodes-base.autopilot",
      "position": [
        870,
        320
      ],
      "parameters": {
        "email": "={{$node[\"Autopilot1\"].parameter[\"email\"]}}",
        "additionalFields": {
          "Company": "n8n"
        }
      },
      "credentials": {
        "autopilotApi": "Autopilot API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Autopilot3",
      "type": "n8n-nodes-base.autopilot",
      "position": [
        1070,
        320
      ],
      "parameters": {
        "listId": "={{$node[\"Autopilot\"].json[\"list_id\"]}}",
        "resource": "contactList",
        "operation": "getAll",
        "returnAll": true
      },
      "credentials": {
        "autopilotApi": "Autopilot API Credentials"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Autopilot": {
      "main": [
        [
          {
            "node": "Autopilot1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Autopilot1": {
      "main": [
        [
          {
            "node": "Autopilot2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Autopilot2": {
      "main": [
        [
          {
            "node": "Autopilot3",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
