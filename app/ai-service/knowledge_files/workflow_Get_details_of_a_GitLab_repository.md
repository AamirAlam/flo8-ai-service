# Get details of a GitLab repository

**[View Template](https://n8n.io/workflows/465-/)**  **Published Date:** 07/09/2020  **Created By:** sshaligr  **Categories:** `Development`  

## Template Description



## Template JSON

```
{
  "id": "7",
  "name": "6",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        440,
        320
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Gitlab",
      "type": "n8n-nodes-base.gitlab",
      "position": [
        780,
        320
      ],
      "parameters": {
        "owner": "shaligramshraddha",
        "resource": "repository",
        "operation": "get",
        "repository": "trial"
      },
      "credentials": {
        "gitlabApi": "new"
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
            "node": "Gitlab",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
