# Create a meeting in Zoom automatically

**[View Template](https://n8n.io/workflows/453-/)**  **Published Date:** 07/08/2020  **Created By:** tanaypant  **Categories:** `Communication`  

## Template Description



## Template JSON

```
{
  "id": "83",
  "name": "Creating a meeting with the Zoom node",
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
      "name": "Zoom",
      "type": "n8n-nodes-base.zoom",
      "position": [
        450,
        300
      ],
      "parameters": {
        "topic": "Something",
        "authentication": "",
        "additionalFields": {}
      },
      "credentials": {
        "zoomOAuth2Api": ""
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Zoom": {
      "main": [
        []
      ]
    },
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Zoom",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
