# Read an RSS Feed

**[View Template](https://n8n.io/workflows/583-/)**  **Published Date:** 08/03/2020  **Created By:** amudhan  **Categories:**   

## Template Description

Companion workflow for RSS Feed Read node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        260,
        320
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "RSS Feed Read",
      "type": "n8n-nodes-base.rssFeedRead",
      "position": [
        460,
        320
      ],
      "parameters": {
        "url": "https://failedmachine.com/rss/"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "RSS Feed Read",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
