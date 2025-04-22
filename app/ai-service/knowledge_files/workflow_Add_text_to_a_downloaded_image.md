# Add text to a downloaded image

**[View Template](https://n8n.io/workflows/591-/)**  **Published Date:** 08/06/2020  **Created By:** tanaypant  **Categories:** `Core Nodes` `Marketing` `Development`  

## Template Description



## Template JSON

```
{
  "id": "1",
  "name": "Add text to an image downloaded from the internet",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        620,
        170
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Edit Image",
      "type": "n8n-nodes-base.editImage",
      "position": [
        1020,
        170
      ],
      "parameters": {
        "text": "This is n8n",
        "options": {},
        "fontSize": 100,
        "operation": "text",
        "positionX": 300,
        "positionY": 500
      },
      "typeVersion": 1
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        820,
        170
      ],
      "parameters": {
        "url": "https://docs.n8n.io/assets/img/final-workflow.f380b957.png",
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
            "node": "Edit Image",
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
