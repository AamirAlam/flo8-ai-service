# Run a SQL query on Postgres

**[View Template](https://n8n.io/workflows/458-/)**  **Published Date:** 07/08/2020  **Created By:** amudhan  **Categories:** `Data & Storage` `Development`  

## Template Description

Companion Workflow for Postgres node docs





## Template JSON

```
{
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
      "name": "Postgres",
      "type": "n8n-nodes-base.postgres",
      "position": [
        450,
        300
      ],
      "parameters": {
        "query": "SELECT * from sometable;",
        "operation": "executeQuery"
      },
      "credentials": {
        "postgres": "postgres-creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Postgres",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
