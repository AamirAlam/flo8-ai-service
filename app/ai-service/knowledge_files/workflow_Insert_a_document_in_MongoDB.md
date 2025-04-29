# Insert a document in MongoDB

**[View Template](https://n8n.io/workflows/503-/)**  **Published Date:** 07/13/2020  **Created By:** amudhan  **Categories:** `Data & Storage` `Development`  

## Template Description

Companion workflow for MongoDB node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        220,
        320
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        420,
        320
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "my_key",
              "value": "my_value"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "name": "MongoDB",
      "type": "n8n-nodes-base.mongoDb",
      "position": [
        620,
        320
      ],
      "parameters": {
        "fields": "my_key",
        "operation": "insert",
        "collection": "n8n-collection"
      },
      "credentials": {
        "mongoDb": "mongodb_credentials"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Set": {
      "main": [
        [
          {
            "node": "MongoDB",
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
