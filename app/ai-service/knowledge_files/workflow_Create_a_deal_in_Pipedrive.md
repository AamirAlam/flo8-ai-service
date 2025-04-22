# Create a deal in Pipedrive

**[View Template](https://n8n.io/workflows/489-/)**  **Published Date:** 07/12/2020  **Created By:** tanaypant  **Categories:** `Sales`  

## Template Description



## Template JSON

```
{
  "id": "113",
  "name": "Create an deal in Pipedrive",
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
      "name": "Pipedrive",
      "type": "n8n-nodes-base.pipedrive",
      "position": [
        450,
        300
      ],
      "parameters": {
        "title": "",
        "additionalFields": {}
      },
      "credentials": {
        "pipedriveApi": ""
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
            "node": "Pipedrive",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
