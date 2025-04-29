# Execute another workflow

**[View Template](https://n8n.io/workflows/588-/)**  **Published Date:** 08/04/2020  **Created By:** amudhan  **Categories:**   

## Template Description

Companion workflow for Execute Workflow node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        220,
        340
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Execute Workflow",
      "type": "n8n-nodes-base.executeWorkflow",
      "position": [
        410,
        340
      ],
      "parameters": {
        "workflowId": "1"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Execute Workflow",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
