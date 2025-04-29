# Encrypt some data using the crypto node

**[View Template](https://n8n.io/workflows/574-/)**  **Published Date:** 08/03/2020  **Created By:** amudhan  **Categories:** `Development` `Core Nodes`  

## Template Description

Companion workflow for Crypto node docs



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
      "name": "Crypto",
      "type": "n8n-nodes-base.crypto",
      "position": [
        450,
        300
      ],
      "parameters": {
        "value": "n8n rocks!"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Crypto",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
