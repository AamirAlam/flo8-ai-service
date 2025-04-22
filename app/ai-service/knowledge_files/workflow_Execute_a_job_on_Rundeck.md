# Execute a job on Rundeck

**[View Template](https://n8n.io/workflows/539-/)**  **Published Date:** 07/20/2020  **Created By:** amudhan  **Categories:** `Development` `Communication`  

## Template Description

Companion workflow for Rundeck node docs



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
      "name": "Rundeck",
      "type": "n8n-nodes-base.rundeck",
      "position": [
        450,
        300
      ],
      "parameters": {
        "jobid": "f02c7661-6f75-4ffe-958c-c0ed5f9bc9e6"
      },
      "credentials": {
        "rundeckApi": "rundeck_creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Rundeck",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
