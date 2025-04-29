# Send an email using AWS SES

**[View Template](https://n8n.io/workflows/507-/)**  **Published Date:** 07/14/2020  **Created By:** amudhan  **Categories:** `Development` `Communication`  

## Template Description

Companion workflow for AWS SES node docs



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
      "name": "AWS SES",
      "type": "n8n-nodes-base.awsSes",
      "position": [
        450,
        300
      ],
      "parameters": {
        "body": "This is a sample message body in an email\n",
        "subject": "n8n Rocks",
        "fromEmail": "n8n@n8n.io",
        "toAddresses": [
          "user@example.com",
          "user2@example.com"
        ],
        "additionalFields": {}
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
            "node": "AWS SES",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
