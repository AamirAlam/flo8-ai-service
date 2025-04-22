# Create a campaign, add a contact, and get the campaign from Emelia

**[View Template](https://n8n.io/workflows/961-/)**  **Published Date:** 03/02/2021  **Created By:** ghagrawal17  **Categories:** `Communication` `Marketing`  

## Template Description

This workflow allows you to create a campaign, add a contact, and get the campaign from Emelia.



Emelia node: This node will create a new campaign in Emelia.

Emelia1 node: This node will add a contact to the campaign that we created in the previous node. Based on your use-case, you can add a Google Sheets node or an Airtable node to get the email address of the contact.

Emelia2 node: This node will get the information about the campaign that we created earlier.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Emelia",
      "type": "n8n-nodes-base.emelia",
      "position": [
        530,
        310
      ],
      "parameters": {
        "operation": "create",
        "campaignName": "n8n-docs"
      },
      "credentials": {
        "emeliaApi": "Emelia API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Emelia1",
      "type": "n8n-nodes-base.emelia",
      "position": [
        730,
        310
      ],
      "parameters": {
        "operation": "addContact",
        "campaignId": "603dfd70cbe34c3c9730fd09",
        "contactEmail": "email@example.com",
        "additionalFields": {
          "firstName": "NAME"
        }
      },
      "credentials": {
        "emeliaApi": "Emelia API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Emelia2",
      "type": "n8n-nodes-base.emelia",
      "position": [
        930,
        310
      ],
      "parameters": {
        "campaignId": "={{$node[\"Emelia\"].json[\"_id\"]}}"
      },
      "credentials": {
        "emeliaApi": "Emelia API Credentials"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Emelia": {
      "main": [
        [
          {
            "node": "Emelia1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Emelia1": {
      "main": [
        [
          {
            "node": "Emelia2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
