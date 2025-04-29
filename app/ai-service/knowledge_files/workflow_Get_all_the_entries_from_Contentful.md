# Get all the entries from Contentful

**[View Template](https://n8n.io/workflows/640-/)**  **Published Date:** 09/09/2020  **Created By:** ghagrawal17  **Categories:** `Development` `Marketing`  

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
        150,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Contentful",
      "type": "n8n-nodes-base.contentful",
      "position": [
        350,
        300
      ],
      "parameters": {
        "operation": "getAll",
        "returnAll": true,
        "additionalFields": {}
      },
      "credentials": {
        "contentfulApi": "contentful"
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
            "node": "Contentful",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
