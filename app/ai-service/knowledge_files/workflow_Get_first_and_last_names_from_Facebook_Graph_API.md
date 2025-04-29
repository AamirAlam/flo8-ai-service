# Get first and last names from Facebook Graph API

**[View Template](https://n8n.io/workflows/514-/)**  **Published Date:** 07/14/2020  **Created By:** amudhan  **Categories:** `Development`  

## Template Description

Companion workflow for Facebook node docs



## Template JSON

```
{
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
      "name": "Facebook Graph API",
      "type": "n8n-nodes-base.facebookGraphApi",
      "position": [
        450,
        300
      ],
      "parameters": {
        "node": "me",
        "options": {
          "fields": {
            "field": [
              {
                "name": "last_name"
              },
              {
                "name": "first_name"
              }
            ]
          }
        }
      },
      "credentials": {
        "facebookGraphApi": "graph_credentials"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Facebook Graph API",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
