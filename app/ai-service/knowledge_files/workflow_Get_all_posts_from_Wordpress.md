# Get all posts from Wordpress

**[View Template](https://n8n.io/workflows/546-/)**  **Published Date:** 07/22/2020  **Created By:** amudhan  **Categories:** `Marketing`  

## Template Description

Companion workflow for Wordpress node docs



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
      "name": "Wordpress",
      "type": "n8n-nodes-base.wordpress",
      "position": [
        450,
        300
      ],
      "parameters": {
        "options": {},
        "operation": "getAll"
      },
      "credentials": {
        "wordpressApi": "wp_creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Wordpress",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
