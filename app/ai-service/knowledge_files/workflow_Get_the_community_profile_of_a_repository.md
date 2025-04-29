# Get the community profile of a repository

**[View Template](https://n8n.io/workflows/450-/)**  **Published Date:** 07/06/2020  **Created By:** sshaligr  **Categories:** `Development`  

## Template Description



## Template JSON

```
{
  "id": "5",
  "name": "new",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        540,
        350
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Github",
      "type": "n8n-nodes-base.github",
      "position": [
        790,
        350
      ],
      "parameters": {
        "owner": "n8n-io",
        "resource": "repository",
        "operation": "getProfile",
        "repository": "n8n"
      },
      "credentials": {
        "githubApi": "shraddha"
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
            "node": "Github",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
