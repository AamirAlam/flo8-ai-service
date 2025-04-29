# Read a file from disk

**[View Template](https://n8n.io/workflows/577-/)**  **Published Date:** 08/03/2020  **Created By:** amudhan  **Categories:**   

## Template Description

Companion workflow for Read Binary File node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        270,
        320
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Read Binary File",
      "type": "n8n-nodes-base.readBinaryFile",
      "position": [
        470,
        320
      ],
      "parameters": {
        "filePath": "/data/picture.jpg"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Read Binary File",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
