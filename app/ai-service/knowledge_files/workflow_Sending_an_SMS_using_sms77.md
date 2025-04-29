# Sending an SMS using sms77

**[View Template](https://n8n.io/workflows/469-/)**  **Published Date:** 07/10/2020  **Created By:** tanaypant  **Categories:** `Communication`  

## Template Description



## Template JSON

```
{
  "id": "92",
  "name": "Sending an SMS using sms77",
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
      "name": "Sms77",
      "type": "n8n-nodes-base.sms77",
      "position": [
        450,
        300
      ],
      "parameters": {
        "message": "Hello from n8n!"
      },
      "credentials": {
        "sms77Api": ""
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
            "node": "Sms77",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
