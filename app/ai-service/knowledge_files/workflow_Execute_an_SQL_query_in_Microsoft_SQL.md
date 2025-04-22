# Execute an SQL query in Microsoft SQL

**[View Template](https://n8n.io/workflows/479-/)**  **Published Date:** 07/10/2020  **Created By:** tanaypant  **Categories:** `Data & Storage` `Development`  

## Template Description



## Template JSON

```
{
  "id": "99",
  "name": "Execute an SQL query in Microsoft SQL",
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
      "name": "Microsoft SQL",
      "type": "n8n-nodes-base.microsoftSql",
      "position": [
        450,
        300
      ],
      "parameters": {
        "query": "",
        "operation": "executeQuery"
      },
      "credentials": {
        "microsoftSql": ""
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
            "node": "Microsoft SQL",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
