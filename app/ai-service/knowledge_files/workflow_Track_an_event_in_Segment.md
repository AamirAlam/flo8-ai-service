# Track an event in Segment

**[View Template](https://n8n.io/workflows/495-/)**  **Published Date:** 07/13/2020  **Created By:** tanaypant  **Categories:** `Development` `Analytics`  

## Template Description



## Template JSON

```
{
  "id": "122",
  "name": "Track an event in Segment",
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
      "name": "Segment",
      "type": "n8n-nodes-base.segment",
      "position": [
        450,
        300
      ],
      "parameters": {
        "event": "",
        "resource": "track"
      },
      "credentials": {
        "segmentApi": ""
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
            "node": "Segment",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
