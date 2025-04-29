# Get a pipeline in CircleCI

**[View Template](https://n8n.io/workflows/454-/)**  **Published Date:** 07/08/2020  **Created By:** tanaypant  **Categories:** `Development`  

## Template Description



## Template JSON

```
{
  "id": "84",
  "name": "Get a pipeline in CircleCI",
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
      "name": "CircleCI",
      "type": "n8n-nodes-base.circleCi",
      "position": [
        450,
        300
      ],
      "parameters": {
        "vcs": "",
        "projectSlug": ""
      },
      "credentials": {
        "circleCiApi": ""
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
            "node": "CircleCI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
