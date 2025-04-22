# Get the value of a key from Redis

**[View Template](https://n8n.io/workflows/557-/)**  **Published Date:** 07/27/2020  **Created By:** amudhan  **Categories:** `Data & Storage` `Development`  

## Template Description

Companion workflow for Redis node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        270,
        320
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Redis",
      "type": "n8n-nodes-base.redis",
      "position": [
        470,
        320
      ],
      "parameters": {
        "key": "hello",
        "options": {},
        "operation": "get"
      },
      "credentials": {
        "redis": "redis-docker_creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Redis",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
