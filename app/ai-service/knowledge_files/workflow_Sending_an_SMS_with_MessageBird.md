# Sending an SMS with MessageBird

**[View Template](https://n8n.io/workflows/455-/)**  **Published Date:** 07/08/2020  **Created By:** tanaypant  **Categories:** `Communication`  

## Template Description



## Template JSON

```
{
  "id": "85",
  "name": "Sending an SMS with MessageBird",
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
      "name": "MessageBird",
      "type": "n8n-nodes-base.messageBird",
      "position": [
        450,
        300
      ],
      "parameters": {
        "message": "",
        "originator": "",
        "recipients": "",
        "additionalFields": {}
      },
      "credentials": {
        "messageBirdApi": ""
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
            "node": "MessageBird",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
