# Extract information from an image of a receipt

**[View Template](https://n8n.io/workflows/702-/)**  **Published Date:** 10/05/2020  **Created By:** ghagrawal17  **Categories:** `Development` `Core Nodes` `Utility`  

## Template Description



## Template JSON

```
{
  "id": "77",
  "name": "Extract information from an image of a receipt",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        250,
        340
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Mindee",
      "type": "n8n-nodes-base.mindee",
      "position": [
        650,
        340
      ],
      "parameters": {},
      "credentials": {
        "mindeeReceiptApi": "mindee"
      },
      "typeVersion": 1
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        450,
        340
      ],
      "parameters": {
        "url": "https://miro.medium.com/max/1400/0*1T9GkAb93w5NSMsf",
        "options": {},
        "responseFormat": "file"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "HTTP Request": {
      "main": [
        [
          {
            "node": "Mindee",
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
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
