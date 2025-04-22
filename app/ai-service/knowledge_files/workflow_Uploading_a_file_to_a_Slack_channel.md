# Uploading a file to a Slack channel

**[View Template](https://n8n.io/workflows/1570-/)**  **Published Date:** 04/01/2022  **Created By:** Max Tkacz  **Categories:** `Development` `Core Nodes` `Communication` `HITL`  

## Template Description

This workflow shows you how to post a message to a Slack channel and add a file attachment. It also shows you the general pattern for working with Binary data in n8n (any file like a PDF, Image etc).


Specifically, this workflow shows how to download a file from a URL into your workflow, and then upload it to Slack.

Video walkthrough
Watch this 3 min Loom video for a walkthrough and more context on this general pattern:




## Template JSON

```
{
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        160,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Download the file",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        420,
        300
      ],
      "parameters": {
        "url": "https://n8n.io/_nuxt/img/sync-data-between-apps.a4be8c7.png",
        "options": {},
        "responseFormat": "file"
      },
      "typeVersion": 1
    },
    {
      "name": "Post to Slack",
      "type": "n8n-nodes-base.slack",
      "position": [
        640,
        300
      ],
      "parameters": {
        "options": {
          "channelIds": [
            "C02GP22NHJ6"
          ],
          "initialComment": "This is the file"
        },
        "resource": "file",
        "binaryData": true,
        "authentication": "oAuth2"
      },
      "credentials": {
        "slackOAuth2Api": {
          "id": "124",
          "name": "cloud_demo"
        }
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Download the file": {
      "main": [
        [
          {
            "node": "Post to Slack",
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
            "node": "Download the file",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
