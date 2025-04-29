# Create an alert on SIGNL4

**[View Template](https://n8n.io/workflows/441-/)**  **Published Date:** 07/01/2020  **Created By:** amudhan  **Categories:** `Development` `Communication`  

## Template Description

Companion workflow for SIGNL4 node docs.
.



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
      "name": "SIGNL4",
      "type": "n8n-nodes-base.signl4",
      "position": [
        450,
        300
      ],
      "parameters": {
        "message": "This is a test alert sent from n8n to SIGNL4",
        "additionalFields": {
          "title": "Sample Title"
        }
      },
      "credentials": {
        "signl4Api": "Signl4 Team Secret"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "SIGNL4",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
