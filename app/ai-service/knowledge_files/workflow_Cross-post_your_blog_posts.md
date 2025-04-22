# Cross-post your blog posts

**[View Template](https://n8n.io/workflows/418-/)**  **Published Date:** 06/24/2020  **Created By:** amudhan  **Categories:** `Development` `Core Nodes` `Marketing`  

## Template Description

This workflow uses Strapi as a CMS and then cross posts new blog posts to Medium and Dev.to.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Medium",
      "type": "n8n-nodes-base.medium",
      "position": [
        650,
        450
      ],
      "parameters": {
        "title": "={{$json[\"body\"][\"entry\"][\"Title\"]}}",
        "content": "={{$json[\"body\"][\"entry\"][\"PostContent\"]}}",
        "contentFormat": "markdown",
        "additionalFields": {}
      },
      "credentials": {
        "mediumApi": "Medium Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        450,
        300
      ],
      "webhookId": "",
      "parameters": {
        "path": "",
        "options": {},
        "httpMethod": "POST",
        "authentication": "headerAuth"
      },
      "credentials": {
        "httpHeaderAuth": "Strapi Webhook Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        650,
        200
      ],
      "parameters": {
        "url": "https://dev.to/api/articles",
        "options": {},
        "requestMethod": "POST",
        "authentication": "headerAuth",
        "jsonParameters": true,
        "bodyParametersJson": "={\n\t\"article\": {\n\t\t\"title\": \"{{$json[\"body\"][\"entry\"][\"Title\"]}}\",\n\t\t\"published\": true,\n\t\t\"body_markdown\": \"{{$json[\"body\"][\"entry\"][\"PostContent\"]}}\",\n\t\t\"tags\":[\"{{$json[\"body\"][\"entry\"][\"Tag\"]}}\"]\n\t}\n}",
        "headerParametersJson": "{\"Content-Type\": \"application/json\"}"
      },
      "credentials": {
        "httpHeaderAuth": "Dev.to Credentials"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          },
          {
            "node": "Medium",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
