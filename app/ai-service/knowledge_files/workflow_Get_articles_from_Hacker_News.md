# Get articles from Hacker News

**[View Template](https://n8n.io/workflows/525-/)**  **Published Date:** 07/16/2020  **Created By:** amudhan  **Categories:** `Communication` `Marketing`  

## Template Description

Companion workflow for Hacker News node docs



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
      "name": "Hacker News",
      "type": "n8n-nodes-base.hackerNews",
      "position": [
        450,
        300
      ],
      "parameters": {
        "resource": "all",
        "additionalFields": {}
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Hacker News",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
