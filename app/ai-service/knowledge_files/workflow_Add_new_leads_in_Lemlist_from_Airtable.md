# Add new leads in Lemlist from Airtable

**[View Template](https://n8n.io/workflows/983-/)**  **Published Date:** 03/15/2021  **Created By:** ghagrawal17  **Categories:** `Data & Storage` `Communication` `Marketing`  

## Template Description

This workflow allows you to add new leads in Lemlist from Airtable.



Airtable node: This node lists all the emails that are stored in your Table. You may have the email addresses stored in a Google Sheet, CRM, or database. Replace the Airtable node with the respective node to get the list of the email addresses.

Lemlist node: This node creates new leads for a campaign in Lemlist taking the information from the previous node.

Lemlist1 node: This node returns the information of a lead from Lemlist.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Airtable",
      "type": "n8n-nodes-base.airtable",
      "position": [
        440,
        320
      ],
      "parameters": {
        "operation": "list",
        "additionalOptions": {}
      },
      "credentials": {
        "airtableApi": "Airtable Credentials n8n"
      },
      "typeVersion": 1
    },
    {
      "name": "Lemlist",
      "type": "n8n-nodes-base.lemlist",
      "position": [
        640,
        320
      ],
      "parameters": {
        "email": "={{$json[\"fields\"][\"Email\"]}}",
        "resource": "lead",
        "campaignId": "cam_H5pYEryq6mRKBiy5v",
        "additionalFields": {
          "firstName": "={{$json[\"fields\"][\"Name\"]}}"
        }
      },
      "credentials": {
        "lemlistApi": "Lemlist API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Lemlist1",
      "type": "n8n-nodes-base.lemlist",
      "position": [
        840,
        320
      ],
      "parameters": {
        "email": "={{$node[\"Airtable\"].json[\"fields\"][\"Email\"]}}",
        "resource": "lead",
        "operation": "get"
      },
      "credentials": {
        "lemlistApi": "Lemlist API Credentials"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Lemlist": {
      "main": [
        [
          {
            "node": "Lemlist1",
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
            "node": "Lemlist",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
