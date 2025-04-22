# Verify email deliverability with Hunter

**[View Template](https://n8n.io/workflows/519-/)**  **Published Date:** 07/15/2020  **Created By:** amudhan  **Categories:** `Sales`  

## Template Description

Companion workflow for Hunter node docs



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
      "name": "Hunter",
      "type": "n8n-nodes-base.hunter",
      "position": [
        450,
        300
      ],
      "parameters": {
        "email": "user@example.com",
        "operation": "emailVerifier"
      },
      "credentials": {
        "hunterApi": "hunter api creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Hunter",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
