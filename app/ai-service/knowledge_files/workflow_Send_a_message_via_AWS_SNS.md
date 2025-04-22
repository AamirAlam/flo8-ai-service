# Send a message via AWS SNS

**[View Template](https://n8n.io/workflows/501-/)**  **Published Date:** 07/13/2020  **Created By:** amudhan  **Categories:** `Development` `Communication`  

## Template Description

Companion workflow for AWS SNS node docs



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
      "name": "AWS SNS",
      "type": "n8n-nodes-base.awsSns",
      "position": [
        450,
        300
      ],
      "parameters": {
        "topic": "n8n-rocks",
        "message": "This is a test message",
        "subject": "This is a test subject"
      },
      "credentials": {
        "aws": "aws"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "AWS SNS",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
