# Receive updates for Bitbucket events

**[View Template](https://n8n.io/workflows/529-/)**  **Published Date:** 07/16/2020  **Created By:** amudhan  **Categories:**   

## Template Description

Companion workflow for Bitbucket Trigger node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "Bitbucket Trigger",
      "type": "n8n-nodes-base.bitbucketTrigger",
      "position": [
        880,
        390
      ],
      "webhookId": "97ca8044-5835-4547-801d-c27dd7f10c2d",
      "parameters": {
        "events": [
          "repo:push"
        ],
        "resource": "repository",
        "repository": "test"
      },
      "credentials": {
        "bitbucketApi": "bitbucket_creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {}
}
```
