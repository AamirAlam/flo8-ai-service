# Create, update and get a post via Discourse

**[View Template](https://n8n.io/workflows/930-/)**  **Published Date:** 02/08/2021  **Created By:** ghagrawal17  **Categories:** `Communication`  

## Template Description

This workflow allows you to create, update and get a post using the Discourse node.



Discourse node: This node creates a new post under a category. Based on your use-case, you can select a different category.

Discourse1 node: This node updates the content of the post.

Discourse2 node: This node fetches the node that we created using the Discourse node. 

Based on your use-case, you can add or remove nodes to connect Discourse to different services.

## Template JSON

```
{
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
      "name": "Discourse",
      "type": "n8n-nodes-base.discourse",
      "position": [
        470,
        300
      ],
      "parameters": {
        "title": "[Created] Discourse node",
        "content": "Thank you Ricardo for creating the Discourse node.",
        "additionalFields": {
          "category": 4
        }
      },
      "credentials": {
        "discourseApi": "n8n Discourse Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Discourse1",
      "type": "n8n-nodes-base.discourse",
      "position": [
        670,
        300
      ],
      "parameters": {
        "postId": "={{$json[\"id\"]}}",
        "content": "Thank you Ricardo for creating the Discourse node. We can now create, update and retrieve posts using n8n.",
        "operation": "update",
        "updateFields": {}
      },
      "credentials": {
        "discourseApi": "n8n Discourse Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Discourse2",
      "type": "n8n-nodes-base.discourse",
      "position": [
        870,
        300
      ],
      "parameters": {
        "postId": "={{$json[\"id\"]}}",
        "operation": "get"
      },
      "credentials": {
        "discourseApi": "n8n Discourse Credentials"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Discourse": {
      "main": [
        [
          {
            "node": "Discourse1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Discourse1": {
      "main": [
        [
          {
            "node": "Discourse2",
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
            "node": "Discourse",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
