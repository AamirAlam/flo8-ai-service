# Create a new folder in Box

**[View Template](https://n8n.io/workflows/559-/)**  **Published Date:** 07/27/2020  **Created By:** amudhan  **Categories:** `Data & Storage`  

## Template Description

Companion workflow for Box node docs



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
      "name": "Box",
      "type": "n8n-nodes-base.box",
      "position": [
        450,
        300
      ],
      "parameters": {
        "name": "n8n-rocks",
        "options": {},
        "resource": "folder"
      },
      "credentials": {
        "boxOAuth2Api": "box"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Box",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
