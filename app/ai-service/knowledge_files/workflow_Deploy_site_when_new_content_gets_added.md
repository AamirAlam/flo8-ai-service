# Deploy site when new content gets added

**[View Template](https://n8n.io/workflows/1254-/)**  **Published Date:** 10/04/2021  **Created By:** ghagrawal17  **Categories:** `Development`  

## Template Description

This workflow demonstrates how to create a new deployment when new content gets added to the database. This example workflow can be used when building a JAMstack site.



Webhook node: This node triggers the workflow when new content gets added. For this example, we have configured the webhook in GraphCMS.

Netlify node: This node will start the build process and deploy the website. You will have to select your site from the Site ID dropdown list. To identify the deployment, we are passing a title.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        450,
        300
      ],
      "webhookId": "0d36a8db-0177-4501-9f7a-e46b6829d07a",
      "parameters": {
        "path": "0d36a8db-0177-4501-9f7a-e46b6829d07a",
        "options": {},
        "httpMethod": "POST"
      },
      "typeVersion": 1
    },
    {
      "name": "Netlify",
      "type": "n8n-nodes-base.netlify",
      "position": [
        650,
        300
      ],
      "parameters": {
        "siteId": "5e15e032-9345-41b8-a98f-509e545f061c",
        "operation": "create",
        "additionalFields": {
          "title": "={{$json[\"body\"][\"data\"][\"title\"]}}"
        }
      },
      "credentials": {
        "netlifyApi": "Netlify account"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Netlify",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
