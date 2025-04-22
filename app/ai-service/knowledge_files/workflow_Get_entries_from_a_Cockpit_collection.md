# Get entries from a Cockpit collection

**[View Template](https://n8n.io/workflows/518-/)**  **Published Date:** 07/15/2020  **Created By:** amudhan  **Categories:** `Development` `Marketing`  

## Template Description

Companion workflow for Cockpit node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        750,
        360
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Cockpit",
      "type": "n8n-nodes-base.cockpit",
      "position": [
        950,
        360
      ],
      "parameters": {
        "options": {},
        "collection": "samplecollection"
      },
      "credentials": {
        "cockpitApi": "cockpit api"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Cockpit",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
