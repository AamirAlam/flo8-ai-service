# Get the job details using the Cortex node

**[View Template](https://n8n.io/workflows/809-/)**  **Published Date:** 12/03/2020  **Created By:** ghagrawal17  **Categories:** `Development` `Analytics`  

## Template Description



## Template JSON

```
{
  "id": "160",
  "name": "Analyze a URL and get the job details using the Cortex node",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        370,
        220
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Cortex",
      "type": "n8n-nodes-base.cortex",
      "position": [
        570,
        220
      ],
      "parameters": {
        "analyzer": "f4abc1b633b80f45af165970793fd4fd::Abuse_Finder_3_0",
        "observableType": "url",
        "observableValue": "https://n8n.io",
        "additionalFields": {}
      },
      "credentials": {
        "cortexApi": "cortex"
      },
      "typeVersion": 1
    },
    {
      "name": "Cortex1",
      "type": "n8n-nodes-base.cortex",
      "position": [
        770,
        220
      ],
      "parameters": {
        "jobId": "={{$node[\"Cortex\"].json[\"_id\"]}}",
        "resource": "job"
      },
      "credentials": {
        "cortexApi": "cortex"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Cortex": {
      "main": [
        [
          {
            "node": "Cortex1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Cortex",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
