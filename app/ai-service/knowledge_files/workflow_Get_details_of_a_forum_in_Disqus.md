# Get details of a forum in Disqus

**[View Template](https://n8n.io/workflows/493-/)**  **Published Date:** 07/13/2020  **Created By:** tanaypant  **Categories:** `Communication`  

## Template Description



## Template JSON

```
{
  "id": "119",
  "name": "Get details of a forum in Disqus",
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
      "name": "Disqus",
      "type": "n8n-nodes-base.disqus",
      "position": [
        450,
        300
      ],
      "parameters": {
        "id": "hackernoon",
        "additionalFields": {}
      },
      "credentials": {
        "disqusApi": ""
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
            "node": "Disqus",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
