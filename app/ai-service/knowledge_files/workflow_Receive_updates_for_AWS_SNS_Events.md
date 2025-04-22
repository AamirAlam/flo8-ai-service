# Receive updates for AWS SNS Events

**[View Template](https://n8n.io/workflows/509-/)**  **Published Date:** 07/14/2020  **Created By:** amudhan  **Categories:**   

## Template Description

Companion workflow for AWS SNS Trigger node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "AWS-SNS-Trigger",
      "type": "n8n-nodes-base.awsSnsTrigger",
      "position": [
        440,
        300
      ],
      "parameters": {
        "topic": "arn:aws:sns:ap-south-1:100558637562:n8n-rocks"
      },
      "credentials": {
        "aws": "amudhan-aws"
      },
      "typeVersion": 1
    }
  ],
  "connections": {}
}
```
