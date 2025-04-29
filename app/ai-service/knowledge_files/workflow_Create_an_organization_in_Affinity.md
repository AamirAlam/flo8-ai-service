# Create an organization in Affinity

**[View Template](https://n8n.io/workflows/476-/)**  **Published Date:** 07/10/2020  **Created By:** tanaypant  **Categories:** `Sales`  

## Template Description



## Template JSON

```
{
  "id": "95",
  "name": "Create an organization in Affinity",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        400,
        250
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Affinity",
      "type": "n8n-nodes-base.affinity",
      "position": [
        600,
        250
      ],
      "parameters": {
        "name": "",
        "domain": "",
        "additionalFields": {}
      },
      "credentials": {
        "affinityApi": ""
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
            "node": "Affinity",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
