# Add Netlify Form submissions to Airtable

**[View Template](https://n8n.io/workflows/1253-/)**  **Published Date:** 10/04/2021  **Created By:** ghagrawal17  **Categories:** `Data & Storage`  

## Template Description

This workflow demonstrates how to use the Netlify Trigger node to capture form submissions and add it Airtable. You can reuse the workflow to add the data to another similar database by replacing the Airtable node with the corresponding node.



Netlify Trigger node: This node triggers the workflow when a new form is submitted. Select your site from the Site Name/ID dropdown list and the form from the Form ID dropdown list.

Set node: This node extract the required data from the Netlify Trigger node. In this example, we only want to add the Name, Email, and Role of the user.

Airtable node: This node appends the data to Airtable. If you want the data to Google Sheets or a database, replace this node with the corresponding node.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Netlify Trigger",
      "type": "n8n-nodes-base.netlifyTrigger",
      "position": [
        450,
        300
      ],
      "webhookId": "df7efc17-09bb-4409-9f6f-09bd5e59546e",
      "parameters": {
        "event": "submissionCreated",
        "formId": "615ad58f9f491e00070abac5",
        "siteId": "b585059c-a19a-487c-831f-c57af6f13bd1"
      },
      "credentials": {
        "netlifyApi": "Netlify account"
      },
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        650,
        300
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "Name",
              "value": "={{$json[\"name\"]}}"
            },
            {
              "name": "Email",
              "value": "={{$json[\"email\"]}}"
            },
            {
              "name": "Role",
              "value": "={{$json[\"role\"][0]}}"
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
        850,
        300
      ],
      "parameters": {
        "table": "Table 1",
        "options": {},
        "operation": "append",
        "application": "apphwBsFxzjDPDBA8"
      },
      "credentials": {
        "airtableApi": "Airtable Credentials @n8n"
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
    "Netlify Trigger": {
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
