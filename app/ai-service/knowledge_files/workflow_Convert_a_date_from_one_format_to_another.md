# Convert a date from one format to another

**[View Template](https://n8n.io/workflows/575-/)**  **Published Date:** 08/03/2020  **Created By:** amudhan  **Categories:**   

## Template Description

Companion workflow for Date & Time node docs



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
      "name": "Date & Time",
      "type": "n8n-nodes-base.dateTime",
      "position": [
        450,
        300
      ],
      "parameters": {
        "value": "14/02/2020",
        "options": {
          "fromFormat": "DD/MM/YYYY"
        }
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Date & Time",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
