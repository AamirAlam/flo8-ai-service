# Send an SMS using the Mocean node

**[View Template](https://n8n.io/workflows/667-/)**  **Published Date:** 09/15/2020  **Created By:** ghagrawal17  **Categories:** `Communication`  

## Template Description



## Template JSON

```
{
  "id": "59",
  "name": "Send an SMS using the Mocean node",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        590,
        260
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Mocean",
      "type": "n8n-nodes-base.mocean",
      "position": [
        790,
        260
      ],
      "parameters": {
        "to": "",
        "from": "",
        "message": ""
      },
      "credentials": {
        "moceanApi": "mocean"
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
            "node": "Mocean",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
