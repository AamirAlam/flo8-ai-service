# Rename a key in n8n

**[View Template](https://n8n.io/workflows/582-/)**  **Published Date:** 08/03/2020  **Created By:** amudhan  **Categories:**   

## Template Description

Companion workflow for Rename Keys node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        250,
        320
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        450,
        320
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "key",
              "value": "somevalue"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "name": "Rename Keys",
      "type": "n8n-nodes-base.renameKeys",
      "position": [
        650,
        320
      ],
      "parameters": {
        "keys": {
          "key": [
            {
              "newKey": "newkey",
              "currentKey": "key"
            }
          ]
        }
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Set": {
      "main": [
        [
          {
            "node": "Rename Keys",
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
