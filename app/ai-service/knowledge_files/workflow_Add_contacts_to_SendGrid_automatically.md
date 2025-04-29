# Add contacts to SendGrid automatically

**[View Template](https://n8n.io/workflows/901-/)**  **Published Date:** 01/22/2021  **Created By:** ghagrawal17  **Categories:** `Communication` `Marketing`  

## Template Description

This workflow allows you to create, update and get a contact using the SendGrid node.



Based on your use-case, you may want to add contacts to SendGrid from a different email service or from your CRM.

Fetch the information of the contact using the node of that service. Connect the node with the SendGrid node and reference the value from the node.

## Template JSON

```
{
  "id": "209",
  "name": "Create, update and get a contact using the SendGrid node",
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
      "name": "SendGrid",
      "type": "n8n-nodes-base.sendGrid",
      "position": [
        470,
        300
      ],
      "parameters": {
        "email": "",
        "resource": "contact",
        "additionalFields": {
          "firstName": ""
        }
      },
      "credentials": {
        "sendGridApi": "SendGrid Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "SendGrid1",
      "type": "n8n-nodes-base.sendGrid",
      "position": [
        670,
        300
      ],
      "parameters": {
        "email": "={{$node[\"SendGrid\"].parameter[\"email\"]}}",
        "resource": "contact",
        "additionalFields": {
          "lastName": ""
        }
      },
      "credentials": {
        "sendGridApi": "SendGrid Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "SendGrid2",
      "type": "n8n-nodes-base.sendGrid",
      "position": [
        870,
        300
      ],
      "parameters": {
        "by": "email",
        "email": "={{$node[\"SendGrid\"].parameter[\"email\"]}}",
        "resource": "contact",
        "operation": "get"
      },
      "credentials": {
        "sendGridApi": "SendGrid Credentials"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "SendGrid": {
      "main": [
        [
          {
            "node": "SendGrid1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "SendGrid1": {
      "main": [
        [
          {
            "node": "SendGrid2",
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
            "node": "SendGrid",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
