# Get list of completed sale orders with Unleashed Software

**[View Template](https://n8n.io/workflows/641-/)**  **Published Date:** 09/09/2020  **Created By:** ghagrawal17  **Categories:** `Sales` `Data & Storage`  

## Template Description



## Template JSON

```
{
  "name": "",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        390,
        220
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Unleashed Software",
      "type": "n8n-nodes-base.unleashedSoftware",
      "position": [
        600,
        220
      ],
      "parameters": {
        "filters": {
          "orderStatus": [
            "Completed"
          ]
        },
        "returnAll": true
      },
      "credentials": {
        "unleashedSoftwareApi": "unleashed"
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
            "node": "Unleashed Software",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
