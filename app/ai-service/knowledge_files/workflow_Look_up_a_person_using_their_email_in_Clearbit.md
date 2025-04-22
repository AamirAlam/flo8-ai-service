# Look up a person using their email in Clearbit

**[View Template](https://n8n.io/workflows/484-/)**  **Published Date:** 07/12/2020  **Created By:** tanaypant  **Categories:** `Sales`  

## Template Description



## Template JSON

```
{
  "id": "104",
  "name": "Look up a person using their email in Clearbit",
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
      "name": "Clearbit",
      "type": "n8n-nodes-base.clearbit",
      "position": [
        450,
        300
      ],
      "parameters": {
        "email": "",
        "resource": "person",
        "additionalFields": {}
      },
      "credentials": {
        "clearbitApi": ""
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
            "node": "Clearbit",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
