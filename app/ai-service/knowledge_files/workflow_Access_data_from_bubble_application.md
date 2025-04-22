# Access data from bubble application

**[View Template](https://n8n.io/workflows/879-/)**  **Published Date:** 01/07/2021  **Created By:** jason  **Categories:** `Development` `Core Nodes`  

## Template Description

This is a proof of concept workflow showing how you would connect n8n to a Bubble data collection. 

## Template JSON

```
{
  "id": "15",
  "name": "Bubble Data Access",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        250,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        450,
        300
      ],
      "parameters": {
        "url": "https://n8n-lessons.bubbleapps.io/version-test/api/1.1/obj/user",
        "options": {},
        "authentication": "headerAuth"
      },
      "credentials": {
        "httpHeaderAuth": "Bubble n8n Lessons Token"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
