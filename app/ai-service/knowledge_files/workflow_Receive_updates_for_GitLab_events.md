# Receive updates for GitLab events

**[View Template](https://n8n.io/workflows/528-/)**  **Published Date:** 07/16/2020  **Created By:** amudhan  **Categories:**   

## Template Description

Companion workflow for GitLab Trigger docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "Gitlab Trigger",
      "type": "n8n-nodes-base.gitlabTrigger",
      "position": [
        460,
        480
      ],
      "webhookId": "0e855b27-6465-42be-9610-c61b2e09cef9",
      "parameters": {
        "owner": "n8n-io",
        "events": [
          "*"
        ],
        "repository": "n8n-docs"
      },
      "credentials": {
        "gitlabApi": "gitlab_creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {}
}
```
